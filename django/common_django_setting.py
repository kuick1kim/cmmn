###############################################################
############### 아래것은 붙여서 사용하면 된다. ###################
###############################################################

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





# INSTALLED_APPS = [
#     ##########################
#     "polls.apps.PollsConfig",
#     'bbb_blog.apps.BbbBlogConfig',
#     'ppp.apps.PppConfig',
#     ###############################
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# ]


# TIME_ZONE = 'Asia/seoul'

# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

# # 이미지 파일을 저장할 디렉터리를 설정
# MEDIA_URL = '/image/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'image')


###############################################################
###############################################################
#### 문제 발생
# MEDIA_ROOT error : _getfullpathname: path should be string, bytes or os.PathLike, not tuple
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media'),  # This is a tuple
# STATIC_ROOT = os.path.join(BASE_DIR, 'static'),  # So is this
# Removing the trailing comma should resolve the problem.

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # This is now a string
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # So is this
###############################################################
###############################################################

###############################################################
###############################################################

###############################################################
###############################################################

###############################################################
###############################################################

###############################################################
###############################################################


