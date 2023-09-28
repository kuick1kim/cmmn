import json




# JSON 문자열 파싱: json.loads() 함수를 사용하여 JSON 문자열을 Python 객체로 파싱합니다.
 
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)

# Python 객체를 JSON 문자열로 직렬화: json.dumps() 함수를 사용하여 Python 객체를 JSON 문자열로 변환합니다.
 
data = {"name": "John", "age": 30}
json_string = json.dumps(data)

# JSON 파일 읽기: JSON 파일을 읽어 Python 객체로 파싱합니다.
 
# with open('data.json', 'r') as file:
#     data = json.load(file)

# Python 객체를 JSON 파일로 저장: Python 객체를 JSON 파일로 저장합니다.
 
data = {"name": "John", "age": 30}
# with open('data.json', 'w') as file:
#     json.dump(data, file)

# JSON pretty-printing: 들여쓰기와 줄 바꿈을 추가하여 읽기 쉬운 형식으로 JSON 문자열을 생성합니다.
 
data = {"name": "John", "age": 30}
pretty_json = json.dumps(data, indent=4)

# JSON 특정 필드 접근: 파싱한 JSON 객체에서 특정 필드에 접근합니다.
 
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
name = data['name']

# JSON 필드 추가: 기존 JSON 객체에 새로운 필드를 추가합니다.
 
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
data['city'] = 'New York'

# JSON 필드 수정: 기존 JSON 객체의 필드 값을 수정합니다.
 
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
data['age'] = 31

# JSON 필드 삭제: JSON 객체에서 필드를 제거합니다.
 
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
del data['age']

# JSON 리스트 처리: JSON 배열에 접근하고 수정합니다.
 
json_string = '{"fruits": ["apple", "banana", "cherry"]}'
data = json.loads(json_string)
first_fruit = data['fruits'][0]

# 누락된 필드 처리: get() 메서드를 사용하여 필드가 누락된 경우 기본 값을 제공합니다.
 
json_string = '{"name": "John"}'
data = json.loads(json_string)
age = data.get('age', 25)  # age 필드가 누락되면 기본 값 25를 사용

# JSON 유효성 검사: json.JSONDecodeError 예외를 처리하여 JSON 유효성을 검사합니다.
 
# json_string = 'invalid_json_string'
# try:
#     data = json.loads(json_string)
# except json.JSONDecodeError as e:
#     print(f"JSON 유효성 검사 오류: {e}")

# 중첩된 JSON 처리: 중첩된 JSON 객체를 다룹니다.
 
json_string = '{"person": {"name": "John", "age": 30}}'
data = json.loads(json_string)
person_name = data['person']['name']

# JSON 배열의 길이 얻기: JSON 배열의 길이를 얻습니다.
 
json_string = '[1, 2, 3, 4, 5]'
data = json.loads(json_string)
array_length = len(data)

# JSON을 정렬된 문자열로 변환: sort_keys 옵션을 사용하여 JSON 키를 정렬하여 문자열로 변환합니다.
 
data = {"b": 2, "a": 1, "c": 3}
sorted_json = json.dumps(data, sort_keys=True)

# JSON 객체 검색: 특정 조건을 충족하는 JSON 객체를 검색합니다.
 
data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
matching_objects = [item for item in data if item['age'] == 30]

# JSON 필드 값 정수로 변환: JSON 필드 값을 정수로 변환합니다.
 
json_string = '{"count": "42"}'
data = json.loads(json_string)
count_as_int = int(data['count'])

# JSON 문자열 예외 처리: try-except 블록을 사용하여 JSON 파싱 예외를 처리합니다.
 
# json_string = 'invalid_json_string'
# try:
#     data = json.loads(json_string)
# except json.JSONDecodeError as e:
#     print(f"JSON 파싱 오류: {e}")

# JSON 필드 존재 여부 확인: 특정 필드가 JSON 객체에 존재하는지 확인합니다.
 
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
has_age = 'age' in data

# JSON 데이터 필터링: 특정 필드를 제외한 JSON 데이터를 필터링합니다.
 
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
filtered_data = {key: value for key, value in data.items() if key != 'age'}






# 특정 필드 추출: JSON 객체에서 특정 필드만 추출합니다.  
data = {"name": "John", "age": 30, "city": "New York"}
filtered_data = {"name": data["name"]}

# 여러 필드 추출: 여러 필드를 동시에 추출합니다.  
data = {"name": "John", "age": 30, "city": "New York"}
filtered_data = {"name": data["name"], "age": data["age"]}

# 특정 필드 제외: 특정 필드를 데이터에서 제외합니다.  
data = {"name": "John", "age": 30, "city": "New York"}
filtered_data = {key: value for key, value in data.items() if key != "age"}

# 특정 값에 따른 필터링: 특정 값에 따라 데이터를 필터링합니다.  
data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
filtered_data = [item for item in data if item["age"] >= 30]

# 특정 키 존재 여부에 따른 필터링: 특정 키의 존재 여부에 따라 데이터를 필터링합니다.  
data = [{"name": "John", "age": 30}, {"name": "Alice"}]
filtered_data = [item for item in data if "age" in item]

# 부분 문자열을 포함하는 데이터 필터링: 부분 문자열을 포함하는 데이터를 필터링합니다.  
data = [{"name": "John"}, {"name": "Alice"}, {"name": "Bob"}]
filtered_data = [item for item in data if "li" in item["name"]]

# 특정 범위의 숫자 필터링: 숫자 필드에서 특정 범위의 값만 필터링합니다.  
data = [{"value": 10}, {"value": 20}, {"value": 30}]
filtered_data = [item for item in data if 15 <= item["value"] <= 25]

# 중첩된 JSON 필터링: 중첩된 JSON 객체의 필드를 필터링합니다.  
data = [{"name": {"first": "John", "last": "Doe"}}, {"name": {"first": "Alice", "last": "Smith"}}]
filtered_data = [{"name": {"first": item["name"]["first"]}} for item in data]

# 리스트 요소 필터링: JSON 배열에서 특정 조건을 충족하는 요소만 필터링합니다.  
data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
filtered_data = [item for item in data if item["age"] > 25]

# 특정 키가 있는 객체 필터링: 특정 키를 가진 객체만 필터링합니다.  
data = [{"name": "John", "age": 30}, {"age": 25}]
filtered_data = [item for item in data if "name" in item]

# 특정 필드가 특정 값인 객체 필터링: 특정 필드의 값이 특정 값인 객체를 필터링합니다.  
data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
filtered_data = [item for item in data if item["name"] == "John"]

# 특정 필드가 없는 객체 필터링: 특정 필드가 없는 객체를 필터링합니다.  
data = [{"name": "John", "age": 30}, {"age": 25}]
filtered_data = [item for item in data if "name" not in item]

# 특정 필드의 유일한 값 추출: 특정 필드의 유일한 값만 추출합니다.  
data = [{"name": "John"}, {"name": "Alice"}, {"name": "John"}]
unique_names = list({item["name"] for item in data})

# 특정 필드의 평균 값 계산: 특정 필드의 평균 값을 계산합니다.  
data = [{"score": 85}, {"score": 90}, {"score": 78}]
scores = [item["score"] for item in data]
average_score = sum(scores) / len(scores)

# 특정 필드의 최댓값 및 최솟값 찾기: 특정 필드의 최댓값과 최솟값을 찾습니다.  
data = [{"value": 10}, {"value": 20}, {"value": 5}]
values = [item["value"] for item in data]
max_value = max(values)
min_value = min(values)

# 특정 필드의 정렬: 특정 필드를 기준으로 데이터를 정렬합니다.  
data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
sorted_data = sorted(data, key=lambda x: x["age"])

# 특정 필드의 값으로 그룹화: 특정 필드의 값으로 데이터를 그룹화합니다.  
data = [{"name": "John", "group": "A"}, {"name": "Alice", "group": "B"}, {"name": "Bob", "group": "A"}]
grouped_data = {}
for item in data:
    group = item["group"]
    if group not in grouped_data:
        grouped_data[group] = []
    grouped_data[group].append(item)

# 특정 필드의 유일한 값 수 세기: 특정 필드의 유일한 값 수를 세어봅니다.  
data = [{"category": "A"}, {"category": "B"}, {"category": "A"}, {"category": "C"}]
unique_categories = {item["category"] for item in data}
unique_category_count = len(unique_categories)

# 특정 필드의 값으로 필터링 및 그룹화: 특정 필드의 값을 기준으로 필터링하고 그룹화합니다.  
data = [{"name": "John", "group": "A"}, {"name": "Alice", "group": "B"}, {"name": "Bob", "group": "A"}]
filtered_and_grouped_data = {}
for item in data:
    if item["group"] == "A":
        if "A" not in filtered_and_grouped_data:
            filtered_and_grouped_data["A"] = []
        filtered_and_grouped_data["A"].append(item)

# 여러 조건을 조합한 필터링: 여러 조건을 조합하여 데이터를 필터링합니다.  
data = [{"name": "John", "age": 30, "city": "New York"}, {"name": "Alice", "age": 25, "city": "Los Angeles"}]
filtered_data = [item for item in data if item["age"] > 25 and item["city"] == "New York"]







##############  중급반  #####################################
##############  중급반  #####################################
##############  중급반  #####################################
##############  중급반  #####################################
##############  중급반  #####################################



# 중첩된 필드 필터링: 중첩된 JSON 객체에서 특정 필드 값을 추출합니다. 

data = {"person": {"name": "John", "address": {"city": "New York"}}}
city = data["person"]["address"]["city"]

# 여러 조건과 중첩 필터링: 여러 조건을 조합하여 중첩된 JSON 데이터를 필터링합니다. 

data = [{"name": "John", "details": {"age": 30, "city": "New York"}},
        {"name": "Alice", "details": {"age": 25, "city": "Los Angeles"}}]
filtered_data = [item for item in data if item["details"]["age"] > 25 and item["details"]["city"] == "New York"]

# JSON 배열에서 중첩된 필드 추출: JSON 배열에서 중첩된 필드 값을 추출합니다.  
data = [{"person": {"name": "John"}}, {"person": {"name": "Alice"}}]
names = [item["person"]["name"] for item in data]

# 중첩된 배열 필터링: 중첩된 배열에서 특정 조건을 충족하는 요소를 추출합니다.  
data = {"groups": [{"name": "Group A", "members": ["Alice", "Bob"]},
                  {"name": "Group B", "members": ["Charlie", "David"]}]}

filtered_groups = [group for group in data["groups"] if "Alice" in group["members"]]

# 중첩된 배열의 요소 수 세기: 중첩된 배열에서 각 객체의 요소 수를 세어봅니다.  
data = {"groups": [{"name": "Group A", "members": ["Alice", "Bob"]},
                  {"name": "Group B", "members": ["Charlie", "David"]}]}

member_counts = [len(group["members"]) for group in data["groups"]]

# 중첩된 JSON 객체를 플랫하게 만들기: 중첩된 JSON 객체를 플랫하게 만들어 단일 객체 목록을 얻습니다.  
data = [{"person": {"name": "John", "age": 30}},
        {"person": {"name": "Alice", "age": 25}}]

flat_data = [{"name": item["person"]["name"], "age": item["person"]["age"]} for item in data]

# 중첩된 필드의 평균 값 계산: 중첩된 필드의 평균 값을 계산합니다.  
data = {"people": [{"name": "John", "grades": [90, 85, 88]},
                  {"name": "Alice", "grades": [95, 92, 89]}]}

average_grades = [sum(person["grades"]) / len(person["grades"]) for person in data["people"]]

# 중첩된 필드에서 최댓값 찾기: 중첩된 필드에서 최댓값을 찾습니다.  
data = {"people": [{"name": "John", "scores": {"math": 90, "english": 88}},
                  {"name": "Alice", "scores": {"math": 95, "english": 92}}]}

max_math_score = max([person["scores"]["math"] for person in data["people"]])

# 중첩된 필드의 특정 조건 충족 여부 확인: 중첩된 필드에서 특정 조건을 충족하는지 확인합니다.  
data = {"people": [{"name": "John", "grades": [90, 85, 88]},
                  {"name": "Alice", "grades": [95, 92, 89]}]}

has_high_scores = any(max(person["grades"]) >= 90 for person in data["people"])

# 중첩된 필드 값 결합: 중첩된 필드 값을 결합하여 새로운 필드 생성합니다.  
data = {"person": {"name": "John", "address": {"city": "New York", "state": "NY"}}}
full_address = f"{data['person']['address']['city']}, {data['person']['address']['state']}"

# 중첩된 필드에서 필드명 추출: 중첩된 필드에서 필드명을 추출합니다.  
data = {"person": {"name": "John", "address": {"city": "New York", "state": "NY"}}}
field_names = list(data["person"]["address"].keys())

# 중첩된 필드에서 특정 필드 유무 확인: 중첩된 필드에서 특정 필드가 존재하는지 확인합니다.  
data = {"person": {"name": "John", "address": {"city": "New York", "state": "NY"}}}
has_state = "state" in data["person"]["address"]

# 중첩된 필드에서 필드명으로 필터링: 중첩된 필드 중 필드명으로 필터링합니다.  
data = {"person": {"name": "John", "address": {"city": "New York", "state": "NY"}}}
filtered_data = {key: value for key, value in data["person"]["address"].items() if key != "state"}

# 중첩된 필드에서 필드 값으로 필터링: 중첩된 필드 중 특정 필드 값으로 필터링합니다.  
data = {"person": {"name": "John", "address": {"city": "New York", "state": "NY"}}}
filtered_data = {key: value for key, value in data["person"]["address"].items() if value != "NY"}

# JSON 배열에서 중첩된 필드 값 추출: JSON 배열에서 중첩된 필드 값을 추출합니다.  
data = [{"person": {"name": "John"}}, {"person": {"name": "Alice"}}]
names = [item["person"]["name"] for item in data]

# 중첩된 필드의 조합 값 추출: 중첩된 필드 값의 조합을 추출합니다.  
data = [{"person": {"first_name": "John", "last_name": "Doe"}},
        {"person": {"first_name": "Alice", "last_name": "Smith"}}]

full_names = [f"{item['person']['first_name']} {item['person']['last_name']}" for item in data]

# 중첩된 필드에서 특정 값의 인덱스 찾기: 중첩된 필드에서 특정 값의 인덱스를 찾습니다.  
data = {"people": [{"name": "John", "score": 90}, {"name": "Alice", "score": 85}, {"name": "Bob", "score": 88}]}
index_of_alice = next((index for index, person in enumerate(data["people"]) if person["name"] == "Alice"), None)

# 중첩된 필드를 기반으로 필터링: 중첩된 필드 값을 기반으로 데이터를 필터링합니다.  
data = [{"person": {"name": "John", "age": 30}},
        {"person": {"name": "Alice", "age": 25}}]

filtered_data = [item for item in data if item["person"]["age"] > 25]

# 중첩된 배열의 중첩 필드 필터링: 중첩된 배열의 중첩된 필드 값을 필터링합니다.  
data = [{"groups": [{"name": "Group A", "members": ["Alice", "Bob"]},
                   {"name": "Group B", "members": ["Charlie", "David"]}]},
        {"groups": [{"name": "Group C", "members": ["Eve", "Frank"]}]}]

filtered_data = [group for item in data for group in item["groups"] if "Alice" in group["members"]]

# 중첩된 필드 값에 함수 적용: 중첩된 필드 값을 함수를 사용하여 가공합니다.  
data = {"people": [{"name": "John", "age": 30},
                  {"name": "Alice", "age": 25}]}

def add_greetings(person):
    person["greeting"] = f"Hello, {person['name']}!"
    return person

modified_data = [add_greetings(person) for person in data["people"]]





##############  고급반  #####################################
##############  고급반  #####################################
##############  고급반  #####################################
##############  고급반  #####################################
##############  고급반  #####################################







# 중첩된 배열 병합: 중첩된 배열을 하나의 배열로 병합합니다.
 
data = [{"numbers": [1, 2, 3]}, {"numbers": [4, 5, 6]}]
merged_numbers = [num for entry in data for num in entry["numbers"]]

# 중첩된 배열 필터링 및 병합: 중첩된 배열에서 특정 조건을 충족하는 요소를 필터링하고 병합합니다.
 
data = [{"numbers": [1, 2, 3]}, {"numbers": [4, 5, 6]}]
filtered_and_merged_numbers = [num for entry in data if sum(entry["numbers"]) > 10 for num in entry["numbers"]]

# 중첩된 필드에서 중복 값 제거: 중첩된 필드에서 중복 값을 제거합니다.
 
data = [{"tags": ["apple", "banana", "apple"]}, {"tags": ["cherry", "banana", "date"]}]
unique_tags = list(set(tag for entry in data for tag in entry["tags"]))

# 중첩된 필드에서 최댓값 찾기: 중첩된 필드에서 최댓값을 찾습니다.
 
data = {"people": [{"name": "John", "grades": [90, 85, 88]},
                  {"name": "Alice", "grades": [95, 92, 89]}]}
max_grade = max(max(person["grades"]) for person in data["people"])

# 중첩된 필드에서 최솟값 찾기: 중첩된 필드에서 최솟값을 찾습니다.
 
data = {"people": [{"name": "John", "grades": [90, 85, 88]},
                  {"name": "Alice", "grades": [95, 92, 89]}]}
min_grade = min(min(person["grades"]) for person in data["people"])

# 중첩된 필드에서 특정 조건 충족하는 값 추출: 중첩된 필드에서 특정 조건을 충족하는 값을 추출합니다.
 
data = {"people": [{"name": "John", "grades": [90, 85, 88]},
                  {"name": "Alice", "grades": [95, 92, 89]}]}
high_scorers = [person for person in data["people"] if all(grade >= 90 for grade in person["grades"])]

# 중첩된 필드에서 여러 조건을 동시에 충족하는 값 추출: 중첩된 필드에서 여러 조건을 동시에 충족하는 값을 추출합니다.
 
data = {"people": [{"name": "John", "grades": [90, 85, 88]},
                  {"name": "Alice", "grades": [95, 92, 89]}]}
top_students = [person for person in data["people"] if all(grade >= 90 for grade in person["grades"]) and len(person["grades"]) == 3]

# JSON 데이터의 복사와 수정: JSON 데이터를 복사하고 일부를 수정합니다.
 
data = {"name": "John", "address": {"city": "New York", "state": "NY"}}
modified_data = json.loads(json.dumps(data))  # 복사
modified_data["address"]["state"] = "CA"  # 수정

# 중첩된 필드에서 필드명 추출 및 수정: 중첩된 필드에서 필드명을 추출하고 수정합니다.
 
data = {"person": {"name": "John", "address": {"city": "New York", "state": "NY"}}}
field_names = list(data["person"]["address"].keys())
modified_field_names = [field + "_modified" for field in field_names]

# JSON 데이터 병합: 두 개의 JSON 데이터를 병합합니다.
 
data1 = {"name": "John", "age": 30}
data2 = {"city": "New York", "country": "USA"}
merged_data = {**data1, **data2}

# 중첩된 필드의 조합 값 계산: 중첩된 필드 값의 조합을 계산합니다.
 
data = {"people": [{"name": {"first": "John", "last": "Doe"}},
                  {"name": {"first": "Alice", "last": "Smith"}}]}

full_names = [f"{person['name']['first']} {person['name']['last']}" for person in data["people"]]

# 중첩된 필드에서 필드 값에 함수 적용: 중첩된 필드 값을 함수를 사용하여 가공합니다.
 
data = {"people": [{"name": "John", "grades": [90, 85, 88]},
                  {"name": "Alice", "grades": [95, 92, 89]}]}

def calculate_average(grades):
    return sum(grades) / len(grades)

modified_data = [{"name": person["name"], "average_grade": calculate_average(person["grades"])} for person in data["people"]]

# 중첩된 필드에서 필드 값 기반 필터링: 중첩된 필드 값을 기반으로 데이터를 필터링합니다.
 
data = {"people": [{"name": "John", "grades": [90, 85, 88]},
                  {"name": "Alice", "grades": [95, 92, 89]}]}

filtered_data = [person for person in data["people"] if calculate_average(person["grades"]) > 90]

# 중첩된 필드에서 필드 값의 합계 계산: 중첩된 필드 값의 합계를 계산합니다.
 
data = {"people": [{"name": "John", "grades": [90, 85, 88]},
                  {"name": "Alice", "grades": [95, 92, 89]}]}

total_grade_sum = sum(sum(person["grades"]) for person in data["people"])

# 중첩된 필드에서 필드 값의 평균 계산: 중첩된 필드 값의 평균을 계산합니다.
 
data = {"people": [{"name": "John", "grades": [90, 85, 88]},
                  {"name": "Alice", "grades": [95, 92, 89]}]}

average_grade = sum(sum(person["grades"]) / len(person["grades"]) for person in data["people"])

# 중첩된 필드 값에서 중복 항목 제거: 중첩된 필드 값에서 중복 항목을 제거합니다.
 
data = {"people": [{"name": "John", "tags": ["A", "B", "A"]},
                  {"name": "Alice", "tags": ["B", "C", "B"]}]}

unique_tags = list(set(tag for person in data["people"] for tag in person["tags"]))

# 중첩된 배열에서 특정 조건에 따라 객체 추출: 중첩된 배열에서 특정 조건을 충족하는 객체를 추출합니다.
 
data = {"groups": [{"name": "Group A", "members": ["Alice", "Bob"]},
                  {"name": "Group B", "members": ["Charlie", "David"]}]}

data = [group for group in data["groups"] if any(member.startswith("C") for member in group["members"])]
print(data)

# JSON 데이터의 필드 순서 변경: JSON 데이터의 필드 순서를 변경합니다.
 
data = {"name": "John", "age": 30, "city": "New York"}
data = {"age": data["age"], "name": data["name"], "city": data["city"]}

# 중첩된 필드에서 특정 조건을 충족하는 값을 가진 객체 추출: 중첩된 필드에서 특정 조건을 충족하는 값을 가진 객체를 추출합니다.
 
data = {"people": [{"name": "John", "grades": [90, 85, 88]},
                  {"name": "Alice", "grades": [95, 92, 89]}]}

target_grade = 92
extracted_people = [person for person in data["people"] if target_grade in person["grades"]]
# print(extracted_people)




# JSON 데이터의 필드 값을 기반으로 필터링 및 정렬: JSON 데이터에서 필드 값을 기반으로 필터링하고 정렬합니다.
 
data = [{"name": "John", "age": 30},
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 35}]

filtered_and_sorted_data = sorted([item for item in data if item["age"] > 25], key=lambda x: x["name"])
# print(filtered_and_sorted_data)




##### 정규표현식으로 일부의 글씨를 찾는 방법

import json
import re

# JSON 데이터를 로드
data = json.loads('{"items": [{"name": "apple"}, {"name": "banana"}, {"name": "cherry"}]}')

# 정규 표현식 패턴
pattern = re.compile(r'ban')

# 정규 표현식을 사용하여 JSON 데이터에서 패턴에 맞는 문자열을 찾음

# 1. 객체 이름에서 패턴에 맞는 값을 찾음
filtered_items = [item for item in data["items"] if pattern.search(item["name"])]

# 2. 중첩된 필드에서 패턴에 맞는 값을 찾음
filtered_people = [person for person in data["people"] if any(pattern.search(value) for value in person.values())]

# 3. 필드 값에서 패턴에 맞는 값을 찾음
filtered_items = [item for item in data["items"] if any(pattern.search(item["name"]))]

# 4. 중첩된 필드에서 패턴에 맞는 필드를 찾음
filtered_fields = {key: value for person in data["people"] for key, value in person["address"].items() if pattern.search(value)}

# 5. JSON 데이터를 문자열로 변환한 후 패턴에 맞는 값을 찾음
json_str = json.dumps(data)
found_values = pattern.findall(json_str)

# 6. JSON 데이터를 문자열로 변환한 후 패턴에 맞는 값을 대체함
replacement = "REPLACED"
modified_json_str = pattern.sub(replacement, json_str)

# 7. JSON 데이터를 문자열로 변환한 후 패턴에 맞는 값을 삭제함
modified_json_str = pattern.sub('', json_str)

# 8. 패턴에 맞는 문자열을 찾아 해당 부분을 추출함
found_text = [match.group() for match in pattern.finditer(json_str)]

# 9. 패턴에 맞는 문자열을 찾아 해당 부분을 추출하고 그룹을 사용함
pattern_with_group = re.compile(r'name": "(.*?)"')
found_names = [match.group(1) for match in pattern_with_group.finditer(json_str)]

# 10. 패턴에 맞는 문자열을 찾아 해당 부분을 추출하고 그룹명을 사용함
pattern_with_named_group = re.compile(r'name": "(?P<fruit_name>.*?)"')
found_fruit_names = [match.group("fruit_name") for match in pattern_with_named_group.finditer(json_str)]



