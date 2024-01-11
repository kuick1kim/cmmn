###############################################################
############### 아래것은 붙여서 사용하면 된다. ###################
###############################################################
###############################################################
# import datetime

# from django.db import models
# from django.utils import timezone

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")
#     def __str__(self):
#         return self.question_text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

###############################################################
###############################################################
#############  모델이후에 admin.py에서 세팅을 해줘야한다. ###########


##### 관리자 페이지 만들기

#  py manage.py createsuperuser
# admin / admin@example.com / admin/ admin / y
# 실행하기 
# py .\manage.py runserver

# http://127.0.0.1:8000/admin/

# from django.contrib import admin
# from bbb_blog.models import Category, Post


# admin.site.register(Category)
# admin.site.register(Post)
###############################################################
###############################################################

# from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

# class Comment(models.Model):
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)

# class Category(models.Model):
#     name = models.CharField(max_length=255)

# class PostCategory(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

###############################################################
###############################################################
# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class UserProfile(AbstractUser):
#     name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15, blank=True)
#     birthdate = models.DateField(blank=True, null=True)
#     lost_email = models.EmailField(blank=True, null=True)


###############################################################
###############################################################

###############################################################
###############################################################

###############################################################
###############################################################



