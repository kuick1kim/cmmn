# pip install openpyxl
# pip install -U scikit-learn
# pip install tensorflow
# \python.exe -m pip install --upgrade pip


from cgitb import reset
import common_pandas
import pandas as pd
from pandas import  DataFrame
import os, time, shutil
import configparser
from tensorflow.python.keras.utils import np_utils

from sklearn.preprocessing import  LabelEncoder

import tensorflow as tf
import numpy as np

from keras.models import load_model

## 엑셀 불러오기
def call_excel(path_name, sheet_namek):### 시트이름이 필요합니다.
    df = pd.read_excel(path_name, sheet_name=sheet_namek, engine ='openpyxl')   
    return df


def pickup_data(df, cal_name):
    DF_X = C04_diff_columns(df, cal_name)
    DF_Y = C03_pick_columns(df, cal_name)

    # #### 데이터를 넘파이로 바꾼다.  여기서 DF_X를넣으면 나와야 한다. array가 나온다. 

    X = DF_X.to_numpy()
    Y = DF_Y.to_numpy()

    return X, Y




def oneHot_Encoding(Y):
    Y = tf.keras.utils.to_categorical(Y)
    # print(Y)
    return Y




def LabelEncoder_k(Y):
    e = LabelEncoder()
    e.fit(Y)
    Y=e.transform(Y)
    return Y





####### 여기는 TRUE 와 FALSE 로 두개의 더미로 만들어준다 
def make_dummies(df):
    df = pd.get_dummies(df)
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
    X = df.to_numpy()
    return X


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
    print(df)
    X = df.to_numpy()
    return X




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
        if start_num == 0:
            df = df.iloc[:,:end_num]
        else :
            df = df.iloc[:,start_num:end_num]


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
    
    X = df.to_numpy()
    print(df)
    print(X)
    print(len(X))
    return X
















#### 마지막 예측해보기


def load_model_k(path):
    ### 사용법 ex
    # model = common_deep.load_model_k('model/a02_housing.h5')
    model = load_model(path)
    return model


#### 예측하고 예측한 값 저장하기

def predict_kms(model1, dataset, X, save_excel_path):
    ### 사용예
    ### common_deep.predict_kms(dataset, X, "output/[[[모델완성_{}]]].xlsx".format(time_k))

    # X데이터와 DF 가 들어들어가면 리턴값 없음
    df= pd.DataFrame()        ## 공df
    df_right = pd.DataFrame() ## 공df

    for i in range(len(X)):     ## 여기서 값을 돌림
        X_pre = X[i]
        list_kms = np.array([X_pre])    ## 여기 괄호가 아주 중요하다
        predicted = model1.predict(list_kms) ## 여기는 예측이다

        df_right1 = common_pandas.A08_mini_input_data2("prediction",predicted[0][0])
        df_right = common_pandas.A06_concat_01(df_right ,df_right1, "8")    

    dataset = dataset.reset_index(drop=True)
    df_right = df_right.reset_index(drop=True)
    df = common_pandas.A06_concat_01(dataset, df_right, "oo")#### 붙이기

    common_pandas.A04_make_excel(df, "predict", save_excel_path)
    print(df)









def uuuuuu(dfk, predicted):
    ###### 스플릿
    predicted= predicted.replace("[","").replace("]","").replace("\n","")
    predicted= predicted.split(" ")
    df11= pd.DataFrame()
    df1= pd.DataFrame()

    for i in predicted:
        if i != '':
            df2 = common_pandas.A08_mini_input_data2("ppp", float(i))
            df1 = common_pandas.A06_concat_01(df1, df2, "8")
    
    df1 = df1.reset_index(drop=True)
    df1 = common_pandas.A06_concat_01(dfk, df1, "oo")

    #### 소트를 해준다. 
    df11 = df1.sort_values(by="ppp",ascending=False)
    df11 = df11.reset_index(drop=True)
    #### 소트가 된후 원래데이터
    #### 여기서 텍스트를 만든다. 
    text1k = ""
    for i in range(3):        
        indexk = df11["원래데이터"][i]
        predic_k = round(df11["ppp"][i] * 100 )
        textk = "[{}번:{}%] {} | ".format(i+1,predic_k,indexk)
        text1k = text1k + textk
        

    # common_pandas.A03_make_csv(df11, "output/[test06]데이터 변환-------------.csv")
    
    return text1k


    # print(df1)




def predict_iris(model1, dataset, X, save_excel_path):
    ### 사용예
    ### common_deep.predict_kms(dataset, X, "output/[[[모델완성_{}]]].xlsx".format(time_k))

    ##### 변환인코딩을 캐쉬에 잡아서 넣어주려고한다. 
    ##### 변환인코딩을 캐쉬에 잡아서 넣어주려고한다. 
    dfk = common_pandas.A01_call_csv( "output/[test06]데이터 변환-인코딩.csv")
    dfk = common_pandas.D04_sort(dfk, "변환후a", True)
    dfk = dfk.reset_index(drop=True)
    ##### 변환인코딩을 캐쉬에 잡아서 넣어주려고한다. 

    # X데이터와 DF 가 들어들어가면 리턴값 없음
    df= pd.DataFrame()        ## 공df
    df_right = pd.DataFrame() ## 공df

    for i in range(len(X)):     ## 여기서 값을 돌림
        X_pre = X[i]
        list_kms = np.array([X_pre])    ## 여기 괄호가 아주 중요하다
        predicted = model1.predict(list_kms) ## 여기는 예측이다

        #############여기가 자꾸 변한다 여기를 체크
        #############여기가 자꾸 변한다 여기를 체크
        predicted = str(predicted[0]) #### 여기가 예측치다

        ############### 여기 들어갔다 나와라
        ############### 여기 들어갔다 나와라
        text_k = uuuuuu(dfk, predicted)
        ############### 여기 들어갔다 나와라

        dic = {"prediction" :predicted, "예측":text_k}
        # df_right1 = common_pandas.A08_mini_input_data2("prediction",predicted)
        df_right1 = common_pandas.A09_input_data_dic(dic)
        df_right = common_pandas.A06_concat_01(df_right ,df_right1, "8")    


    dataset = dataset.reset_index(drop=True)
    df_right = df_right.reset_index(drop=True)
    df = common_pandas.A06_concat_01(dataset, df_right, "oo")#### 붙이기
    df = common_pandas.A06_concat_01(dataset, df_right, "oo")#### 붙이기

    common_pandas.A04_make_excel(df, "predict", save_excel_path)
    # common_pandas.A03_make_csv(df, save_excel_path)
    print(df)


# kkk = len(predicted[0])
# "prediction",str(predicted[0]))
# {
# "p0rediction" :1, "김민상":2}