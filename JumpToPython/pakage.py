
# echo.py 모듈 호출
import game.sound.echo
game.sound.echo.echo_test()

# from 모듈이름 import 모듈함수로 호출
from game.sound.echo import echo_test
echo_test()

print("========================================================")

# 패키지 변수 및 함수 정의
# __init__.py

import game
print(game.VERSION)

game.print_version_info()
print("========================================================")


# game에서 render을 import해서
# game을 호출해 간편하게 render_test 함수 사용 가능
import game
game.render_test()
print("========================================================")

# 패키지 초기화
import game
# 초기화 코드는 한 번 실행된 후에는 다시 import를 수행하더라도 실행되지 않음

import game
from importlib import reload # reload 하면 실행 됨

reload(game)

print("========================================================")

# __all__ : * 을 사용하여 import할 경우, 이 곳에 정의된
#           echo 모듈만 import 된다는 의미
import game 
from game.sound import *
echo.echo_test()

print("========================================================")

# 상대경로 패키지

from game.graphic.render import render_test
render_test()