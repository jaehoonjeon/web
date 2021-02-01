# 이것은 주석
print("hello world")

# type 함수
print(type("123"), type(1), type(1.0), type(True))

print('################## 문자열 관련 ##################')

# 개행, 탭
print("123\n456\t789")

# 여러줄 가능
print("""multy line1
line2""")

# 3연방
print("hello! " * 3)

# 문자열 선택
print("안녕하세요"[0])
# 역순으로 선택
print("안녕하세요"[-1])
print("안녕하세요"[-2])
# 문자열 범위 선택자 0,1,2 (0 <= x < 3)
print("안녕하세요"[0:3])
# 입력 안하면 최소값:최대값
print("안녕하세요"[2:]), print("안녕하세요"[:3])

# 문자열 길이
print(len("123"))

# format
print("{}년 {}월 {}일 {}요일".format(2021, 1, 9, "월"))

# upper() 대문자, lower() 소문자로 변환
print("upper".upper(), "LOWER".lower())

# strip() , lstrip(), rstrim()
print("     공백을 지워보자    ".strip())

# 왼쪽부터 찾기 find(), 오른쪽부터 찾기 rfind()
print("find b index  :: ", ("abcde".find("c")))
print("rfind b index :: ", ("abcde".rfind("c")))
# in 안에 있나 없나 True, False
print("c in abcde :: ", ("c" in "abcde"))

# split()
print("10 20 30 40 50".split(" "))

# join()
print(":".join(["10", "20", "30", "40"]))
print(":".join(map(str, [10, 20, 30, 40])))

# count()
print("count :: {}".format("10 20 30 40 50 10 10".count("10")))

print('################### 숫자 관련 ###################')

# 제곱
print(2 ** 10)
# 정수 나누기 연산자(몫 구하기)
print(15 // 7)

print('################### 변수 관련 ###################')

# 사용자에게 입력을 받는 함수 (문자열 리턴)
# a = input("input your data : ")
# print(a)
# print(type(a))

# 형변환
a = int("100")
b = float("200")
c = str(300)
# 123 + "" (int + str -> str?) -> !!ERROR!!

# a b 스위치
a, b = b, a

print('################### Boolean ###################')

# 비교 연산자
# ==   !=   >   <   >=   <=
# 단항 연산자
print(not True)
print(not False)
# 이항연산자
print(True and True)
print(True or False)

print('################## 조건문 ##################')

# 조건문 개행 \
if True or True or \
        True:
    print("line 1")
    print("line 2")

# if else
if True:
    print("if-else")
else:
    print(False)

# if elseif
if False:
    print(True)
elif True:
    print("elif!")
else:
    print(False)

# iif  ("True Value" if condition else "False Value")
print("aa" if True else "bb")  # aa
print("aa" if False else "bb")  # bb

# bool() - False 가 나오는 경우
bool(0), bool(0.0), bool(""), bool(()), bool({}), bool([])

# pass 미구현 상태를 표현하는 keyword (안쓰고 비우면 에러)
if 1 != 0:
    pass
else:
    pass

print('##################  list ##################')

# list
arry = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arry[0][0], arry[0][0:])

# list 합치기 => [1,2,3,4,5,6]
arry = [1, 2, 3] + [4, 5, 6]

# list in , not in
print(1 in [1, 2, 3])
print(4 not in [1, 2, 3])

# list 추가
# append(object)
a = [1, 2, 3]
a.append(5)
# insert(index, object)
a.insert(1, 6)
# extend(iterable)
a.extend([7, 8, 9])

# list 삭제
ab = [1, 2, 3, 4, 5, 6, 7]
del a[0]  # index로 삭제
del a[0:3]  # index 범위로 삭제
a.pop(0)  # index로 삭제
a.pop()  # 마지막 요소가 제거됨 a.pop(-1)
a.remove(6)  # 값으로 삭제(한개만 삭제)
a.clear()  # 전부 다 지우기

print('##################  for ##################')
# for
for obj in [1, 2, 3]:
    print(obj)

print('##################  dict ##################')
# dictionary
dics = {
    "a": "value a",
    "b": 123,
    273: [1, 2, 3, 4],
    True: False
}
# 딕셔너리의 key 값은 python 자료형으로만 들어감 (a:123 이런건 안됨)

dics["a"] = "value changed"  # 변경
dics["c"] = "value appended"  # 추가
del dics[True]  # 삭제

for dic in dics:
    print("{} : {}".format(dic, dics[dic]))

# dictionary 안에 key 값이 있는지 확인
if "a" in dics:
    pass
else:
    pass

if dics.get("a") == None:
    pass
else:
    pass

# 헤깔릴꺼 같은 예제 하나
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for key_ in character[key]:
            print("{} : {}".format(key_, character[key][key_]))
    elif type(character[key]) is list:
        for value in character[key]:
            print("{} : {}".format(key, value))
    else:
        print("{} : {}".format(key, character[key]))

print('##################  range ##################')
# range(start = 0, end, step = 1)
for i in range(0, 3, 1):
    print(i)  # 0, 1, 2
# 아래와 결과가 같다
for i in range(3):
    print(i)
for i in range(0, 3):
    print(i)

arry = [283, 123, 55, 213, 555]

for i in range(len(arry)):
    print("index:{} , value:{}".format(i, arry[i]))

# range 를 이용한 문자열 자르기
today_weather = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print("{} {} {]".format(year, day, weather))

print('##################  while ##################')
# while
numbers = [1, 2, 1, 2, 1, 2, 1, 1, 2]
while 1 in numbers:
    numbers.remove(1)
print(numbers)

print('##################  min, max, sum, reserved, enumerate, items ##################')

# break, continue 반복문에서 사용

# min(list) max(list) sum(list)
arry = [273, 52, 32, 56, 103]
print("min:{} max:{} sum:{}".format(min(arry), max(arry), sum(arry)))

# reversed 는  1회용 함수이기때문에 변수에 넣어서 사용하지 말기
print("reversed {}".format(list(reversed(arry))))

##############################################################
# enumerate (list 의 반복을 사용할 때)
##############################################################
# enumerate 는  1회용 함수이기때문에 변수에 넣어서 사용하지 말기
for i, element in enumerate(arry):
    print("enumerate index:{} value:{}".format(i, element))

##############################################################
# item  (Dict 에 반복을 사용할 때)
##############################################################
aDict = {"key0": "value0", "key1": "value1", "key2": "vakue2"}
for key, value in aDict.items():
    print("items key:{} value:{}".format(key, value))

# list 내포 (list 에 값 바로 꼽기?)
arry_1 = [i * i for i in range(0, 20, 2)]
arry_2 = [1 for i in range(10)]
arry_3 = [i for i in range(10) if i % 2 == 0]

print("list 내포 {} {} {}".format(arry_1, arry_2, arry_3))
