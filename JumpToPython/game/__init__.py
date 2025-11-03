# 패키지 내 모듈을 미리 import
from .graphic.render import render_test


VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

# 패키지 초기화 코드
print ("Initializing game...")

__all__ = ['echo']