# management.py
# 일/월 매출 조회 UI.
# 월 매출 파일(관리/<MM>-total.txt)을 읽어 표기하고
# 현재 메모리의 일 매출도 표기
# month_margin()은 월 합계 파일을 딕셔너리로 로드

import datetime as t


# 월 매출을 파일에서 읽어와서 딕셔너리 형태로 저장한 다음 반환
def month_margin(month) :
    import os   # 파일 존재 여부 확인을 위해 표준 모듈 os 임포트

    
    path = "관리/"+month+"-total.txt" # 읽고/생성할 월 매출 파일
    tmp_dic = {}    # 최종 반환 딕셔너리
    tmp_month = {}  # 월 내부 항목 딕셔너리

    # 파일 없으면 0으로 초기 생성 (card/cash만 우선)
    if not os.path.exists(path) :   # 해당 파일이 없는 첫 실행 상황인지 검사
        f = open(path,'w')          # 없으면 'w' 모드로 새 파일 생성 (기존 파일이 있다면 덮어씀)
        f.write("card/0\n")         # 기본 결제수단 card를 0으로 초기화하여 기록
        f.write("cash/0\n")         # 기본 결제수단 cash를 0으로 초기화하여 기록
        f.close()                   # 파일 닫기 (리소스 반납)
        tmp_month['card'] = 0       # 메모리 상 딕셔너리에도 동일한 초기 상태 반영
        tmp_month['cash'] = 0       # cash 키도 0으로 초기 반영
        tmp_dic[month] = tmp_month  # 바깥 딕셔너리에 담기
        return tmp_dic              # 초기 생성된 결과를 즉시 반환

    # 파일이 있으면 읽어서 로드
    f = open(path, 'r')         # 파일이 존재할 경우 읽기 모드로 오픈
    while True:                 # 파일 끝까지 한 줄씩 읽는 루프
        line = f.readline()     # 한 줄 일기
        if line == '':          # 빈 문자열이면 EOF (파일 끝) → 반복종료
            break
        line = line.rstrip('\n')
        if line == '':
            continue
        tmp_list = line.split('/')
        tmp_month[tmp_list[0]] = int(tmp_list[1])

    # card/cash 키가 누락된 파일 대비 보정
    if 'card' not in tmp_month:
        tmp_month['card'] = 0
    if 'cash' not in tmp_month:
        tmp_month['cash'] = 0

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


