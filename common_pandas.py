from cgitb import reset
# import common
import pandas as pd
from pandas import  DataFrame
import os, time, shutil
import configparser




def getTime(needs): #### needs 는 Y-M-D-H-m-S 형식으로 "-"로 분리한다. 
    now = time
    ktime = str(now.strftime('%Y-%m-%d-%H-%M-%S'))
    ktime = ktime.split("-")
    Y,M,D,H,m,S = ktime[0],ktime[1],ktime[2],ktime[3],ktime[4],ktime[5]
    mtime = ""
    if "Y" in needs:
        mtime = mtime + Y[-2:]
    if "M" in needs:
        mtime = mtime + M
    if "D" in needs:
        mtime = mtime + D
    if "H" in needs:
        mtime = mtime + H
    if "m" in needs:
        mtime = mtime + m
    if "S" in needs:
        mtime = mtime + S
    return mtime
    

def meke_folder(folder_name):
    try:
        if folder_name not in os.listdir(): 
            os.mkdir(folder_name) ###폴더를 만듭니다. 
    except:
        pass
        print(folder_name)


def del_folder(folder_name): ### 폴더를 지우고 다시 만드는 로직
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








def list_in_folder(path_dir):
    file_list = os.listdir(path_dir)
    return file_list

#### 리스트에서 한파일만 가져올때

#### 리스트에서 여러파일을 가져올때 

def list_minus(listk, jogun):
    # [x for x in listk if ".png" in str(x)]
    ### 리스트중에 특정조건을 추출해낸다. 예를들면 csv파일 같은것
    file_list= [x for x in listk if jogun in str(x)]
    return file_list











######################################################
###############  1. BASIC ############################
###############  1. BASIC ############################
###############  1. BASIC ############################
######################################################



def zero_df():
    """
    공 데이터 프레임 만드는 함수
    Retruns:
        df `Object`: 빈 데이터 프레임을 하나 생성해준다
    """
    df = pd.DataFrame()
    return df












# df 불러오기 CSV에서 특정 파일명 불러오기(주소만 있으면 불러올 수 있음)
def A01_call_csv(path_name):
    """
    오픈하는 함수
        path_name(str): 어디에 있는지 주소만 넣어주면됨
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    df = pd.read_csv(path_name,low_memory=False)    
    #### sep ="|", sep = "\t" 로변경하여 컴마가 아닐 경우에도 사용가능하다
    #### encoding = 'utf-8' , encoding ='cp949' 로 변경가능 하다. 
    #### 열면서 컬럼명을 바로 변경하며 열 수 있다. 오픈하자마자 컬럼을 변경가능
    # df = pd.read_csv(path_name, low_memory=False,  names=['1','2','3','4'])   
    return df




## 엑셀 불러오기
def A02_call_excel(path_name, sheet_namek):### 시트이름이 필요합니다.
    df = pd.read_excel(path_name, sheet_name=sheet_namek, engine ='openpyxl')   
    return df





# csv만들기
def A03_make_csv(df,path_name): ######저장된 엑셀넣는것 df와 시트명을 넣어주세요     
    try:
        df.to_csv(path_name,index=False, mode='w', encoding='utf-8-sig')
    except:
        print("여기가 나오면 저장오류 : 그래도 파일은 생성되게 만들었어요[저장오류]")
        print("다음번에는 프로그램 수행중에 csv파일을 꺼주세요")
        print("파일 끄고 [[Enter]] 누르세요 : 알겠지요? ")
        print("파일 끄고 [[Enter]] 누르세요 : 알았습니까? ")
        input("파일 끄고 [[Enter]] 누르세요 : 진짜로?")
        df.to_csv(path_name,index=False, mode='w', encoding='utf-8-sig')
        print("============================================================")
        print("잘 하셨습니다. 저장완료 파일명 :  {}\n".format(path_name)*3)

    # os.startfile(path_name)




# excel 저장하기
def A04_make_excel(df,sheet_nameA,path_file_name): ######저장된 엑셀넣는것 df와 시트명을 넣어주세요
    if not os.path.exists('{}'.format(path_file_name)):
        df.to_excel('{}'.format(path_file_name), index=False, sheet_name=sheet_nameA )
        # with pd.ExcelWriter('{}'.format(path_file_name), mode='w', engine='openpyxl'  ) as writer:
        #     df.to_excel(writer, index=False, sheet_name=sheet_nameA ,encoding="UTF-8" )
        #     writer.save()
    else:
        try:
            df.to_excel('{}'.format(path_file_name), index=False, sheet_name=sheet_nameA ,encoding="UTF-8" )
            # with pd.ExcelWriter('{}'.format(path_file_name), mode='a', engine='openpyxl' , if_sheet_exists='replace') as writer:  ######## 여기가 나온것은 엑셀파일이 열린것 같다
            #     df.to_excel(writer, index=False, sheet_name=sheet_nameA,encoding="UTF-8" )
            #     writer.save()
        except:
            print("파일 끄고 [[Enter]] 누르세요 : 알겠지요? ")
            print("파일 끄고 [[Enter]] 누르세요 : 알았습니까? ")
            input("파일 끄고 [[Enter]] 누르세요 : 진짜로?")
            df.to_excel('{}'.format(path_file_name), index=False, sheet_name=sheet_nameA ,encoding="UTF-8" )
            # with pd.ExcelWriter('{}'.format(path_file_name), mode='w', engine='openpyxl' , if_sheet_exists='replace') as writer:  ######## 여기가 나온것은 엑셀파일이 열린것 같다
            #     df.to_excel(writer, index=False, sheet_name=sheet_nameA,encoding="UTF-8" )
            #     writer.save()
    print("잘 하셨습니다. 저장완료 파일명 :  {}\n".format(path_file_name)*3)
    # os.startfile(path_file_name)




#### 여기는 어떤 폴더안에 여러 CSV파일을 한줄로 저장하면 들러 붙이는 용도임
def A05_concat(path_name): ###폴더를 넣어주면 그안에 csv파일을 가져와서 붙임
    df = pd.DataFrame()  
    for filename in os.listdir(path_name):  ### 폴더에 어떤 파일이 있느뇨....
        if '.csv' in filename:              ### 그중에 csv파일만 가져오라하느뇨.... 
            ff = path_name+"/"+filename     ### 폴더이릉에 파일이름을 붙여서 오픈하였느뇨       
            df2 = pd.read_csv(ff, low_memory=False)  
            df= pd.concat([df,df2])
    return df
       



# 데이터를 넣으면 concat으로 붙는 함수
# 여러개를 붙일때는 그냥 손으로 써라. 
# 여기서 데이터 양이 다를 경우 라인이 안맞을 수 있다. 인덱스 정렬이 필요할 수 있다. 
# df2 = df2.reset_index(drop=True) ### 여기서 재정렬이 필요할 수 있다. 
def A06_concat_01(df1, df2, oo_8): ### 문자로 "8"을 넣거나 문자로 "oo" 를 넣으면 된다. 
    if oo_8 == "8":
        df = pd.concat([df1,df2], axis=0)
    if oo_8 == "oo":
        df = pd.concat([df1,df2], axis=1)
    
    # print(df)
    return df






def A07_input_data(df, data):
    """
    이 함수는 데이터를 넣기 어려울때 값만 넣어주면 기존 df에 추가하는 함수입니다.  
        df `Object`: 표 
        data (str): 바꿔줄 컬럼명을 '||' 으로 분리합니다. 
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    #사용예 # data = "getkmsList||getkms_VTC1||GET||주소 없슈" ### 사용 예
    #사용예 # common_pandas.z06_input_data(df, data) ### 사용예

    dic1 = {} ### 공 딕셔너리를 넣어준다. 
    data = data.split("||") ### 데이터를 나눠준다. 
    for i, j in zip(df.columns, data):
        dic1[i]= j
    df1 = pd.DataFrame([dic1])
    df = pd.concat([df,df1])
    print(df)
    return df


def A08_mini_input_data2(col_name, data):
    # df1 = common_pandas.A08_mini_input_data2(123, 3)
    """
    이 함수는 데이터를 넣기 어려울때 값만 넣어주면 df를 만들어줍니다
        cal_name (str): 컬럼명 
        data (str): 입력할 데이터
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    df = pd.DataFrame([{col_name:data}])
    # print(df)
    return df


def A09_input_data_dic(dic_data):
    """
    이 함수는 데이터를 넣기 어려울때 딕셔너리만 넣어주면 df를 만들어줍니다. 
    데이터 입력이 어려울때 사용합니다. 
        dic_data `Object`: 딕셔너리 형태로 넣는다 하단 사용예를 보세요 
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    #사용예
    # dic = {"prediction" :1, "김민상":2}
    # df1 = common_pandas.A09_input_data_dic(dic)

    df = pd.DataFrame([dic_data])
    print(df)
    return df















############################################################
#########################   2. INFO   ######################
#########################   2. INFO   ######################
#########################   2. INFO   ######################
############################################################


   # 000 가장 기본중에 기본 데이터가 어떤 형태인지 알아봄
def B01_basic(df):
    print()
    print("=========전체 정보를 확인해 보자 df.info() : =====================================")
    print(df.info())
    print()
    print("========= 전체 정보를 확인해 보자  df.describe() : ===============================")
    print(df.describe())
    print()
    print("=========결측데이터가 있는지 좀 확인해 보자 df.isnull().sum() : ===================")
    print(df.isnull().sum())
    print()
    print("=========전체 컬럼명을 확인해 보자 df.columns : ==============================================")
    print(df.columns)
    print()
    print("=========전체 df를 확인해 보자 df : ==============================================")
    print(df)





    # 위의 베이직을 수행해보고, 특정열을 조금더 확인해봄
    # 01 유니크 값이 어떤지
    # 02 유니크 값은 어떤 내용인지
    # 03 컬럼명은 무슨 내용인가
def B02_uniq(df,col_name):
    ### 컬럼에 대한 정보들을 뽑아낼 수 있다. 
    ### 여기에서는 컬럼명의 종류와 갯수를 포함한다 
    ###값을 return 할 수도 있고 안할 수도 있다
    ### 값을 retrun 하면 df.to_csv로 저장도 가능하다. 
    df2 = df[col_name].value_counts()
    df2 = df2.reset_index()
    print("==========================================================")
    print("여기는 df['{}'].value_counts()값입니다 (유일값이 어떻게 분포되어 있는가?) ".format(col_name))
    print(df2)
    print()
    print("==========================================================")
    print("여기는 df['{}'].unuque()값입니다 (유일한 값 리스트) ".format(col_name))
    print(df[col_name].unique())
    print()
    print("==========================================================")
    print("여기는 df.columns 명 다른것 찾아보고 싶을때 : ")
    print(df.columns)
    return df2






















##########################################################################################
####################################  3. Slice  ##########################################
####################################  3. Slice  ##########################################
####################################  3. Slice  ##########################################
##########################################################################################


### 필터하기01 정확한 값만  filter filter filter filter filter
### 컬럼명과 정확한 값이 있어야 필터가 된다  filter filter filter
def C01_filter(df,col_name,check_name):
    """
    이 함수는 특정값만 필터하는 로직이다
        df `Object`: 표
        col_name (str): 컬럼명을 넣어준다
        check_name: 내가 찾고싶은 값만 필터를 걸어준다
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    df = df[df[col_name] == check_name]
    ### df를 만들고, 그것을 info에다가 넣어준다. 
    ### df = df.loc[(df[col_name] == check_name) | (df[col_name] == check_name)] 이중 조건 이상 
    # "|" = or , "&" = and
    #  
    # B01_basic(df)
    return df



### 필터하기02 비슷한 값도 출력가능///str.contains(check_name) filter filter
def C02_filter_s(df,col_name,check_name):
    """
    이 함수는 특정값만 필터하는 로직이다
        df `Object`: 표
        col_name (str): 컬럼명을 넣어준다
        check_name: 내가 찾고싶은 값만 필터를 걸어준다
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    df= df[df[col_name].str.contains(check_name)]
    # B01_basic(df)
    print(df)
    return df




#################### 여기는 선택하고 싶은 열만 처리하는 곳 ################
def C03_pick_columns(df, col_name): #### 여기서는 꼭 '||'를 써야한다. 
    """
    이 함수는 원하는 열만 슬라이싱 하는 것이다 원하는 열 이름을 넣으면 된다. . 
        df `Object`: 표
        col_name (str): 바꿔줄 컬럼명을 '||' 으로 분리합니다.  'API명||TC' 
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    col_name = col_name.split("||")
    # print("===============================선택된 컬럼명은 이것 입니다. ===")
    # print("전체 컬럼명 : ")
    # print(df.columns)
    # print("제외된 컬럼명 : "+str(col_name))
    # print("===============================선택된 컬럼명은 이것 입니다. ===")
    df = df[col_name]
    # print(df)
    return df

#################### 이 함수는 위의것과 반대입니다. ################
def C04_diff_columns(df, col_name):
    """
    이 함수는 위의것과 반대입니다.
        df `Object`: 표
        col_name (str): 바꿔줄 컬럼명을 '||' 으로 분리합니다.  'API명||TC' 
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """    
    col_name = col_name.split("||")
    print("=============================== 현재 DF에서 선택안된 컬럼명은 이것 입니다. ===")
    print("전체 컬럼명 : ")
    print(df.columns)
    print("제외된 컬럼명 : "+str(col_name))
    print("=============================== 현재 DF에서 선택안된 컬럼명은 이것 입니다. ===")
        
    df = df[df.columns.difference(col_name)]
    print(df)
    return df
####
####
####
####
####
####
### 01 행 번호로 슬라이싱
def C05_slicing_row(df,list_row):
    """
    이 함수는 슬라이싱 하는 것
        df `Object`: 표
        list_row (str): 하단에 설명이 있다. 
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    # 01 ("3~4") 로 설정하면 split 을 둘로나누며 계산하고 (1옆에 있는 물결)
    # 02 ("2,3,4") 로 설정하면 split 을 "||" 로 나누어 행을 추출해 냅니다. 
    # 여기서는 숫자로만 나눕니다. 
    # 추가로 여기서 DataFrame 을 번호를 reset 해줍니다. 정렬이 안될 수 있기에

    df = df.reset_index(drop=True) ### 여기서 재정렬하고 시작한다. 

    if "~" in str(list_row): ### 리스트에 "-"표시가 있으면 두개를 나눠준다
        list_row = list_row.split("~") ### (1옆에 있는 물결)
        start_num, end_num = int(list_row[0]),int(list_row[1])
        if end_num == 0:
            df = df.iloc[start_num:,:]
        else :
            df = df.iloc[start_num:end_num,:]
    elif "||" in str(list_row): ### 리스트에 "||" 표시가 있으면 여기로 온다. 
        df2= pd.DataFrame()     ### 공 df를 만들어 준다. 
        list_row = list_row.split("||")   ### 리스트를 나눠준다. 
        for i in list_row:
            df1 = df.iloc[int(i):int(i)+1,:]         
            df2 = pd.concat([df2,df1])
        df = df2
    print(df)
    return df



### 02 열 번호로 슬라이싱 세가지 방법으로 슬라이스 가능합니다.. 
### 

def C06_slicing_col(df,list_row):
    """
    이 함수는 슬라이싱 하는 것
        df `Object`: 표
        list_row (str): 하단에 설명이 있다. 
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    # df = a02_slicing_col(df,"0~3") ### 연결된 번호로
    # df = a02_slicing_col(df,"0||3") ### 특정열
    # df = a02_slicing_col(df,"||TC") ### 특정 이름으로 찾음
    # df = a02_slicing_col(df,"3||TC") ### 복합적으로 숫자도 되고 문자로도 찾음
    print()
    df = df.reset_index(drop=True) ### 여기서 재정렬하고 시작한다. 

    if "~" in str(list_row): #번호로 가를때(1옆에 있는 물결)
        list_row = list_row.split("~")
        start_num, end_num = int(list_row[0]),int(list_row[1])
        if end_num == 0:
            df = df.iloc[start_num:,:]
        else :
            df = df.iloc[start_num:end_num,:]

    else:               
        df2= pd.DataFrame()
        list_row = list_row.split("||")

        list_row = [x for x in list_row if pd.isnull(x) == False] 
        #리스트에서 내용이 없는것은 빼세요
        for i in list_row:
            if i != "": 
                if str.isdigit(i) == True:
                    
                    df1 = df.iloc[:,int(i):int(i)+1]            
                    df2 = pd.concat([df2,df1], axis=1)
                else:
                    df1 = df.loc[:,i]
                    df2 = pd.concat([df2,df1], axis=1)
        df = df2
    print(df)
    return df


#### 열 이름을 알고 있을때 알고있는 열을 제거할때
def C07_drop(df,list_col):
    list_col = list_col.split("||")
    list_col = [x for x in list_col if pd.isnull(x) == False]     
    for i in list_col:
        df = df.drop(columns = [i])
    print(df)
    return df


#### 데이터를 유니크 리스트 만들기
def C08_return_uniq_list(df, col_name):
    listk=df[col_name].unique()
    print(listk)
    return listk

#### 두개의 리스트 비교하기
def C09_compare_2list(listA, listB):
    ### 1 교집합
    listA = set(listA)
    
    listB = set(listB)
    intersec = listA & listB
    print("\n\n\n\n\n\n\n\n공통부분(교집합) ============================")
    print(intersec)
    subtractionA = listA - listB
    print("\n\n\nA리스트에만 있는 고유값 =======================")
    print(subtractionA)
    subtractionB = listB - listA
    print("\n\n\nB리스트에만 있는 고유값 =======================")
    print(subtractionB)











######################################################################################
#################################  4. 여기는 예쁘게 꾸미는 곳 ##########################
#################################  4. 여기는 예쁘게 꾸미는 곳 ##########################
#################################  4. 여기는 예쁘게 꾸미는 곳 ##########################
######################################################################################


def D01_change_col_name_all(df, col_name):
    """
    이 함수는 컬럼명을 바꿔주는 것입니다. - 전체 컬럼명을 입력해야 합니다. (갯수가 맞아야함) 
        df `Object`: 표가 들어옵니다. 
        col_name (str): 바꿔줄 컬럼명을 '||' 으로 분리합니다. 
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    col_name = col_name.split("||")
    df.columns = col_name
    print(df)
    return df


def D02_change_col_name_some(df, col_name):
    """
    이 함수는 일부 컬럼명을 바꿔주는 것입니다. - 일부만 바꿀 수 있으나 로직에 맞아야 합니다.  
        df `Object`: 표가 들어옵니다. 
        col_name (str): 바꿔줄 컬럼명만 사용 'TC||명명명**METHOD||니맘' ===> (원래명)||(바뀐후)**(원래)||(바뀐후)
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    # print("===============컬럼명이 이렇게 바뀌었어요==========================")
    col_name = col_name.split("**")
    name1 = {} #### 이것은 딕셔너리이다
    for i in col_name:
        i = i.split("||") #### split으로 나눠서
        name1[i[0]]= i[1] #### 키눈 i[0] 이고 값은 i[1]이다
        # print("origin : ["+i[0]+"] \t===> ["+i[1]+"]")    
    # print("===============컬럼명이 이렇게 바뀌었어요==========================")    
    df.rename(columns = name1, inplace = True)
    # print(df)
    return df



### 동일셀 삭제하기  df.drop_duplicates
def D03_drop_dup(df,col_name): 
    df = df.drop_duplicates(subset=col_name,keep='first') ### 동일한 내용이 있으면 지워버려
    return df

def D03_drop_nan(df, oo_8):
    if oo_8 == "oo": #결측값이 있는 행제거
        df.dropna(axis = 0)
    elif oo_8 == "8": #결측값이 있는 행제거
        df.dropna(axis = 1)
    return df


### 정렬하기 정렬 정렬 정렬 정렬 정렬 정렬 정렬 정렬
def D04_sort(df,sort_list,T_F): ### 
    """
    이 함수는 특정값만 필터하는 로직이다
        df `Object`: 표
        sort_list (str): 여기 값이 "" 값이 없으면 index 기준이다. 
        T_F (bool): True(순차) , False(역순)
    Retruns:
        df `Object`: 데이터 프레임을 되돌려준다. 
    """
    # print()
    if sort_list =="": ### 중간에 데이터가 없으면 "" =  index 기준으로 정렬한다. 
        df = df.sort_index(ascending=T_F)
    else: #### 중간 값이 있으면 그 컬럼에서 정렬한다. 
        df = df.sort_values(by=sort_list,ascending=T_F)
        ### 여기는 컬럼명의 값으로 정렬하는것
    print(df)
    return df

def D05_set_index(df,index_name): #### 여기에 인덱스 네임을 "" 로 아무것도 안넣으면 
    ### reset_index가 된다. 
    if index_name == "": #### 맨앞에를 날리는것
        df = df.reset_index(drop = True)
    elif index_name == "0": #### 맨앞을 살리는것
        df = df.reset_index()
    else :
        df = df.set_index(index_name)

    return df



### 데이터 입력하기
# 1. 컬럼명을 데이터 프레임에서 가져온다. 
# 2. 데이터를 입력한다. 
# 3. 데이터 프레임으로 만들고
# 4. concat으로 붙이고





############################################################################################
############# 추가 서비스 ###################################################################
############################################################################################

# 그룹별 평균값 구하기
# df[df['Gender']=='Male']['Height'].mean())
# 설명 성별이 남자인 애들만 모아 그래서 그것의 "키" 컬럼의 평균을 구해봐.
#  df[df['Gender']=='Male']['Fruit'].mode()[0])        mode() = 최빈값 제일 많은값 0번을 가져와
# 설명 성별이 남자인 애들만 모아 그래서 "Fruit" 열에서 최빈값을 가져와

# 결측치가 있으면 평균값을 추가해봐
# df['Height'].fillna(df.groupby('Gender')['Height'].transform('mean'), inplace=True)
# df"키" 에다가 fillna 채워 그룹의 평균값을 알아서 채워 넣어 그룹별로 말이야

# 결측치가 있으면 최빈값을 추가해
# df['Fruit'].fillna(df.groupby('Gender')['Fruit'].transform(lambda x: x.value_counts().idxmax()), inplace=True)
# df"Fruint" 에다가 fillna 채워 성별별로 알아서 채워 넣어. 제일 많은 값을채워 넣어. 

### 어플라이 해보기
# def kms(x):
#     x = x+ 1
#     return x

# df['kkk'] = df['NUM1'].apply(kms)



### 그룹 바이 김씨가 몇명인지 세어보세요 https://zephyrus1111.tistory.com/185 ### 이해가 좀 안됨
# def get_lastname_count(series):
#     res = len([ _ for x in series if x[0]=='김'])
#     return res

# df.groupby('성별').agg({'이름':get_lastname_count}).reset_index()


### 그룹바이 남자키 180이상 여자키 160 이상을 세어보세요
# def get_count_by_height(series):
#     if df.iloc[series.index[0], :]['성별'] == '남자':
#         res = len([_ for x in series if x>=180])
#     else:
#         res = len([_ for x in series if x>=160])
#     return res

# df.groupby('성별').agg({'키':get_count_by_height}).reset_index()







# https://zephyrus1111.tistory.com/207
# 주가와 이동평균선 만들고 차트로 보기









#################################################################################
################### 필터 추가 ####################################################

# 특정 col 만 보고 싶을때
# df.filter(items=['PROCESS_A', 'SUB_A'], axis=1) ## PROCESS_A SUB_A 칼럼 추출

# 특정 row 만 보고 싶을때 
# df.filter(items=['PRODUCT_A', 'PRODUCT_B'], axis=0) ## PRODUCT_A PRODUCT_B 행 추출


# col 중에서 "PROCESS" 라는단어가 들어간 col만 
# df.filter(like='PROCESS', axis=1) ## PROCESS가 포함된 칼럼 추출

# row 중에 like='_A' 포함된 row만 인덱스가  
# df.filter(like='_A', axis=0) ## _A가 포함된 행 추출


# col중에서 A로 끝나는 col 추출
# df.filter(regex='A$', axis=1) ## A로 끝나는 칼럼 추출

# col중에서 A 또는 B 또는 D 로 끝나는 col 추출
# df.filter(regex='[ABD]$', axis=0) ## A, B, D로 끝나는  행 추출











##################################################################
######################    여기는 INI     ##########################
######################    여기는 INI     ##########################
######################    여기는 INI     ##########################
##################################################################