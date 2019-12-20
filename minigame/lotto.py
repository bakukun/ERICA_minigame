from new_login import *
import random
import time

def lotto_main(money, ID, passwd, icecream_ok, roulette_ok, thief_ok):
    members = load_members()
    cnt = 0
    a = [] #print용도
    real = [] #비교할 용도
    player = [] #플레이어의 번호(출력용)
    player_real =  [] #플레이어의 번호(비교용)

    for _ in range(6): #나와 컴퓨터의 원소 배정
        a.append(random.randrange(1,46))
        player.append(random.randrange(1,46))
    a.sort()
    player.sort()

    while not a[0] != a[1] != a[2] != a[3] != a[4] != a[5]:
        a = []
        for _ in range(6):
            a.append(random.randrange(1, 46))
        a.sort()

    while not player[0] != player[1] != player[2] != player[3] != player[4] != player[5]:
        player = []
        for _ in range(6):
            player.append(random.randrange(1, 46))
        player.sort()

    for i in range(6): #비교용 추가
        real.append(a[i])
        player_real.append(player[i])


    for i in range(6): #출력용 조정
        if 1<= a[i] <=9:
            a[i] = "0"+str(a[i])
        if 1<= player[i] <= 9:
            player[i] = "0"+str(player[i])

    print("당신의 번호 : ", end="")
    for i in range(6):
        print(player[i], end=" ")
    print("\n")
    ment = "로또 번호 추첨 중입니다 잠시만 기다려주세요\n"
    for i in ment:
        time.sleep(0.1)
        print(i, end='')
    print("당첨 번호 : ", end="")



    for index, value in enumerate(a):
            print(value, end=' ')
    print("\n")
    for i in range(6):
        cnt += player_real.count(real[i])
    print("숫자",cnt,"개를 맞으셨네요!")

    if (cnt==6):
        money += 2100000000
        print("와 이런 미니게임에서 숫자 6개가 나오다니......\n현실로또 꼭 사세요")
        print("21억원이 추가되어 현재 보유금액은", money, "원 입니다")
    elif (cnt == 5):
        money += 100000000
        print("와 이런 미니게임에서 숫자 5개가 나오다니......\n현실로또 꼭 사세요")
        print("1억원이 추가되어 현재 보유금액은", money, "원 입니다")
    elif (cnt == 4):
        money += 1000000
        print("와 이런 미니게임에서 숫자 4개가 나오다니......\n현실로또 꼭 사세요")
        print("백만원이 추가되어 현재 보유금액은", money, "원 입니다")
    elif (cnt == 3):
        money += 30000
        print("오 현실로또에선 5000원이지만......\n여기서는 3만원입니다^^*")
        print("만원이 추가되어 현재 보유금액은", money, "원 입니다")
    elif (cnt == 2):
        money += 5000
        print("오 현실로또에선 이지만......\n여기서는 5000원입니다^^*")
        print("만원이 추가되어 현재 보유금액은", money, "원 입니다")
    elif (cnt == 1):
        money += 1000
        print("오 현실로또에선 꽝이지만......\n여기서는 천원입니다^^* 본전 개이득")
        print("천원이 추가되어 현재 보유금액은", money, "원 입니다")
    else:
        print("꽝이네요....... \n그럴 수 있어요(토닥토닥)")
        print("현재 보유금액은", money, "원 입니다꽝")
    print("===============================================")
    members[ID] = passwd, money, icecream_ok, roulette_ok, thief_ok
    store_members(members)
    lottoregame(money, ID, passwd, icecream_ok, roulette_ok, thief_ok)

def lottoregame(money, ID, passwd, icecream_ok, roulette_ok, thief_ok):
    members = load_members()
    restart = input("\n다시 한 번 로또를 구매하시겠습니까?(Y/N)\n")
    while (restart != "Y" and restart != "y" and restart !=  "N" and  restart != "n"):
        restart = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
    if (restart == "Y" or restart == "y"):
        members[ID] = passwd, money, icecream_ok, roulette_ok, thief_ok
        store_members(members)
        lottogame2(money, ID, passwd, icecream_ok, roulette_ok, thief_ok)
    elif (restart == "N" or restart == "n"):
        members[ID] = passwd, money, icecream_ok, roulette_ok, thief_ok
        store_members(members)
        print("게임을 종료합니다")



def lottogame(money, ID, passwd, icecream_ok, roulette_ok, thief_ok):
    members = load_members()
    print("============================\n")
    print("일확천금 운빨겜 로또를 하러 오신걸 환영합니다!\n한 장에 천원입니다\n통상적인 로또와 사뭇 다릅니다\n")
    print(ID, "님은 ", money, "원을 가지고 있어요")
    print("============당첨금============")
    print("1등 (숫자 6개 같을 경우) : 21억원")
    print("2등 (숫자 5개 같을 경우) : 1억원")
    print("3등 (숫자 4개 같을 경우) : 백만원")
    print("4등 (숫자 3개 같을 경우) : 만원")
    print("5등 (숫자 2개 같을 경우) : 오천원")
    print("6등 (숫자 1개 같을 경우) : 천원")
    print("============================\n")

    start = input("로또를 구매하시겠습니까?(Y/N)\n")
    while (start != "Y" and start != "y" and start != "N" and start != "n"):
        start = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
    if (start == "Y" or start == "y"):
        if (money >= 1000):
            money -= 1000
            print("천원이 차감되어 ", money, "원을 갖고 있습니다.")
            members[ID] = passwd, money, icecream_ok, roulette_ok, thief_ok
            store_members(members)
            lotto_main(money, ID, passwd, icecream_ok, roulette_ok, thief_ok)
        else:
            print("당신의 돈으론 로또를 사지 못합니다.\n도박은 가정파탄의 지름길 입니다.\n정말 빚을 내어 구매하시겠습니까?")
            start2 = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
            while (start2 != "Y" and start2 != "y" and start2 != "N" and start2 != "n"):
                start2 = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
            if (start2 == "Y" or start2 == "y"):
                money -= 1000
                print("천원이 차감되어 ", abs(money), "원의 빚을 갖고 있습니다.")
                members[ID] = passwd, money, icecream_ok, roulette_ok, thief_ok
                store_members(members)
                lotto_main(money, ID, passwd, icecream_ok, roulette_ok, thief_ok)
            elif (start2 == "N" or start2 == "n"):
                print("게임을 종료합니다")
                members[ID] = passwd, money , icecream_ok, roulette_ok, thief_ok
                store_members(members)
    elif (start == "N" or start == "n"):
        print("게임을 종료합니다")
        members[ID] = passwd, money , icecream_ok, roulette_ok, thief_ok
        store_members(members)

def lottogame2(money, ID, passwd, icecream_ok, roulette_ok, thief_ok):
    members = load_members()
    if (money>=1000):
        money -= 1000
        print("천원이 차감되어 ",money, "원을 갖고 있습니다.")
        lotto_main(money, ID, passwd, icecream_ok, roulette_ok, thief_ok)
    else:
        print("당신의 돈으론 로또를 사지 못합니다.\n도박은 가정파탄의 지름길 입니다.\n정말 빚을 내어 구매하시겠습니까?")
        start2 = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
        while (start2 != "Y" and start2 != "y" and start2 != "N" and start2 != "n"):
            start2 = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
        if (start2 == "Y" or start2 == "y"):
            money -= 1000
            print("천원이 차감되어 ", abs(money), "원의 빚을 갖고 있습니다.")
            members[ID] = passwd, money, icecream_ok, roulette_ok, thief_ok
            store_members(members)
            lotto_main(money, ID, passwd, icecream_ok, roulette_ok, thief_ok)
        elif (start2 == "N" or start2 == "n"):
            print("게임을 종료합니다")
            members[ID] = passwd, money, icecream_ok, roulette_ok, thief_ok
            store_members(members)

