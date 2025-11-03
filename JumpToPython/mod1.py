# 모듈 만들기

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

if __name__ == "__main__":
    print(add(1,4))
    print(sub(4,2))

# __name__ : 파이썬 내부적으로 사용하는 특별한 변수명
# 직접 mod1.py 파일을 실행 할 경우 mod1.py __name__ 변수에는 __main__값이 저장 됨
# 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import할 경우에는 mod1.py의 __name__ 변수에 mod1.py의 
# 모듈 이름인 mod1이 저장됨