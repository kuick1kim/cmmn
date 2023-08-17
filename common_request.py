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
    url = #### 여기를 넣으세요
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
    SLACK_BOT_TOKEN = #### 여기를 넣으세요  "f9fac51b02ab38f"  # 슬랙 봇의 API token
    CHANNEL_ID = ##### 여기를 넣으세요 "D034F97PDNJ"  # 채널 ID
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
    EMAIL_PASSWORD = ### 여기를 넣으세요'wbr'

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
    

    account_sid = #### 여기를 넣으세요 '392b44fe877'
    auth_token = #### 여기를 넣으세요'372f39083df49ed97'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="연습해보는 것입니다. 잘 들어갑니까?",
                        from_='+15074458900',
                        to='+82{}'.format(phone_number)
                    )

    print("잘 보냈슈{}".format(phone_number[1:]))





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

