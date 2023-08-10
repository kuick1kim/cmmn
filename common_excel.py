import pandas as pd
import common_selenium
import time



def path_c(file_name): 
    path1= "C:/Users/MZ-USER/Desktop/{}".format(file_name)
    return path1

def DI2_call_excel(path_name, sheet_namek):
    df = pd.read_excel(path_name, sheet_name=sheet_namek, engine ='openpyxl')   
    return df







def from_excel_click(driver, dfii, df, tc_name, count_tc,start_time):
    countkk = 0
    while True: 
        if countkk < 10:
            print(countkk)
        
        countkk +=1
    #### 시간이 여기에서 체크 시작됨
    """
    엑셀에서 데이터 프레임의 내용을 받아 수행하는 함수입니다.
        driver (webdriver): 기본적인 웹드라이버
        dfii `Object`: 엑셀에서 호출한 데이터 프레임이 옵니다. 
        df `Object`: 결과물을 저장중인 데이터 프레임이 옵니다. 
        tc_name (str): tc 이름을 넣어서 저장용으로 사용하려고 합니다. 
        count_tc (int): 저장용으로 사용할 실행 번호입니다. 
    Retruns:
        count_tc (int) : 번호를 다시 돌려주어 계속 진행하게 해줍니다. 
        df `Object` : 데이터 프레임을 돌려주어 리포트를 쓸수 있게한다
        start_time (time) : 시간을 돌려주어 계속 시간을 사용할 수 있게 한다. 
    """      
    #############  첫번째 for문 확인하기 ####################################
    #############  첫번째 로직 체크를 할것인가?###############################  

    for action_k,element_j,back_key,next_sheet_a in zip(dfii['action'],dfii['element'],dfii['back_key'],dfii['next_sheet']):
        ######## 여기는 사이트 오픈 ##################################################
        if "open" in str(action_k) : ### 여기는 로딩이 안될때 휴식
            common_selenium.open_selenium(driver, element_j)
            df, count_tc, start_time= common_selenium.input_screenshot(driver, tc_name, count_tc, start_time, df, "[{}] 사이트 오픈".format(element_j))
        

        elif action_k == "check" or action_k == "": ### NO가 아니면 체크를 한다
            xpath_here=common_selenium.elem_1_here(driver, element_j, action_k)
            text_k = "["+element_j.replace("$","-").replace("|","-")+ "]- 확인되었습니다. "  ## $로하면 엑셀저장안됨
            df, count_tc, start_time= common_selenium.input_df(driver, tc_name, count_tc, start_time, df , text_k)

            # df, count_tc, start_time = check_logic(driver, element_j, tc_name, count_tc, start_time, df)
        ##############################################
        ##############################################
        elif "elem_" in str(action_k):

            if "_1_" in str(action_k):
                xpath_here = common_selenium.elem_1_here(driver,element_j, action_k)

            ##### 여러개의 요소를 찾으려면 여기로 들어와야 한다. 
            ##### 여기는 여러개 요소여야만 한다. 변경하라
            elif "_2_" in str(action_k):
                xpath_list = common_selenium.elem_2_here(driver,element_j, action_k)
                
                
        elif "elems_" in str(action_k):
            if "text_csv" in str(action_k):
                xpath_list = common_selenium.elem_2_here(driver,element_j, action_k)
                ##### CSV파일로 만든다. 
                common_selenium.elem_text_csv(xpath_list, "image/{}.csv".format(count_tc))
                df, count_tc, start_time= common_selenium.input_screenshot(driver, tc_name, count_tc, start_time, df,"elements 데이터를 [{}.csv]에 저장했습니다. 없으면 내용이 없는것 ".format(count_tc))     
        
                
                

        ##############################################
        ########### 타임 슬립 관련#####################
        elif "timesleep" in str(action_k) : ### 여기는 로딩이 안될때 휴식
            time_k = int(action_k.split("_")[1])
            time.sleep(time_k)                    
            df, count_tc, start_time= common_selenium.input_df(driver, tc_name, count_tc, start_time, df, str(time_k)+"초 sleep")

        ##############################################
        ########### 클릭 관련 #########################
        elif "click" in str(action_k): ##### 클릭1 이라는 요소가 있을때는 클릭해서 들어갑니다. 

            try:
                #### 
                if "click_1" in str(action_k) or "_1" in str(action_k) or "_path" in str(action_k) or "_text" in str(action_k): ### 동일하지 않을때 사용함  
                    xpath_here=common_selenium.elem_1_here(driver, element_j, action_k) ; xpath_here.click()               

                ####### 스크린샷 찍으세요 - 클릭했으면 ###########
                text_k = "["+element_j.replace("$","-").replace("|","-")+ "]- clicked"  ## $로하면 엑셀저장안됨 클릭후 1초후 저장
                df, count_tc, start_time= common_selenium.input_screenshot(driver, tc_name, count_tc, start_time, df, text_k)   

                #### 클릭했으면 다음시트에 들어가서 할일이 있는가?
                if next_sheet_a != "NO":
                    dfkk = DI2_call_excel(path_c(), next_sheet_a) ### 여기패스는 path_c() 에서 가져온다
                    count_tc, df, start_time = from_excel_click(driver, dfkk, df, tc_name, count_tc,start_time)  
                                    
                #### 뒤로가기를 뭐로 누를 것인가?
                if back_key == "home_back": #### 백키가 있으면 백키를 누르고 아니면 그냥 넘어간다.
                #### 반드시 클릭을 했다면 뒤로나오기 키를 사용해야합니다. 
                #### 아이들나라에서는 뒤로가기가 없을때는 다음키를 누르고
                #### 있을때는 되돌아 나오기 키를 누르려고 준비해 놨습니다.  
                    driver.back()
                    time.sleep(0.1)
                elif "$" in back_key:
                    xpath_here=common_selenium.elem_1_here(driver, element_j, action_k) ; xpath_here.click()   
                elif back_key == "driver":
                    driver.back()
                    time.sleep(0.1)
                    driver.refresh()
                    time.sleep(0.4)
                elif back_key == "NO" or back_key =="no" or back_key =="":
                    pass
                else:
                    pass
                
            except Exception as e:
                data= {"테스트": ["이유를 모르는 오류가 남"], "시간":  [str(format(time.time()-start_time, ".2f"))], "성공여부": ["-FAIL-"]} ;  df = common_selenium.make_csv(df, data, "image/{}.csv".format(tc_name)) 
                print("없어요---"+e)

        #####################################################################################
        #####################################################################################
        elif "scroll" in str(action_k): ##### 앞으로 이동하는 로직을 짜려고 합니다. 

            if "scroll+up+" in str(action_k) or "scroll+down+" in str(action_k):
            #### 아래로 이동
                scroll_a = action_k.split("+")
                common_selenium.scroll_down(driver, scroll_a[-2],int(scroll_a[-1]))    
                text_k ="["+scroll_a[-2]+" "+str(scroll_a[-1])+ "회] 스크롤함"
                df, count_tc, start_time= common_selenium.input_screenshot(driver, tc_name, count_tc, start_time, df, text_k)            
            
            elif "slowup" in str(action_k):
                common_selenium.slow_up(driver)
                df, count_tc, start_time= common_selenium.input_screenshot(driver, tc_name, count_tc, start_time, df, "거꾸로 올렸습니다.")

            elif "scroll+save" in str(action_k): ##### 스크롤 하면서 이미지를 다운 합니다. 
                common_selenium.scroll_save(driver,element_j,int(action_k.split("+")[-1]))
                df, count_tc, start_time= common_selenium.input_screenshot(driver, tc_name, count_tc, start_time, df, "스크롤 하고 세이브합니다")


        #####################################################################################
        #####################################################################################
        ##### 이미지 세이브하기 ##############################################################
        elif "save_image" in str(action_k):
            if "save_image_all" in str(action_k):
                name = element_j.split("+")[1]
                element_jj = element_j.split("+")[0]
                xpath_list = common_selenium.elem_2_here(driver,element_jj, action_k)

                common_selenium.save_image_all(name, xpath_list)                
                df, count_tc, start_time= common_selenium.input_screenshot(driver, tc_name, count_tc, start_time, df, "이미지를 모두 저장합니다. [{}]개 ".format(len(xpath_list)))

        #####################################################################################
        #####################################################################################
        ##### 테이블 가져오기 ##############################################################
        elif "table" in str(action_k):
            table_num = int(action_k.split("+")[-1])
            common_selenium.table_save(driver, element_j, table_num , count_tc)
            df, count_tc, start_time= common_selenium.input_screenshot(driver, tc_name, count_tc, start_time, df, "{}번째 테이블을 저장 filename: {}.csv".format(table_num, element_j))

        #####################################################################################
        #####################################################################################

        else:
            print("======================================")

    return count_tc, df, start_time















def check_logic(driver,  element_j, tc_name, count_tc, start_time, df):     

    if common_selenium.display_elem(driver, element_j):
        endtime = time.time()-start_time ; start_time = time.time() ; count_tc = count_tc + 1 ; element_2= element_j.replace("$","-").replace("|","-")## $로하면 엑셀저장안됨
        input_text = tc_name+ " ["+str(count_tc)+"] [time_"+str(format(endtime, ".2f"))+"] # ["+element_2+ "]- PASS-checked" 
        print(input_text)
        data= {"테스트": [input_text], "시간":  [str(format(endtime, ".2f"))], "성공여부": ["PASS"]} 
        df = common_selenium.make_csv(df, data, "image/{}.csv".format(tc_name)) 
    else:
        endtime = time.time()-start_time ; start_time = time.time() ; count_tc = count_tc + 1 ; element_2= element_j.replace("$","-").replace("|","-")## $로하면 엑셀저장안됨
        input_text = tc_name+ " ["+str(count_tc)+"] [time_"+str(format(endtime, ".2f"))+"] # ["+element_2+ "]- [[[ERROR]]]-checked" 
        data= {"테스트": [input_text], "시간":  [str(format(endtime, ".2f"))], "성공여부": ["-FAIL-"]} 
        df = common_selenium.make_csv(df, data, "image/{}.csv".format(tc_name)) 

        print("없어요 오류 ------------------------------------")
    return df, count_tc, start_time

def check_logic_text(driver, element_j, tc_name, count_tc, start_time, df):    
    if common_selenium.display_elem_text(driver, element_j):################################### 여기가 다르다
        endtime = time.time()-start_time ; start_time = time.time() ; count_tc = count_tc + 1 ; element_2= element_j.replace("$","-").replace("|","-")## $로하면 엑셀저장안됨
        input_text = tc_name+ " ["+str(count_tc)+"] [time_"+str(format(endtime, ".2f"))+"] # ["+element_2+ "]-PASS-checked" ;  print(input_text)
        data= {"테스트": [input_text], "시간":  [str(format(endtime, ".2f"))], "성공여부": ["PASS"]} 
        df = common_selenium.make_csv(df, data, "image/{}.csv".format(tc_name)) 
    else:
        endtime = time.time()-start_time ; start_time = time.time() ; count_tc = count_tc + 1 ; element_2= element_j.replace("$","-").replace("|","-")## $로하면 엑셀저장안됨
        input_text = tc_name+ " ["+str(count_tc)+"] [time_"+str(format(endtime, ".2f"))+"] # ["+element_2+ "]-[[[ERROR]]]-checked" 
        data= {"테스트": [input_text], "시간":  [str(format(endtime, ".2f"))], "성공여부": ["-FAIL-"]} 
        df = common_selenium.make_csv(df, data, "image/{}.csv".format(tc_name)) 
        print("없어요 오류 ------------------------------------")
    return df, count_tc, start_time


def check_logic_path(driver, element_j, tc_name, count_tc, start_time, df):    
    if common_selenium.display_elem_path(driver, element_j):################################### 여기가 다르다
        endtime = time.time()-start_time ; start_time = time.time() ; count_tc = count_tc + 1 ; element_2= element_j.replace("$","-").replace("|","-")## $로하면 엑셀저장안됨
        input_text = tc_name+ " ["+str(count_tc)+"] [time_"+str(format(endtime, ".2f"))+"] # ["+element_2+ "]-PASS-checked" ;  print(input_text)
        data= {"테스트": [input_text], "시간":  [str(format(endtime, ".2f"))], "성공여부": ["PASS"]} 
        df = common_selenium.make_csv(df, data, "image/{}.csv".format(tc_name)) 
    else:
        endtime = time.time()-start_time ; start_time = time.time() ; count_tc = count_tc + 1 ; element_2= element_j.replace("$","-").replace("|","-")## $로하면 엑셀저장안됨
        input_text = tc_name+ " ["+str(count_tc)+"] [time_"+str(format(endtime, ".2f"))+"] # ["+element_2+ "]-[[[ERROR]]]-checked" 
        data= {"테스트": [input_text], "시간":  [str(format(endtime, ".2f"))], "성공여부": ["-FAIL-"]} 
        df = common_selenium.make_csv(df, data, "image/{}.csv".format(tc_name)) 
        print("없어요 오류 ------------------------------------")
    return df, count_tc, start_time














def from_excel_click22(driver):
    countkk = 0
    while True: 
        if countkk < 10:
            rowk = input("행 번호를 넣으세요 치세요 : ")
            dfii= DI2_call_excel(path_c("google.xlsx"), "lab")
            dfii = dfii.iloc[rowk-1:rowk,:]
            print(dfii)


            print(countkk)
        else:
            break
        
        countkk +=1
    