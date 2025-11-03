# import 모듈이름
import mod1

print(mod1.add(3,4))
print(mod1.sub(4,2))

print("========================================================")
# 함수만 사용하고 싶을 때
# from 모듈이름 import 모듈함수

from mod1 import add
print(add(3,4))
# ---------------------------
from mod1 import add, sub # 여러개 호출
print(add(9,1))
print(sub(5,6))
# ---------------------------
from mod1 import * # 다수 호출
print(add(9,1))
print(sub(5,6))

print("========================================================")

# __name__ 변수
import mod1
print(mod1.__name__)

print("========================================================")
# 클래스나 변수 등을 포함한 모듈
import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI,4.4))