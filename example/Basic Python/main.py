# -*- coding: utf-8 -*-
"""
파이썬 기초 문법 예제 모음
Python Basic Syntax Examples

이 파일은 파이썬을 처음 배우는 사람들을 위한 기본적인 문법과 개념들을 다룹니다.
"""

print("=" * 50)
print("파이썬 기초 문법 예제에 오신 것을 환영합니다!")
print("=" * 50)

# ========================================
# 1. 변수와 데이터 타입
# ========================================
print("\n1. 변수와 데이터 타입")
print("-" * 30)

# 문자열 (String)
name = "홍길동"
greeting = '안녕하세요'
print(f"이름: {name}")
print(f"인사: {greeting}")

# 숫자 (Numbers)
age = 25          # 정수 (int)
height = 175.5    # 실수 (float)
print(f"나이: {age}세")
print(f"키: {height}cm")

# 불린 (Boolean)
is_student = True
is_working = False
print(f"학생 여부: {is_student}")
print(f"직장인 여부: {is_working}")

# 타입 확인
print(f"\nname의 타입: {type(name)}")
print(f"age의 타입: {type(age)}")
print(f"height의 타입: {type(height)}")
print(f"is_student의 타입: {type(is_student)}")

# ========================================
# 2. 기본 연산자
# ========================================
print("\n\n2. 기본 연산자")
print("-" * 30)

# 산술 연산자
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"덧셈: {a} + {b} = {a + b}")
print(f"뺄셈: {a} - {b} = {a - b}")
print(f"곱셈: {a} * {b} = {a * b}")
print(f"나눗셈: {a} / {b} = {a / b}")
print(f"몫: {a} // {b} = {a // b}")
print(f"나머지: {a} % {b} = {a % b}")
print(f"거듭제곱: {a} ** {b} = {a ** b}")

# 비교 연산자
print(f"\n비교 연산자:")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")

# 논리 연산자
x = True
y = False
print(f"\n논리 연산자:")
print(f"x = {x}, y = {y}")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# ========================================
# 3. 문자열 처리
# ========================================
print("\n\n3. 문자열 처리")
print("-" * 30)

text = "Python Programming"
print(f"원본 문자열: '{text}'")
print(f"길이: {len(text)}")
print(f"대문자로: '{text.upper()}'")
print(f"소문자로: '{text.lower()}'")
print(f"첫 글자만 대문자: '{text.capitalize()}'")
print(f"'Python' 포함 여부: {text.find('Python')}")
print(f"공백으로 분리: {text.split(' ')}")

# 문자열 포맷팅
name = "김철수"
score = 95.5
print(f"\n문자열 포맷팅:")
print(f"f-string: {name}님의 점수는 {score}점입니다.")
print("format(): {}님의 점수는 {}점입니다.".format(name, score))
print("%s님의 점수는 %.1f점입니다." % (name, score))

# ========================================
# 4. 조건문 (if-else)
# ========================================
print("\n\n4. 조건문 (if-else)")
print("-" * 30)

# 기본 if문
age = 20
if age >= 18:
    print(f"나이 {age}세: 성인입니다.")
else:
    print(f"나이 {age}세: 미성년자입니다.")

# if-elif-else문
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"점수 {score}점: {grade}학점")

# 중첩 조건문
weather = "맑음"
temperature = 25

if weather == "맑음":
    if temperature >= 25:
        print("날씨가 좋으니 외출하기 좋은 날입니다!")
    else:
        print("맑지만 조금 쌀쌀합니다.")
else:
    print("실내 활동을 추천합니다.")

# ========================================
# 5. 반복문 (for, while)
# ========================================
print("\n\n5. 반복문")
print("-" * 30)

# for문 - 숫자 범위
print("1부터 5까지 출력:")
for i in range(1, 6):
    print(f"숫자: {i}")

# for문 - 리스트 순회
fruits = ["사과", "바나나", "오렌지", "포도"]
print(f"\n과일 목록:")
for fruit in fruits:
    print(f"- {fruit}")

# for문 - enumerate 사용
print(f"\n과일 목록 (번호 포함):")
for index, fruit in enumerate(fruits, 1):
    print(f"{index}. {fruit}")

# while문
print(f"\nwhile문으로 카운트다운:")
count = 5
while count > 0:
    print(f"남은 시간: {count}초")
    count -= 1
print("시간 종료!")

# break와 continue
print(f"\n1부터 10까지 중 짝수만 출력 (continue 사용):")
for i in range(1, 11):
    if i % 2 == 1:  # 홀수면 건너뛰기
        continue
    print(f"짝수: {i}")

print(f"\n1부터 시작해서 첫 번째 5의 배수까지 출력 (break 사용):")
num = 1
while True:
    if num % 5 == 0:
        print(f"5의 배수 발견: {num}")
        break
    print(f"숫자: {num}")
    num += 1

# ========================================
# 6. 함수 (Functions)
# ========================================
print("\n\n6. 함수")
print("-" * 30)

# 기본 함수 정의와 호출
def greet(name):
    """이름을 받아서 인사말을 출력하는 함수"""
    return f"안녕하세요, {name}님!"

print(greet("파이썬"))

# 매개변수가 있는 함수
def add_numbers(a, b):
    """두 숫자를 더하는 함수"""
    result = a + b
    return result

result = add_numbers(10, 20)
print(f"10 + 20 = {result}")

# 기본값이 있는 매개변수
def introduce(name, age=20, city="서울"):
    """자기소개를 하는 함수 (기본값 설정)"""
    return f"안녕하세요! 저는 {name}이고, {age}세이며, {city}에 살고 있습니다."

print(introduce("김민수"))
print(introduce("이영희", 25))
print(introduce("박철수", 30, "부산"))

# 가변 인수 함수
def calculate_average(*numbers):
    """여러 숫자의 평균을 계산하는 함수"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(f"평균 계산: {calculate_average(10, 20, 30, 40, 50)}")

# 람다 함수 (익명 함수)
square = lambda x: x ** 2
print(f"람다 함수로 5의 제곱: {square(5)}")

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"리스트의 모든 수를 제곱: {squared_numbers}")

# ========================================
# 7. 클래스와 객체 (Object-Oriented Programming)
# ========================================
print("\n\n7. 클래스와 객체")
print("-" * 30)

# 기본 클래스 정의
class Person:
    """사람을 나타내는 클래스"""
    
    def __init__(self, name, age):
        """생성자 함수"""
        self.name = name
        self.age = age
    
    def introduce(self):
        """자기소개 메서드"""
        return f"안녕하세요! 저는 {self.name}이고, {self.age}세입니다."
    
    def have_birthday(self):
        """생일을 맞이하는 메서드"""
        self.age += 1
        return f"{self.name}님, 생일 축하합니다! 이제 {self.age}세입니다."

# 객체 생성과 사용
person1 = Person("홍길동", 25)
person2 = Person("김영희", 30)

print(person1.introduce())
print(person2.introduce())
print(person1.have_birthday())

# 상속 예제
class Student(Person):
    """학생 클래스 (Person 클래스를 상속)"""
    
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 부모 클래스의 생성자 호출
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        """성적 추가 메서드"""
        self.grades.append(grade)
    
    def get_average(self):
        """평균 성적 계산 메서드"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def introduce(self):
        """오버라이딩된 자기소개 메서드"""
        return f"안녕하세요! 저는 학번 {self.student_id}번 {self.name}이고, {self.age}세입니다."

# 학생 객체 생성과 사용
student = Student("박학생", 20, "2024001")
print(student.introduce())
student.add_grade(90)
student.add_grade(85)
student.add_grade(95)
print(f"{student.name}님의 평균 성적: {student.get_average():.1f}점")

# ========================================
# 8. 데이터 구조 (Data Structures)
# ========================================
print("\n\n8. 데이터 구조")
print("-" * 30)

# 리스트 (List) - 순서가 있고 변경 가능
print("리스트 (List):")
fruits = ["사과", "바나나", "오렌지"]
print(f"초기 리스트: {fruits}")

fruits.append("포도")  # 끝에 추가
print(f"포도 추가 후: {fruits}")

fruits.insert(1, "딸기")  # 특정 위치에 추가
print(f"1번 위치에 딸기 추가: {fruits}")

fruits.remove("바나나")  # 특정 값 제거
print(f"바나나 제거 후: {fruits}")

print(f"첫 번째 과일: {fruits[0]}")
print(f"마지막 과일: {fruits[-1]}")
print(f"리스트 길이: {len(fruits)}")

# 리스트 슬라이싱
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\n숫자 리스트: {numbers}")
print(f"처음 5개: {numbers[:5]}")
print(f"마지막 3개: {numbers[-3:]}")
print(f"3번째부터 7번째까지: {numbers[2:7]}")
print(f"짝수 인덱스만: {numbers[::2]}")

# 튜플 (Tuple) - 순서가 있고 변경 불가능
print(f"\n튜플 (Tuple):")
coordinates = (10, 20)
print(f"좌표: {coordinates}")
print(f"x좌표: {coordinates[0]}, y좌표: {coordinates[1]}")

# 튜플 언패킹
x, y = coordinates
print(f"언패킹된 좌표: x={x}, y={y}")

# 딕셔너리 (Dictionary) - 키-값 쌍
print(f"\n딕셔너리 (Dictionary):")
student_info = {
    "이름": "김학생",
    "나이": 20,
    "전공": "컴퓨터공학",
    "성적": [90, 85, 95]
}

print(f"학생 정보: {student_info}")
print(f"이름: {student_info['이름']}")
print(f"전공: {student_info['전공']}")

# 딕셔너리 메서드
print(f"모든 키: {list(student_info.keys())}")
print(f"모든 값: {list(student_info.values())}")
print(f"키-값 쌍: {list(student_info.items())}")

# 딕셔너리에 새 항목 추가
student_info["학년"] = 2
print(f"학년 추가 후: {student_info}")

# 집합 (Set) - 중복되지 않는 요소들의 모음
print(f"\n집합 (Set):")
numbers_set = {1, 2, 3, 4, 5, 3, 2, 1}  # 중복 제거됨
print(f"집합: {numbers_set}")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"집합1: {set1}")
print(f"집합2: {set2}")
print(f"합집합: {set1 | set2}")
print(f"교집합: {set1 & set2}")
print(f"차집합: {set1 - set2}")

# 리스트 컴프리헨션
print(f"\n리스트 컴프리헨션:")
squares = [x**2 for x in range(1, 6)]
print(f"1부터 5까지의 제곱: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"1부터 10까지 짝수의 제곱: {even_squares}")

# 딕셔너리 컴프리헨션
square_dict = {x: x**2 for x in range(1, 6)}
print(f"제곱 딕셔너리: {square_dict}")

# ========================================
# 9. 파일 처리
# ========================================
print("\n\n9. 파일 처리")
print("-" * 30)

# 파일 쓰기
filename = "sample.txt"
try:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("안녕하세요, 파이썬!\n")
        file.write("파일 처리 예제입니다.\n")
        file.write("여러 줄을 작성할 수 있습니다.\n")
    print(f"'{filename}' 파일을 성공적으로 생성했습니다.")
except Exception as e:
    print(f"파일 쓰기 중 오류 발생: {e}")

# 파일 읽기
try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"\n파일 내용:\n{content}")
except FileNotFoundError:
    print(f"'{filename}' 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"파일 읽기 중 오류 발생: {e}")

# 파일을 한 줄씩 읽기
try:
    with open(filename, 'r', encoding='utf-8') as file:
        print("파일을 한 줄씩 읽기:")
        line_number = 1
        for line in file:
            print(f"{line_number}: {line.strip()}")
            line_number += 1
except Exception as e:
    print(f"파일 읽기 중 오류 발생: {e}")

# ========================================
# 10. 예외 처리 (Exception Handling)
# ========================================
print("\n\n10. 예외 처리")
print("-" * 30)

# 기본 try-except
def safe_divide(a, b):
    """안전한 나눗셈 함수"""
    try:
        result = a / b
        return f"{a} ÷ {b} = {result}"
    except ZeroDivisionError:
        return "오류: 0으로 나눌 수 없습니다!"
    except TypeError:
        return "오류: 숫자가 아닌 값이 입력되었습니다!"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))

# 여러 예외 처리
def process_list_item(lst, index):
    """리스트 항목 처리 함수"""
    try:
        value = lst[index]
        result = 100 / value
        return f"인덱스 {index}의 값 {value}로 100을 나눈 결과: {result}"
    except IndexError:
        return f"오류: 인덱스 {index}가 리스트 범위를 벗어났습니다!"
    except ZeroDivisionError:
        return f"오류: 인덱스 {index}의 값이 0이므로 나눌 수 없습니다!"
    except TypeError:
        return f"오류: 인덱스 {index}의 값이 숫자가 아닙니다!"
    except Exception as e:
        return f"예상치 못한 오류 발생: {e}"

test_list = [10, 0, "문자", 5]
for i in range(6):  # 의도적으로 범위를 벗어나게 함
    print(process_list_item(test_list, i))

# try-except-else-finally
def file_operation_demo():
    """파일 처리와 예외 처리 종합 예제"""
    filename = "test_file.txt"
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("테스트 파일입니다.")
        print(f"'{filename}' 파일 생성 완료")
    except Exception as e:
        print(f"파일 생성 중 오류: {e}")
    else:
        print("파일 생성 작업이 성공적으로 완료되었습니다.")
    finally:
        print("파일 작업이 종료되었습니다.")

file_operation_demo()

# 사용자 정의 예외
class CustomError(Exception):
    """사용자 정의 예외 클래스"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    """나이 확인 함수"""
    try:
        if age < 0:
            raise CustomError("나이는 음수일 수 없습니다!")
        elif age > 150:
            raise CustomError("나이가 너무 큽니다!")
        else:
            return f"유효한 나이입니다: {age}세"
    except CustomError as e:
        return f"사용자 정의 오류: {e.message}"

print(f"\n나이 검증 예제:")
print(check_age(25))
print(check_age(-5))
print(check_age(200))

# ========================================
# 마무리
# ========================================
print("\n" + "=" * 50)
print("파이썬 기초 문법 예제를 모두 완료했습니다!")
print("이 예제들을 통해 파이썬의 기본적인 개념들을 익히셨기를 바랍니다.")
print("더 많은 연습을 통해 파이썬 실력을 향상시켜 보세요!")
print("=" * 50)