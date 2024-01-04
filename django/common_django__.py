

# 1. 버추얼 환경에서 따로 실행 # 장고 처음시작할때 
# .\myenv\Scripts\activate
# 벤브 환경에서 실행한다


# 2. 버추얼 환경이므로 라이브러리를 깔아야함
# pip install Django


# 3 프로젝트 만들기 
####  django-admin startproject [mysite]


# 4 디렉토리 변경
# cd .\[mysite]\


# 5 런서버 한다
# py .\manage.py runserver


# 6 앱을 하나 만들때
#### python manage.py startapp {myapp}







# print(django.get_version())





#### 데이터베이스를 사용하려면
# https://docs.djangoproject.com/ko/4.2/intro/tutorial02/

# 11111
# py manage.py makemigrations

# py manage.py migrate



##### 데이터베이스 연결
# 22222  polls/models.py¶
# from django.db import models

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")



# 333333
# mysite/settings.py
# INSTALLED_APPS = [
#     "polls.apps.PollsConfig",
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
# ]


# 4444
# py manage.py makemigrations polls


# 5555
# py manage.py migrate


# 6666
# API 가지고 놀기¶
#  py manage.py shell







##### 관리자 페이지 만들기

#  py manage.py createsuperuser

# admin / admin@example.com / admin/ admin / y

##### 페이지 열기 

# py manage.py runserver

# http://127.0.0.1:8000/admin/

#############################################
#############################################
#############################################
#############################################

# db지우기 rm -r myapp/migrations
# db지우기 python manage.py migrate ppp zero

# 


# 이미지를 연결하려면
# index.html 파일은 templates 폴더 안에 있어야 한다

# 이미지와 css js는 
# static 폴더를 만들어 줘야한다 - 외부에 만들어줘야함
# 그리고 스테틱 폴더를 
# setting.py 에서 세팅해야 하고
# url.py 에서 세팅해야한다

# 내앱/
# ├── static/
# │   └── images/
# │       └── myimage.jpg
# │   └── css/
# │   └── js/
# └── templates/
#     └── index.html


# 그리고 index.html 파일에서 다시 세팅해줘야한다. 
# 맨위에 {%load static%}

# href="{% static 'css/style.css' %}">
# <img src="{%static 'images/logo.png' %}"
#       <script src="{%static 'js/jquery.min.js' %}"></script>
# 이런식으로 모두 바꿔야한다. 

# 참조사이트
# https://chocohaim1121.tistory.com/78
# https://free-eunb.tistory.com/42












