import os, time

## 깃허브 끝낼때 'ESC' ':' 'q'

def update(text):
    os.system('git add .')
    os.system(f'git commit -m "{text}"')    
    os.system('git push origin master')

def look_log():
    os.system('git log')

def del_commit():
    os.system('git reset --hard HEAD~1')

# 강제진행
def force_upload():
    os.system('git push -u origin +master')





# 날짜와 분을 가져오기
# print("문자열 변환 : ", time.strftime('%Y-%m-%d %H:%M:%S'))




# 오리진이 문제가 있을때 지우기
# error: remote origin already exists.  
# os.system('git remote remove origin')


# 문제2 
# error: failed to push some refs to 'https://github.com/kuick1kim/common_git.git'


# 문제3
# fatal: a branch named 'master' already exists
# 삭제해줘야 한다. 
# fatal: a branch named 'master' already exists
# git branch -d master    

