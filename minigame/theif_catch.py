import random, time
class Outrange(Exception) : pass


def create_deck() :
    cards = [2,3,4,5,6,7,8,9,10,'A','J','Q','K']
    random.shuffle(cards)
    return cards

def give_card(deck) :
    if (deck == []) :
        deck = create_deck()
        random.shuffle(deck)
    return deck[0], deck[1:]

def deck() :
    deck = create_deck()
    player_deck = []
    computer1_deck = []
    computer2_deck = []
    computer3_deck = []
    for i in range(0, 13) :
        card, deck = give_card(deck)
        if card in player_deck :
            player_deck.remove(card)
        else :
            player_deck.append(card)
        card, deck = give_card(deck)
        if card in computer1_deck :
            computer1_deck.remove(card)
        else :
            computer1_deck.append(card)
        card, deck = give_card(deck)
        if card in computer2_deck:
            computer2_deck.remove(card)
        else:
            computer2_deck.append(card)
        card, deck = give_card(deck)
        if card in computer3_deck:
            computer3_deck.remove(card)
        else:
            computer3_deck.append(card)
    num = random.randint(0,3)
    if (num == 0) :
        player_deck.append("JOKER")
    elif (num == 1) :
        computer1_deck.append("JOKER")
    elif (num == 2) :
        computer2_deck.append("JOKER")
    else :
        computer3_deck.append("JOKER")
    random.shuffle(player_deck)
    random.shuffle(computer1_deck)
    random.shuffle(computer2_deck)
    random.shuffle(computer3_deck)
    return player_deck, computer1_deck, computer2_deck, computer3_deck

def show_table(player_deck, computer1_deck, computer2_deck, computer3_deck) :
    print("                         ", end='')
    print("Computer2 cards :", end='')
    for _ in range(len(computer2_deck)):
        print('', "*", end='')
    print("\n")
    print("Computer1 cards :", end='')
    for _ in range(len(computer1_deck)):
        print('', "*", end='')
    print("                     ", end='')
    print("Computer3 cards :", end='')
    for _ in range(len(computer3_deck)):
        print('', "*", end='')
    print("\n")
    print("                         ", end='')
    print("Player cards : ", end='')
    for i in range(len(player_deck)):
        print('', player_deck[i], end='')

def More() :
    restart = input("\n다시 한 번 실감나는 도둑잡를 하시겠습니까?(Y/N)\n")
    while (restart != "Y" and restart != "y" and restart !=  "N" and  restart != "n"):
        restart = input("대문자 혹은 소문자로 y와 n을 정확하게 입력해주세요!\n")
    if (restart == "Y" or restart == "y"):
        return True
    elif (restart == "N" or restart == "n"):
        return False


def Thief_catch(ID) :
    print("================================================================")
    print("도둑잡기에 오신것을 환영합니다.")
    print("플레이어를 포함해 사람은 총 4명. 카드는 플레이어를 시작으로 시계 방향으로 뽑습니다.")
    print("그리고 카드를 먼저 다 털어낸 사람이 승리합니다.")
    print("그럼 즐겁게 플레이하십시오 ^^.")
    print("===============================================================")
    while (True) :
        player_deck, computer1_deck, computer2_deck, computer3_deck = deck()
        while (True) :
            print("-------------------------------------------------------")
            show_table(player_deck, computer1_deck, computer2_deck, computer3_deck)
            print("\n-------------------------------------------------------")
            print(ID,"님의 차례입니다")
            while (True) :
                try :
                    index = int(input(("Computer1의 몇 번째 카드를 뽑겠습니까?(왼쪽부터 1 ~ {:}) : ".format(len(computer1_deck)))))
                    if (index < 1 or index > len(computer1_deck)) :
                        raise Outrange
                except ValueError :
                    print("자연수를 입력해주세요.")
                except Outrange :
                    print("범위를 벗어났습니다. 다시 골라주세요.")
                else :
                    break
            card = computer1_deck[index-1]
            print("뽑은 카드 : {:}".format(card))
            computer1_deck.remove(card)
            if (computer1_deck == []) :
                if (card in player_deck) and (len(player_deck) == 1):
                    print(ID,"님과 Computer1 둘다 카드를 다 털었습니다!!")
                    print(ID,"님과 Computer1 비김!")
                    break
                print("Computer1이 먼저 카드를 다 털어냈습니다!")
                print("Computer1 승!")
                break
            if card in player_deck :
                player_deck.remove(card)
                if (player_deck == []) :
                    print(ID,"님이 먼저 카드를 다 털어냈습니다!")
                    print(ID,"님 승!")
                    break
            else :
                player_deck.append(card)

            print("-------------------------------------------------------")
            print("Computer1의 턴")
            time.sleep(0.5)
            index = random.randint(1, len(computer2_deck))
            card = computer2_deck[index-1]
            computer2_deck.remove(card)
            if (computer2_deck == []) :
                if (card in computer1_deck) and (len(computer1_deck) == 1) :
                    print("Computer1과 Computer2 둘다 카드를 다 털었습니다!!")
                    print("Computer1과 Computer2 비김!")
                    break
                print("Computer2가 먼저 카드를 다 털어냈습니다!")
                print("Computer2 승!")
                break
            if card in computer1_deck :
                computer1_deck.remove(card)
                if (computer1_deck == []) :
                    print("Computer1이 먼저 카드를 다 털어냈습니다!")
                    print("Computer1 승!")
                    break
            else :
                computer1_deck.append(card)
                random.shuffle(computer1_deck)

            print("-------------------------------------------------------")
            print("Computer2의 턴")
            time.sleep(0.5)
            index = random.randint(1, len(computer3_deck))
            card = computer3_deck[index - 1]
            computer3_deck.remove(card)
            if (computer3_deck == []) :
                if (card in computer2_deck) and (len(computer2_deck) == 1) :
                    print("Computer2와 Computer3 둘다 카드를 다 털었습니다!!")
                    print("Computer2와 Computer3 비김!")
                    break
                print("Computer3이 먼저 카드를 다 털어냈습니다!")
                print("Computer3 승!")
                break
            if card in computer2_deck:
                computer2_deck.remove(card)
                if (computer2_deck == []):
                    print("Computer2가 먼저 카드를 다 털어냈습니다!")
                    print("Computer2 승!")
                    break
            else:
                computer2_deck.append(card)
                random.shuffle(computer2_deck)

            print("-------------------------------------------------------")
            print("Computer3의 턴")
            time.sleep(0.5)
            index = random.randint(1, len([player_deck]))
            card = player_deck[index - 1]
            print("Computer3이 뽑아간 카드 : {:}".format(card))
            player_deck.remove(card)
            if (player_deck == []) :
                if (card in computer3_deck) and (len(computer3_deck) == 1) :
                    print("Computer3과", ID  ,"님 둘다 카드를 다 털었습니다!!")
                    print("Computer3과", ID  ,"님 비김!")
                    break
                print(ID,"님이 먼저 카드를 다 털어냈습니다!")
                print(ID,"승!")
                break
            if card in computer3_deck:
                computer3_deck.remove(card)
                if (computer3_deck == []):
                    print("Computer3이 먼저 카드를 다 털어냈습니다!")
                    print("Computer3 승!")
                    break
            else:
                computer3_deck.append(card)
                random.shuffle(computer3_deck)
            time.sleep(0.5)

        if not (More()) :
            print("\n게임을 종료합니다.\n")
            break