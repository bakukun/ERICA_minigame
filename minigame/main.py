from new_login import *
from store import *
from lotto import *
from explain import *
from thief_catch import *
from roulette import *
from icecream import *
from bank import *
import time

def main():
    while (1):
        try:
            ID, money, passwd, icecream_ok, roulette_ok, thief_ok = login(load_members())
        except TypeError:
            print("대문자 혹은 한글이 아이디에 포함되면 계정생성시에만, 다시 로그인을 실행해야 합니다ㅠㅠ")
            print("로그인을 다시 해주시면 감사하겠습니다!")
            time.sleep(1)
            ID, money, passwd, icecream_ok, roulette_ok, thief_ok = login(load_members())
        print(ID, "님 안녕하세요!")
        break
    ment = "ERCIA OPEN_SW 미니게임입니다\n"
    for i in ment:
        time.sleep(0.1)
        print(i, end='')
        ment2 = "로딩중 입니다...\n"
    for k in ment2:
        time.sleep(0.3)
        print(k, end='')
    while (main2(money,ID,passwd, icecream_ok, roulette_ok, thief_ok) != 0):
        money, icecream_ok, roulette_ok, thief_ok = load(ID)
        time.sleep(0.7)


def main2(money, ID, passwd, icecream_ok, roulette_ok, thief_ok):
    print("================================")
    if (money >= 0):
        print("현재 ", money, "원을 보유하고 계십니다")
    elif (money < 0):
        print("현재 ", money, "원을 보유하고 계십니다\n어서 빚을 갚아봐요!")
    time.sleep(0.5)
    print("================================")
    print("1. 게임 설명듣기")
    print("2. 로또")
    print("3. 베스킨라빈스 31")
    print("4. 러시안룰렛")
    print("5. 도둑 잡기")
    print("6. 게임 구매 상점")
    print("7. 긴급 충전소")
    print("8. 나가기")
    number = input("플레이 하실 게임 혹은 기능의 번호를 선택해주세요\n")
    while (
            number != "1" and number != "2" and number != "3" and number != "4" and number != "5" and number != "6" and number != "7" and number != "8"):
        number = input("숫자를 정확하게 입력해주세요!\n")
    if (number == "1"):
        explain()
    elif (number == "2"):
        lottogame(money, ID, passwd, icecream_ok, roulette_ok, thief_ok)
    elif (number == "3"):
        if (icecream_ok == 0):
            print("게임을 구매하시지 않으셨어요! 게임을 구매 후 진행 부탁드립니다.")
            print("게임 가격은 100000원 입니다")
        else:
            icecreamgame(money, ID, passwd, icecream_ok, roulette_ok, thief_ok)
    elif (number == "4"):
        if (roulette_ok == 0):
            print("게임을 구매하시지 않으셨어요! 게임을 구매 후 진행 부탁드립니다.")
            print("게임 가격은 100000원 입니다")
        else:
            roulettegame(money, ID, passwd, icecream_ok, roulette_ok, thief_ok)
    elif (number == "5"):
        if (thief_ok == 0):
            print("게임을 구매하시지 않으셨어요! 게임을 구매 후 진행 부탁드립니다.")
            print("게임 가격은 200000원 입니다")
        else:
            Thief_catch(ID)
    elif (number == "6"):
        if (thief_ok == 1 and icecream_ok == 1 and roulette_ok == 1):
            print("구매하실 게임이 없습니다. 초기화면으로 돌아갑니다")
        else:
            store(money, ID, passwd, icecream_ok, roulette_ok, thief_ok)
    elif (number == "7"):
        bank_main(money, ID, passwd, icecream_ok, roulette_ok, thief_ok)
    elif (number == "8"):
        print("================================")
        print("게임을 종료합니다 또 만나요~")
        return 0



main()