import requests
import time
from bs4 import BeautifulSoup
import os , json,shutil
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
 

from datetime import datetime

import smtplib
from email.message import EmailMessage


import psutil 




def post_c(url, headers, data):
    response = requests.post(url, headers=headers, data =data)
    if response.status_code == requests.codes.ok:
        
        data1 = str(response.text)  
        print(data1)

















# from twilio.rest import Client

def list_in_folder(path_dir):
    file_list = os.listdir(path_dir)
    return file_list


def REq(url , get_post):
    # print()
    # print(url)
    # print()

    if  "him-mobile" in url : #### 여기서는 일반텍스트로 나옴
        headers = {'Accept':'*/*'}         

    elif "hsu-mobile.cf.lguplus.com" in url : #### 여기서는 JSON 으로 나옴
        headers = {'Accept':'application/json'}

    elif "suf2." in url : #### 여기서는 JSON 으로 나옴
        headers = {'Accept':'application/json'}

    ############ 여기는 GET / POST 방식을 나누는곳 #########
    if get_post == "GET":
        # print(headers)
        # print("\t\t\t # API 호출중 현재 GET 방식입니다. ...======")
        response = requests.get(url, headers=headers)
    elif get_post == "POST" :
        # print("\t\t\t # API 호출중 현재 POST 방식입니다. ======")
        response = requests.post(url, headers=headers)
    elif get_post == "DELETE" :
        # print("\t\t\t # API 호출중 현재 POST 방식입니다. ======")
        response = requests.delete(url, headers=headers)
    else:
        print(" 'GET'/ 'POST' / 'DELETE' 방식 글씨를 잘못 넣었어요")


    if response.status_code == requests.codes.ok:
        

        if "m-mobile" in url : #### 여기서는 그냥 일반 텍스트로 가져온다. 
            data1 = str(response.text)  
        
        elif "su-mobile.cf" or "suf2." in url : #### json데이터만 따로처리한다. 
            data1 = response.content
            if data1 != "":
                soup = BeautifulSoup(data1, "html.parser").text
                data1 = json.loads(soup) ###처음에 파싱을 하고
                data1 = json.dumps(data1, indent=2, ensure_ascii = False)
                # print(data1) #### 여기는 나중에 지워라 보기 싫다.
                data1 = json.loads(data1) ###처음에 파싱을 하고
                with open("image/{}.json".format("임시저장"), "w", encoding="utf-8") as json_file:
                    json.dump(data1, json_file, indent=2, ensure_ascii = False)
                

    else :
        # print(str(response.status_code)+"==== url : "+url)        
        data1 = ""

    
    # print("접속시간 : ",end_time)
    return data1 

# data1 = REq(url , get_post)
#### 여기서 데이터가 나왔고 이 데이터를 다시 처리하게 넣어줘라. 









# 위에것 1번 성공
# 위에것 2번 기존 데이터 존재

# 아래것 1번 성공
# 아래것 2번 검색 결과 없음

def check_json(data, count, input_text, want_text): ### 사용법
    ### 1. json 데이터를 넣는다
    ### 2. count 는 2개 넣는다, 
    ### 3. input_text 몇개를 넣는데, 슬래쉬를 넣어서 분리를 한다
    ### 4. 결과를 원하는 텍스트를 넣는다. 
    if count == 2 :
        text0= input_text.split("|")[0] 
        text1= input_text.split("|")[1] 
        if data[text0][text1] == want_text:
            return True
        else : 
            return False
    elif count == 3 :

        text0= input_text.split("|")[0] 
        text1= input_text.split("|")[1] 
        text2= input_text.split("|")[2] 
        if data[text0][text1][text2] == want_text:
            return True
        else : 
            return False








def check_json_like(data, input_text, want_text): ### 사용법 좋아요확인할때만 사용한다. 
    ### 1. json 데이터를 넣는다
    ### 2. count 는 2개 넣는다, 
    ### 3. input_text 몇개를 넣는데, 슬래쉬를 넣어서 분리를 한다
    ### 4. 결과를 원하는 텍스트를 넣는다. 
    text0= input_text.split("|")[0] 
    text1= input_text.split("|")[1] 
    text2= input_text.split("|")[2] 

    a= data[text0]
    b = a[text1]
    try:
        c= b[text2]
        if c == want_text:
            return True
        else:
            print(c)
    except:
        c= b[0][text2]
        if c == want_text:
            return True
        else:
            c = b[0][text2][0]
            if c == want_text:
                return True
            else:
                return False
        
def check_json_002(data):
    album_name =  data['result']['list'][2]['dataset'][0]['name']
    album_id =  data['result']['list'][2]['dataset'][0]['id']

    return album_name,album_id





##### 여기는 응답이 나올때 까지 쏘는것

def api_logic(url, get_post, logic_object, text_k):
    count_k = 0 
    while text_k != logic_object:
        try :
            data1 = REq(url, get_post) ###데이터는 리퀘스트를 쏘면 나온다
            data1 = logic_object### 기존데이터 존재
            print(data1)
            return True
        except:
            print(count_k)
            time.sleep(0.5)
            count_k= count_k +1
            if count_k > 20:
                print("error===================================")
                return False
            pass









def kakao_call2(): ##### 여기는 토큰 발행하는 곳이다. 
    url = 'https://kauth.kakao.com/oauth/token'
    client_id = '89d89a6d3c629cf6754c931e14e82ca1'  #### #'여기를 변경'
    redirect_uri = 'https://example.com/oauth'      #### #'여기를 변경'
    code = 'Y3qy7Sxh4GGYtXijcGoUOtpc4uJ_2EBH5xd9hrHwH9lYXBnsgITyJr-yS6uVu6wIUimeKworDNQAAAGGvtNqyw' #'자신의 CODE 값'

    data = {
        'grant_type':'authorization_code',
        'client_id':client_id,
        'redirect_uri':redirect_uri,
        'code': code,
        }

    response = requests.post(url, data=data)
    tokens = response.json()

    #발행된 토큰 저장
    with open("input/token.json","w") as kakao:
        json.dump(tokens, kakao)






def kakao_call3(): ##### 여기는 토큰 발행하는 곳이다. 
    url = "https://kauth.kakao.com/oauth/token"
    data = {
    "grant_type" : "refresh_token",
    "client_id" : "874789",
    "refresh_token" : "LCou6Aw-SQbgTwQJ5htH5z9N8YoSqH9oAstLPsxVCinI2QAAAYa-1ah7"
    }
    response = requests.post(url, data=data)
    tokens = response.json()
    # print(response.json())

    with open("token.json","w") as fp:
        json.dump(tokens, fp)


##########################################################
def kakao_call(): ###### 여기는 카톡 보내는 곳이다. 
    with open("input/token.json","r") as kakao:
        tokens = json.load(kakao)

    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers={
        "Authorization" : "Bearer " + tokens["access_token"]
    }
    data = {
        'object_type': 'text',
        'text': '오류가 났습니다.',
        'link': {
            'web_url': 'https://developers.kakao.com',
            'mobile_web_url': 'https://developers.kakao.com'
        },
        'button_title': '키워드'
    }
    
    data = {'template_object': json.dumps(data)}
    response = requests.post(url, headers=headers, data=data)
    response.status_code
















##########################################################








def send_slack(mamasg): ###### 인터넷이 안되서 안보내지는 경우도 있었음
    # 웹훅으로 보낸다.   
    # 생성한 웹훅 주소
    url = 123#### 여기를 넣으세요
    title = '[오류발생]\t'*3
    content = '[모바일 오류가 발생했습니다.]  :pepe_rolling: [어서빨리 확인해 주세요]\n\n'*3
    jsonk={ 'text': title, ###### 여기는 알림창에 뜨는 내용입니다. 
                'blocks': [
                        
                        {   "type": "header",
                            "text": {   "type": "plain_text",    "text": title, }
                        },
                        {   "type": "divider"},                        
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "\n"
                                    },
                            "accessory": {
                                "type": "image",
                                "image_url": "https://pbs.twimg.com/profile_images/625633822235693056/lNGUneLX_400x400.jpg",
                                "alt_text": "cute cat"
                                    }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": content
                                     }
                        },
                        {
                            "type": "divider"
                        }
                        ]}  
    # 메시지 전송
    requests.post( url, headers={'content-type': 'application/json'}, json=jsonk )
    ########################################
    ######################################### 사진 몇장 보내기 
    SLACK_BOT_TOKEN = 123 #### 여기를 넣으세요  "f9fac51b02ab38f"  # 슬랙 봇의 API token
    CHANNEL_ID = 123##### 여기를 넣으세요 "D034F97PDNJ"  # 채널 ID
    # WebClient 인스턴스 생성
    client = WebClient(token=SLACK_BOT_TOKEN)

    # IMAGE_PATH = "aaa.png" # 업로드할 이미지 파일 경로
    #####################################################
    #####################################################

    ###################################################

    listk= list_in_folder("image")
    listk= [x for x in listk if ".png" in str(x)][-2:]  ###리스트에서 빼는 방법  
    if len(listk) == 0:
        print("사진이 없다.======================")
    for i in listk:
        file = "image/{}".format(i)

        upload=client.files_upload_v2(file=file,filename=file)
        mamasg=mamasg+"<"+upload['file']['permalink']+"| >"
    #### 여기가 호출 ###########################################
    
    client.chat_postMessage(
        channel=CHANNEL_ID, text=mamasg )
    
   
    ###################################################
    ################# Chat GPT가 만들어준###############
    # for i in listk:
    #     IMAGE_PATH = "image/{}".format(i)
    #     # 이미지 업로드
    #     try:
    #         response = client.files_upload(
    #             channels=CHANNEL_ID,
    #             file=IMAGE_PATH )
    #         print(f"File uploaded: {response['file']['name']}")
    #     except SlackApiError as e:
    #         print("Error uploading file: {}".format(e))











def send_email(to_someone, textk): #### 여기서는 자신의 비밀번호가 노출되어야 한다. 
    # textk= '[모바일 오류가 발생했습니다. 어서빨리 확인해 주세요]'
    # common_request.send_email('kuick1@naver.com', textk)####
    # STMP 서버의 url과 port 번호
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465

    # 1. SMTP 서버 연결
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

    EMAIL_ADDR = 'mzkuick1@mz.co.kr'
    EMAIL_PASSWORD = 123### 여기를 넣으세요'wbr'

    # 2. SMTP 서버에 로그인
    smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)

    # 3. MIME 형태의 이메일 메세지 작성
    message = EmailMessage()
    message.set_content(textk)
    message["Subject"] = "[오류발생] [모바일 오류발생] [오류발생]"
    message["From"] = EMAIL_ADDR  #보내는 사람의 이메일 계정
    message["To"] = to_someone

    # 4. 서버로 메일 보내기
    smtp.send_message(message)
    # smtp.quit()
    smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)
    smtp.send_message(message)
    # smtp.quit()
    smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)
    smtp.send_message(message)

    # 5. 메일을 보내면 서버와의 연결 끊기
    smtp.quit()
    print("MESSAGE : {}".format(textk))
    print("이메일 3개 전송완료하였습니다.")



def send_SMS(phone_number): ####send_SMS("01025713111")
    # Download the helper library from https://www.twilio.com/docs/python/install
    

    account_sid = 123#### 여기를 넣으세요 '392b44fe877'
    auth_token = 123#### 여기를 넣으세요'372f39083df49ed97'
    # client = Client(account_sid, auth_token)

    # message = client.messages \
    #                 .create(
    #                     body="연습해보는 것입니다. 잘 들어갑니까?",
    #                     from_='+15074458900',
    #                     to='+82{}'.format(phone_number)
    #                 )

    # print("잘 보냈슈{}".format(phone_number[1:]))





def kill_pid(ProcessName1):##### 여기서는 크롬드라이버가 있으면 항상 지울 것이다. 

    # common_request.kill_pid("UiPath.RobotJS.UserHost.exe")
    # common_request.kill_pid("adb.exe")
    # common_request.kill_pid("python.exe")
    for proc in psutil.process_iter():
        # print(proc)
        try:
            # 프로세스 이름, PID값 가져오기
            processName = proc.name()   #### pid에서 이름을 가져오세요
            processID = proc.pid        #### PID 번호를 가져오세요
    
            if processName == ProcessName1:
                print("지워진 process : " + processName , ' -', processID)
                parent_pid = processID  #PID
                parent = psutil.Process(parent_pid) # PID 찾기
                for child in parent.children(recursive=True):  #자식-부모 종료
                    child.kill()
                parent.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):   #예외처리
            pass













# GET 요청 보내기: 
# response = requests.get("https://www.example.com")
# print(response.text)

# GET 요청에 쿼리 매개변수 추가: 
# params = {"key1": "value1", "key2": "value2"}
# response = requests.get("https://www.example.com", params=params)
# print(response.text)

# HTTP 헤더 추가하기: 
# headers = {"User-Agent": "My App 1.0"}
# response = requests.get("https://www.example.com", headers=headers)
# print(response.text)




# POST 요청 보내기: 
# data = {"key1": "value1", "key2": "value2"}
# response = requests.post("https://www.example.com", data=data)
# print(response.text)


# JSON 데이터 보내기: 
# import json
# data = {"key1": "value1", "key2": "value2"}
# headers = {"Content-Type": "application/json"}
# response = requests.post("https://www.example.com", data=json.dumps(data), headers=headers)
# print(response.text)

# 상태 코드 확인하기: 
# response = requests.get("https://www.example.com")
# if response.status_code == 200:
#     print("Success!")
# else:
#     print("Failed with status code:", response.status_code)


# 응답 헤더 확인하기: 
# response = requests.get("https://www.example.com")
# print(response.headers)


# 예외 처리 추가하기: 
# try:
#     response = requests.get("https://www.example.com")
#     response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print("Request Error:", e)



# 세션 유지하기: 
# session = requests.Session()
# response = session.get("https://www.example.com")
# # 이제 같은 세션으로 여러 요청을 보낼 수 있음

# 인증 정보 전달하기: 
# from requests.auth import HTTPBasicAuth
# auth = HTTPBasicAuth("username", "password")
# response = requests.get("https://www.example.com", auth=auth)
# print(response.text)




# 파일 다운로드: 
# url = "https://www.example.com/somefile.zip"
# response = requests.get(url)
# with open("downloaded_file.zip", "wb") as file:
#     file.write(response.content)

# 세션 쿠키 관리: 
# session = requests.Session()
# session.get("https://www.example.com/login")
# # 세션을 통해 로그인 및 쿠키를 관리할 수 있음

# 리다이렉트 제어: 
# response = requests.get("https://www.example.com", allow_redirects=False)
# if response.status_code == 302:
#     print("Redirected to:", response.headers['Location'])

# 인코딩 처리: 
# response = requests.get("https://www.example.com")
# response.encoding = "utf-8"  # 수동으로 인코딩 설정
# print(response.text)

# 타임아웃 설정: 
# try:
#     response = requests.get("https://www.example.com", timeout=5)  # 최대 5초 대기
#     print(response.text)
# except requests.exceptions.Timeout:
#     print("Request Timed Out")

# 사용자 정의 예외 처리: 
# class CustomException(Exception):
#     pass
# try:
#     response = requests.get("https://www.example.com")
#     if response.status_code != 200:
#         raise CustomException("Request failed with status code:", response.status_code)
# except CustomException as e:
#     print(e)

# 사용자 정의 헤더와 쿠키 설정: 
# headers = {"User-Agent": "My App 1.0"}
# cookies = {"session_id": "abcdef123456"}
# response = requests.get("https://www.example.com", headers=headers, cookies=cookies)

# JSON 응답 처리: 
# response = requests.get("https://api.example.com/data.json")
# data = response.json()  # JSON 응답을 파이썬 딕셔너리로 파싱

# 세션 프록시 설정: 
# proxies = {
#     "http": "http://proxy.example.com:8080",
#     "https": "https://proxy.example.com:8080"
# }
# response = requests.get("https://www.example.com", proxies=proxies)

# 멀티파트 파일 업로드: 
# files = {'file': open('file.txt', 'rb')}
# response = requests.post("https://www.example.com/upload", files=files)



# response.text: HTTP 응답의 본문 텍스트를 반환합니다.

# response.status_code: HTTP 응답의 상태 코드를 반환합니다. 예를 들어, 200은 "성공"을 나타냅니다.

# response.headers: HTTP 응답의 헤더 정보를 포함하는 딕셔너리를 반환합니다.

# response.json(): HTTP 응답의 JSON 데이터를 파싱하여 파이썬 객체로 반환합니다. 이 메서드는 JSON 응답을 다룰 때 유용합니다.

# response.content: HTTP 응답의 바이너리 데이터를 반환합니다. 주로 이미지, 파일 다운로드 등의 작업에서 사용됩니다.

# response.url: HTTP 요청 후 최종적으로 연결된 URL을 반환합니다. 리다이렉션 발생 시 유용합니다.

# response.raise_for_status(): HTTP 응답의 상태 코드를 확인하고, 상태 코드가 에러(4xx 또는 5xx)일 경우 예외를 발생시킵니다.

# response.cookies: HTTP 응답에서 받은 쿠키 정보를 포함하는 RequestsCookieJar 객체를 반환합니다. 쿠키를 읽거나 설정하는 데 사용됩니다.

# response.headers.get('Header-Name'): 특정 헤더의 값을 가져올 때 사용합니다. 'Header-Name'에 헤더 이름을 지정하면 해당 헤더의 값을 반환합니다.

# response.request: 현재 응답과 관련된 원래 요청 객체에 접근할 때 사용합니다. 원본 요청에 대한 정보를 확인하거나 수정할 수 있습니다.

# response.encoding: HTTP 응답의 텍스트 인코딩을 나타내는 문자열을 반환합니다. 보통 이 값을 자동으로 설정하지만, 필요한 경우 수동으로 설정할 수 있습니다.

# response.iter_content(chunk_size): HTTP 응답의 내용을 일정 크기(chunk_size)로 나누어 제너레이터로 반환합니다. 대용량 파일 다운로드 시 유용합니다.

# response.iter_lines(chunk_size): HTTP 응답의 내용을 줄 단위로 나누어 제너레이터로 반환합니다. 텍스트 데이터를 줄 단위로 처리할 때 유용합니다.

# response.elapsed: 요청이 보내진 후 서버 응답까지 걸린 시간을 나타내는 timedelta 객체를 반환합니다.

# response.history: 리다이렉션을 따라 이동한 모든 중간 응답을 나타내는 리스트를 반환합니다. 이전 응답을 확인할 때 유용합니다.

# response.is_redirect: 응답이 리다이렉트인지 여부를 확인하는 불리언 값을 반환합니다.

# response.ok: 응답이 성공(상태 코드 200-299)인 경우 True를, 그렇지 않으면 False를 반환합니다.

# response.links: HTTP 응답의 Link 헤더를 파싱하여 링크 정보를 담은 딕셔너리를 반환합니다. 관련 링크를 쉽게 추출할 수 있습니다.

# response.close(): HTTP 응답과 관련된 리소스를 닫습니다. 일부 경우에는 자동으로 호출되지만, 명시적으로 호출할 수도 있습니다.

# response.raise_for_redirect(): 응답이 리다이렉트(3xx) 상태 코드인 경우 예외를 발생시킵니다. 이를 사용하여 리다이렉션을 처리할 수 있습니다.
