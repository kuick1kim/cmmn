import os

def update(text):
    os.system('git add .')
    os.system(f'git commit -m "{text}"')    
    os.system('git push origin master')




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

