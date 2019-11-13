import math,random,time

def login(members):
    ID = input("아이디를 입력하세요\n아이디가 없다면 계정이 새로 생성됩니다(최대 8자리 제한):\n")
    while (len(ID) == 0):
        ID = input("아이디는 공백이 될 수 없습니다 ! 다시 입력해주세요\n")
    else:
        while len(ID) > 9:
            ID = input("아이디의 길이가 너무 깁니다! 다시 입력해주세요\n")
        trypasswd = input("비밀번호를 입력하세요\n새로운 계정을 만드는 경우라면, 지금 입력하는 문자열이 비밀번호입니다!\n")
        if ID in members:
            passwd, money = members[ID]
            if trypasswd == passwd:
                if money >=0:
                    print('당신은', money ,'원을 보유하고 있군요!')
                elif money < 0:
                    print('당신은', abs(money) ,'원의 빚이 있어요 ㅠㅠ')
                return ID, money, members
            else:
                print("비밀번호가 다릅니다 다시 시도해주세요")
                return login(members)
        else:
            members[ID] = (trypasswd,0)# ID을 members 사전에 추가한다.
            return ID, 0, members


def load_members():
    file = open("members.txt","r")
    members = {}
    for data in file:
        name, passwd, money = data.strip('\n').split(',')
        members[name] = (passwd,int(money))
    file.close()
    return members

def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd,money = members[name]
        data = name + ',' + passwd + ',' + str(money) + '\n'
        file.write(data)
    file.close()

ID, money, members = login(load_members())

