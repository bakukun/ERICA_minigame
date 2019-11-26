from main import *


def explain():
    print("================================")
    print("1. 게임 종류")
    print("2. 게임 방법")
    print("3. 게임 가격")
    print("4. 나가기")
    number = input("번호를 선택해주세요\n")
    while (number != "1" and number != "2" and number != "3" and number != "4"):
        number = input("숫자 정확하게 입력해주세요!\n")
    if (number == "1"):
        print("================================")
        print("1. 로또")
        print("2. 다함께 암산왕")
        print("3. 러시안 룰렛")
        print("4. 베스킨라빈스31 내기")
        number1 = input("궁금하신 게임의 번호를 선택해주세요")
        while (number1 != "1" and number1 != "2" and number1 != "3" and number1 != "4"):
            number1 = input("숫자 정확하게 입력해주세요!\n")
        if (number1 == "1"):
            lotto_explain()
            request()
        elif (number1 == "2"):
            math_explain()
            request()
        elif (number1 == "3"):
            roulette_explain()
            request()
        elif (number1 == "4"):
            icecream_explain()
            request()
    elif (number == "2"):
        print("================================")
        request()
    elif (number == "3"):
        print("================================")
        request()
    elif (number == "4"):
        print("================================")
        request()


def request():
    restart = input("\n다시 한 번 설명을 들으시겠습니까?(Y/N)")
    while (restart != "Y" and restart != "y" and restart != "N" and restart != "n"):
        restart = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
    if (restart == "Y" or restart == "y"):
        print("설명화면으로 돌아갑니다!")
        explain()
    elif (restart == "N" or restart == "n"):
        print("초기화면으로 돌아갑니다")
        main2()


def lotto_explain():
    print("미정")


def math_explain():
    print("미정2")


def roulette_explain():
    print("미정3")


def icecream_explain():
    print("미정")
