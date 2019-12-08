def login(members):
    print("=================================================================")
    ID = input("아이디를 입력하세요(한글 or 영어 or 숫자만 가능합니다)\n영어는 대소문자를 구분합니다.\n"
               "아이디가 없다면 계정이 새로 생성됩니다(최대 8자리 제한): \n")
    while (len(ID) > 9 or len(ID) < 1 or not(ID.isalnum())):
        ID = input("아이디의 형식이 적절하지 않습니다! 다시 입력해주세요\n")
    trypasswd = input("비밀번호를 입력하세요(한글 or 영어 or 숫자만 가능합니다)\n영어는 대소문자를 구분합니다.\n새로운 계정을 만드는 경우라면, 지금 입력하는 문자열이 비밀번호입니다!\n")
    while (not(trypasswd.isalnum())):
        trypasswd = input("비밀번호에 적절하지 않은 문자열이 포함 되어있습니다! 다시 입력해주세요\n")
    if ID in members:
        passwd, money, icecream_ok, roulette_ok, thief_ok = members[ID]
        if trypasswd == passwd:
            return ID, money, passwd, icecream_ok, roulette_ok, thief_ok
        else:
            print("비밀번호가 틀립니다. 처음 화면으로 돌아갑니다\n")
            return login(members)
    else:
        members[ID] = (trypasswd,100000,0,0,0)
        store_members(members)
        print("새로운 계정을 생성했습니다.\n새로운 계정으로 로그인 해주세요")
        login(load_members())


def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd ,money, icecream_ok, roulette_ok, thief_ok = members[name]
        data = name + ',' + passwd + ',' + str(money) + ',' + str(icecream_ok) + ',' + str(roulette_ok) + ',' + str(thief_ok) + '\n'
        file.write(data)
    file.close()

def load_members():
    file = open("members.txt","r")
    members = {}
    for data in file:
        name, passwd, money, icecream_ok, roulette_ok, thief_ok = data.strip('\n').split(',')
        members[name] = [passwd,int(money), int(icecream_ok), int(roulette_ok), int(thief_ok)]
    file.close()
    return members

def load(ID):
    members = load_members()
    money = members[ID][1]
    icecream_ok = members[ID][2]
    roulette_ok = members[ID][3]
    thief_ok = members[ID][4]
    return money,icecream_ok,roulette_ok,thief_ok

def new_ice(ID,icecream_ok):
    members = load_members()
    icecream_ok = members[ID][2]
    icecream_ok = 1
    return icecream_ok

def new_roulette(ID):
    members = load_members()
    roulette_ok = members[ID][3]
    roulette_ok = 1
    return roulette_ok

def new_thief(ID):
    members = load_members()
    thief_ok = members[ID][4]
    thief_ok = 1
    return thief_ok