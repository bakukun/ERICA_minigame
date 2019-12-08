from new_login import *
import time


def store(money, ID, passwd, icecream_ok, roulette_ok, theif_ok):
    members = load_members()
    print(ID, "님 상점에 오신걸 환영합니다. 현재 구매하실 수 있는 게임은 다음과 같습니다")
    time.sleep(0.5)
    print("=============================================================")
    if (icecream_ok == 0):
        print("베스킨라빈스 31")
    if (roulette_ok == 0):
        print("러시안 룰렛")
    if (theif_ok == 0):
        print("도둑잡기")
    if (theif_ok == 1 and icecream_ok == 1 and roulette_ok == 1):
        print("구매하실 게임이 없습니다. 초기화면으로 돌아갑니다")
    print("=============================================================")
    time.sleep(1)
    print("어느 게임을 구매하시겠습니까?")
    print("1. 베스킨라빈스 31 구매하기")
    print("2. 러시안 룰렛 구매하기")
    print("3. 도둑잡기 구매하기\n")
    print("4. 나가기")
    ask = input("구매하실 게임 설명의 번호를 선택해주세요 (1~4)\n")
    while (ask != "1" and ask != "2" and ask != "3" and ask != "4"):
        ask = input("숫자 정확하게 입력해주세요!\n")
    if (ask == "1"):
        print("================================")
        if (icecream_ok == 1):
            if (roulette_ok == 1 and theif_ok == 1):
                print("이미 구매하신 게임입니다. 구매할 게임이 없으시므로 초기 화면으로 돌아갑니다")
            else:
                print("이미 구매하신 게임입니다.")
                request(money, ID, passwd, icecream_ok, roulette_ok, theif_ok)
        elif (icecream_oak == 0):
            ask2 = input("술게임의 원조 베스킨라빈스 31을 구매하시겠습니까? 가격은 10만원 입니다(Y/N)\n")
            while (ask2 != "Y" and ask2 != "y" and ask2 != "N" and ask2 != "n"):
                ask2 = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
            if (money >= 100000):
                money -= 100000
                new_ice(ID, icecream_ok)
                print("게임 구매가 완료되었습니다 즐겁게 플레이해주세요!")
                request(money, ID, passwd, icecream_ok, roulette_ok, theif_ok)
            else:
                print("돈이 부족하여 게임 구매가 거절되었습니다. 초기화면으로 돌아갑니다")
    elif (ask == "2"):
        print("================================")
        if (roulette_ok == 1):
            if (icecream_ok == 1 and theif_ok == 1):
                print("이미 구매하신 게임입니다. 구매할 게임이 없으시므로 초기 화면으로 돌아갑니다")
            else:
                print("이미 구매하신 게임입니다.")
                request(money, ID, passwd, icecream_ok, roulette_ok, theif_ok)
        elif (roulette_ok == 0):
            ask2 = input("실감나는 도박 러시안룰렛을 구매하시겠습니까? 가격은 10만원 입니다(Y/N)\n")
            while (ask2 != "Y" and ask2 != "y" and ask2 != "N" and ask2 != "n"):
                ask2 = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
            if (money >= 100000):
                money -= 100000
                new_roulette(ID, roulette_ok)
                print("게임 구매가 완료되었습니다 즐겁게 플레이해주세요!")
                request(money, ID, passwd, icecream_ok, roulette_ok, theif_ok)
            else:
                print("돈이 부족하여 게임 구매가 거절되었습니다. 초기화면으로 돌아갑니다")
    elif (ask == "3"):
        print("================================")
        if (theif_ok == 1):
            if (roulette_ok == 1 and ice_ok == 1):
                print("이미 구매하신 게임입니다. 구매할 게임이 없으시므로 초기 화면으로 돌아갑니다")
            else:
                print("이미 구매하신 게임입니다.")
                request(money, ID, passwd, icecream_ok, roulette_ok, theif_ok)
        elif (theif_ok == 0):
            ask2 = input("4명이서 하는 도둑잡기! 구매하시겠습니까? 가격은 20만원 입니다(Y/N)\n")
            while (ask2 != "Y" and ask2 != "y" and ask2 != "N" and ask2 != "n"):
                ask2 = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
            if (money >= 200000):
                money -= 200000
                new_theif(ID, theif_ok)
                print("게임 구매가 완료되었습니다 즐겁게 플레이해주세요!")
                request(money, ID, passwd, icecream_ok, roulette_ok, theif_ok)
            else:
                print("돈이 부족하여 게임 구매가 거절되었습니다. 초기화면으로 돌아갑니다")
    elif (ask == "4"):
        print("초기화면으로 돌아갑니다")
    members[ID] = passwd, money, icecream_ok, roulette_ok, theif_ok
    store_members(members)


def request(money, ID, passwd, icecream_ok, roulette_ok, theif_ok):
    members = load_members()
    restart = input("다른 게임도 구매하시겠습니까?(Y/N)\n")
    while (restart != "Y" and restart != "y" and restart != "N" and restart != "n"):
        restart = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
    if (restart == "Y" or restart == "y"):
        print("구매화면으로 돌아갑니다!\n")
        time.sleep(0.5)
        store(money, ID, passwd, icecream_ok, roulette_ok, theif_ok)
    elif (restart == "N" or restart == "n"):
        print("초기화면으로 돌아갑니다")
        members[ID] = passwd, money, icecream_ok, roulette_ok, theif_ok
        store_members(members)