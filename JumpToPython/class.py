# 계산기의 더하기 기능을 구현한 파이썬 코드
from symtable import Class

result = 0
def add(num):
  global result
  result += num # 결과값(result)에 입력값(num) 더하기
  return result # 결과값 리턴
                # add라는 함수는 정의만 되어있는 상태
print(add(3))   # result = 0 + 3 = 3
print(add(4))   # result = 3 + 4 = 7


print("========================================================")
# 2개의 계산기를 필요로할 때

result1 = 0
result2 = 0

def add1(num):  # 계산기1
    global result1
    result1 += num
    return result1

def add2(num):  # 계산기2
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))


print("========================================================")
# 클래스를 사용했을 경우
class Calculator:           # 클래스 정의
    def __init__(self):     # 객체가 만들어질 때 자동으로 실행할 함수 (생성자)
        self.result = 0     # 이름을 바꾸면 파이썬이 인식하지 못함

    def add(self, num):
        self.result += num
        return self.result
# cal1 과 cal2는 서로 다른 객체
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

print("========================================================")

# 클래스와 객체
class Cookie:
    pass # 아무것도 수행하지 않는 문법, 임시 코드를 작성할 때 주로 사용
a = Cookie()
b = Cookie()

print("========================================================")

# 사칙 연산 클래스 만들기

class FourCal:
    def setdata(self, first, second): # 메서드 ( 메서드의 매개변수 )
        self.first = first   # 메서드의 수행문
        self.second = second    # 메서드의 수행문


a = FourCal()
a.setdata(4,2)
print(a.first)
print(a.second)
# setdata는 매개변수가 3개인데 2개만 전달에도 호출이 됨
# a.setdata(4,2) 형태로 호출하면 a가 self, 4가 first, 2가 second
# 메서드의 첫 번째 매개변수 self를 명시적으로 구현하는건 파이썬만의 독특한 특징

a = FourCal()
b = FourCal()
a.setdata(4,2)
print(a.first)
b.setdata(3,7)
print(b.first)


print("========================================================")

# 더하기 기능 만들기

class FourCal:
    def setdata(self, first, second):
       self.first = first
       self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4,2)
print(a.add())

print("========================================================")

# 곱하기, 빼기, 나누기 기능 추가하기

class FourCal:
     def setdata(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result
     def mul(self):
         result = self.first * self.second
         return result
     def sub(self):
         result = self.first - self.second
         return result
     def div(self):
         result = self.first / self.second
         return result

a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,8)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

print("========================================================")

# __init__ 생성자 사용하기
# setdata 메서드와 이름만 다르고 모든게 동일하지만
# __init__ 을 사용했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출 됨
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result
# ------------------------------------------
# a = FourCal()
#------------------------------------------
# Traceback (most recent call last):
#   File "C:\Python_workspace\JumpToPython\.venv\calculator.py", line 168, in <module>
#     a = FourCal()
# TypeError: FourCal.__init__() missing 2 required positional arguments: 'first' and 'second'
#------------------------------------------
# a = FourCal()를 수행할 때 생성자 __init__이 호출되어 오류가 발생함
# __init__ 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문
a = FourCal(4,2)# 해당하는 값을 전달하여 객체를 생성해야 한다
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())


print("========================================================")

# 클래스의 상속
# class 클래스명(상속받을클래스명):
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

print("========================================================")

# 제곱 계산하는 클래스 만들기

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result
a = MoreFourCal(4,2)
print(a.pow())
print(a.add())


print("========================================================")

# 메서드 오버라이딩
# : 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것
# a = FourCal(4,0)
# a.div()
# print(a.add())
# 4를 0으로 나누려고 했기 때문에 오류 발생

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0: # 나눈 값이 0일 경우
            return 0 # 0을 반환하도록 설정
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.div())


print("========================================================")

# 클래스 변수
class Family:
    lastname = "김" # 클래스 변수
a = Family()
b = Family()

print(Family.lastname)
print(a.lastname)
print(b.lastname)

a.lastname = "최"
print(a.lastname) # Family 클리스의 lastname이 바뀌는 것이 아니라
                  # a 객체에 lastname이라는 객체변수가 새롭게 생성 됨
                  # 객체변수는 클래스 변수와 동일한 이름으로 생성할 수 있다
                  # a.lastname 객체변수를 생성하더라도 Family 클래스의 lastname과는 상관 없음을 알 수 있음

print(Family.lastname) # 변화없음
print(b.lastname) # 변화없음
