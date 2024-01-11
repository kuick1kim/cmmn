

# 1. 버추얼 환경에서 따로 실행 # 장고 처음시작할때 
# .\myenv\Scripts\activate
# 벤브 환경에서 실행한다


# 2. 버추얼 환경이므로 라이브러리를 깔아야함
# pip install Django
# pip install Pillow
# pip install django-widget-tweaks #### 입력폼 예쁘게 만들기 위해
# 3 프로젝트 만들기 
####  django-admin startproject [mysite]


# 4 디렉토리 변경
# cd .\[mysite]\


# 5 런서버 한다
# py .\manage.py runserver


# 6 앱을 하나 만들때
#### python manage.py startapp {myapp}
# 앱이 만들어지면

# 6-1-1 static 폴더 만들기
# 6-1-2 static setting.py 초기에 변경해 주기

# 6-2-1 app 내에 template 폴더 손으로 만들어주기
# 6-2-2 html 변경할 예정이므로 common_html.py 복사해서 html {% load static %} 변경해주기

# 6-3-1 app 내에 url 파일이 없다 만들어주기 
# 6-3-2 common_url.py 주석으로 전부 때려박기

# 6-4 app 내에 view에 common view 주석으로 때려박고 시작

# 6-5 app 내에 model 에 common model 주석으로 때려박고 시작

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


##### 관리자 페이지 만들기

#  py manage.py createsuperuser

# admin / admin@example.com / admin/ admin / y

# 6666
# API 가지고 놀기¶
#  py manage.py shell







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








# https://www.pythonanywhere.com/user/kuick2/consoles/31832607/
# bash 에 들어가서
# 1. 깃에서 클론함
#  git clone https://github.com/kuick1kim/bbbb.git

# 2. cd bbbb
# 2. virtualenv venv --python=python3.9.6
# 2. 버츄얼 환경으로 변경하고 라이브라리 설치
# 2. source venv/bin/activate

# 3. 라이브러리 설치
# pip install Django
# pip install Pillow
# pip install django-widget-tweaks #### 입력폼 예쁘게 만들기 위해

# 4. python manage.py migrate 다시설치하기 

# 5. python manage.py createsuperuser
# 5. kuick1 | 이메일 | 비번 | 비번확인

# 6. web 으로 이동해서
# 6. Python version: 3.9 변경하기
# 6. /home/kuick2/bbbb/venv

# 6. /static/	/home/kuick2/bbbb/static
# 6. WSGI configuration file:/var/www/kuick2_pythonanywhere_com_wsgi.py
#####################################################################
#####################################################################
# import os
# import sys
# path = '/home/kuick2/{{{변경할 부분 bbbb}}}'
# if path not in sys.path:
#     sys.path.append(path)
# os.environ['DJANGO_SETTINGS_MODULE'] = '{{{변경할 부분 bbbb}}}.settings'
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
#####################################################################
#####################################################################

# 6. setting.py 
# ALLOWED_HOSTS = ['kuick2.pythonanywhere.com'] 변경
# WSGI_APPLICATION = '{{{확인하기 bbbb}}}.wsgi.application'














