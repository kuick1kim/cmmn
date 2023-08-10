import cv2
import matplotlib.pyplot as plt
import time
import numpy as np


 


# 아무것도 없는 공 image만들기
def make_zero_background(x_size, y_size):
    image = np.full((x_size, y_size, 3), 255, np.uint8)
    return image

### 그림에 선하나 그리기
def draw_line_in_image(image, from_x1_x2, from_y1_y2):
    x1,x2 = from_x1_x2.split("-")
    y1,y2 = from_y1_y2.split("-")
    x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)
    image = cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    # 1) 선그리기
    # cv2.line(image, start, end, color, thickness): 하나의 직선을 그리는 함수
    # start: 시작 좌표 (2차원)
    # end: 종료 좌표 (2차원)
    # thickness: 선의 두께
    return image


### 그림에 네모하나 그리기
def draw_rectangle_in_image(image, from_x1_x2, from_y1_y2):
    x1,x2 = from_x1_x2.split("-")
    y1,y2 = from_y1_y2.split("-")
    x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)
    image = cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 10)

    # cv2.rectangle(image, start, end, color, thickness): 하나의 사각형을 그리는 함수
    # start: 시작 좌표 (2차원)
    # end: 종료 좌표 (2차원)
    # thickness: 선의 두께 (채우기: -1)
    return image



### 그림에 원하나 그리기
def draw_circle_in_image(image, from_x1_y1, radian):
    x1,y1 = from_x1_y1.split("-")    
    x1,y1,r = int(x1),int(y1),int(radian)
    image = cv2.circle(image, (x1, y1), r, (100, 100, 200), 3)
    # cv2.circle(image, center, radian, color, thickness): 하나의 원을 그리는 함수
    # center: 원의 중심 (2차원)
    # radian: 반지름
    # thickness: 선의 두께 (채우기: -1)
    return image

    
### 그림에 다각형 그리기
def draw_polylines_in_image(image, points):
    ### 사용예 points = np.array([[5, 5], [128, 258], [483, 444], [400, 150]])
    image = cv2.polylines(image, [points],True, (100,100, 200), 4)
    # cv2.polylines(image, points, is_closed, color, thickness): 하나의 다각형을 그리는 함수
    # points: 꼭지점들
    # is_closed: 닫힌 도형 여부
    # thickness: 선의 두께 (채우기: -1)
    return image

    
### 그림에 글씨 넣기
def draw_putText_in_image(image, text):
    image = cv2.putText(image, text, (20, 200), cv2.FONT_ITALIC, 1.5, (100, 100, 200))
    # cv2.putText(image, text, position, font_type, font_scale, color): 하나의 텍스트를 그리는 함수
    # position: 텍스트가 출력될 위치
    # font_type: 글씨체
    # font_scale: 글씨 크기 가중치
    return image

    






def print_pic_window(img):    
    cv2.imshow('Enter space_bar',img)
    cv2.waitKey(0)
    plt.show() 
    time.sleep(3)
    cv2.destroyAllWindows()






def print_pic_matplotlib(img):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) #### 
    ##### OpenCV는 BGR을 기준으로 하며, Matplotlib는 RGB를 기준으로 합니다.
    plt.pause(4) #### 멈췄다 닫으세요
    plt.close()    #### 멈췄다 닫으세요
    
    





def open_img1(path):
    # ex img_basic= common_opencv1.open_img1('A01_test/cat.jfif')
    img_basic = cv2.imread(path, cv2.IMREAD_COLOR)
    print("이미지 형태 : "+ str(img_basic.shape)) ### 여기는 이미지 사이즈 비교하는것
    
    # print_pic_window(img_basic)
    # print_pic_matplotlib(img_basic)
    return img_basic


def save_img1(path, object_k):
    # ex: common_opencv1.save_img1('A01_test/cat2.png', img_basic)
    cv2.imwrite(path, object_k)


def comvert_img_grey1(object_k):
    # ex: img_grey = common_opencv1.comvert_img_grey1(img_basic)
    img_gray = cv2.cvtColor(object_k, cv2.COLOR_BGR2GRAY)
    # print_pic_window(img_gray)
    # print_pic_matplotlib(img_gray)
    return img_gray



def chage_big_or_small(img, change_x, change_y):
    ###### 사이즈를 크게 만들기 작게 만들기
    # 사용예 image = common_opencv1.chage_big_or_small(image, 2,2)
    if change_x > 1:
        img = cv2.resize(img, None, fx=change_x, fy=change_y, interpolation=cv2.INTER_CUBIC)
    elif change_x < 1:
        img = cv2.resize(img, None, fx=change_x, fy=change_y, interpolation=cv2.INTER_AREA)

    print("크기 변경후 : "+ str(img.shape)) ### 여기는 이미지 사이즈 비교하는것
    
    return img
    



def move_img(img, move_x, move_y):
    ### 사용예  image = common_opencv1.move_img(image, 50, 10)
    
    height, width = img.shape[:2] ### 2번째 까지 가져오세요
    ## x와 Y를 가져와 
    M = np.float32([[1, 0, move_x], [0, 1, move_y]]) 
    ### X축으로 50픽셀 옮기고 Y축으로 10만큼 움직여라
    img = cv2.warpAffine(img, M, (width, height))
    return img




def rotate_img(img, rotate, scale): #스케일은 크기이다. 
    ### 사용예 image = common_opencv1.rotate_img(image, 90, 2)
    # 행과 열 정보만 저장합니다.
    height, width = img.shape[:2]
    M = cv2.getRotationMatrix2D((width / 2, height / 2),  rotate, scale)
    img = cv2.warpAffine(img, M, (width, height))
    return img