import os, time
import shutil


#### exe파일 만들때1
# python.exe -m pip install --upgrade pip
# pip freeze > requirements.txt
# pip install -r .\requirements.txt
# pip install --upgrade pyinstaller # 업그레이드 해야 할 수 있음

#1. pip install pyinstaller 로 venv에서 설치합니다
#2. pyinstaller -w -F --icon=app.ico main.py 로 콘솔창도 안뜨고, 한파일로 만듭니다. 

#################################################################
##########아이콘 미리 만들어 두세요 라이브러리 설치 동안에 ##########
#################################################################
# 백그라운드제거 https://www.remove.bg/ko/upload
# png를 아이콘으로 https://convertico.com/#google_vignette    
#3. pyinstaller.exe --onefile --windowed --icon=app.ico .\bible.py 


##########################################################
##########환경설정 해주세요 라이브러리 설치 동안에 ##########
##########################################################
# QT_PLUGIN_PATH
# G:\python\20230811 pyqt2pandas\kimkim\Lib\site-packages\PyQt5\Qt5\plugins

### 환경설정 해줘야 한다. 
# 1. pip install pyinstaller
# 2. 위에것이 바이러스로 인해 자꾸 삭제된다
# --- pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz
# 3. pip install PyQt5
# 3. pip install pyqt5-tools
# 3. pip install pandas
# 3. pip install matplotlib

# 3. pip install BeautifulSoup4
# 3. pip install openpyxl

def make_venv(folder_name):
    with open('venv_name.txt', "w") as file:
            file.write(folder_name)
            file.close()
    os.system(f'python -m venv {folder_name}')
    ### 액티베이트
    # Set-ExecutionPolicy RemoteSigned
    # 빨간글자가 나오면 이것을 해줘야함


    print("activate 아래를 입력후 엔터를 눌러주세요")
    print(f"./{folder_name}/Scripts/activate")
    print("\n 다되면 requirementx.txt 설치하셔요")
    print("또는 pip list 확인해보기 \n 또는 필요한것 pip install 하기\n")


### 나가는 방법######################################
### 나가는 방법######################################
### 나가는 방법######################################
# 1. deactivate 
# 2. rmdir aaa폴더
### 나가는 방법######################################
### 나가는 방법######################################
### 나가는 방법######################################


# f = open("venv_name.txt", 'r')
# data = f.read()
# print(data)
# f.close()
def rmdir(folder_name):
    shutil.rmtree(f"{folder_name}")




def install_pip():
#### 두번째 인스톨하기
    print('pip list \n'*3)
    os.system('pip list')
    print('python.exe -m pip install --upgrade pip \n'*3)
    os.system('python.exe -m pip install --upgrade pip')
    print('pip install -r requirements.txt \n'*3)
    os.system('pip install -r requirements.txt')
    print('pip list \n'*3)
    os.system('pip list')

    print("\n\n deactivate는 나갈때 확인해 주세요 rmdir 확인")



def pip_list():
    ### 리스트로 리콰이어먼트 만들기 
    os.system('pip freeze > requirements.txt')
    


def del_pip_list():
    ### 리스트로 리콰이어먼트 만들기 
    print('pip list \n'*3)
    os.system('pip list')
    print('pip uninstall -r requirements.txt \n'*3)
    os.system('pip uninstall -r requirements.txt')
    print('pip list \n'*3)
    os.system('pip list')

    
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################
####################################################

namek = 'myenv'



print('=================================================')
print('\t 여기서 하단의 번호를 눌러주세요 ')
print(f'\t 1. venv 생성 : 현재 폴더명은 ./{namek}/Scripts/activate ')
print('\t 2. pip install -r requirement.txt')
print('\t 3. deactivate & rmdir \n')
print('\t a. pip freeze > requirements.txt')
print('\t d. pip uninstall -r requirements.txt')
print('=================================================')
number_l = input('번호를 입력해 주세요 1, 2, 3, a, d :  ')

if number_l == '1':
    print('지금 가상환경이 만들어 지고 있슈.. 띠리디리디....')
    make_venv(namek)    

elif number_l == '2':
    # ### 인스톨하기
    install_pip()

elif number_l == '3':    
    rmdir(namek)
    print('deactivate 가 눌러지지 않았다면 눌러주세요')

elif number_l == 'a':  
    pip_list()  

elif number_l == 'd':  
    del_pip_list()  
  
else :
    print('1, 2, 3, a를 눌러야 해요 : 안뇽')