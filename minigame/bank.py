from new_login import *
import time


def bank_main(money, ID, passwd, icecream_ok, roulette_ok, thief_ok):
    members = load_members()

    print("되돌릴 수 없는 빚을 진 여러분들을 위한 긴급충전소입니다.\n보유금액이 10000원 이하인 경우 빚을 탕감해줍니다")
    time.sleep(1)
    if (money > 10000):
        print("구제 대상이 아닙니다. 초기 화면으로 돌아갑니다")
    else:
        money = 10000
        print("구제 대상에 포함됩니다!")
        time.sleep(1)
        print("빚 청산과 함께", money, "원을 추가로 충전해 드렸습니다.")
        print("도박은 가정파탄의 지름길 입니다. 착하게 사세용")
        time.sleep(0.2)
    members[ID] = passwd, money, icecream_ok, roulette_ok, thief_ok
    store_members(members)
