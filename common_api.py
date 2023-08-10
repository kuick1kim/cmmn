# pip install bs4


import os, shutil 
import zipfile, time
import requests
import pandas as pd
from pandas import  DataFrame
import configparser, json
# from pandas.io.json import json_normalize
import json

from bs4 import BeautifulSoup


# ### 카카오 증권

# headers = {
#     'Content-Type': 'text/html; charset=UTF-8',
#     'Referer': 'https://finance.daum.net/chart/A005490',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
#     }





def REq(url , get_post):

    headersA = {'Accept':'*/*'}
    headersB = {'Accept':'*/*'}
    headers = headersA

    start_time = time.time()    
    if get_post == "GET":
        response = requests.get(url, headers=headers)
    elif get_post == "POST" :
        response = requests.post(url, headers=headers)

    if response.status_code == requests.codes.ok:        
        kkkms =":::접속성공:::"
        if "</html>" in str(response.text):
            data = response
        else :
            data = str(response.text)
    else :
        kkkms =":::접속실패:::"
        data = ""

    end_time = round((time.time() - start_time),2)
    print(kkkms+"  접속시간 :"+ str(end_time))
    print("데이터 :\t"+ data)
    return data 




# request API 쏘기 URL로 쏘면
# 데이터와 시간과 성공여부가 날아옴

# BeautyfulSoup 파싱하기 

# 셀레니움은 따로 만들기


def html_parsing(url): 
    get_post = "GET"
    html = REq(url , get_post)
    soup = BeautifulSoup(html.content, 'html.parser')
    soup1 = soup.prettify()
    save_html(soup1)
    # print(soup)
    
    return soup


def api_call_normal(url, get_post):
    data = REq(url , get_post)
    data = str(data.text) ### 텍스트로 올테니까
    return data



def api_call_json(url, get_post):
    data = REq(url , get_post)
    return data
# if __name__ == "__main__":
#     main()
   
    



def save_html(soup):
    html_file = open('image/html_file.html', 'w', encoding='utf-8')
    html_file.write(soup)
    html_file.close()




def find_table(soup):
    num = 0
    tables = soup.find_all("table")
    for t in tables:
        k = pd.read_html(str(t))
        print(k) ; num+= 1
        print("[{}]=============================================================".format(num))
    if num == 0 :
        print("테이블이 없습니다")



##########################################################################################
######################### BeautifulSoup select 사용법   ##################################
######################### BeautifulSoup select 사용법   ##################################
######################### BeautifulSoup select 사용법   ##################################
##########################################################################################
# BeautifulSoup select 사용법
# soup.select('a[class="red italic"]') == # soup.select('a.italic.red')
# oup.select_one('a[class=italic]') == # soup.select_one('a.italic')

# soup.select_one('a[class*=re]') 
# soup.select("div a") #div 태그 아래에 있는 a 태그 찾기
# soup.select("head > title")
# soup.select("head > #link1") #아이디로 태그 찾음
# soup.select(".sister")#CSS class로 태그 찾기



# BeautifulSoup Find 사용법
# soup.find_all('a', {'class': 'italic red'})
# soup.find_all('a', class_='italic red')
# soup.find_all('a', {'class': ['italic', 'red']})

# soup.find('a', {'class': 'italic'}) == soup.find('a', {'class': ['italic']})
# 태그 이름만 특정 

# soup.find('p') 
# soup.find(class_='example') 
# soup.find(attrs = {'class':'exmaple'}) 
# soup.find('p', class_='example')






##########################################################################################
######################### BeautifulSoup select 사용법   ##################################
######################### BeautifulSoup select 사용법   ##################################
######################### BeautifulSoup select 사용법   ##################################
##########################################################################################



def req4saveJson(url, GetPost, path_name):   ### api_name 은 저장할때만 씀
    """
    이 함수는 결과 값이 json 으로 호출되는 것
        url (str): url
        GetPost (str): "GET" 또는 "POST" "DELETE"
        path_name (str): "파일명.json" 저장경로
    Retruns:
        jsonjson `Object`: 불러온 json 데이터를 보냄. 
    """
    headersA = {'Accept':'application/json'}
    headers = headersA

    if GetPost == "GET":
        response1 = requests.get(url, headers=headers)
    elif GetPost == "POST" :
        response1 = requests.post(url, headers=headers)   

    ##################################################       
    if response1.status_code == requests.codes.ok:   
        html_k = response1.content        
    else :
        html_k = ""
    
    if html_k != "":
        soup = BeautifulSoup(html_k, "html.parser").text
        jsonjson = json.loads(soup) ###처음에 파싱을 하고   
        try:
            bus_number = jsonjson['name']
            path_name=path_name.replace("json.json","json_{}.json".format(bus_number))
            print(bus_number)
        except:
            pbus_number = "없음"
        jsonjson= json.dumps(jsonjson, indent =2, sort_keys=True, ensure_ascii = False) ####바로 sort_keys로 정렬을 해준다. ####여기에서 정렬을 해줌 이것은 str로 나옴
        # bus_number = jsonjson[9]

        # print(jsonjson)
        jsonjson = json.loads(jsonjson)### 다시 파싱을 해야함

        #######################  RAW 데이터를 저장해서 보기   ##################################
        # api_name = save_name.replace("/","_")        
        if len(str(jsonjson)) > 30:
            with open("{}".format(path_name), "w", encoding="utf-8") as json_file:
                json.dump(jsonjson, json_file, indent=2, ensure_ascii = False)
        #######################  RAW 데이터를 저장해서 보기   ##################################
    else:
        print(" json 내용이 없습니다. ")
        jsonjson = ""
        if len(str(jsonjson)) > 30:
            with open("{}".format(path_name), "w", encoding="utf-8") as json_file:
                json.dump(jsonjson, json_file, indent=2, ensure_ascii = False)
    return jsonjson





def open_json(path_name):  #### 예쁘게 출력도됨
    """
    이 함수는 경로를 넣으면 json 을 불러올 수 있다. 
        path_name (str): "파일명.json" 저장경로
    Retruns:
        jsonjson `Object`: 불러온 json 데이터를 보냄. 
    """
    with open('{}'.format(path_name), 'r', encoding="utf-8") as json_file:
        jsonjson = json.load(json_file)
        jsonjson= json.dumps(jsonjson, indent =2, sort_keys=True, ensure_ascii = False) ####바로 sort_keys로 정렬을 해준다. ####여기에서 정렬을 해줌 이것은 str로 나옴
        # print(jsonjson)
        jsonjson = json.loads(jsonjson)### 예쁘게만 잠깐 보일뿐 실제는 현상 그자체임
    return jsonjson




def save_json(json_file, path_name):    
    """
    이 함수는 json 변환후 save 할 수 있게 한 것이다. 
        jsonjson `Object`: json 을 넣는다. 
        path_name (str): "파일명.json" 저장경로
    """
    with open("{}".format(path_name), "w", encoding="utf-8") as json_file:
           json.dump(json_file, json_file, indent=2, ensure_ascii = False)


def df_to_json(df, path_name):
    """
    이 함수는 dataframe 을 json으로 만들어 준다.
        df `Object`: dataframe 이다. 
        path_name (str): "파일명.json" 저장경로
    """
    
    df.to_json("{}".format(path_name), orient = 'table', force_ascii=False)
    time.sleep(0.3)
    jsonjson= open_json(path_name) ### 저장후 다시 연다. 그리고 재저장 예쁘게 
    time.sleep(0.3)
    with open("{}".format(path_name), "w", encoding="utf-8") as json_file:
           json.dump(jsonjson, json_file, indent=2, ensure_ascii = False)
    return jsonjson



# 간단한 json파일을 df와 csv파일로 만들기 복잡한것은 따로 자체 제작하여 만들어야함
def json_to_df_csv(jsonjson):
    df = pd.DataFrame(jsonjson)
    return df




# 간단한 json파일을 df와 csv파일로 만들기 복잡한것은 따로 자체 제작하여 만들어야함
def json_to_df_csv(jsonjson, key_s, path_name):
    """
    이 함수는 json을 넣으면 dataframe 으로 만들어 준다.
        jsonjson `Object`: json data
        key_s (str): "result||commentList" 처럼 "||"로 분리된다.
        path_name (str): "파일명.csv" 저장경로
    Retruns:
        df `Object`: dataframe을 돌려줌
    """
    if "||" in key_s:
        key_s = key_s.split("||")
        key_s2 = key_s[1]        
        key_s = key_s[0]
    df =""
    try:
        df = pd.json_normalize(jsonjson, key_s)
        try:
            df = df.set_index("index")
        except:
            pass
    except KeyError as e:
        pass
        # print(f"키에러 : {json.dumps(jsonjson, indent=4)}")
    except TypeError as e:
        pass
        # print(f"타입에러: {json.dumps(jsonjson, indent=4)}")

    if str(df) == "":
        jsonjson = jsonjson[key_s]
        try:
            df = pd.json_normalize(jsonjson,key_s2)
        except KeyError as e:
            df = pd.json_normalize(jsonjson)
    print(df)
    df.to_csv(path_name,index=False, mode='w', encoding='utf-8-sig')
    return df




