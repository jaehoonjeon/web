print('##################  함수  ##################')


# 함수 선언, 변수의 기본값, 호출
def function(param='World'):
    print("Hello " + str(param))
    return "return Hello " + str(param)


print(function())


# 가변 매개변수 함수(한개만 사용 가능, 가장 마지막에 들어가야 함)
def function(param1, param2, *paramV):
    print(param1, param2, "가변 매개변수:{}".format(paramV))


function(1, 1, 2, 2, 2, 2, 2)


# 매개변수의 순서, 실행
def function(normalParam, *vParam, defaultParam=10):
    returnVal = str(normalParam) + " "

    for i, element in enumerate(vParam):
        returnVal += "/{}:{}/".format(str(i), str(element))
    returnVal += str(defaultParam)
    return returnVal


print(function(1, 2, 2, 2, defaultParam=333))

# 함수내에서 함수 밖 변수를 사용할 경우 (global keyword 사용)
counter = 0


def f(n):
    global counter
    counter += 1
    return counter


print('##################  튜플  ##################')

# 함수의 2가지 이상의 Return 있는 경우 자주 사용함, ( ) 괄호 생략 가능
tuple_a = (0, 1, 2, 3)
# tuple_a[0] = 4 수정 불가
print("tuple a[0] : {}".format(tuple_a[0]))
# 요소가 하나인 튜플
tuple_b = (273,)
print("tuple_b type : {}".format(type(tuple_b)))
# dict 에 key 로 튜플이 올 수 있다
tuple_dict = {
    (0, 0): 10,
    (0, 1): 20
}
print("tuple_dict : {}, {}".format(tuple_dict[0, 0], tuple_dict[(0, 1)]))


# 함수의 매개변수로 함수를 사용
def call_2_times(func):
    for i in range(2):
        # 콜백함수
        func(i)


def print_hello(number):
    print("안녕하세요", number)


call_2_times(print_hello)

print('##################  lamda, filter, map, generator ##################')
# lamda 람다 한줄짜리만 가능
call_2_times(lambda number: print("안녕하세요"))


# filter (함수, list)
def 짝수만(number):
    return number % 2 == 0


fun_짝수만 = lambda number: number % 2 == 0

a = list(range(10))
# b = filter(짝수만, a)
# b = filter(lambda number: number % 2 == 0, a)
b = filter(fun_짝수만, a)
print("print even using filter {}".format(list(b)))


# map (기존의 list 를 기반으로 새로운 list 를 만들때 사용, 메모리용량을 절약 가능)
def 제곱(number):
    return number * number


a = list(range(10))
# print("create new list using map {}".format(list(map(제곱,a))))
print("create new list using map {}".format(list(map(lambda number: number * number, a))))


############################################################################
# filter, map, list 내포 비슷한 기능인데, list 내포를 더 많이 사용하는 추세이다
############################################################################

# generator 함수 (1회용) 언제쓰냐?? 메모리를 절약할 수 있다
# iterator 를 직접 만들 때 사용하는문
def 함수():
    print("printA")
    yield 100  # 정지
    print("printB")
    yield 200  # 정지


# 사용
제너레이터 = 함수()
# next(제너레이터)
# next(제너레이터)

for i in 제너레이터:
    pass

print('##################  예외처리  ##################')

try:
    print(float("str") ** 2)
except ValueError as e:
    print("Value Err")
except IndexError as e:
    print("Index Err")
except Exception as e:
    print("unkown Err {}".format(e))
finally:
    print("finally")

# raise 강제 예외
# raise Exception("일부러 예외를 발생")


print('##################  Class  ##################')


# Class 내부에 함수의 매개변수의 첫번째 파라미터는 self
class Student:
    # 생성자
    # __functionName__ 미리만들어진 함수 이것 저것 쓸만한게 많다
    def __init__(self, name, korean, math, english):
        # private var :: __varName
        self.__name = name
        self.__korean = korean
        self.__math = math
        self.__english = english

    # getter
    def get_name(self):
        return self.__name

    # setter
    def set_name(self, name):
        if str(name).isdigit():
            raise Exception("이름은 숫자는 불가능합니다")
        self.__name = name

    # getter
    @property
    def korean(self):
        return self.__korean

    # setter
    @korean.setter
    def korean(self, korean):
        if type(korean) is str :
            print.log("점수는 숫자로 입력하세요")
            raise Exception("점수는 숫자로 입력하세요")
        self.__korean = korean

    def sumScore(self):
        return self.__korean + self.__math + self.__english

    def aveScore(self):
        return self.sumScore() / 4

    def printScore(self):
        print(self.__name, self.sumScore(), self.aveScore(), sep="\t")


students = [
    Student("김길동", 50, 60, 70),
    Student("홍길동", 10, 20, 30)
]

for student in students:
    student.printScore()

print('##################  module  ##################')

import math

print("import math pi, sin(10) :: ", math.pi, math.sin(10))

# import 하는 방법 5가지

# import mat
# import math as 수학
# math = __import__("math")

# from math import pi, sin
# from math import *

# 내장 module library
# https://docs.python.org/3/library/index.html

import datetime
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

# string formatting?

import time
print("before sleep")
time.sleep(1.5)
print("after sleep")

from urllib import request
target = request.urlopen("https://www.theksa.or.kr")
content = target.read()
print(content[:200])


print('##################  함수 데코레이터, 상속  ##################')

# decorator (함수를 감싸서 어떠한 선처리를 한다?)

def out_decorator(paramS): #파라미터를 전하려면 한번더 감싸야한다
    def decorator(fun):
        print("미리 어떤 처리를 진행합니다", paramS)
        return fun
    return decorator

@out_decorator(paramS="parameter!")
def test_dec():
    print("안녕하세요")


# 상속 ClassName(ParentsClassName)

class Parents:
    def func_parents(self):
        print("부모의 함수 입니다")

class Sun(Parents):
    pass

c = Sun()
c.func_parents()

