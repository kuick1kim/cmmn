import os, time

## 깃허브 끝낼때 'ESC' ':' 'q'

def update(text):
    os.system('git add .')
    os.system(f'git commit -m "{text}"')    
    os.system('git push origin master')

def look_log():
    os.system('git log --oneline --all --graph')

### 마지막 커밋한것 지워줌
def del_commit():
    os.system('git reset --hard HEAD~1')
    # os.system('git reset --hard HEAD~2') 이것은 두개를 지워주는 것

# 강제진행
def force_upload():
    os.system('git push -u origin +master')



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

