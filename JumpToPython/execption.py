# 예외처리

print("========================================================")

# try-except문
# try :
#      ...
# except [발생오료 [as 오류변수]]:
#      ...

try :
    4/0
except ZeroDivisionError as e:
    print(e)
    
print("========================================================")

# try-finally 문
# try:
#    f = open('foo.txt','w')
#    # 수행
#    (... 생략 ...)
# finally:
#   f.close() # 중간에 오류가 발생하더라도 무조건 실행됨

try:
    f = open('example.txt', 'w')  # 파일 열기
    f.write("Hello, world!\n")
    # 일부러 에러 발생시키기

finally:
    print("파일을 닫습니다.")
    f.close()  # 오류가 나도 반드시 실행됨

print("프로그램 정상 종료")

print("========================================================")

# 여러 개의 오류 처리하기
# try:
#    ...
#except 발생오류1:
#   ...
# except 발생오류2:
 #  ...
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

    try:
        a = [1, 2]
        print(a[3])
        4 / 0
    except ZeroDivisionError as e:
        print(e)
    except IndexError as e:
        print(e)
print("========================================================")

# try-else 문
# try:
#    ...
# except [발생오류 [as 오류변수]]:
#    ...
# else:  # 오류가 없을 경우에만 수행
#    ...

try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
