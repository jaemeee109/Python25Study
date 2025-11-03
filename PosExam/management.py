# management.py
# 일/월 매출 조회 UI.
# 월 매출 파일(관리/<MM>-total.txt)을 읽어 표기하고
# 현재 메모리의 일 매출도 표기
# month_margin()은 월 합계 파일을 딕셔너리로 로드

import datetime as t


# 월 매출을 파일에서 읽어와서 딕셔너리 형태로 저장한 다음 반환
def month_margin(month) :
    
    f = open("관리/"+month+"-total.txt",'r')
    tmp_dic = {}    # 최종 반환 딕셔너리
    tmp_month = {}  # 월 내부 항목 딕셔너리

    while True :
        line = f.readline()
        if line == '' :
            break
        line = line.rstrip('\n')
        tmp_list = line.split('/')
        tmp_month[tmp_list[0]] = int(tmp_list[1]) # 키/값 로드

    tmp_dic[month] = tmp_month

    return tmp_dic

# # 일매출/월매출 조회 UI
# 받아온 day_sale 딕셔너리를 이용하여 일매출을 화면에 출력
# 월매출 딕셔너리를 반환 받아서 화면에 출력
def main(goods,day_sale) :

    now = t.datetime.now()
    month = now.month
    day = now.day

    # 월 / 일 2자리 포맷
    if month < 10 :
        month = '0'+str(month)
    else :
        month = str(month)

    if day < 10 :
        day = '0'+str(day)
    else :
        day = str(day)
    

    while True :
        try :
            print("="*30)
            s_num = int(input("1. 일 매출 / 2. 월 매출 / 5. 종료 : "))
            print("="*30,end="\n")

        except :
            continue
        # 1) 일 매출 표시
        if s_num == 1 :
            print("  일  매  출")
            print("="*30)
            for i in day_sale.keys() :
                if i == 'card' or i == 'cash':
                    continue
                else :
                    # 품목명과 해당 품목의 일 매출 표시
                    print("{}. {} : {}".format(i,goods[i]['품목'],day_sale[i]))
            
            print("="*30,end="\n")
            # 결제수단 합계
            print("{} : {}\n{} : {}\n".format('card',day_sale['card'],'cash',day_sale['cash']))
            print("="*30,end="\n")
            print()

        # 2) 월 매출 표시 (파일에서 로드)
        elif s_num == 2 :
            
            dic = month_margin(month)
            tmp_dic = dic[month]
            print(  "월  매  출")
            print("="*30)
            for i in tmp_dic.keys() :
                if i == 'card' or i == 'cash':
                    continue
                else :
                    
                    print("{}. {} : {}".format(i,goods[i]['품목'],tmp_dic[i]))

            print("="*30,end="\n")
            print("{} : {}\n{} : {}\n".format('card',tmp_dic['card'],'cash',tmp_dic['cash']))
            print("="*30,end="\n")
            print()

        # 5) 종료 (상위 메뉴로 복귀)
        elif s_num == 5 :
            break

        else :
            print("="*30) 
            print("다시 입력하세요")
            print("="*30,end="\n")
            print()


