###############################################################
############### 아래것은 붙여서 사용하면 된다. ###################
###############################################################
###############################################################

# from django.urls import path
# from . import views

# app_name = "polls"
# urlpatterns = [
#     # ex: /polls/
#     path("", views.index, name="index"),
#     # ex: /polls/aaa 앞에 이거 빼야한다
#     path("aaa/", views.index2, name="index2"),
#     # ex: /polls/222 앞에 이거 빼야한다
#     path("bbb/", views.index3, name="index3"),
#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]

# app_name = "polls"
# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
#     path("<int:pk>/", views.DetailView.as_view(), name="detail"),
#     path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]
###############################################################
###############################################################

# from bbb_blog import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     # path("index/", views.index, name="index2"),
#     path("fashion/", views.fashion, name="fashion"),
#     path("about/", views.about_1, name="about"),
#     path("photography/", views.photo1, name="photography"),
#     path("travel/", views.travel1, name="travel"),
#     path("contact/", views.contact1, name="contact"),
#     # path("a/", views.fashion, name="fashion")
# ]
###############################################################
###############################################################

# from . import views

# app_name = "polls"
# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
#     path("<int:pk>/", views.DetailView.as_view(), name="detail"),
#     path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]
###############################################################
###############################################################
# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path('signup/',  views.signup, name='signup'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),  # 추가
#     path('home/', views.home_ee, name='home'),
#      path('sel/', views.selenium_01, name='selenium_example'),
# ]
###############################################################
###############################################################
















###############################################################
##################여기는 메인 사이트 입니다. ####################
##################여기는 메인 사이트 입니다. ####################
###############################################################
###############################################################
##################여기는 메인 사이트 입니다. ####################
##################여기는 메인 사이트 입니다. ####################
###############################################################




# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path("polls/", include("polls.urls")),
#     path('admin/', admin.site.urls),
# ]
###############################################################
###############################################################

# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.generic import RedirectView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('blog/', include("bbb_blog.urls")),
#     path('', RedirectView.as_view(url="/blog/", permanent=True)),
# ] 
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

###############################################################
###############################################################

# urlpatterns = [
#     path("polls/", include("polls.urls")),
#     # path("", views.IndexView.as_view(), name="index"),
#     # vote
#     path("", include("polls.urls")),
#     path("admin/", admin.site.urls),    
# ]
###############################################################
###############################################################
# from django.contrib import admin
# from django.urls import include, path

# from django.conf.urls.static import static
# from django.conf import settings

# urlpatterns = [
#     path("", include("polls.urls")),    
#     path("admin/", admin.site.urls),
# ]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
###############################################################
###############################################################





