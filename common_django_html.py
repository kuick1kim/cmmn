
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


####################################################################
####################################################################
# 그리고 index.html 파일에서 다시 세팅해줘야한다. 
# 맨위에 {%load static%}

# 참조사이트
# https://chocohaim1121.tistory.com/78
# https://free-eunb.tistory.com/42

# {% load static %}

# <link rel="stylesheet" href="{% static 'css/open-iconic-bootstrap.min.css' %}">
# <h1 id="colorlib-logo"><a href="{% url 'index' %}">elen<span>.</span></a></h1>
# <div class="slider-item js-fullheight" style="background-image:url({%static 'images/bg_2.jpg' %})">

# <li><a href="{% url 'index' %}">Home</a></li>
# <li><a href="#"><img src="{%static 'images/search-icon.png' %}"></a></li>
#
####################################################################
####################################################################
# <h1>{{ question.question_text }}</h1>

# <ul>
# {% for choice in question.choice_set.all %}
#     <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
# {% endfor %}
# </ul>

# <a href="{% url 'polls:detail' question.id %}">Vote again?</a>

####################################################################
####################################################################

# <form action="{% url 'polls:vote' question.id %}" method="post">
#     {% csrf_token %}
#     <fieldset>
#         <legend><h1>{{ question.question_text }}</h1></legend>
#         {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
            ## 포문
            ## 포문
#         {% for choice in question.choice_set.all %}
#             <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
#             <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
#         {% endfor %}
#     </fieldset>
#     <input type="submit" value="Vote">
#     </form>

# <h1>{{ question.question_text }}</h1>
# <ul>
# {% for choice in question.choice_set.all %}
#     <li>{{ choice.choice_text }}</li>
# {% endfor %}
# </ul>

####################################################################
####################################################################
# 여기가 if문
# 여기가 if문
# {% if latest_question_list %}
#     <ul>
#     <h5>여기가 for문이에요1111111</h5>
#     {% for question in latest_question_list %}
#         <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a> 1번</li>
        
#         <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a> 3번</li>

#     {% endfor %}
#     </ul>
# {% else %}
#     <p>No polls are available.</p>
# {% endif %}
####################################################################
####################################################################
# {% if user.is_authenticated %}
#     <a href="{% url 'logout' %}">로그아웃</a>
# {% else %}
#     <a href="{% url 'login' %}">로그인</a> | <a href="{% url 'signup' %}">회원 가입</a>
# {% endif %}

####################################################################
####################################################################
    # <h2>로그인</h2>
    # <form method="post">
    #     {% csrf_token %}
    #     {{ form.as_p }}
    #     <button type="submit">로그인</button>
    # </form>
#
####################################################################
####################################################################
# <body style="text-align: center;">
#     <h1>{{ home1 }}</h1>
#     <!-- 데이터 표시 -->
#     <pre>{{ data }}</pre>
#     <p>
#     <!-- 이미지 표시 -->    
#     <img src="{{ image }}" alt="Image" style="width: 50%;">  
#     <!-- 데이터 표시 -->
#     <pre>{{ data|safe }}</pre>
# </body>
#
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
#
#
#
#
#
#
#
#
#
#
#
#










###############################################################
############### 아래것은 붙여서 사용하면 된다. ###################
###############################################################
###############################################################







# import os
# import re

# def findPatterns(str):
#     pattern = r'(([\'|"])(css|js|demo-images|fonts|images)\/.*\.(css|js|png|jpg|gif)([\'|"]))'
    
#     p = re.compile(pattern)
#     results = p.findall(str)
    
#     return results

# #다음으로는 이 경로를 장고 경로로 바꿔줘야 하지.
# #"css/~~.css" -> "{% static '/css/~~.css' %}"
# #일단 "나 '로 시작하는지 판단하고
# #그 문자를 앞뒤에서 제거한다.

# def transformLink(link):
#     curQuote = None
#     quote1 = "'"
#     quote2 = '"'

#     if link.startswith(quote1):
#         _link = link.strip(quote1)
#         curQuote = quote1
#     else:
#         _link = link.strip(quote2)
#         curQuote = quote2
    
# ##    if not _link.startswith("/"):
# ##        _link = f"/{_link}"

#     if curQuote == quote1:
#         newLink = f'{{% static "{_link}" %}}'
#         newLink = quote1 + newLink + quote1
#     else:
#         newLink = f"{{% static '{_link}' %}}"
#         newLink = quote2 + newLink + quote2
#     return newLink

# currentPath = os.path.dirname(os.path.abspath(__file__))

# #os.walk를 이용해서 모든 하위 폴더의 파일까지 순차적으로 접근
# for root, dirs, files in os.walk(currentPath):
#     for file in files:
#         #파일을 하나씩 접근해서 .cs로 끝나지 않는 파일은 제외
#         filePath = os.path.join(root, file)
#         if not filePath.endswith(".html"):
#             continue
        
#         print(filePath)
#         #파일에서 내용 읽어오기
#         with open(filePath, 'r', encoding='utf8') as file :
#             filedata = file.read()

#         with open(filePath, 'w', encoding='utf8') as file:
#             file.write("{% load static %}\n")

#         results = findPatterns(filedata)
#         print(results)
#         for result in results:
#             transformed = transformLink(result[0])
#             print(f"from : {result[0]} -> {transformed}")
#             filedata = filedata.replace(result[0], transformed)
        
            
#         #바꾼 내용을 파일에 다시 기록
#         with open(filePath, 'a', encoding='utf8') as file:
#             file.write(filedata)