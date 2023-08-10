import common_git

common_git.pip_freeze()

 
### 이것이 안됨
# git init
### 이것으로 확인해봄
# git remote -v
# origin  https://github.com/kuick1kim/common_git.git (fetch)
# origin  https://github.com/kuick1kim/common_git.git (push) 

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


common_git.update('kms')

