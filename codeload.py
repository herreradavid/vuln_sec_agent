import json

f = open('findings.json',) 
data = json.load(f) 
findings_array = data["Issues"]
for finding in findings_array:
    print(finding['file'])
print("---------------------------------")
file_name = findings_array[1]['file']
print(file_name)
file_code = open("data"+"/"+file_name)
code = file_code.read()
print(code)