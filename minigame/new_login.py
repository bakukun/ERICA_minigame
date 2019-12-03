def login(members):
    print("=================================================================")
    ID = input("아이디를 입력하세요\n아이디가 없다면 계정이 새로 생성됩니다(최대 8자리 제한): \n")
    while len(ID) > 9:
        ID = input("아이디의 길이가 너무 깁니다! 다시 입력해주세요\n")
    trypasswd = input("비밀번호를 입력하세요\n새로운 계정을 만드는 경우라면, 지금 입력하는 문자열이 비밀번호입니다!\n")
    if ID in members:
        passwd, money = members[ID]
        if trypasswd == passwd:
            return ID, money, passwd
        else:
            print("비밀번호가 틀립니다. 처음 화면으로 돌아갑니다\n")
            return login(members)
    else:
        members[ID] = (trypasswd,10000)
        store_members(members)
        print("새로운 계정을 생성했습니다. 새로운 계정으로 로그인 해주세요\n")
        login(load_members())


def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd ,money = members[name]
        data = name + ',' + passwd + ',' + str(money) + '\n'
        file.write(data)
    file.close()

def load_members():
    file = open("members.txt","r")
    members = {}
    for data in file:
        name, passwd, money = data.strip('\n').split(',')
        members[name] = (passwd,int(money))
    file.close()
    return members

def load(ID):
    members = load_members()
    money = members[ID][1]
    return money