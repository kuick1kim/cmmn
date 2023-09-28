

import re

# 메일 주소 추출: 
# text = "Contact us at email@example.com or support@example.org"
# emails = re.findall(r'\S+@\S+', text)
# print(emails)

# # 전화번호 추출: 
# text = "Call me at 123-456-7890 or 987-654-3210"
# phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)
# print(phone_numbers)

# URL 추출: 
# text = "Visit our website at http://www.example.com"
# urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
# print(urls)

# # 숫자 추출: 
# text = "There are 42 apples and 7 oranges in the basket"
# numbers = re.findall(r'\d+', text)
# print(numbers)

# # 단어 추출: 
# text = "This is a simple example sentence."
# words = re.findall(r'\w+', text)
# print(words)

# # 공백 제거: 
# text = "   This has leading and trailing spaces.   "
# clean_text = re.sub(r'\s+', ' ', text).strip()
# print(clean_text)

# # HTML 태그 제거: 
# text = "<p>This is <b>bold</b> text.</p>"
# clean_text = re.sub(r'<[^>]+>', '', text)
# print(clean_text)

# # 특정 문자 치환: 
# text = "Hello, world!"
# modified_text = re.sub(r'world', 'Python', text)
# print(modified_text)

# # 대소문자 무시: 
# text = "Hello, World!"
# matches = re.findall(r'hello', text, re.IGNORECASE)
# print(matches)

# # 시작 문자열 확인: 
# text = "Python is easy to learn."
# if re.match(r'^Python', text):
#     print("Starts with 'Python'")

# # 숫자 개수 세기: 
# text = "There are 42 apples and 7 oranges in the basket"
# count = len(re.findall(r'\d+', text))
# print(count)

# 특정 단어 존재 확인: 
# text = "The quick brown fox jumps over the lazy dog."
# if re.search(r'fox', text):
#     print("The word 'fox' is found.")

# # 이름과 성 추출: 
# text = "John Smith, Jane Doe, Alice Johnson"
# names = re.findall(r'[A-Z][a-z]+ [A-Z][a-z]+', text)
# print(names)

# # 메타문자 이스케이프: 
# text = "Use \\. to match a period."
# matches = re.findall(r'\\.', text)
# print(matches)

# # 문자열 분할: 
# text = "apple,banana, cherry, date"
# fruits = re.split(r',\s*', text)
# print(fruits)

# # 숫자와 문자 조합 추출: 
# text = "ID: 1234, Name: Alice"
# result = re.findall(r'(\d+), Name: (\w+)', text)
# print(result)

# 주소 추출 (그룹): 
# text = "123 Main St, City: Anytown, State: CA"
# match = re.search(r'(\d+) (.*), City: (.*), State: (.*)', text)
# if match:
#     print("Street:", match.group(1))
#     print("City:", match.group(3))
#     print("State:", match.group(4))

# # 패턴 매칭 위치 확인: 
# text = "The quick brown fox"
# match = re.search(r'brown', text)
# if match:
#     print("Found at index:", match.start())

# # 패턴 매칭 위치와 부분 문자열 확인: 
# text = "The quick brown fox"
# match = re.search(r'quick (.*?) fox', text)
# if match:
#     print("Matched text:", match.group(0))
#     print("Start index:", match.start())

# # 패턴 매칭 여부 확인 및 매칭된 문자열 출력: 
# text = "The quick brown fox"
# match = re.search(r'lazy', text)
# if match:
#     print("Found:", match.group())
# else:
#     print("Not found.")









# # 단어 경계 매칭: 
# text = "Hello, World!"
# matches = re.findall(r'\bWorld\b', text)
# print(matches)


# # 대문자로 시작하는 단어 추출: 
# text = "This is a Sentence with Title Case words."
# matches = re.findall(r'\b[A-Z][a-z]+\b', text)
# print(matches)

# # 띄어쓰기가 아닌 문자열 추출: 
# text = "Let's meet at 3PM."
# matches = re.findall(r'\S+', text)
# print(matches)

# # 전화번호 형식 매칭: 
# text = "Call me at (123) 456-7890"
# phone_numbers = re.findall(r'\(\d{3}\) \d{3}-\d{4}', text)
# print(phone_numbers)

# 이름과 성을 그룹화하여 추출: 
# text = "John Smith, Jane Doe, Alice Johnson"
# names = re.findall(r'(\w+) (\w+)', text)
# print(names)

# # 특정 문자가 아닌 문자열 추출: 
# text = "Remove special characters: $@#^&!"
# result = re.findall(r'[^$@#^&!]+', text)
# print(result)

# # 이름의 첫 글자만 추출: 
# text = "John Smith, Jane Doe, Alice Johnson"
# initials = re.findall(r'\b(\w)\w+ \w+', text)
# print(initials)

# # 연속된 문자열 추출: 
# text = "Mississippi"
# matches = re.findall(r'(.)\1+', text)
# print(matches)

# # 특정 문자 반복 매칭: 
# text = "aaaaaabbbbbbccccccd"
# matches = re.findall(r'(a+|b+|c+)', text)
# print(matches)

# # 전화번호 마스킹: 
# text = "Call me at 123-456-7890"
# masked_text = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
# print(masked_text)

# # 단어 끝에 'ing'가 있는 단어 추출: 
# text = "Walking, Running, Eating"
# ing_words = re.findall(r'\b\w+ing\b', text)
# print(ing_words)

# # 소수 추출: 
# text = "These are some numbers: 3.14, 42.0, 0.123"
# floats = re.findall(r'\b\d+\.\d+\b', text)
# print(floats)

# # 중복 없이 단어 추출: 
# text = "apple apple banana cherry cherry apple"
# unique_words = list(set(re.findall(r'\b\w+\b', text)))
# print(unique_words)

# # 특수 문자 추출: 
# text = "Special characters: @#$%^&*()"
# special_chars = re.findall(r'[!@#$%^&*()]+', text)
# print(special_chars)

# # 전화번호 형식 유효성 검사: 
# def is_valid_phone_number(text):
#     pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
#     return bool(re.match(pattern, text))
# print(is_valid_phone_number("(123) 456-7890"))

# 주석 제거: 
text = """
# This is a comment
Hello, World!
"""
cleaned_text = re.sub(r'#.*', '', text)
print(cleaned_text.strip())

# 이메일 주소 유효성 검사: 
def is_valid_email(text):
    pattern = r'\S+@\S+'
    return bool(re.match(pattern, text))
print(is_valid_email("email@example.com"))

text = "123 Main St, City: Anytown, State: CA"
match = re.search(r'(\d+) (.*), City: (.*), State: (.*)', text)
if match:
    print("Street:", match.group(1))
    print("City:", match.group(3))
    print("State:", match.group(4))


# 시간 형식 유효성 검사: 
def is_valid_time(text):
    pattern = r'\d{2}:\d{2}:\d{2}'
    return bool(re.match(pattern, text))
print(is_valid_time("12:34:56"))


# XML 태그 내용 추출: 
xml = "<tag>This is the content</tag>"
content = re.search(r'<tag>(.*?)</tag>', xml).group(1)
print(content)






# 이스케이프된 문자열 추출: 
text = "Escaped: \* \+ \? \. \{ \} \[ \] \( \) \^ \$"
escaped_chars = re.findall(r'\\[.*+?{}[\]()^$]', text)
print(escaped_chars)


# 소문자로 된 단어 추출: 
text = "The quick brown Fox jumps over the lazy Dog."
lowercase_words = re.findall(r'\b[a-z]+\b', text)
print(lowercase_words)


# 숫자로 시작하는 단어 추출: 
text = "42 apples, 7 oranges, and 99 bananas"
starts_with_number = re.findall(r'\b\d+\w*\b', text)
print(starts_with_number)


# 특정 문자열로 끝나는 단어 추출: 
text = "Words ending with ing: walking, running, singing"
ing_words = re.findall(r'\b\w+ing\b', text)
print(ing_words)


# 특정 문자열로 시작하는 단어 추출: 
text = "Words starting with apple: applepie, applejack, apple"
apple_words = re.findall(r'\bapple\w*\b', text)
print(apple_words)


# 문자열 중간에 있는 단어 추출: 
text = "Extract words: hello, world, this, is, Python"
middle_words = re.findall(r', (\w+),', text)
print(middle_words)


# 모든 숫자 제거: 
text = "Remove 42 numbers and 7 digits from this text."
no_numbers = re.sub(r'\d', '', text)
print(no_numbers)


# 주석 내용 추출: 
text = """# This is a comment
# Another comment
Text inside comment
# End of comment"""
comments = re.findall(r'# (.+)', text)
print(comments)


# 웹 URL 추출: 
text = "Visit my website at https://www.example.com"
urls = re.findall(r'https?://\S+', text)
print(urls)


# 우편번호 형식 매칭: 
text = "ZIP codes: 90210, 12345-6789, 98765"
zip_codes = re.findall(r'\b\d{5}(?:-\d{4})?\b', text)
print(zip_codes)


# 빈 줄 제거: 
text = """Line 1

Line 3


Line 6"""
non_empty_lines = re.sub(r'\n\s*\n', '\n', text)
print(non_empty_lines)


# 특정 단어 뒤에 나오는 문자열 추출: 
text = "Find words after 'apple': apple pie, apple juice, apple"
after_apple = re.findall(r'apple (\w+)', text)
print(after_apple)


# 주어진 길이의 숫자 추출: 
text = "123 4567 89012 3456789 12345"
four_digits = re.findall(r'\b\d{4}\b', text)
print(four_digits)


# 전화번호 포맷 변경: 
text = "Call me at 123.456.7890 or 987-654-3210"
formatted_numbers = re.sub(r'(\d{3})[.-](\d{3})[.-](\d{4})', r'\1-\2-\3', text)
print(formatted_numbers)


# 탭 문자로 분리된 필드 추출: 
text = "Name\tAge\tCity\nJohn\t30\tNew York\nAlice\t25\tLos Angeles"
fields = re.findall(r'([^\t]+)\t', text)
print(fields)


# 첫 글자가 대문자인 단어 추출: 
text = "The Quick Brown Fox Jumps Over The Lazy Dog."
title_case_words = re.findall(r'\b[A-Z][a-z]+\b', text)
print(title_case_words)


# 특정 문자열 앞에 있는 단어 추출: 
text = "Extract words before 'example': This is an example sentence."
before_example = re.findall(r'(\w+)\s+example', text)
print(before_example)


# 메일 주소 형식 매칭: 
text = "Contact us at contact@example.com or support@example.org"
emails = re.findall(r'\b\S+@\S+\.\w+\b', text)
print(emails)


# 태그 이름 추출: 
xml = "<tag1>Content</tag1><tag2>More Content</tag2>"
tag_names = re.findall(r'<(\w+)>', xml)
print(tag_names)


# 시간 형식 매칭 (12시간과 24시간 표기): 
text = "Times: 12:34 PM, 23:45, 09:15 AM"
times = re.findall(r'\b\d{1,2}:\d{2}(?: [APap][Mm])?\b', text)
print(times)