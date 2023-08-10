import os, time

## 깃허브 끝낼때 'ESC' ':' 'q'
timek = time.strftime('%Y-%m-%d %H:%M:%S')
### requirements 만들기
def pip_freeze():
    os.system('pip freeze > requirements.txt')

### requirements 설치
def pip_install():
    os.system('pip install -r requirements.txt')

##################################################
##################################################
##################################################
##################################################
##################################################
def first_init(git_url):
    ### 사용법 common_git.first_init('https://github.com/kuick1kim/cmmn.git')
    os.system('git remote rm origin') ### 기본주소 비우기
    os.system('echo "# cmmn" >> README1.md')
    os.system('git init')
    os.system('git add README1.md')
    os.system('git commit -m "first commit"')
    os.system('git branch -M main')
    os.system(f'git remote add origin {git_url}')
    os.system('git push -u origin main') 
 
# 초기화 하는 방법
### 이것으로 자름
# git remote rm origin
### 이것으로 다시확인
# git remote -v
### 이것으로 README.md 파일 생성
# echo "# cmmn" >> README.md
### 이것으로 git 파일 애드
# git add README.md
### 이것으로 git 첫번째 커밋
# git commit -m "first commit"

#깃 브랜치 이름을 main으로 함
# git branch -M main

# 여기에 이동할 주소를 적어줌
# git remote add origin https://github.com/kuick1kim/cmmn.git

# 여기서 깃 푸쉬함 
# git push -u origin main

# common_git.first_init('https://github.com/kuick1kim/cmmn.git')



def update(text):
    os.system('git add .')
    os.system(f'git commit -m "{text}-{timek}"')    
    os.system('git push origin main')

def look_log():
    os.system('git log --oneline --all --graph')

# 강제진행
def force_upload():
    os.system('git push -u origin +master')


### 마지막 커밋한것 지워줌
def del_commit():
    os.system('git reset --hard HEAD~1')
    # os.system('git reset --hard HEAD~2') 이것은 두개를 지워주는 것



##### 브랜치를 이동하는 명령어는 switch 이다햐

# 깃 현재 브랜치 확인 내가 어디서 작업하는지 확인해야함
def check_branch():
    os.system('git branch')

# 브랜치 만들기
def mk_branch(branch_name):
    os.system(f'git branch {branch_name}')
    os.system(f'git switch {branch_name}') #### 브랜치로 자동이동

# 브랜치 사이로 이동하기 메인브랜치- sub브랜치
def mv_branch(branch_name):
    os.system(f'git switch {branch_name}') #### 브랜치로 자동이동

# 머지 브랜치 
# 1 합치려는 메인 브랜치로 이동한다 Main도 좋고/ Sub도 좋다
def merge_branch():
    base_branch = input("1 기준 브랜치로 이동 : ")
    os.system(f'git switch {base_branch}') #### 브랜치로 자동이동
    get_branch = input("2 합치기 원하는 브랜치명 입력 : ")
    os.system(f'git merge {get_branch}') #### 브랜치로 자동이동
    input("3 머지상에 문제가 있으면 고쳐주세요 : [수정 완료 되면 Enter]")
    
    os.system('git add .')
    os.system(f'git commit -m "{get_branch}브랜치가 합쳐짐"')   





 
### 이것이 안됨
# git init
### 이것으로 확인해봄
# git remote -v
# origin  https://github.com/kuick1kim/common_git.git (fetch)
# origin  https://github.com/kuick1kim/common_git.git (push) 





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

# 문제4
# rebase 도중에 문제가 발생 
#  git rebase --quit




