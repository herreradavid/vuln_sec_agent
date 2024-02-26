import json

from openai import OpenAI
from loadfiles import read_files, preprocess_text
from sprint import add_task_backlog, compute_next_sprint, sample_backlog, assign_sprint, by_priority_then_points,parse_report
from test_data import finding_tasks, expected_sprint, task_backlog, test_developers
from test_data import finding_tasks, expected_sprint, task_backlog, test_developers
from dotenv import load_dotenv


def read(file_name):
    return open(file_name).read()

load_dotenv()

directory_path = './server/'
length, texts = read_files(directory_path)
train_code = preprocess_text(texts)
#print(train_code[0])
#print(length)


directory_path = './data/'
_, eval_texts = read_files(directory_path)
eval_code = preprocess_text(eval_texts)



findings_server = read("findings-server.json")
findings = read("findings.json")
train_report1 = read("train/report1.json")
train_report2 = read("train/report2.json")
train_report3 = read("train/report3.json")

client = OpenAI()

f = open('findings.json',) 
   
findings_file= json.load(f) 
findings_list = findings_file["Issues"]
#for finding in findings_array:
    #print(finding['file'])

new_backlog = []
extra_backlog = []

findingsLength = len(findings_list)
#findingsLength = 3
for i in range(0,findingsLength):
  finding = findings_list[i]
  print(finding)
  file_path = finding["file"]
  vuln_line = finding["line"]
  code_inline = finding["code"]
  print("path to file: ",file_path)
  print("line:", vuln_line)


  completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
      {"role": "system", "content": "You are a security engineer expert in understanding Go programming and JSON. Learn to find code issues to match the following examples keeping in mind the level of severity CWE gives to each code is more accurate in the json gosec issues findings. :"},
      {"role": "system", "content": f"Understand the issues in the training set, note the file location: {findings_server} where the code is in {train_code}"},
      {"role": "system", "content": f"The correlation between number of lines_affected and the number of story_points is directly related. The output must be in strict JSON with out any trailing or leading characters"},
      {"role": "user", "content": f"Compute the priority of the finding and the time to fix for the server/internal/handlers/handlers.go line 89"},
      {"role": "assistant", "content": f"{train_report1}"}, 
      {"role": "user", "content": f"Compute the priority of finding and time to fix for server/internal/repository/product/product.go line 58 as before"},
      {"role": "assistant", "content": f"{train_report2}"}, 
      {"role": "user", "content": f"Compute the priority of finding and time to fix for server/internal/app/app.go line 52 as before"},
      {"role": "assistant", "content": f"{train_report3}"}, 
      #{"role": "user", "content": f"Assuming now your context for findings is now {findings} where the code is in {eval_code}. Then Compute the priority of finding and time to fix for /main.go line 12 as before"},
      {"role": "user", "content": f"Assuming your context for findings is now {findings} where the code is in {eval_code}. Then Compute the priority of finding and time to fix for {file_path} line {vuln_line} as before"},
    ]
  )


  response_report_json = completion.choices[0].message.content
  print(response_report_json)

  new_task = parse_report(json.loads(response_report_json))

  extra_backlog.append(new_task)
new_backlog = add_task_backlog(task_backlog, extra_backlog)
print("This is the new task backlog: ",new_backlog)
#new_backlog = add_task_backlog(new_backlog, new_task)
#breakpoint()
sprint = compute_next_sprint(new_backlog)
print("This is the new sprint: ", sprint)
