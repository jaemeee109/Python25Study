# pos/ep.py
# 종료 처리(Export/Persist)
# 변경된 재고를 재고/goods.txt로 저장
# 당일 일 매출을 (관리/<mm><dd>.txt)로 저장
# 월 매출 파일 (관리/<mm>-total.txt)을 기존 월 매출 + 당일 매출로 갱신해 다시 저장
import management   # 월 매출 합계 읽기 함수 사용
import datetime as t    # 날짜 포맷에 사용


# 변경된 재고 정보를 텍스트 파일에 저장
# 포맷 : 코드/분류/품목/가격/재고 
def re_stock(goods) :
    f = open("재고/goods.txt","w")

    for i in goods.keys() :
        f.write("{}/{}/{}/{}/{}\n".format(i,goods[i]['분류'],goods[i]['품목'],goods[i]['가격'],goods[i]['재고']))

    f.close()


# 일 매출 정보를 텍스트 파일에 저장
# 파일명: 관리/<MM><DD>.txt, 라인: 키/값
def make_day_sale(month,day,day_sale) :

    f = open("관리/"+month+day+".txt","w")

    for i in day_sale.keys() :
        f.write("{}/{}\n".format(i,day_sale[i]))

    f.close()

    
# 월 매출 정보를 불러와서 일 매출 정보를 더한 다음에 다시 텍스트 파일에 저장
# 대상 파일 : 관리/<MM>-total.txt
def make_month_sale(month,day_sale) :
    tmp_dic = management.month_margin(month)    # {'MM':{...}}
    month_sale = tmp_dic[month] # 월 누적 딕셔너리
    f_dic = {}
    
    # 키별로 기존 월매출 + 오늘 일매출
    for i in month_sale.keys() :
        prev = month_sale[i] if i in month_sale else 0 # 안전 가드 : month_sale에 키가 있으면 그 값,
        f_dic[i] = prev + day_sale[i]                  # 없으면 0 (현재 루프에선 항상 존재)
                                                       # 당일(day_sale)의 같은 키 금액을 더해 누적값으로 저장
                                                       # (키가 day_sale에 없으면 KeyError 위험)
    
    f = open("관리/"+month+"-total.txt","w")

    for i in f_dic.keys() :
        f.write("{}/{}\n".format(i,f_dic[i]))

    f.close()


# 종료 시 전체 저장을 묶는 엔트리
def main(goods,day_sale) :
    
    now = t.datetime.now()
    month = now.month
    day = now.day

    # 2자리 포맷
    if month < 10 :
        month = '0'+str(month)
    else :
        month = str(month)

    if day < 10 :
        day = '0'+str(day)
    else :
        day = str(day)


    re_stock(goods) # 1) 재고 저장
    make_day_sale(month,day,day_sale) # 2) 당일 일매출 저장
    make_month_sale(month,day_sale) # 3) 월매출 합산 저장
