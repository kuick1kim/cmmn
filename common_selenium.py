# pip install --upgrade pip
# pip install selenium
# pip install beautifulsoup4 
# pip install requests


import pandas as pd
from bs4 import BeautifulSoup     
import json, requests , shutil, os
import urllib.request


import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time







def del_folder(folder_name):
    """
    폴더를 지우는 것이 불편하기 때문에 폴더를 지워준다
        folder_name (str): 폴더명을 넣어주면 된다. 
    """
    try:
        if folder_name not in os.listdir(): 
            os.mkdir(folder_name) ###폴더를 만듭니다. 
        else :
            shutil.rmtree(folder_name) ###폴더지우기
            time.sleep(0.3)
            os.mkdir(folder_name) ###폴더를 만듭니다. 
    except:
        input("파일이 열려있어서 지워지지 않아요 닫고 [Enter] 눌러 주세요 :   [Enter]    ")
        if folder_name not in os.listdir(): 
            os.mkdir(folder_name) ###폴더를 만듭니다. 
        else :
            shutil.rmtree(folder_name) ###폴더지우기
            time.sleep(0.3)
            os.mkdir(folder_name) ###폴더를 만듭니다. 

    time.sleep(0.3)




def driver1():
    ###################드라이버 세팅###########
    s= Service("c:/chrome/chromedriver.exe")
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("disable-gpu") 
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=s ,options=options)
    return driver


def open_selenium(driver, url):
   #네이버 로그인 페이지로 이동
    driver.get(url)


def refresh(driver):
    time.sleep(0.3)
    driver.refresh()





def screenshot(driver, save_filename):
    """
    다양한 엘레멘트가 있을때 요소를 csv로 저장한다
        driver `Object`: 엘레멘트를 찾기위해
        input_text (str): 저장하려는 파일명을 입력해줍니다        
    """
    print(save_filename)
    save_filename = save_filename.replace(":","-").replace('"','').replace('/','_').replace('*','').replace('@','').replace('?','')
    save_filename = save_filename.replace("&","-").replace(".","-")
    time.sleep(4.5)
    make_html(driver, save_filename)
    driver.save_screenshot('image/{}.png'.format(save_filename))


def make_html(driver, save_filename):
    """
    다양한 엘레멘트가 있을때 요소를 csv로 저장한다
        driver `Object`: 엘레멘트를 찾기위해
        input_text (str): 저장하려는 파일명을 입력해줍니다        
    """
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser').prettify()    

    html_file = open('image/{}.html'.format(save_filename), 'w', encoding='utf-8')
    html_file.write(str(soup))
    html_file.close()


def table_save(driver, save_name,table_num):
    """
    다양한 엘레멘트가 있을때 요소를 csv로 저장한다
        driver `Object`: 엘레멘트를 찾기위해
        save_name (str): 저장하려는 파일명을 입력해줍니다
        table_num (int): 현재페이지 안에서 몇번째 테이블인지 숫자를 넣어준다
    """
    soup = driver.page_source
    dd = pd.read_html(soup)
    print("이 페이지에는 테이블이 "+str(len(dd))+"개 있어요")

    df = pd.read_html(soup)[table_num]
    save_csv(df, "image/{}.csv".format(save_name) )







############################################################################
################ 전체 시스템 관련 ############################################
################ 전체 시스템 관련 ############################################
################ 전체 시스템 관련 ############################################
############################################################################




def zero_df():
    """
    공 데이터 프레임 만드는 함수
    Retruns:
        df `Object`: 빈 데이터 프레임을 하나 생성해준다
    """
    df = pd.DataFrame()
    return df



def elem_text_csv(xpath_list, path):
    """
    데이터 리스트가 들어가면 csv파일로 저장하는 로직
        xpath_list `Object`: 데이터 리스트가 들어가 있다
        path (str): 저장경로와 파일명을 입력해줍니다 "image/{}.csv" 같은 풀패스를 넣어줌
    """
    if len(xpath_list) > 2:
        df = zero_df()
        for i in xpath_list:
            print(i.text)
            data= {"0": [i.text]}
            df = make_csv(df, data, path)
        print("======{} 개의 요소가 들어 있습니다. =====".format(len(xpath_list)))


def make_csv(df, data, path):
    """
    기존 데이터 프레임에 한개의 데이터를 넣어주면, CSV를 저장해주는 함수
        df `Object`: 데이터 프레임을 입력한다
        data `Object`: 한 라인의 데이터를 넣어준다.
        path (str): 저장경로와 파일명을 입력해줍니다 
    Retruns:
        df `Object`: 합쳐진 데이터 프레임을 되돌려준다. 
    """
    df1 = pd.DataFrame(data)
    df = pd.concat([df,df1])
    df = df.reset_index(drop=True)
    save_csv(df, path)

    return df



def save_csv(df, path):
    """
    다양한 엘레멘트가 있을때 요소를 csv로 저장한다
        df `Object`: 데이터 프레임을 입력하여 저장한다
        path (str): 저장하려는 파일경로와 파일명을 입력해줍니다        
    """
    try:
        df.to_csv("{}".format(path), index=False, mode='w', encoding='utf-8-sig')    
    except:
        input("CSV 파일을 닫고 [Enter] 눌러 주세요 :   [Enter]")
        df.to_csv("{}".format(path), index=False, mode='w', encoding='utf-8-sig') 
    # print(df)  




def make_memojang_w(path):
    with open(path, "w", encoding='utf-8') as file:
        file.write("")
        file.close()

def make_memojang_add(path,text):
    with open(path, "a", encoding='utf-8') as file:
        file.write(text+"\n")
        file.close()

def make_memojang_add_list(path,text_list_elements):
    with open(path, "a", encoding='utf-8') as file:
        for a in text_list_elements:
            file.write(a.text+"\n")
        file.close()


############################################################################
################ 판다스 관련 #################################################
################ 판다스 관련 #################################################
################ 판다스 관련 #################################################
############################################################################
#클릭은 3가지다 1클릭 1은 기존방식으로 클릭
# text클릭은 

############################################################################
################ 클릭 관련 ##################################################
################ 클릭 관련 ##################################################
################ 클릭 관련 ##################################################
############################################################################


def elem_1_here(driver,  action_k, element_j): 
    """
    한개의 요소가 확인될때까지 찾는다. 
        driver `Object`: 기본 드라이버를 가져옴
        element_j (str): 요소의 주소를 가져옴
        action_k (str): 행동과 관련해서 변수를 주기위해 
    Retruns:
        xpath_here `Object`: 엘레멘트를 가지고 다양한 액션을 취할 수 있다. 
    """
    numb = 0
    while numb <= 100 :
        try: 
            if "click_path" in str(action_k) or "[" in str(element_j): #### xpath 기반으로 만든로직
                #### 여기는 XPATH 기반인 요소를 찾는다. 
                xpath_here = driver.find_element(By.XPATH, element_j)
                xpath_here.is_displayed()                
                break

            elif "click_1" in str(action_k) : #### 김민상이 만든로직으롤 찾음 
                xpath_here = class_part_logic(element_j) #### 요소를 만들어온다
                xpath_here = driver.find_element(By.XPATH, xpath_here)
                xpath_here.is_displayed()
                break

            elif "click_2" in str(action_k) : #### 김민상이 만든로직 요소만 찾고 클릭은 말아라
                num = int(action_k.split("+")[1])
                if "$" in str(element_j):
                    xpath_here = class_part_logic(element_j) #### 요소를 만들어온다
                elif "[" in str(element_j):
                    xpath_here = element_j
                xpath_here = driver.find_element(By.XPATH, xpath_here)[num]
                xpath_here.is_displayed()
                break

            elif "_text" in str(action_k): #### 간단하게 링크 텍스트로 요소를 찾고 싶을때
                xpath_here = driver.find_element(By.LINK_TEXT, element_j)
                xpath_here.is_displayed()
                break
            else:
                print("확인 좀 해봐라 뭔 action_k 글씨가 안맞나보다")
            
        except Exception as e:
            time.sleep(0.1)
            if numb % 20 == 0:
                print("============= element '{}'가 찾아지지 않고 있습니다. [{}회] =====".format(element_j, ))
            if numb % 100 == 0:
                print("============ 100번 찾았는데 더이상은 힘들어서 못찾겠다")
                break
        numb = numb + 1

    return xpath_here



def elem_2_here(driver, element_j, action_k ): 
    """
    다양한 엘레멘트가 있을때 요소를 csv로 저장한다
        driver `Object`: 엘레멘트를 찾기위해
        element_j (str): 특정 XPATH 경로가 온다. 
        action_k (str): 분류를 하기위해 데이터를 넣어줌
    Retruns:
        xpath_list `Object`: 리스트 모아진것을 다시 넘겨준다. 
    """

    try:        
        
        if "[" in str(action_k):
            xpath_list = driver.find_elements(By.XPATH, element_j)     
        elif "$" in str(action_k):
            xpath_here = class_part_logic(element_j) #### 요소를 만들어온다
            xpath_list = driver.find_elements(By.XPATH, xpath_here)

        else:
            print("xpath가 형식을 확인해 보세요")

        print(str(len(xpath_list))+ "개의 요소가 있습니다. ")
        
    except Exception as e:
        time.sleep(0.1)
        print("============ 아무것도 나오지 않았습니다.")

    if len(xpath_list) <2 :
        print("=====[{}개] 리스트가 몇개 안나오네 확인좀 해보세요======".format(len(xpath_list)))
        print("=====[{}개] 리스트가 몇개 안나오네 확인좀 해보세요======".format(len(xpath_list)))
        print("=====[{}개] 리스트가 몇개 안나오네 확인좀 해보세요======".format(len(xpath_list)))

    ####### 여기가 리스트로 온다. 
    return xpath_list




def class_part_logic(class_part):
    """
    class_part_logic 특정 형식으로 글씨를 입력하면 재가공 하는 함수이다. 
        class_part (str) : "index$1-text$하하-bounds$1134,153][1233,252]"  $로 스플릿됨 "|"로 스플릿됨 
    """
    class_part = class_part.split("-")
    kk ='//*[ '
    for i in class_part:
        i = i.split('$')
        kk = kk + "@"+i[0] +"='"+i[1]+"'" +" and "
    xpath_element = kk[:-5]+"]"
    return xpath_element

















def click_DBOX(driver, text1, xpath):
        try:
            time.sleep(0.4) 
            dropbox = driver.find_element(By.XPATH, xpath)
            dropbox.select_by_visible_text(text1)
        except:
            try:
                time.sleep(0.3) 
                dropbox = driver.find_element(By.XPATH, xpath)
                dropbox.select_by_visible_text(text1)
            except:
                time.sleep(1) 
                dropbox = driver.find_element(By.XPATH, xpath)
                dropbox.select_by_visible_text(text1)
    # dropbox.select_by_value('1')### 여기서 value가 있다면 몇번째 밸류로 쓸 수 있다 밸류번호로
    # dropbox.select_by_index(0) ### 인덱스중에 몇번째를 선택할 수 있다. 
    # dropbox.send_keys(text1)
    # driver.find_element_by_css_selector("#fruits01 [value='1']").click()
    # 여기는 소스들을 모아놓은 것이다. 



def click_N_input(driver, text1, xpath):
    try:
        time.sleep(0.2) 
        driver.find_element(By.XPATH, xpath).send_keys(text1)
    except:
        try:
            time.sleep(0.3) 
            driver.find_element(By.XPATH, xpath).send_keys(text1)
        except:
            time.sleep(1) 
            driver.find_element(By.XPATH, xpath).send_keys(text1)



def click_CW(driver):
    print("창변경")
    try:
        time.sleep(0.4) 
        driver.switch_to.window(driver.window_handles[-1]) ###마지막 창으로 변경해 준다
        # driver.switch_to.window(driver.window_handles[num])
    except:
        time.sleep(0.4) 
        driver.switch_to.window(driver.window_handles[-1]) ###마지막 창으로 변경해 준다
        # driver.switch_to.window(driver.window_handles[num])

def close_window(driver):
    driver.quit()





# 01 얼럿창 관리하기

def accept(driver): 
    """
    얼럿창이 뜨면 클릭하는 로직
        driver `Object`: 기본 드라이버를 가져옴
    """
    counta = 1    
    while counta <=500 :
        try:### 시도해봐 되면 여기서 끝내 안되면 아래로
            driver.switch_to.alert.accept()
            break
        except: ### 여기서 시도해봐 되면 끝내 안되면 아래로
            try:### 여기서 시도해봐 되면 끝내 안되면 아래로
                time.sleep(0.3)         
                driver.switch_to.alert.dismiss()
                break
            except: ### 여기서도 안되면, 카운트를 추가 하는거야 
                time.sleep(0.3) 
                counta += 1
                if counta == 500:
                    print("해봐도 안됨 억셉트 기다리다 오류냄")
                    break







def scroll(driver):
    #스크롤 내리기 이동 전 위치
    scroll_location = driver.execute_script("return document.body.scrollHeight")

    while True:
        #현재 스크롤의 가장 아래로 내림
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        
        #전체 스크롤이 늘어날 때까지 대기
        time.sleep(2)
        
        #늘어난 스크롤 높이
        scroll_height = driver.execute_script("return document.body.scrollHeight")

        #늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
        if scroll_location == scroll_height:
            break
            
        #같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
        else:
            #스크롤 위치값을 수정
            scroll_location = driver.execute_script("return document.body.scrollHeight")




















###############################################################
########## scroll 하는 곳#######################################
########## scroll 하는 곳#######################################
########## scroll 하는 곳#######################################
###############################################################



##### 창을 아래로 내리기
def scroll_down(driver, up_down,num):
    if up_down == "down":
        for i in range(num):
            # 끝까지 스크롤 다운
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 1초 대기
            time.sleep(1.3)
    elif up_down == "up":
        for i in range(num):
            # 끝까지 스크롤 다운
            driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
            # 1초 대기
            time.sleep(1.3)
            print(i)
    else:
        print("'up' 또는 'down'을 사용해 주세요")


def slow_up(driver):
    a =  int(driver.execute_script("return document.body.scrollHeight"))
    b = int(a/1000)    
    for i in range(b):        
        driver.execute_script("window.scrollTo({},{});".format(a, a-1000))
        a = a - 1000
        time.sleep(2)
    driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")    

def scroll_save(driver,element_j,count):
    a= 0
    for i in range(count):
        # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo({}, {});".format(a, a+1500))
        a = a+ 1500
        # 1초 대기
        time.sleep(2.5)
        save_image_all(driver, element_j)






###############################################################
########## image save 하는 곳#########################################
########## image save 하는 곳#########################################
########## image save 하는 곳#########################################
###############################################################
def save_image_all(name, xpath_list):
    count_j=0

    for img in xpath_list:

        img1 = img.get_attribute("src")
        try:
            name2 = img.get_attribute("alt")
            name2 = str(name2.replace("?","").replace(":","").replace("/","").replace("|","_").replace('"',''))
        except:
            name2 = ""
        # print(name2)
        urllib.request.urlretrieve(img1, "image/"+ name +"_"+ str(count_j).zfill(3)+"_"+name2+".jpg")
        count_j = count_j +1


###############################################################
########## 이미지 한개 추출#####################################
########## 이미지 한개 추출#####################################
########## 이미지 한개 추출#####################################
###############################################################

def get_one_image(driver, file_name, xpath_k):
    images = driver.find_element(By.XPATH, xpath_k)
    url = images.get_attribute('src')
    urllib.request.urlretrieve(url, "{}.jpg".format(file_name))


###############################################################
########## 이미지 여러개 추출###################################
########## 이미지 여러개 추출###################################
###############################################################

# 사용법  '/html/body/div[3]/div[2]/div/div[1]/section[2]/div/div[1]/div[1]/div[@data-cr-area="img"]'
def get_xpath_list(driver, xpath_k):
    xpath_list = driver.find_elements(By.XPATH, xpath_k) 
    return xpath_list


# xpath_list = driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/section[2]/div/div[1]/div[1]/div[@data-cr-area="img"]') 
# '/html/body/div[3]/div[2]/div/div[1]/section[2]/div/div[1]/div[1]/div[@data-cr-area="img"]'
# print(len(xpath_list))


## xpath 예제 "/html/body/div[3]/div[2]/div/div[1]/section[2]/div/div[1]/div[1]/div[@data-cr-area='img'][{}]/div/div[1]/a/img"
def get_image_all2(driver, len_xpath, xpath_k):
    
    for i in range(1,len_xpath,1):
        try:
            images= driver.find_element(By.XPATH, xpath_k.format(i))
            url = images.get_attribute('src')
            k = str(i).zfill(3)
            urllib.request.urlretrieve(url, "img/{}.jpg".format(k))

        except:
            print(i)
            pass




###############################################################
########## 이미지 한개 추출#####################################
########## 이미지 한개 추출#####################################
########## 이미지 한개 추출#####################################
###############################################################


def input_df(driver, tc_name, count_tc, start_time, df, text):
    endtime = time.time()-start_time ; start_time = time.time() ; count_tc = count_tc + 1 
    input_text = tc_name+ " ["+str(count_tc)+"] [time_"+str(format(endtime, ".2f"))+"] # "+text 
    print(input_text)
    data= {"테스트": [input_text], "시간":  [str(format(endtime, ".2f"))], "성공여부": ["PASS"]} 
    df = make_csv(df, data, "image/{}.csv".format(tc_name))    
    return df, count_tc, start_time

def input_screenshot(driver, tc_name, count_tc, start_time, df, text):
    endtime = time.time()-start_time ; start_time = time.time() ; count_tc = count_tc + 1 
    input_text = tc_name+ " ["+str(count_tc)+"] [time_"+str(format(endtime, ".2f"))+"] # "+text 
    data= {"테스트": [input_text], "시간":  [str(format(endtime, ".2f"))], "성공여부": ["PASS"]} 
    df = make_csv(df, data, "image/{}.csv".format(tc_name)) 
    screenshot(driver, input_text)
    return df, count_tc, start_time











