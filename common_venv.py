import os, time



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

### 나가는 방법######################################
### 나가는 방법######################################
### 나가는 방법######################################
# 1. deactivate 
# 2. rmdir aaa폴더
### 나가는 방법######################################
### 나가는 방법######################################
### 나가는 방법######################################




def install_pip():
#### 두번째 인스톨하기
    os.system('python.exe -m pip install --upgrade pip')
    os.system('pip install -r requirements.txt')
    os.system('pip list')

    print("\n\n deactivate는 나갈때 확인해 주세요 rmdir 확인")







