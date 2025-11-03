# pos/update.py
# pay.main()이 반환한 거래로그를 이용해
# 재고 차감 및 일매출(day_sale) 집계를 갱신
import datetime as t
import ep

def main(goods,guest_log,day_sale) :

    guest_dic = guest_log["판매"]     # {상품코드: 수량}
    guest_dic_key = list(guest_dic.keys())

    # 품목별 일매출 계산 및 재고 차감
    for i in list(day_sale.keys()) :       # day_sale 키: 'card','cash',그리고 상품코드들
        if i not in guest_dic_key :
            continue
        
        # 품목별 일매출 누적 = 기존금액 + (이번 거래 수량 * 단가)
        day_sale[i] += guest_dic[i] * goods[i]['가격']
        # 재고 차감
        goods[i]['재고'] = goods[i]['재고'] - guest_dic[i]
        
    # 결제수단 합계 반영
    if guest_log['결제'] == 'cash' :                  # 금액 입력부분
        day_sale["cash"] = day_sale["cash"] + guest_log["판매금액"]  

    elif guest_log['결제'] == 'card' :
        day_sale["card"] = day_sale["card"] + guest_log["판매금액"]

    # 결제 직후 월 합계 파일에 즉시 갱신
    # day_sale이 갱신된 직후, 매번 월 누적 파일 (관리/<MM>-total.txt)을 즉시 반영
    now = t.datetime.now()
    month = f"{now.month:02d}"
    day = f"{now.day:02d}"
    ep.make_day_sale(month, day, day_sale)  # 오늘 일매출 파일 저장: 관리/MMDD.txt
    ep.make_month_sale(month, day_sale)  # 월매출 파일 갱신:   관리/MM-total.txt