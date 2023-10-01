# 셀레니움 패스 알아보기

# //*[@class="product_list"]/*/div/div/p/a
# //*[@class="product_list" and @id="product_list"]/*/div/div/p/a
# //*[@class="product_list" and @id="product_list"]/*/p/a


# 페이지의 전체 HTML 가져오기
# page_source = driver.page_source




# Python Selenium에서 get_attribute() 메서드를 사용하여 얻을 수 있는 속성 중 일부를 다음과 같이 나열합니다. 
# get_attribute() 메서드를 사용하여 요소의 특정 속성을 검색할 수 있습니다.

# id: 요소의 id 속성 값
# name: 요소의 name 속성 값
# class: 요소의 class 속성 값
# href: <a> 태그의 링크 URL
# src: 이미지 또는 소리 파일의 소스 URL
# value: 입력 필드(<input>, <textarea>)의 값
# type: 입력 필드의 타입 (예: "text", "checkbox" 등)
# alt: 이미지 태그(<img>)의 대체 텍스트
# title: 요소의 타이틀 속성 값
# disabled: 요소가 비활성화되었는지 여부 (True 또는 False)
# readonly: 읽기 전용 입력 필드인지 여부 (True 또는 False)
# checked: 체크박스 또는 라디오 버튼이 선택되었는지 여부 (True 또는 False)
# style: 요소의 CSS 스타일 속성 값
# data-*: 데이터 속성의 값 (예: data-custom="value")
# aria-*: ARIA 속성의 값 (예: aria-label, aria-describedby)
# role: 요소의 역할 (예: "button", "menu", "listbox" 등)
# aria-role: ARIA 역할 속성 값
# aria-label: ARIA 레이블 속성 값
# aria-labelledby: ARIA 레이블을 참조하는 레이블 요소의 ID
# aria-describedby: ARIA 설명을 참조하는 설명 요소의 ID
# aria-hidden: 요소가 스크린 리더에서 숨겨져야 하는지 여부 (True 또는 False)
# aria-expanded: ARIA 확장 상태 속성 값
# aria-selected: ARIA 선택 상태 속성 값
# aria-pressed: ARIA 눌림 상태 속성 값
# aria-disabled: ARIA 비활성화 상태 속성 값
# aria-checked: ARIA 체크 상태 속성 값
# aria-valuemin: ARIA 최소 값 속성 값
# aria-valuemax: ARIA 최대 값 속성 값
# aria-valuenow: ARIA 현재 값 속성 값
# aria-valuetext: ARIA 값 텍스트 속성 값


#



# Python Selenium에서 driver. 뒤에 올 수 있는 일반적인 메서드와 속성을 나열하겠습니다. Selenium의 API는 꾸준히 업데이트되므로 모든 가능한 메서드와 속성을 포함할 수는 없지만, 다음은 많이 사용되는 몇 가지입니다.

# driver.get(url) :  주어진 URL로 이동합니다.

# driver.current_url :  현재 페이지의 URL을 반환합니다.
# driver.title :  현재 페이지의 제목을 반환합니다.

# driver.page_source :  현재 페이지의 전체 HTML 소스 코드를 반환합니다.


# driver.find_element(by, value) :  주어진 선택자로 요소를 찾습니다.
# driver.find_elements(by, value) :  주어진 선택자로 여러 요소를 찾습니다.
# driver.switch_to.window(window_name) :  다른 브라우저 창 또는 탭으로 전환합니다.
# driver.switch_to.frame(frame_reference) :  다른 프레임으로 전환합니다.
# driver.back() :  이전 페이지로 이동합니다.
# driver.forward() :  다음 페이지로 이동합니다.
# driver.refresh() :  현재 페이지를 새로고침합니다.
# driver.execute_script(script, *args) :  JavaScript 코드를 실행합니다.
# driver.save_screenshot(filename) :  스크린샷을 저장합니다.
# driver.quit() :  브라우저를 종료하고 세션을 닫습니다.
# driver.maximize_window() :  브라우저 창을 최대화합니다.
# driver.minimize_window() :  브라우저 창을 최소화합니다.
# driver.fullscreen_window() :  브라우저 창을 전체 화면 모드로 전환합니다.
# driver.set_window_size(width, height) :  브라우저 창의 크기를 설정합니다.
# driver.set_window_position(x, y) :  브라우저 창의 위치를 설정합니다.
# driver.get_cookies() :  현재 페이지의 쿠키를 반환합니다.

# driver.find_element(By.id, value) :  주어진 id 속성으로 요소를 찾습니다.
# driver.find_element(By.name, value) :  주어진 name 속성으로 요소를 찾습니다.
# driver.find_element(By.tag_name, value) :  주어진 HTML 태그로 요소를 찾습니다.
# driver.find_element(By.class_name, value) :  주어진 클래스 이름으로 요소를 찾습니다.
# driver.find_element(By.link_text, value) :  주어진 링크 텍스트로 <a> 태그 요소를 찾습니다.
# driver.find_element(By.partial_link_text, value) :  주어진 부분 링크 텍스트로 요소를 찾습니다.
# driver.find_element(By.css_selector, value) :  주어진 CSS 선택자로 요소를 찾습니다.
# driver.find_element(By.xpath, value) :  주어진 XPath로 요소를 찾습니다.
# driver.find_elements_by_*() :  위와 유사한 메서드로, 해당 선택자로 여러 요소를 찾습니다.


# driver.switch_to.alert :  경고 다이얼로그에 대한 상호 작용을 위한 객체를 반환합니다.
# driver.switch_to.frame_to_default_content() :  최상위 프레임으로 돌아갑니다.

# driver.switch_to.active_element :  현재 활성 요소를 반환합니다.
# driver.switch_to.parent_frame() :  부모 프레임으로 전환합니다.
# driver.switch_to.window_handles :  현재 열린 모든 창 또는 탭의 핸들을 반환합니다.
# driver.window_handles :  현재 열린 모든 창 또는 탭의 핸들을 반환합니다.
# driver.window_handles :  현재 열린 모든 창 또는 탭의 핸들 목록을 반환합니다.
# driver.current_window_handle :  현재 창 또는 탭의 핸들을 반환합니다.
# driver.save_screenshot(filename) :  현재 화면을 스크린샷으로 저장합니다.
# driver.get_screenshot_as_base64() :  화면 스크린샷을 Base64 문자열로 가져옵니다.
# driver.get_screenshot_as_file(filename) :  화면 스크린샷을 파일로 저장합니다.
# driver.get_screenshot_as_png() :  화면 스크린샷을 PNG 형식으로 가져옵니다.



# driver.capabilities :  현재 세션의 브라우저 설정 및 능력을 나타내는 객체입니다.

# driver.session_id :  현재 세션의 고유 식별자를 반환합니다.

# driver.back() :  브라우저에서 이전 페이지로 이동합니다.
# driver.forward() :  브라우저에서 다음 페이지로 이동합니다.

# driver.get_cookies() :  현재 페이지의 쿠키 목록을 반환합니다.
# driver.add_cookie(cookie_dict) :  쿠키를 추가합니다.
# driver.delete_cookie(name) :  특정 이름의 쿠키를 삭제합니다.
# driver.delete_all_cookies() :  모든 쿠키를 삭제합니다.

# driver.get_window_size(windowHandle="current") :  창 또는 탭의 크기를 가져옵니다.
# driver.set_window_size(width, height, windowHandle="current") :  창 또는 탭의 크기를 설정합니다.
# driver.get_window_position(windowHandle="current") :  창 또는 탭의 위치를 가져옵니다.
# driver.set_window_position(x, y, windowHandle="current") :  창 또는 탭의 위치를 설정합니다.


# driver.get_log(log_type) :  브라우저 로그를 가져옵니다.

# driver.switch_to.window(window_name) :  다른 창 또는 탭으로 전환합니다.


# driver.switch_to.default_content() :  최상위 프레임으로 돌아갑니다.
# driver.close() :  현재 창 또는 탭을 닫습니다.

# driver.name :  현재 사용 중인 웹 드라이버의 이름을 반환합니다.
# driver.orientation :  디바이스 방향을 반환합니다.


# driver.alert :  경고 다이얼로그에 대한 상호 작용을 위한 객체를 반환합니다.
# driver.context :  현재 컨텍스트(네이티브 앱, 웹뷰 등)를 반환합니다.

# driver.application_cache :  페이지의 애플리케이션 캐시를 나타내는 객체를 반환합니다.

# driver.get_window_rect() :  창 또는 탭의 좌표와 크기 정보를 가져옵니다.

# driver.set_window_rect(x, y, width, height) :  창 또는 탭의 좌표와 크기를 설정합니다.



# driver.get_log("browser") :  브라우저 로그를 가져옵니다.
# driver.get_log("client") :  클라이언트 로그를 가져옵니다.
# driver.get_log("driver") :  드라이버 로그를 가져옵니다.

# driver.get_log("performance") :  성능 로그를 가져옵니다.

# driver.get_network_conditions() :  네트워크 조건 설정을 가져옵니다.
# driver.set_network_conditions(offline, latency, throughput) :  네트워크 조건을 설정합니다.
# driver.session_capabilities :  현재 세션의 브라우저 설정 및 능력을 나타내는 객체를 반환합니다.
# driver.application_cache_status :  페이지의 애플리케이션 캐시 상태를 반환합니다.

# driver.location :  현재 창 또는 탭의 위치 정보를 반환합니다.
# driver.rotation :  화면 회전 정보를 반환합니다.
# driver.window :  현재 창 또는 탭의 핸들 및 기본 속성을 반환합니다.

# driver.file_detector :  파일 전송을 위한 자동 탐지기 설정을 반환합니다.

# driver.get_local_storage_item(key) :  로컬 스토리지에서 특정 항목을 가져옵니다.
# driver.get_local_storage_keys() :  로컬 스토리지의 모든 키 목록을 가져옵니다.
# driver.set_local_storage_item(key, value) :  로컬 스토리지에 항목을 설정합니다.
# driver.remove_local_storage_item(key) :  로컬 스토리지에서 항목을 제거합니다.
# driver.clear_local_storage() :  로컬 스토리지를 모두 지웁니다.


# driver.get_session_storage_item(key) :  세션 스토리지에서 특정 항목을 가져옵니다.
# driver.get_session_storage_keys() :  세션 스토리지의 모든 키 목록을 가져옵니다.
# driver.set_session_storage_item(key, value) :  세션 스토리지에 항목을 설정합니다.
# driver.remove_session_storage_item(key) :  세션 스토리지에서 항목을 제거합니다.
# driver.clear_session_storage() :  세션 스토리지를 모두 지웁니다.
# driver.get_application_cache_status() :  애플리케이션 캐시의 상태를 반환합니다.
# driver.get_active_element() :  현재 활성 요소를 반환합니다.





# By.ID: id 속성을 사용하여 요소를 찾습니다.
# By.NAME: name 속성을 사용하여 요소를 찾습니다.
# By.CLASS_NAME: class 이름을 사용하여 요소를 찾습니다.
# By.TAG_NAME: HTML 태그 이름을 사용하여 요소를 찾습니다.
# By.LINK_TEXT: 링크 텍스트를 사용하여 <a> 태그 요소를 찾습니다.
# By.PARTIAL_LINK_TEXT: 부분 링크 텍스트를 사용하여 요소를 찾습니다.
# By.CSS_SELECTOR: CSS 선택자를 사용하여 요소를 찾습니다.
# By.XPATH: XPath 표현식을 사용하여 요소를 찾습니다.


# 기본
# element1 = driver.find_element(By.XPATH, '//input[@id="search-box"]')


# # 예제 2: 다양한 XPath 표현식 사용
# element2 = driver.find_element(By.XPATH, '//*[@class="example-class"]')
# print("예제 2:", element2.text)

# # 예제 3: 부모 요소에서 자식 요소 찾기
# element3 = driver.find_element(By.XPATH, '//div[@class="parent"]/p')
# print("예제 3:", element3.text)

# # 예제 4: 속성 값으로 요소 찾기
# element4 = driver.find_element(By.XPATH, '//*[@name="submit-button"]')
# print("예제 4:", element4.get_attribute('value'))

# # 예제 5: 인덱스를 사용하여 요소 찾기
# element5 = driver.find_element(By.XPATH, '(//a[@class="nav-link"])[2]')
# print("예제 5:", element5.text)

# # 예제 6: 조건을 사용한 요소 찾기
# element6 = driver.find_element(By.XPATH, '//input[@type="text" and @name="username"]')
# print("예제 6:", element6.get_attribute('placeholder'))

# # 예제 7: 텍스트 내용으로 요소 찾기 #########################################
# element7 = driver.find_element(By.XPATH, '//*[contains(text(), "Example Text")]')
# print("예제 7:", element7.text)

# # 예제 8: XPath 함수 사용 (부모 요소에서 자식 요소 찾기)#########################################
# element8 = driver.find_element(By.XPATH, '//div[@class="parent"]/p[last()]')
# print("예제 8:", element8.text)

# # 예제 9: XPath 함수 사용 (텍스트 속성 값으로 요소 찾기) #########################################
# element9 = driver.find_element(By.XPATH, '//*[normalize-space(text())=" Example Text "]/..')
# print("예제 9:", element9.get_attribute('class'))

# # 예제 10: XPath 함수 사용 (여러 속성으로 요소 찾기) #########################################
# element10 = driver.find_element(By.XPATH, '//*[@name="username" and contains(@class, "input-field")]')
# print("예제 10:", element10.get_attribute('placeholder'))

# # 예제 11: 특정 텍스트를 가진 버튼 요소 찾기
# element11 = driver.find_element(By.XPATH, '//button[text()="Submit"]')
# print("예제 11:", element11.get_attribute('id'))

# # 예제 12: 자식 요소의 개수로 요소 찾기 #########################################
# element12 = driver.find_element(By.XPATH, '//ul[@class="menu"]/li[count(*)=3]')
# print("예제 12:", element12.text)

# # 예제 13: 속성 값에 특정 문자열이 포함된 요소 찾기 #########################################
# element13 = driver.find_element(By.XPATH, '//*[contains(@class, "example")]')
# print("예제 13:", element13.get_attribute('class'))

# # 예제 14: 형제 요소 중 특정 요소 찾기  #########################################
# element14 = driver.find_element(By.XPATH, '//a[@class="nav-link"]/following-sibling::a')
# print("예제 14:", element14.text)

# # 예제 15: 부모 요소에서 자식 요소 중 하나 선택하기 
# element15 = driver.find_element(By.XPATH, '//div[@class="parent"]/p[1]')
# print("예제 15:", element15.text)

# # 예제 16: 속성 이름으로 요소 찾기
# element16 = driver.find_element(By.XPATH, '//*[@data-testid="example-element"]')
# print("예제 16:", element16.get_attribute('id'))

# # 예제 17: 여러 속성 및 값으로 요소 찾기
# element17 = driver.find_element(By.XPATH, '//*[@class="example-class" and @name="example-name"]')
# print("예제 17:", element17.get_attribute('placeholder'))

# # 예제 18: 다중 클래스 속성을 가진 요소 찾기
# element18 = driver.find_element(By.XPATH, '//*[contains(@class, "class1") and contains(@class, "class2")]')
# print("예제 18:", element18.get_attribute('id'))

# # 예제 19: 특정 속성을 포함하지 않은 요소 찾기  #########################################
# element19 = driver.find_element(By.XPATH, '//*[@data-testid and not(@disabled)]')
# print("예제 19:", element19.get_attribute('id'))

# # 예제 20: 요소의 자식 요소에 접근하기
# element20 = driver.find_element(By.XPATH, '//div[@class="parent"]/p/span')
# print("예제 20:", element20.text)





# # 예제 21: XPath 축(axis) 사용하여 요소 찾기 (자식 요소) 
# element21 = driver.find_element(By.XPATH, '//div[@class="parent"]/*')
# print("예제 21:", element21.text)

# # 예제 22: XPath 축(axis) 사용하여 요소 찾기 (부모 요소)
# element22 = driver.find_element(By.XPATH, '//span[text()="Child Text"]/parent::p')
# print("예제 22:", element22.text)

# # 예제 23: XPath 축(axis) 사용하여 요소 찾기 (형제 요소)
# element23 = driver.find_element(By.XPATH, '//a[text()="Link 1"]/following-sibling::a')
# print("예제 23:", element23.text)

# # 예제 24: XPath 함수 사용 (문자열 길이 비교) #########################################
# element24 = driver.find_element(By.XPATH, '//input[string-length(@value) > 10]')
# print("예제 24:", element24.get_attribute('value'))

# # 예제 25: XPath 함수 사용 (문자열 변환) #########################################
# element25 = driver.find_element(By.XPATH, '//p[contains(text(), "Count: ")][number(text()) > 5]')
# print("예제 25:", element25.text)

# # 예제 26: XPath 함수 사용 (속성 값 비교) #########################################
# element26 = driver.find_element(By.XPATH, '//*[@id="example-element"][@data-testid="test-id"]')
# print("예제 26:", element26.get_attribute('class'))

# # 예제 27: 다수의 속성 중 하나를 가진 요소 찾기 #########################################
# element27 = driver.find_element(By.XPATH, '//*[@id="example-element"][contains(@class, "class1") or contains(@class, "class2")]')
# print("예제 27:", element27.get_attribute('id'))

# # 예제 28: 요소의 인덱스 위치에 따라 찾기
# element28 = driver.find_element(By.XPATH, '(//div[@class="example"])[2]')
# print("예제 28:", element28.text)

# # 예제 29: XPath 축(axis) 사용하여 조상 요소 찾기
# element29 = driver.find_element(By.XPATH, '//a[text()="Link 1"]/ancestor::div')
# print("예제 29:", element29.get_attribute('class'))

# # 예제 30: 논리 연산자를 사용하여 여러 조건 결합 #########################################
# element30 = driver.find_element(By.XPATH, '//*[@class="example-class" and contains(@id, "element") and not(contains(@class, "disabled"))]')
# print("예제 30:", element30.get_attribute('id'))






#############################################################
################# ActionChain   #############################
################# ActionChain   #############################
################# ActionChain   #############################
################# ActionChain   #############################
#############################################################\

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# WebDriver 초기화
driver = webdriver.Chrome(executable_path='경로/chromedriver')  # chromedriver 경로를 설정하세요.

# 웹 페이지 열기
driver.get("https://example.com")  # 원하는 웹 페이지 URL로 변경하세요.

# ActionChains 객체 생성
# actions = ActionChains(driver)

# # 1. 요소를 클릭
# element = driver.find_element_by_id("element_id")
# actions.click(element).perform()

# # 2. 요소를 더블 클릭
# element = driver.find_element_by_id("element_id")
# actions.double_click(element).perform()

# # 3. 요소에 우클릭
# element = driver.find_element_by_id("element_id")
# actions.context_click(element).perform()

# # 4. 요소로 마우스 이동
# element = driver.find_element_by_id("element_id")
# actions.move_to_element(element).perform()

# # 5. 키보드 입력 (예: "Hello" 입력)
# actions.send_keys("Hello").perform()

# # 6. 키보드 단축키 입력 (예: Ctrl+A)
# actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# # 7. 스크롤 내리기 (예: 아래로 200픽셀)
# actions.send_keys(Keys.PAGE_DOWN * 2).perform()

# # 8. 액션 초기화
# actions.reset_actions()

# # 9. 요소에 대한 컨텍스트 메뉴 열기
# element = driver.find_element_by_id("element_id")
# actions.context_click(element).perform()

# # 10. 요소에서 특정 위치로 드래그 앤 드롭
# source_element = driver.find_element_by_id("source_element")
# target_element = driver.find_element_by_id("target_element")
# actions.click_and_hold(source_element).move_to_element(target_element).release().perform()

# # 11. 요소에서 특정 오프셋으로 드래그 앤 드롭
# element = driver.find_element_by_id("element_id")
# actions.click_and_hold(element).move_by_offset(100, 0).release().perform()

# # 12. 브라우저 뒤로 가기
# actions.move_back().perform()

# # 13. 브라우저 앞으로 가기
# actions.move_forward().perform()

# # 14. 새 탭 열기 (Ctrl+T)
# actions.key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()

# # 15. 현재 탭 닫기 (Ctrl+W)
# actions.key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()

# # 16. 마우스 드래그 액션
# actions.click_and_hold().move_by_offset(100, 0).release().perform()

# # 17. 엔터 키 입력
# actions.send_keys(Keys.RETURN).perform()

# # 18. 마우스 휠 스크롤 (예: 아래로 3번)
# actions.move(0, 0).perform()
# actions.move(0, 3).perform()

# # 19. 현재 탭에서 새 창 열기 (Ctrl+클릭)
# element = driver.find_element_by_id("element_id")
# actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

# # 20. 요소를 드래그해서 다른 요소로 놓기
# source_element = driver.find_element_by_id("source_element")
# target_element = driver.find_element_by_id("target_element")
# actions.drag_and_drop(source_element, target_element).perform()



# # 21. 요소에서 Shift 키와 함께 클릭
# element = driver.find_element_by_id("element_id")
# actions.key_down(Keys.SHIFT).click(element).key_up(Keys.SHIFT).perform()

# # 22. 요소에서 Alt 키와 함께 클릭
# element = driver.find_element_by_id("element_id")
# actions.key_down(Keys.ALT).click(element).key_up(Keys.ALT).perform()

# # 23. 요소에서 Ctrl 키와 함께 클릭
# element = driver.find_element_by_id("element_id")
# actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

# # 24. 요소에 마우스 우클릭하고 메뉴에서 아이템 선택
# element = driver.find_element_by_id("element_id")
# actions.context_click(element).perform()

# # 25. 요소에서 마우스 우클릭하고 메뉴에서 아이템 선택 (2단계)
# element = driver.find_element_by_id("element_id")
# sub_menu_item = driver.find_element_by_id("sub_menu_item_id")
# actions.context_click(element).click(sub_menu_item).perform()

# # 26. 요소에서 드래그 앤 드롭 (두 번의 드래그 액션)
# source_element = driver.find_element_by_id("source_element")
# target_element = driver.find_element_by_id("target_element")
# actions.drag_and_drop(source_element, target_element).perform()
# actions.drag_and_drop(source_element, target_element).perform()

# # 27. 요소에서 Shift 키와 함께 드래그 앤 드롭
# actions.key_down(Keys.SHIFT).drag_and_drop(source_element, target_element).key_up(Keys.SHIFT).perform()

# # 28. 요소에서 Ctrl 키와 함께 드래그 앤 드롭
# actions.key_down(Keys.CONTROL).drag_and_drop(source_element, target_element).key_up(Keys.CONTROL).perform()

# # 29. 요소에서 Shift 키와 함께 드래그 앤 드롭 (2단계)
# actions.key_down(Keys.SHIFT).drag_and_drop(source_element, target_element).key_up(Keys.SHIFT).perform()
# actions.drag_and_drop(source_element, target_element).perform()

# # 30. 요소에서 Ctrl 키와 함께 드래그 앤 드롭 (2단계)
# actions.key_down(Keys.CONTROL).drag_and_drop(source_element, target_element).key_up(Keys.CONTROL).perform()
# actions.drag_and_drop(source_element, target_element).perform()

# # 31. 요소에서 특정 키 조합 입력 (Ctrl+Shift+A)
# element = driver.find_element_by_id("element_id")
# actions.click(element).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys("a").key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()

# # 32. 요소에서 Ctrl+A 후 텍스트 입력
# element = driver.find_element_by_id("element_id")
# actions.click(element).key_down(Keys.CONTROL).send_keys("a").send_keys("Hello").perform()

# # 33. 키보드 키 누르기와 떼기 (Shift 키 누르기)
# actions.key_down(Keys.SHIFT).perform()
# actions.key_up(Keys.SHIFT).perform()

# # 34. 키보드 키 누르기와 떼기 (Ctrl 키 누르기)
# actions.key_down(Keys.CONTROL).perform()
# actions.key_up(Keys.CONTROL).perform()

# # 35. 요소에서 마우스 이동하고 클릭 (move_to_element과 click 조합)
# element = driver.find_element_by_id("element_id")
# actions.move_to_element(element).click().perform()

# # 36. 요소에서 마우스 우클릭하고 메뉴에서 아이템 선택 (순차적으로)
# element = driver.find_element_by_id("element_id")
# actions.context_click(element).perform()
# actions.click(sub_menu_item).perform()

# # 37. 요소에서 Shift 키와 함께 클릭 (2단계)
# element = driver.find_element_by_id("element_id")
# actions.key_down(Keys.SHIFT).click(element).key_up(Keys.SHIFT).perform()

# # 38. 요소에서 특정 키 누르기와 클릭
# element = driver.find_element_by_id("element_id")
# actions.click(element).key_down(Keys.ALT).click().key_up(Keys.ALT).perform()

# # 39. 요소에서 특정 키 누르기와 마우스 이동 (2단계)
# element = driver.find_element_by_id("element_id")
# actions.move_to_element(element).key_down(Keys.ALT).move_to_element(target_element).key_up(Keys.ALT).perform()

# # 40. 요소에서 특정 키 누르기와 드래그 앤 드롭 (2단계)
# element = driver.find_element_by_id("element_id")
# actions.click_and_hold(element).key_down(Keys.ALT).move_to_element(target_element).key_up(Keys.ALT).release().perform()






# # 41. 요소에서 특정 키 누르기와 텍스트 입력 (Shift 키 누르고 "Hello" 입력)
# element = driver.find_element_by_id("element_id")
# actions.click(element).key_down(Keys.SHIFT).send_keys("Hello").key_up(Keys.SHIFT).perform()

# # 42. 요소에서 마우스 이동 후 키보드 키 입력
# element = driver.find_element_by_id("element_id")
# actions.move_to_element(element).send_keys("Hello").perform()

# # 43. 요소에서 특정 키 누르기와 떼기 (Ctrl 키 누르고 떼기)
# actions.key_down(Keys.CONTROL).perform()
# actions.key_up(Keys.CONTROL).perform()

# # 44. 마우스 우클릭하고 메뉴에서 아이템 선택 (메뉴 열기)
# actions.context_click().perform()

# # 45. 특정 키 조합 입력 (Alt+Shift+D)
# actions.key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys("d").key_up(Keys.SHIFT).key_up(Keys.ALT).perform()

# # 46. 요소에서 마우스 우클릭하고 메뉴에서 아이템 선택 (다단계 메뉴)
# element = driver.find_element_by_id("element_id")
# sub_menu1 = driver.find_element_by_id("sub_menu1_id")
# sub_menu2 = driver.find_element_by_id("sub_menu2_id")
# actions.context_click(element).click(sub_menu1).click(sub_menu2).perform()

# # 47. 드래그 앤 드롭 후 키보드 키 입력
# source_element = driver.find_element_by_id("source_element")
# target_element = driver.find_element_by_id("target_element")
# actions.drag_and_drop(source_element, target_element).send_keys("Hello").perform()

# # 48. 요소에서 Ctrl 키와 함께 드래그 앤 드롭 (다단계)
# actions.key_down(Keys.CONTROL).drag_and_drop(source_element, target_element).key_up(Keys.CONTROL).perform()
# actions.drag_and_drop(source_element, target_element).perform()

# # 49. 요소에서 Shift 키와 함께 드래그 앤 드롭 (다단계)
# actions.key_down(Keys.SHIFT).drag_and_drop(source_element, target_element).key_up(Keys.SHIFT).perform()
# actions.drag_and_drop(source_element, target_element).perform()

# # 50. 요소에서 클릭하고 텍스트 입력
# element = driver.find_element_by_id("element_id")
# actions.click(element).send_keys("Hello").perform()

# # 51. 요소에서 마우스 이동 후 텍스트 입력 (2단계)
# element = driver.find_element_by_id("element_id")
# actions.move_to_element(element).send_keys("Hello").perform()

# # 52. 요소에서 Ctrl 키와 함께 클릭
# element = driver.find_element_by_id("element_id")
# actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

# # 53. 요소에서 Ctrl 키와 함께 드래그 앤 드롭 (Ctrl+드래그+클릭)
# actions.key_down(Keys.CONTROL).click_and_hold(element).drag_and_drop(target_element).release().key_up(Keys.CONTROL).perform()

# # 54. 마우스 이동 후 클릭
# actions.move_by_offset(100, 0).click().perform()

# # 55. 요소에서 드래그 앤 드롭 후 키보드 키 입력 (다단계)
# actions.drag_and_drop(source_element, target_element).send_keys("Hello").perform()
# actions.drag_and_drop(source_element, target_element).send_keys("World").perform()

# # 56. 요소에서 드래그 앤 드롭 후 스크롤 (다단계)
# actions.drag_and_drop(source_element, target_element).perform()
# actions.move(0, 200).perform()

# # 57. 요소에서 드래그 앤 드롭 후 마우스 우클릭 (다단계)
# actions.drag_and_drop(source_element, target_element).context_click().perform()

# # 58. 요소에서 드래그 앤 드롭 후 요소에 우클릭 (다단계)
# actions.drag_and_drop(source_element, target_element).perform()
# actions.context_click(element).perform()

# # 59. 요소에서 드래그 앤 드롭 후 요소로 이동 (다단계)
# actions.drag_and_drop(source_element, target_element).move_to_element(element).perform()

# # 60. 요소에서 드래그 앤 드롭 후 요소에서 특정 키 누르기 (다단계)
# actions.drag_and_drop(source_element, target_element).key_down(Keys.ALT).perform()
# actions.key_up(Keys.ALT).perform()




# # 61. 요소에서 클릭하고 Ctrl 키와 함께 텍스트 입력
# element = driver.find_element_by_id("element_id")
# actions.click(element).key_down(Keys.CONTROL).send_keys("Hello").key_up(Keys.CONTROL).perform()

# # 62. 요소에서 Shift 키와 함께 드래그 앤 드롭 (2단계)
# element = driver.find_element_by_id("element_id")
# target_element = driver.find_element_by_id("target_element")
# actions.click_and_hold(element).move_to_element(target_element).release().key_down(Keys.SHIFT).perform()

# # 63. 요소에서 클릭하고 Shift 키와 함께 텍스트 입력 (다단계)
# element = driver.find_element_by_id("element_id")
# actions.click(element).key_down(Keys.SHIFT).send_keys("Hello").key_up(Keys.SHIFT).perform()

# # 64. 요소에서 마우스 우클릭하고 메뉴에서 아이템 선택 (3단계)
# element = driver.find_element_by_id("element_id")
# sub_menu1 = driver.find_element_by_id("sub_menu1_id")
# sub_menu2 = driver.find_element_by_id("sub_menu2_id")
# actions.context_click(element).click(sub_menu1).click(sub_menu2).perform()

# # 65. 요소에서 특정 키 누르기와 떼기 (Shift+Ctrl+D)
# element = driver.find_element_by_id("element_id")
# actions.click(element).key_down(Keys.SHIFT).key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL).key_up(Keys.SHIFT).perform()

# # 66. 요소에서 드래그 앤 드롭 후 요소에 마우스 우클릭 (다단계)
# source_element = driver.find_element_by_id("source_element")
# target_element = driver.find_element_by_id("target_element")
# actions.drag_and_drop(source_element, target_element).context_click(element).perform()

# # 67. 요소에서 클릭하고 텍스트 입력 후 엔터 (다단계)
# element = driver.find_element_by_id("element_id")
# actions.click(element).send_keys("Hello").send_keys(Keys.RETURN).perform()

# # 68. 요소에서 Shift 키와 함께 드래그 앤 드롭 후 키보드 키 입력 (다단계)
# actions.key_down(Keys.SHIFT).drag_and_drop(source_element, target_element).key_up(Keys.SHIFT).send_keys("Hello").perform()

# # 69. 요소에서 드래그 앤 드롭 후 특정 키 누르기와 마우스 우클릭 (다단계)
# actions.drag_and_drop(source_element, target_element).key_down(Keys.ALT).context_click().perform()

# # 70. 요소에서 클릭하고 텍스트 입력 후 특정 키 누르기와 드래그 앤 드롭 (다단계)
# actions.click(element).send_keys("Hello").key_down(Keys.ALT).drag_and_drop(source_element, target_element).key_up(Keys.ALT).perform()

# # 71. 요소에서 마우스 이동 후 특정 키 누르기와 클릭 (다단계)
# actions.move_to_element(element).key_down(Keys.ALT).click().key_up(Keys.ALT).perform()

# # 72. 요소에서 마우스 이동 후 특정 키 누르기와 드래그 앤 드롭 (다단계)
# actions.move_to_element(element).key_down(Keys.ALT).drag_and_drop(source_element, target_element).key_up(Keys.ALT).perform()

# # 73. 요소에서 클릭하고 텍스트 입력 후 특정 키 누르기와 엔터 (다단계)
# actions.click(element).send_keys("Hello").key_down(Keys.ALT).send_keys(Keys.RETURN).key_up(Keys.ALT).perform()

# # 74. 요소에서 드래그 앤 드롭 후 스크롤 (3단계)
# actions.drag_and_drop(source_element, target_element).move_by_offset(0, 100).perform()

# # 75. 요소에서 드래그 앤 드롭 후 클릭 (다단계)
# actions.drag_and_drop(source_element, target_element).click().perform()

# # 76. 요소에서 텍스트 입력 후 키보드 키 입력 (2단계)
# actions.send_keys("Hello").send_keys(Keys.ENTER).perform()

# # 77. 요소에서 Ctrl 키와 함께 클릭 후 특정 키 누르기 (다단계)
# actions.click(element).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# # 78. 요소에서 드래그 앤 드롭 후 마우스 이동 (3단계)
# actions.drag_and_drop(source_element, target_element).move_to_element(element).perform()

# # 79. 요소에서 드래그 앤 드롭 후 요소 클릭 (다단계)
# actions.drag_and_drop(source_element, target_element).click(element).perform()

# # 80. 요소에서 드래그 앤 드롭 후 키보드 키 입력 후 스크롤 (다단계)
# actions.drag_and_drop(source_element, target_element).send_keys("Hello").move_by_offset(0, 100).perform()
