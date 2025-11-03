# pos/main.py
# 프로그램 진입점
# 재고/가격을 파일에서 읽어 goods, day_sale을 구성하고
# 결제·재고관리·매출관리 메뉴를 라우팅함
# 종료시 ep.main()으로 당일 데이터 저장

import pay # 결제플로우
import update # 결제 결과로 재고/일매출 갱신
import management # 일/월 매출조회 UI
import gmanagement # 재고관리 (현황/발주) UI
import ep # 종료 시 파일 저장 / 갱신




#재고 및 물품 정보를 텍스트 파일에서 읽기
# goods : {상품번호: {"분류":str,"품목":str,"가격":str,"재고":int}}
# day_sale : {상품번호: int, "card":int, "cash":int}
f = open("재고/goods.txt", "r", encoding="utf-8")
goods ={}                       # 물품 정보 및 재고 저장
day_sale = {"card":0,"cash":0}  # 일 매출 정보 저장 (결제수단, 합계)

# 파일 한 줄씩 읽어서 goods/day_sale 초기화
while(True) :
    tmp_dic = {} # 한 상품의 속성 임시 저장
    line = f.readline() # 한 줄 읽기
    line = line.rstrip("\n") # 오른쪽 끝에있는 \n 제거
    if(line==""):   # EOF(빈줄)면 종료
        break
    
    st_list = line.split("/") # 포맷 : 코드/분류/품목/가격/재고
                              # split 함수 : 문자열을 일정한 규칙으로 잘라서 리스트로 만들어주는 함수
    tmp_dic["분류"] = st_list[1] # st_list[1] 의 값을 가져와 tmp_dic 딕셔너리 안의 "분류"라는 키에 저장한다는 뜻
    tmp_dic["품목"] = st_list[2]
    tmp_dic["가격"] = int(st_list[3])
    tmp_dic["재고"] = int(st_list[4])

    goods[st_list[0]] = tmp_dic # goods(딕셔너리)에 저장
    day_sale[st_list[0]] = 0 # 품목별 일 매출 초기값 0으로 저장
    
#  일매출 누적
import os, datetime as t
_now = t.datetime.now()
_MM = f"{_now.month:02d}"
_DD = f"{_now.day:02d}"
_day_path = f"관리/{_MM}{_DD}.txt"

if os.path.exists(_day_path):
    with open(_day_path, "r") as _f:
        for _line in _f:
            _line = _line.strip()
            if not _line:
                continue
            _k, _v = _line.split("/")
            _v = int(_v)
            # 기존에 있는 키면 덮어쓰고, 없던 키면 추가
            day_sale[_k] = _v


# 메인 메뉴 루프

while True:
    print("="*30)
    print("1. 결제 \n2. 물품 관리 \n3. 매출 관리 \n9. 종료")
    print("="*30,end="\n")
    select_num = input('선택 : ') # 사용자 입력

    # 1) 판매 및 재고, 일매출 정리
    if select_num == '1':
        tmp = pay.main(goods) # 결제 수행 → 거래 로그 반환
        update.main(goods,tmp,day_sale) # 재고/매출 갱신

    # 2) 재고 및 발주 관리
    elif select_num == '2':
        gmanagement.main(goods)

    # 3) 일매출 및 월매출 확인
    elif select_num == '3':
        management.main(goods,day_sale)

    # 9) 종료 : 메모리 내용을 파일로 반영 후 종료
    elif select_num == '9':       
        ep.main(goods,day_sale)  # 재고/일매출/월매출 파일 저장
        break
    else:
        print("다시 선택 하세요\n")

print("\nSystem down")  # 프로그램 종료 메시지
