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
driver.find_element(By.XPATH


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

