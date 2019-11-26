from new_login import *
from lotto import *

def main():
    ID, money, passwd = login(load_members())
    print(ID,"님 안녕하세요! 테스트입니다\n\n")
    lottogame(money, ID, passwd)

main()