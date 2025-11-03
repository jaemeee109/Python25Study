# pos/pay.py
# 결제 플로우 전담
# (고객 성별 / 연령 입력 → 상품/수량 선택 → 영수증출력 → 카드/현금결제)
# 구매품목에 10을 고르면 lotto.main()호출
# 결제 결과(일시, 결제수단, 판매금액, 잔돈, 품목/수량)를 딕셔너리로 변환
import datetime as t    # 현재시각 표시
import lotto    # 로또 번호 생성 유틸 (상품 10번 선택 시 사용)


# 고객의 성별 정보를 저장 guest_Log에 저장
def choice_gender(guest_log) :
    print("="*30)
    gender = input("\n성별 입력\n1. 남자 / 2. 여자 : ")
    print("="*30,end="\n")

    if gender == '1' :
        guest_log["gender"] = 'man'
    elif gender == '2' :
        guest_log["gender"] = 'woman'
    else :
        return True # 잘못입력 → 재입력 유도

    return False    # 정상 입력


# 고객의 대략적인 연령대를 guest_Log에 저장
def choice_age(guest_log) :
    print("="*30)
    print("\n나이 입력\n0. 10대 이전\n1. 10대\n2. 20대\n3. 30대\n4. 40대\n5. 50대\n6. 60대\n7. 60대 이상")
    print("="*30,end="\n")
    age = input("선택 : ")
    print()

#   선택 값을 대표 나이로 매핑
    if age == '0':
        guest_log['age'] = 0
    elif age == '1':
        guest_log['age'] = 10
    elif age == '2':
        guest_log['age'] = 20
    elif age == '3':
        guest_log['age'] = 30
    elif age == '4':
        guest_log['age'] = 40
    elif age == '5':
        guest_log['age'] = 50
    elif age == '6':
        guest_log['age'] = 60
    elif age == '7':
        guest_log['age'] = 70
    else :
        return True #   잘못입력

    return False


# 물건 목록을 띄우고 그 중에서 어떤 물건을 구매할지 선택
# 물건의 수량 정보까지 취합하여 저장
# 구매 물건으로 로또를 선택했을 경우 lotto.main() 호출
def select_goods(tmp,goods) :
    tmp_list = list(goods.keys()) # 상품 코드 목록
    
    print("="*30)

    for i in tmp_list :
        print("\n{}.\t{}\t/\t금액\t:\t{}".format(i,goods[i]['품목'],goods[i]['가격']))
    # ex) 8. 콜라 / 금액 : 1500
    print("="*30,end="\n")
    
    #   유효한 상품 코드 입력될 때까지 반복
    s_num = 0
    while True :
        s_num = input("\n구매 상품 번호 : ")
        if s_num in goods :
            break              

    #   수량 입력 ( 정수만 허용 )
    while True :
        try :
            count = int(input("\n구매 상품 수량 : "))
            break
        except :
            continue    

    # 상품번호 10 → 로또 모듈 실행
    if s_num == '10':
        lotto.main(count)
    # 선택 확인 / 취소
    while True :
        print("="*30)
        print("제품 : {} / 수량 : {}".format(goods[s_num]['품목'],count))
        print("="*30,end="\n")
        num = input("1. 확인 / 2.취소 : ")
        print("="*30,end="\n")
        if num == '1' :
            tmp[s_num] = count # 장바구니(판매 dict)에 반영
            return False    # 정상 종료
        elif num == '2' :
            return True # 취소 → 상위에서 재선택


# 구매하고자 하는 물건의 종류와 수량을 선택하는 흐름 제어
def flow_choice(guest_log,goods) :

    boolean = True
    service = 0
    tmp_goods = guest_log['판매']     # 현재까지 선택한 품목 dict
   
   # 최소 1품목 확정될 때까지 select_goods 반복
    while boolean :
        boolean = select_goods(tmp_goods,goods)    

    guest_log['판매'] = tmp_goods

    # 추가로 다른 품목도 선택할지 여부
    while True :
        print("="*30)
        end_flag = input("1. 다음 / 2. 다른 물품 선택 : ")
        print("="*30,end="\n")

        if end_flag == '1' :
            return False    # 결제 단계로 진행
        elif end_flag == '2':
            return True     # 다시 품목 선택으로


# 영수증 출력을 위하여 구매한 물건의 수량과 합계금액 정보를 저장
def calc_cost(tmp_dic,goods) :
    total = 0
    tmp_list = list(tmp_dic.keys())
    sale_dic = {}    # {1:{품목,수량,총금액}, 2:{...},...}
    count = 0
    for i in tmp_list :
        tmp = {}
        count += 1
        t = goods[i]['가격'] * tmp_dic[i]
        total += t
        tmp['품목'] = goods[i]['품목']
        tmp['수량'] = tmp_dic[i]
        tmp['총금액'] = t
        sale_dic[count] = tmp

    return sale_dic,total


# 결제 방법 선택 ( 카드/현금) 선택
def select_payment() :
    print("="*30)
    payment = input("1. 카드 / 2. 현금 : ")
    print("="*30,end="\n")
    tmp = 0

    if payment == '1' :
        tmp = 1

    elif payment == '2' :
        tmp = 2

    else :
        return True, tmp # 잘못입력

    return False, tmp # {성공여부, 수단}


# 카드 결제 처리 (영수증 출력 후 확인/취소)
def select_card(sale_dic,total,guest_log) :
    print()
    print()
    print("========== 영수증 ============")
    print("품목\t수량\t금액")
    print()

    for i in sale_dic.keys() :
        print("{}\t{}\t{}".format(sale_dic[i]['품목'],sale_dic[i]['수량'],sale_dic[i]['총금액']))

    print()
    print("="*30,end="\n")

    print("\ntotal : {}".format(total))

    print("="*30,end="\n")
        
    tmp = input("1. 확인 / 2. 취소 : ")

    print("="*30,end="\n")

    if tmp == '1' :
        print("결제 완료")
        print("="*15)
        guest_log["결제"] = "card"
        guest_log["판매금액"] = total
        guest_log["거스름돈"] = None
        return False
    elif tmp == '2' :
        print("결제 취소")
        print("="*15)
        return True # 재시도
    else :
        print("다시 입력하세요")
        return True


#  현금 결제 처리 (영수증, 받은 현금, 거스름돈 계산)
def select_cash(sale_dic, total,guest_log) :
    print()
    print()
    print("========== 영수증 ============")
    print("품목\t수량\t금액")
    print()

    for i in sale_dic.keys() :
       print("{}\t{}\t{}".format(sale_dic[i]['품목'],sale_dic[i]['수량'],sale_dic[i]['총금액']))

    print()
    print("="*30,end="\n")
    print("\ntotal : {}".format(total))
    print("="*30,end="\n")
    
    while True :
        tmp = input("\n받은 현금 : ")
    
        try :
            tmp = int(tmp)
            break
        except :
            continue

    if tmp - total < 0 :
        print("="*30,end="\n")
        print("받은 현금이 부족합니다")
        print("="*30,end="\n")
        return True # 재시도
    else :
        print("="*30,end="\n")
        print("\n결제 완료")
        print("="*30,end="\n")
        print("잔돈 : {}원".format(tmp - total))
        print("="*30,end="\n")
        guest_log["결제"] = "cash"
        guest_log["판매금액"] = total
        guest_log["거스름돈"] = tmp - total
        return False        


# 결제 전체 플로우 (수단 선택 → 카드/현금 처리)
def flow_payment(guest_log,goods) :
  
    boolean = True
    select_num = 0
    tmp_goods = guest_log["판매"]
    sale_dic, total = calc_cost(tmp_goods,goods) # 영수증 / 합계 준비

    # 유효 수단 선택까지 반복
    while boolean :
        boolean, select_num = select_payment()
    # 선택 수단별 결제 처리
    boolean = True
    if select_num == 1 :
        while boolean :
            boolean = select_card(sale_dic,total,guest_log)
    elif select_num == 2 :
        while boolean :
            boolean = select_cash(sale_dic,total,guest_log)

    return False # 결제 완료


# 결제 진입점 : 고객 속성 입력 → 상품선택 → 결제 → 거래로그 반환
def main(goods) :
    
    now = t.datetime.now()
    guest_log = {'판매':{}} # 거래로그 기본 구조
    print("="*30)
    print(now)   # 현재 시각 표시
    print("="*30,end="\n")
    while choice_gender(guest_log) :
        print("\n다시 입력하세요")
    
    while choice_age(guest_log) :
        print("\n다시 입력하세요")

    while flow_choice(guest_log,goods) :
        continue

    while flow_payment(guest_log,goods) :
        continue

    # 거래 일시 (YYYY-M-D/H:M)
    now_time = "{}-{}-{}/{}:{}".format(now.year,now.month,now.day,now.hour,now.minute)

    guest_log["일시"] = now_time

    print("="*30,end="\n")
    print()

    return(guest_log)   #    상위(update)에서 재고/매출 갱신에 사용

