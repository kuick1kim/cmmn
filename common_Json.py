##### 여기는폴더에다 넣고 돌리면 모두 합쳐지는 프로그램이다. 




import pandas as pd
import os, json
import time
import pandas as pd

# json_data = json.loads(data)
def json_dumps(data):
    data = json.dumps(data, ensure_ascii=False, indent=3)
    print(data)
    return data
    

def list_to_oneline(data):
    text =""
    for i in data:
        text = text+i+" | "
    return text



def open_json(path):
    with open(path, 'r', encoding="utf-8") as json_file:
        temp = json.load(json_file)
    return temp


##### 1. 모든 폴더에 있는 모든 json리스트 가져오기
def get_folder_list(file_path):   
    listk =[]
    for filename in os.listdir(file_path): #인풋 폴더안에 json 파일을 모두 읽어서 데이터 프레임으로 만든다
        if '.json' in filename:
            print(filename)
            listk.append(filename)
    return listk

##### 2. json내용 임포트
def get_json_temp(file_path):
    # json 파일 읽어오기
    with open('{}'.format(file_path), 'r', encoding="utf-8") as json_file:
        temp = json.load(json_file)
    return temp



##### 3. json 저장

def save_json(temp, file_path):
    
    with open('{}'.format(file_path), 'w', encoding="UTF-8") as f:
        json.dump(temp, f, ensure_ascii=False, indent=4)

##### 글씨 입력
##### 글씨 입력
# allk['info']['name'] = "검증팀_김민상의_IMCS시험자동화_PHASE99-1"

##### 판다스 그냥 데이터 합치기
# df2 = pd.DataFrame()  
# df2 = pd.concat([df2, pd.DataFrame({'API':i["name"],'파일': filename.split(".")[0]},index = [numk])])##### 이건 전체데이터이다. 
                




########### temp를 넣기만하면 자동으로 구조가 나온다. 
# yeobak = ""
# common_json.forfor1(temp, yeobak)

###########1단계
def forfor1(temp, yeobak):     
    ####################################################    
    ########## 여기는 이너 함수 ##############################    
    def listlist1(temp,yeobak): #### 리스트면 여기로 들어오세요
        number = 0
        print("{}리스트 갯수 :  ".format(yeobak)+str(len(temp)))
        #### temp 원래는 temp items 여야한다. 
        try: ### temp[0]이 오류가 날때가 있어요
            for kk,vv in temp[0].items(): ### 여기는 분명히 리스트이기 때문에 여기로 온것이다. 
                number +=1
                yeobak2 = yeobak+ "\t"               
                print("{}".format(yeobak2)+"[{}] : ".format(number)+kk)     
                if isinstance(vv, dict):                
                    yeobak2 = yeobak+ "\t\t"
                    forfor1(vv,yeobak2) 
                elif isinstance(vv, list):
                    yeobak2 = yeobak+ "\t"    
                    listlist1(vv,yeobak2)
                elif isinstance(vv, str):
                    pass  
                elif isinstance(vv, int):
                    pass    
                else:
                    yeobak2 = yeobak+ "\t"               
                    print("{}".format(yeobak2)+"[{}] : ".format(number)+kk)    
        except:         
            number +=1   
            yeobak2 = yeobak+ "\t"     
            if isinstance(temp[0], dict):    
                pass
            elif isinstance(temp[0], list):
                listlist1(temp[0],yeobak2)
            else:
                print("{}".format(yeobak2)+"[{}] : ".format(number)+temp[0]) 
    ####################################################    
    ########## 여기는 함수 ##############################        

    ####################################################    
    ########## 여기가 실제 ############################## 
   
    if isinstance(temp, list):

        listlist1(temp,yeobak) 
    if isinstance(temp, dict):
        number = 0
        for k,v in temp.items():
            number += 1
            print("{}".format(yeobak)+"[{}] : ".format(number)+k)
            if isinstance(v, dict):  #### 딕셔너리 다시 원점으로 들어오세요              
                yeobak2 = yeobak+ "\t"
                forfor1(v,yeobak2) 
            elif isinstance(v, list): #### 리스트면 중간 함수로 들어오세요
                # yeobak2 = yeobak+ "\t"
                listlist1(v,yeobak) 
            elif isinstance(v, str): #### 텍스트면 패스
                pass        
            elif isinstance(v, str):
                # print("몰라자샤str") 
                pass
    
            elif isinstance(v, int):
                # print("몰라자샤int") 
                pass    
            else:
                pass
                # yeobak2 = yeobak+ "\t"               
                # print("{}".format(yeobak2),k)    
        print()



def ImportJson_sub(file_path):
   
    for filename in os.listdir(file_path): #인풋 폴더안에 json 파일을 모두 읽어서 데이터 프레임으로 만든다
        if '.json' in filename:
            print("\n\n\n")
            print(filename)
            
            # json 파일 읽어오기
            with open('{}/{}'.format(file_path,filename), 'r', encoding="utf-8") as json_file:
                temp = json.load(json_file)

    yeobak = ""
    forfor1(temp, yeobak)



if __name__ == "__main__":
    ImportJson_sub(".")
   