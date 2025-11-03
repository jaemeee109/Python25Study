# pos/lotto.py
# 수동/자동 로또 번호 생성 유틸
# pay.py에서 상품 코드 10 선택시 사용
import random

# main → 수동 / 자동 선택을 받아 count회 번호 생성
def main(count):
    print("="*30)
    while True:
        print("="*30)
        s_num = input("1. 수동\n2. 자동\n: ")
        

        if s_num == '1':
            print("="*30)
            for i in range(count) :
                lotto_num = manual()
                
                print("로또 번호 : ", lotto_num)
            break
        elif s_num == '2':
            print("="*30)
            for i in range(count) :
                lotto_num = auto()
                
                print("로또 번호 : ", lotto_num)
            break
        else:
            print("="*30)
            print("다시 입력하세요")
            print("="*30,end="\n")
        print("="*30,end="\n")
   

#수동 로또 : 6개 정수 입력 → 검증 / 정렬 후 반환
def manual():
    while True:
        num1 = int(input("첫번째 수 : "))
        num2 = int(input("두번째 수 : "))
        num3 = int(input("세번째 수 : "))
        num4 = int(input("네번째 수 : "))
        num5 = int(input("다섯번째 수 : "))
        num6 = int(input("여섯번째 수 : "))
        print("="*30,end="\n")
        
        manual = [num1, num2, num3, num4, num5, num6]
        dupli = check(manual) # 중복 체크
        
        if dupli == False:
            print("\n중복값이 있습니다. 다시 입력하세요\n")
            print("="*30,end="\n")
            continue
        else:
            manual.sort()

        if manual[-1] > 45: # 1~45 범위 확인
            print("\n45 이하 의 숫자로 다시 입력하세요\n")
            print("="*30,end="\n")
            continue
        else:
            break
        
    return manual
        

#자동 로또 번호 생성 (1~44 사이 정수 난수, 중복 없으면 정렬 후 반환)
def auto():
    while True:
        num1 = random.randrange(1,45)
        num2 = random.randrange(1,45)
        num3 = random.randrange(1,45)
        num4 = random.randrange(1,45)
        num5 = random.randrange(1,45)
        num6 = random.randrange(1,45)

        auto = [num1, num2, num3, num4, num5, num6]

        dupli = check(auto)
        
        if dupli == False:
            continue
        else:
            auto.sort()
            break

    return auto

# 중복 확인 : 리스트 내 같은 값이 2개 이상이면 False
def check(lotto_num):
    i=0;
    dupli = True

    while i<45:
        if lotto_num.count(i) < 2:  # 값 i 가 2개 이상이면 중복
            i+=1
            continue
        else:
            dupli = False
            break

    return dupli



