import os

def update():
    os.system('git add .')
    os.system('git commit -m "first commit"')
    os.system('git remote add origin https://github.com/kuick1kim/common_git.git')
    os.system('git push origin master')
