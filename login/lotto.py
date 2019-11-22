import random
import time

def lotto_main():
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
    print(cnt)

def lottogame():
    start = input("일확천금 운빨겜 로또를 하러 오신걸 환영합니다!\n 로또를 구매하시겠습니까?(Y/N)")
    while (start != "Y" and start != "y" and start !=  "N" and  start != "n"):
        start = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
    if (start == "Y" or start == "y"):
        lotto_main()
    elif (start == "N" or start == "n"):
        print("게임을 종료합니다")


lottogame()