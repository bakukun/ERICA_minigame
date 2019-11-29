def explain():
    print("================================")
    print("1. 본 게임 설명")
    print("2. 미니게임 종류와 설명")
    print("3. 한눈에 보는 게임 가격표")
    print("4. 나가기")
    number = input("번호를 선택해주세요\n")
    while (number != "1" and number != "2" and number != "3" and number != "4"):
        number = input("숫자 정확하게 입력해주세요!\n")
    if (number == "1"):
        print("안녕하세요! 에리카 오픈소스기초 수업을 위해 만들어본 미니게임입니다.")
        print("개발 언어는 파이썬이고, 게임 속의 다양한 기능들을 구현했습니다")
        print("로그인 시스템 구현, 화폐시스템 구현 및 게임 해금 기능 구현, 이외 다양한 미니게임 구현")
        print("본 프로젝트의 아이디어는 옛 피처폰 시절의 게임인 미니게임 천국에서 따왔습니다")
        print("즐겁게 플레이해주세요!")
        request()
    elif (number == "2"):
        print("================================")
        print("1. 로또")
        print("2. 다함께 암산왕")
        print("3. 러시안 룰렛")
        print("4. 베스킨라빈스31 내기")
        print("5. 도둑잡기")
        number2 = input("궁금하신 게임 설명의 번호를 선택해주세요\n")
        while (number2 != "1" and number2 != "2" and number2 != "3" and number2 != "4" and number2 != "5"):
            number2 = input("숫자 정확하게 입력해주세요!\n")
        if (number2 == "1"):
            print("================================")
            lotto_explain()
            request()
        elif (number2 == "2"):
            print("================================")
            math_explain()
            request()
        elif (number2 == "3"):
            print("================================")
            roulette_explain()
            request()
        elif (number2 == "4"):
            print("================================")
            icecream_explain()
            request()
        elif (number2 == "5"):
            print("================================")
            theif_explain()
            request()
    elif (number == "3"):
        print("================================")
        print("로또 무료")
        print("다함께 암산왕 : 5만원")
        print("러시안 룰렛: 10만원")
        print("베스킨 라빈스31: 10만원")
        print("도둑잡기 : 20만원")
        print("================================")
        request()
    elif (number == "4"):
        print("초기화면으로 돌아갑니다")


def request():
    restart = input("\n다시 한 번 설명을 들으시겠습니까?(Y/N)\n")
    while (restart != "Y" and restart != "y" and restart != "N" and restart != "n"):
        restart = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
    if (restart == "Y" or restart == "y"):
        print("설명화면으로 돌아갑니다!")
        explain()
    elif (restart == "N" or restart == "n"):
        print("초기화면으로 돌아갑니다")


def lotto_explain():
    print("통상적인 로또와 사뭇 다른 OPENSW 미니게임만의 로또입니다")
    print("당첨 금액표는 다음과 같습니다")
    print("============당첨금============")
    print("1등 (숫자 6개 같을 경우) : 21억원")
    print("2등 (숫자 5개 같을 경우) : 1억원")
    print("3등 (숫자 4개 같을 경우) : 백만원")
    print("4등 (숫자 3개 같을 경우) : 만원")
    print("5등 (숫자 2개 같을 경우) : 천원")
    print("============================")
    print("게임 해금 여부 상관 없이 이용 가능합니다.")

def math_explain():
    print("간단한 사칙연산을 바탕으로 빠른시간안에 정확하게 주어진 20문제를 풀어야 하는 게임입니다!")
    print("난이도는 하 / 상 이 있으며, 난이도 구분은 연산 기호로 나눠집니다")
    print("하 난이도는 덧셈과 뺄셈만 출현, 상 난이도는 덧셈 뺄셈 곱셈 나눗셈 전부 출현")
    print("연속해서 문제를 틀리지 않고 정확히 맞추면 더 많은 돈을 획득 할 수 있습니다!")
    print("게임이 시작하고 나서 주어진 시간안에 문제를 빠르게 푼다면 더 많은 돈을 획득 할 수 있습니다!")
    print("게임 구매 비용은 오만원 입니다")

def roulette_explain():
    print("컴퓨터와 돈을 걸고 진땀나는 승부를 겨뤄보세요!")
    print("어쩌면 가장 돈을 빨리 딸 수 있는 게임이 될 것입니다!")
    print("룰은 간단합니다! 방아쇠를 당겨 총알이 상대방을 쏘면 내기 금액의 2배!")
    print("하지만, 상대가 당신에게 총알을 쏜다면 내기 금액을 모두 잃습니다")
    print("총알은 총 6개이고, 진짜 총알은 단 한개 입니다")
    print("게임 구매 비용은 십만원 입니다")

def icecream_explain():
    print("귀엽고! 깜찍하게!! 베스킨라빈스 31게임을 컴퓨터와 즐겨보세요")
    print("과연 컴퓨터를 이길 수 있을까요?")
    print("1부터 31까지의 숫자를 연속으로 1개~3개 언급하면 됩니다")
    print("상대방과 숫자를 주고받으며 31을 어떻게든 외치게 된 플레이어는 패배하게 됩니다")
    print("머리를 써보세요~")
    print("게임 구매금액은 십만원 입니다.")

def theif_explain():
    print("카드게임입니다~ 문양과 상관없이 같은 숫자로 된 카드 2장을 내려놓습니다")
    print("상대방의 카드를 번갈아 뽑다보면 숫자 / JKQ 카드는 전부 내려놓게 됩니다")
    print("다만 조커 카드를 가지고 있다면 이야기가 달라집니다. 조커카드를 마지막 까지 갖고있다면 패배하게 됩니다")
    print("플레이어 수는 무려 4명입니다! 유일하게 돈을 걸지 않는 게임이네요 ㅎㅎ")
    print("게임 구매금액은 이십만원 입니다")
