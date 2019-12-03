from new_login import *
import random,time

def icecreamgame(money, ID, passwd):
    members = load_members()
    print("============================\n")
    print("귀엽고! 깜찍하게!! 베스킨라빈스 31게임을 컴퓨터와 즐겨보세요")
    print("과연 컴퓨터를 이길 수 있을까요?")
    print("1부터 31까지의 숫자를 연속으로 1개~3개 언급하면 됩니다")
    print("상대방과 숫자를 주고받으며 31을 어떻게든 외치게 된 플레이어는 패배하게 됩니다")
    print("이것도 러시안룰렛과 같이 배팅 게임입니다. 이기면 배팅금액의 반을 얻고, 지면 배팅금액의 반을 잃습니다")
    print("반액의 소수점 부분은 버림 됩니다 참고하세요")
    print("게임 구매금액은 십만원 입니다.")
    print("============================\n")

    start = input("베스킨라빈스 31을 정말 하시겠습니까?(Y/N)\n")
    while (start != "Y" and start != "y" and start !=  "N" and  start != "n"):
        start = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
    if (start == "Y" or start == "y"):
        print("현재 ",money,"원 보유중입니다")
        while (True):  # 입력 예외처리
            try:
                bat = int(input("내기로 거실 금액을 입력해주세요 이기면 반액 얻고 지면 반액 잃음!\n"))
            except ValueError:
                print("자연수를 입력해주세요.")
            else :
                break
        real_bat = round(bat/2)
        if (money>=bat):
            money -= real_bat
            print("내기 금액의 반인",real_bat,"원이 차감되어 ",money,"원을 갖고 있습니다.")
            members[ID] = passwd, money
            store_members(members)
            icecream_main(money, ID, passwd, real_bat)
        else:
            print("\n당신의 보유금액으론 내기를 하지 못니다.\n도박은 가정파탄의 지름길 입니다.\n")
            print("배팅금액에 비해 정해진 기준의 잔고가 부족하여 게임을 종료합니다 다른 게임으로 돈을 벌고 오세요^0^")
            members[ID] = passwd, money
            store_members(members)
    elif (start == "N" or start == "n"):
        print("게임을 종료합니다")
        members[ID] = passwd, money
        store_members(members)

def icecreamgame2(money, ID, passwd):
    members = load_members()
    print("현재 ", money, "원 보유중입니다")
    while (True):  # 입력 예외처리
        try:
            bat = int(input("내기로 거실 금액을 입력해주세요 이기면 반액 얻구 지면 반액 잃음!\n"))
        except ValueError:
            print("자연수를 입력해주세요.")
        else:
            break
    real_bat = round(bat / 2)
    if (money>=bat):
        money -= real_bat
        print("내기 금액의 반인",real_bat,"이 차감되어 ",money, "원을 갖고 있습니다.")
        roulette_main(money, ID, passwd, bat)
    else:
        print("\n당신의 보유금액으론 내기를 하지 못니다.\n도박은 가정파탄의 지름길 입니다.\n")
        print("배팅금액에 비해 정해진 기준의 잔고가 부족하여 게임을 종료합니다 다른 게임으로 돈을 벌고 오세요^0^")
        members[ID] = passwd, money
        store_members(members)

def icecreamregame(money, ID, passwd):
    members = load_members()
    restart = input("\n다시 한 번 내기를 하시겠습니까?(Y/N)\n")
    while (restart != "Y" and restart != "y" and restart !=  "N" and  restart != "n"):
        restart = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
    if (restart == "Y" or restart == "y"):
        members[ID] = passwd, money
        store_members(members)
        icecreamgame2(money, ID, passwd)
    elif (restart == "N" or restart == "n"):
        members[ID] = passwd, money
        store_members(members)
        print("게임을 종료합니다")

def icecream_main(money, ID, passwd,real_bat):
    members = load_members()
    ment = "베스킨라빈스 31~~~\n"
    for k in ment:
        time.sleep(0.3)
        print(k, end='')
    print("게임을 시작합니다")
    while True:
        order = input("먼저 하시려면 1, 나중에 하시려면 0을 입력해주세요\n")
        if order in ['0', '1']:
            order = int(order)
            break
        else:
            print("잘못된 입력입니다. 재입력해주세요.\n")
    call = 0
    count = 1
    while call < 31:
        if count % 2 == order:
            print('사용자의 차례')
            while True:
                size_of_call = input("말할 숫자의 개수를 입력하세요 (1~3개) :\n")
                if size_of_call in ['1', '2', '3']:
                    size_of_call = int(size_of_call)
                    break
                else:
                    print("잘못된 입력입니다. 재입력해주세요.\n")
            for _ in range(size_of_call):
                call += 1
                print("사용자 : '{0}'!!!".format(call))
                if call == 31:
                    break
        else:
            # 컴퓨터의 차례
            print('컴퓨터의 차례')
            size_of_call = random.randint(1, 3)
            for _ in range(size_of_call):
                call += 1
                print("컴퓨터 : '{0}'!!!".format(call))
                if call == 31:
                    break

        count += 1
    if count % 2 == order:
        print(ID,"의 승리!!")
        money += (real_bat *2)
        print("상금 ",real_bat,"원을 얻어 현재",money,"원 보유중입니다")
    else:
        print("컴퓨터의 승리!!")
        print("현재 ",money,"원 보유중입니다")
    members[ID] = passwd, money
    store_members(members)
    icecreamregame(money, ID, passwd)