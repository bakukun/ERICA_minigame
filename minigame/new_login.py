def login(members):
    print("=================================================================")
    ID = input("아이디를 입력하세요(영어만 가능합니다)\n아이디가 없다면 계정이 새로 생성됩니다(최대 8자리 제한): \n")
    while (len(ID) > 9 or len(ID) < 1 or ID.count(" ")>0):
        ID = input("아이디의 형식이 적절하지 않습니다! 다시 입력해주세요\n")
    trypasswd = input("비밀번호를 입력하세요\n새로운 계정을 만드는 경우라면, 지금 입력하는 문자열이 비밀번호입니다!\n")
    if ID in members:
        passwd, money, icecream_ok, roulette_ok, theif_ok = members[ID]
        if trypasswd == passwd:
            return ID, money, passwd, icecream_ok, roulette_ok, theif_ok
        else:
            print("비밀번호가 틀립니다. 처음 화면으로 돌아갑니다\n")
            return login(members)
    else:
        members[ID] = (trypasswd,10000,0,0,0)
        store_members(members)
        print("새로운 계정을 생성했습니다. 새로운 계정으로 로그인 해주세요\n")
        login(load_members())


def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd ,money, icecream_ok, roulette_ok, theif_ok = members[name]
        data = name + ',' + passwd + ',' + str(money) + ',' + str(icecream_ok) + ',' + str(roulette_ok) + ',' + str(theif_ok) + '\n'
        file.write(data)
    file.close()

def load_members():
    file = open("members.txt","r")
    members = {}
    for data in file:
        name, passwd, money, icecream_ok, roulette_ok, theif_ok = data.strip('\n').split(',')
        members[name] = [passwd,int(money), int(icecream_ok), int(roulette_ok), int(theif_ok)]
    file.close()
    return members

def load(ID):
    members = load_members()
    money = members[ID][1]
    icecream_ok = members[ID][2]
    roulette_ok = members[ID][3]
    theif_ok = members[ID][4]
    return money,icecream_ok,roulette_ok,theif_ok

def new_ice(ID,icecream_ok):
    members = load_members()
    members[ID][2] = 1
    members[ID] = passwd, money, icecream_ok, roulette_ok, theif_ok
    store_members()

def new_roulette(ID,roulette_ok):
    members = load_members()
    members[ID][3] = 1
    members[ID] = passwd, money, icecream_ok, roulette_ok, theif_ok
    store_members()

def new_theif(ID, theif_ok):
    members = load_members()
    members[ID][4] = 1
    members[ID] = passwd, money, icecream_ok, roulette_ok, theif_ok
    store_members()