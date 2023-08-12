import requests

listk= ['common_api.py','common_deep.py','common_excel.py',
        'common_git.py','common_Json.py','common_lab.py',
        'common_opencv.py','common_opencv1.py','common_pandas.py',
        'common_pyqt.py','common_request.py',
        'common_selenium.py','common_selenium_beautifulsoup.py','common_venv.py']

fileks = ['common_venv.py']

for filek in fileks:
    github_raw_url = f"https://raw.githubusercontent.com/kuick1kim/cmmn/main/{filek}"
    response = requests.get(github_raw_url)
    text1 = str(response.text)    
    with open(filek, "w", encoding='utf-8') as file:
        file.write(text1)

print('======= 파일상단에 import 시켜주세요\n')
ooo = "import "
for i in fileks:
    k = i.split(".")[0]
    k = k+", "
    ooo = ooo + k
print(ooo[:-2])
print()
