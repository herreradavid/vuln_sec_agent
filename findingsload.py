import json
import os

#from langchain import HuggingFaceHub, LLMChain#, HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv

load_dotenv()
HUGGING_FACE_KEY = os.getenv('HUGGING_FACE_API')

repor_m_id = "codellama/CodeLlama-70b-Instruct-hf"
#repor_m_id = "codellama/CodeLlama-70b-hf"

llm = HuggingFaceEndpoint(
    repo_id=repor_m_id,  temperature=0.01, token=HUGGING_FACE_KEY,max_length=128) #max_length=128,

#hub_llm = HuggingFaceHub(repo_id="codellama/CodeLlama-70b-Instruct-hf")
load_dotenv()
f = open('findings.json',) 
   
data = json.load(f) 
findings_array = data["Issues"]
for finding in findings_array:
    print(finding['file'])

file_name_path = findings_array[8]['file']
vuln_line_code = findings_array[8]['code']
print(file_name_path)
file_code = open("data"+"/"+file_name_path)
code = file_code.read()
#print(code)

prompt_and_code = PromptTemplate(
    input_variables = ["code_snippet","line_issue"],
    template = """what is the variable exposed in the vulnerability in the line below\n
      '''{line_issue} ''' 
      ----------------------------------
    Is that variable mentioned in other parts of the code
    The code is below\n:  '''{code_snippet}''' """
)
hub_chain = LLMChain(prompt=prompt_and_code, llm=llm, verbose=True )
response = hub_chain.invoke({"code_snippet":code, "line_issue":vuln_line_code})
print(response['text'])