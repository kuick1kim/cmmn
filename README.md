import requests

filek = "common_git.py"
github_raw_url = f"https://raw.githubusercontent.com/kuick1kim/cmmn/main/{filek}"

response = requests.get(github_raw_url)
text1 = str(response.text)    
with open(filek, "w", encoding='utf-8') as file:
    file.write(text1)
 
 
