from new_login import *
from lotto import *
from explain import *
import time

def main():
    ID, money, passwd = login(load_members())
    print(ID, "님 안녕하세요!")
    ment = "ERCIA OPEN_SW 미니게임입니다\n"
    for i in ment:
        time.sleep(0.1)
        print(i, end='')
    ment2 = "로딩중 입니다...\n"
    for k in ment2:
        time.sleep(0.3)
        print(k, end='')
    while (main2(money, ID, passwd) != 0):
        members = load_members() #여기서 money를 새로운 값으로 갱신해야 할텐데 모르겠음


def main2(money, ID, passwd):
    if (money >= 0):
        print("현재 ", money, "원을 보유하고 계십니다")
    elif (money < 0):
        print("현재 ", money, "원을 보유하고 계십니다\n어서 빚을 갚아봐요!")
    time.sleep(0.5)
    print("================================")
    print("1. 게임 설명듣기")
    print("2. 로또")
    print("3. 러시안룰렛")
    print("4. 다함께 암산왕")
    print("5. 도둑 잡기")
    print("6. 베스킨라빈스 31")
    print("7. 나가기")
    number = input("플레이 하실 게임의 번호를 선택해주세요\n")
    while (number != "1" and number != "2" and number != "3" and number != "4" and number != "5" and number != "6" and number != "7"):
        number = input("숫자를 정확하게 입력해주세요!\n")
    if (number == "1"):
        explain()
    elif (number == "2"):
        lottogame(money, ID, passwd)
    elif (number == "3"):
        print("================================")
    elif (number == "4"):
        print("================================")
    elif (number == "5"):
        print("================================")
    elif (number == "6"):
        print("================================")
    elif (number == "7"):
        print("================================")
        print("게임을 종료합니다 또 만나요~")
        return 0




main()