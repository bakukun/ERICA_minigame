from new_login import *
class Outrange(Exception) : pass
import random
import time


def roulettegame(money, ID, passwd):
    members = load_members()
    print("============================\n")
    print("컴퓨터와 돈을 걸고 진땀나는 승부를 겨뤄보세요!")
    print("어쩌면 가장 돈을 빨리 딸 수 있는 게임이 될 것입니다!")
    print("룰은 간단합니다! 세번의 방아쇠를 자신에게 먼저 당겨 총알이 전부 가짜라면 내기 금액의 2배!")
    print("하지만, 그곳에 진짜 총알이 없다면... 내기 금액을 모두 잃습니다")
    print("총알은 총 6개이고, 진짜 총알은 단 한개 입니다")
    print("보유금액보다 더 많은 금액을 배팅할 시 게임이 거부됩니다.")
    print("게임 구매 비용은 십만원 입니다")
    print("============================\n")

    start = input("러시안 룰렛을 정말 하시겠습니까?(Y/N)\n")
    while (start != "Y" and start != "y" and start !=  "N" and  start != "n"):
        start = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
    if (start == "Y" or start == "y"):
        print("현재 ",money,"원 보유중입니다")
        bat = int(input("내기로 거실 금액을 입력해주세요 이기면 두배 지면 전부 잃음!\n"))
        if (money>=bat):
            money -= bat
            print(bat,"원이 차감되어 ",money,"원을 갖고 있습니다.")
            members[ID] = passwd, money
            store_members(members)
            roulette_main(money, ID, passwd, bat)
        else:
            print("\n당신의 보유금액으론 내기를 하지 못니다.\n도박은 가정파탄의 지름길 입니다.\n")
            print("잔고가 부족하여 게임을 종료합니다 다른 게임으로 돈을 벌고 오세요^0^")
            members[ID] = passwd, money
            store_members(members)
    elif (start == "N" or start == "n"):
        print("게임을 종료합니다")
        members[ID] = passwd, money
        store_members(members)

def roulettegame2(money, ID, passwd):
    members = load_members()
    print("현재 ", money, "원 보유중입니다")
    bat = int(input("내기로 거실 금액을 입력해주세요 이기면 두배 지면 전부 잃음!\n"))
    if (money>=bat):
        money -= bat
        print(bat,"원이 차감되어 ",money, "원을 갖고 있습니다.")
        roulette_main(money, ID, passwd, bat)
    else:
        print("\n당신의 보유금액으론 내기를 하지 못니다.\n도박은 가정파탄의 지름길 입니다.\n")
        print("잔고가 부족하여 게임을 종료합니다 다른 게임으로 돈을 벌고 오세요^0^")
        members[ID] = passwd, money
        store_members(members)

def rouletteregame(money, ID, passwd):
    members = load_members()
    restart = input("\n다시 한 번 내기를 하시겠습니까?(Y/N)\n")
    while (restart != "Y" and restart != "y" and restart !=  "N" and  restart != "n"):
        restart = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
    if (restart == "Y" or restart == "y"):
        members[ID] = passwd, money
        store_members(members)
        roulettegame2(money, ID, passwd)
    elif (restart == "N" or restart == "n"):
        members[ID] = passwd, money
        store_members(members)
        print("게임을 종료합니다")


def roulette_main(money, ID, passwd, bat):
    members = load_members()
    bullet = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]]
    cnt = 0
    win_bat = bat * 2
    real_bullet = bullet[random.randrange(0, 6)]
    print("=============================================================")
    print("딜러: 당신은 ",bat,"원을 거셨구만... 나와 러시안룰렛 한 번 하지 않겠는가?")
    ment = "...\n"
    for i in ment:
        time.sleep(0.8)
        print(i, end='')
    print("당신부터 총알을 고르도록 하세요...")
    while(real_bullet.count(1)!= 0):
        while (True): #입력 예외처리
            try :
                index = int(input(("몇 번째 총알을 뽑겠습니까? 총알을 뽑을 때 마다 순서가 앞당겨 집니다!(1 ~ {:}번째 총알 선택가능) : \n".format(len(real_bullet)))))
                if (index < 1 or index > len(real_bullet)) :
                    raise Outrange
            except ValueError:
                print("자연수를 입력해주세요.")
            except Outrange :
                print("범위를 벗어났습니다. 다시 골라주세요.")
            else :
                break?
        print("현재 ",index,"번째 총알을 골랐습니다. 당겨볼까요..?")
        time.sleep(0.5)
        print("장전완료")
        time.sleep(0.5)
        print("3")
        time.sleep(0.5)
        print("2")
        time.sleep(0.5)
        print("1")
        if(real_bullet[index-1] == 1):
            print("빵!... 당신은 죽었습니다 내기금액을 모두 잃습니다")
            break
        else:
            print("후.. 빈 총알이군요")
            cnt += 1
            del real_bullet[index-1]
            if (cnt == 3):
                print("축하합니다 당신은 고난을 모두 견뎌냈어요")
                print("상금 ", win_bat,"원을 드립니다")
                money += win_bat
                break
            else:
                print("한번 더 뽑으세요!")

    members[ID] = passwd, money
    store_members(members)
    rouletteregame(money, ID, passwd)