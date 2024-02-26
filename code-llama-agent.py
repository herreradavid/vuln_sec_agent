import json
import os
from langchain.text_splitter import Language
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from loadfiles import read_files, preprocess_text, read_files_v2
from sprint import add_task_backlog, compute_next_sprint, sample_backlog, assign_sprint, by_priority_then_points, parse_report
from test_data import finding_tasks, expected_sprint, task_backlog, test_developers
from test_data import finding_tasks, expected_sprint, task_backlog, test_developers
from dotenv import load_dotenv

# from langchain import HuggingFaceHub, LLMChain#, HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceEndpoint, Replicate
from langchain.prompts import PromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv
import replicate


def read(file_name):
    return open(file_name).read()


load_dotenv()
HUGGING_FACE_KEY = os.getenv('HUGGING_FACE_API')
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')

model_id = "codellama/CodeLlama-70b-Instruct-hf"
replicate_code_llama = "meta/codellama-70b-instruct:a279116fe47a0f65701a8817188601e2fe8f4b9e04a518789655ea7b995851bf"
llm = Replicate(model=replicate_code_llama, temperature=0.6, top_k=40,
                top_p=0.1, token=REPLICATE_API_TOKEN)  # max_length=128, , max_length=128

# llm = HuggingFaceEndpoint(    repo_id=model_id,  temperature=0.6, top_k=40, top_p=0.1, token=HUGGING_FACE_KEY)  # max_length=128, , max_length=128


loader_server_samples = GenericLoader.from_filesystem(
    "./server",
    glob="**/*",
    suffixes=[".go"],
    exclude=["**/non-utf8-encoding.go"],
    parser=LanguageParser(language=Language.GO, parser_threshold=500),
)
documents = loader_server_samples.load()

loader_vulnerable_code = GenericLoader.from_filesystem(
    "./data",
    glob="**/*",
    suffixes=[".go"],
    exclude=["**/non-utf8-encoding.go"],
    parser=LanguageParser(language=Language.GO, parser_threshold=500),
)
documents = loader_vulnerable_code.load()
# len(documents)
# print(documents)


directory_path = './server_short/'
length, texts = read_files(directory_path)
train_code = preprocess_text(texts)

directory_path = './data/'
_, eval_texts = read_files_v2(directory_path)
eval_code = preprocess_text(eval_texts)


findings_server = read("findings-server.json")
findings = read("findings.json")
train_report1 = read("train/report1.json")
train_report2 = read("train/report2.json")
train_report3 = read("train/report3.json")

f = open('findings.json',)

findings_file = json.load(f)
findings_list = findings_file["Issues"]
# for finding in findings_array:
# print(finding['file'])

new_backlog = []
extra_backlog = []
finding = findings_list[1]
file_path = finding["file"]
vuln_line = finding["line"]
code_inline = finding["code"]

#
prompt_and_code = PromptTemplate(
    input_variables=["findings_server", "train_code",
                     "train_report1", "finding", "eval_code", "code_inline", "file_path", "vuln_line"],
    template="""
<s>Source: system

 You are a helptful and honest coder expert in code security in Golang  also known as go understand criticality and priotiry of software vulnerabilities in go languange.The output must be in strict JSON with out any trailing or leading characters <step> Source: user
Learn to find code vulnerabilities to in following examples keeping in mind the level of severity CWE gives to each code is more accurate in the json gosec issues findings.
Understand the security vulnerabilities in the results of the gosec analysis: {findings_server} that was completed in the code {train_code}
<step> Source: user

 Compute the priority of the finding and the number story points in days for this vulnerability ```query := fmt.Sprintf("SELECT id, description FROM Products WHERE id = '%s'", id)``` present in the file server/internal/handlers/handlers.go in line 89


<step> Source: assistant

 {train_report1}

 
<step> Source: user

 Assuming your context for findings is now {finding} where the code is in {eval_code}. Then Compute the priority of finding and story points for the vulnerability ```{code_inline}``` {file_path} line {vuln_line} as before"

 Destination: user

"""
)
hub_chain = LLMChain(prompt=prompt_and_code, llm=llm, verbose=True)
response = hub_chain.invoke(
    {"findings_server": findings_server,
     "train_report1": train_report1,
     "train_code": train_code,
     "finding": finding,
     "eval_code": eval_code,
     "code_inline": code_inline,
     "file_path": file_path,
     "vuln_line": vuln_line
     }

)
print(response['text'])
