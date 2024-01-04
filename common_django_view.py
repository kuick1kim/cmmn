###############################################################
############### 아래것은 붙여서 사용하면 된다. ###################
###############################################################
###############################################################
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404, render
# 제일간단하게 표현하기
# def index(req):
#     context1 = {
#     }
#     return render(req, "index.html", context=context1)



# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
###############################################################
###############################################################

# from django.template import loader
# from django.http import Http404
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from .models import Choice, Question
# from django.views import generic

# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by("-pub_date")[:5]

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"

# # def detail(request, question_id):
# #     try:
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         #### 없으면 이짝으로 들어가라
# #         addr = f"/polls/{question_id}/ ---- 주소가 없슈"
# #         return render(request, "polls/detail2.html", {"question": addr})
    
# #     return render(request, "polls/detail.html", {"question": question})

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = "polls/results.html"

# def index3(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index3.html")
#     context = {        "latest_question_list": latest_question_list    }
#     return HttpResponse(template.render(context, request))

# def index2(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
# # def index(request):
# #     return HttpResponse("Hello, world. You're at the polls index. 김민상")

# # def detail(request, question_id):
# #     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
       
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})









###############################################################
###############################################################
# from django.shortcuts import render
# # Create your views here.
# from django.http import HttpResponse

# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import logout

# import time,json
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# def index(request):
#     return render(request, 'index.html')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/')  # 회원 가입 후 home 페이지로 이동
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

# def home_ee(request):
#     return render(request, 'index.html')

# def user_logout(request):
#     logout(request)
#     return redirect('/')  # 로그아웃 후 home 페이지로 이동

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('/')  # 로그인 후 home 페이지로 이동
#     else:
#         form = AuthenticationForm()

#     return render(request, 'login.html', {'form': form})

# ##### 사용법
# ##### http://127.0.0.1:8000/sel/?url=https://www.naver.com
# def selenium_01(request):
#     start_time = time.time()
#     sympathy = 0 ;  comment = 0
#     return_obj = {}

#     current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
#     return_obj["date"] = current_time

#     # Chrome 웹 드라이버 생성
#     s = Service("chrome/chromedriver.exe")
#     options = webdriver.ChromeOptions()
#     options.add_argument('headless')
#     options.add_argument('window-size=1920x1080')
#     options.add_argument('--no-sandbox')
#     options.add_argument("disable-gpu")
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
#     driver = webdriver.Chrome(service=s, options=options)

#     try:
#         aaa = request.GET.get('url', None)
#         print('aaa = ', str(aaa))
#         blog_url = request.GET.get('url', None)      
#         screenshot_filename = f"image/hohoho.png"
#         # screenshot_filename = f"image/{blog_url.split('.')[-2]}.png"

#         return_obj["url"] = blog_url    

#     except:
#         blog_url = 'unknown'
#         print(blog_url)
#         print()        
        
#     # Load Page
#     driver.get(url=blog_url)
#     time.sleep(0.5)

#     # Capture screenshot    
#     driver.save_screenshot(screenshot_filename)
#     #### 사진찍고 문 닫음
#     driver.quit()

#     return_obj["sympathy"] = sympathy
#     return_obj["comment"] = comment
#     return_obj["process_time"] = round(time.time() - start_time, 2)

#     # show_image(screenshot_filename)
#     image_url =f'http://127.0.0.1:8000/{screenshot_filename}'

#     return render(request, 'selenium_example.html', {'image': image_url,'home1': blog_url, 'data': json.dumps(return_obj, indent=2)})
    










###############################################################
###############################################################
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.views import generic

# from .models import Choice, Question
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

# def vote(request, question_id):
#     # return HttpResponse("You're voting on question %s." % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by("-pub_date")[:5]

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = "polls/results.html"

# # views.py (또는 해당 코드를 사용하는 파일)

# # from django.shortcuts import render

# # def my_view(request):
# #     sections = [
# #         {
# #             "title": "Shooting Stars",
# #             "content": "Blue bottle crucifix vinyl post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine.",
# #             "link": {"text": "Learn More", "icon_path": "path/to/icon.svg"}
# #         },
# #         {
# #             "title": "The Catalyzer",
# #             "content": "Blue bottle crucifix vinyl post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine.",
# #             "link": {"text": "Learn More", "icon_path": "path/to/icon.svg"}
# #         },
# #         {
# #             "title": "The 400 Blows",
# #             "content": "Blue bottle crucifix vinyl post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine.",
# #             "link": {"text": "Learn More", "icon_path": "path/to/icon.svg"}
# #         },
# #     ]
# #     button_text = "Button"
# #     return render(request, 'my_template.html', {'sections': sections, 'button_text': button_text})


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
