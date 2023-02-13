import random
import time

gameLst = []
nextGame = True
raceLst = ["H","T","C","P"]
typeLst = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for i in range(3):
    for r in raceLst:
        for t in typeLst:
            gameLst.append(r+t)

count = 0
def randomcard():
    card = (gameLst[random.randint(0, len(gameLst))])
    gameLst.remove(card)
    if card[-1] == "2":
        cardvalue = 2
    elif card[-1] == "3":
        cardvalue = 3
    elif card[-1] == "4":
        cardvalue = 4
    elif card[-1] == "5":
        cardvalue = 5
    elif card[-1] == "6":
        cardvalue = 6
    elif card[-1] == "7":
        cardvalue = 7
    elif card[-1] == "8":
        cardvalue = 8
    elif card[-1] == "9":
        cardvalue = 9
    elif card[-1] == "A":
        cardvalue = 11
    else:
        cardvalue = 10
    return card,cardvalue

def play():
    dealerUp = randomcard()
    dealerDown = randomcard()
    player1 = randomcard()
    player2 = randomcard()
    playerVal = player1[1] + player2[1]
    dealerVal = dealerUp[1] + dealerDown[1]
    print("Dealer cards: ",dealerUp[0],"??\nPlayer cards: ",player1[0],";",player2[0])
    if playerVal == 21 and playerVal > dealerVal:
        print("Blackjack!")
    else:
        ask1 = input("What do you want to do? H,S?")
    if ask1 == "H" or ask1 == "h":
        player3 = randomcard()
        print("Dealer cards: ", dealerUp[0], "??\nPlayer cards: ", player1[0], ";", player2[0],";", player3[0])
        newPlayerVal = playerVal + player3[1]
        if newPlayerVal > 21:
            print("Bust")
            contin()
        else:
            cont2 = input("Hit or stand? H,S")
            if cont2 == "H" or cont2 == "h":
                player4 = randomcard()
                print("Dealer cards: ", dealerUp[0], "??\nPlayer cards: ", player1[0], ";", player2[0], ";", player3[0], ";", player4[0])
                newPlayerVal2 = newPlayerVal + player4[1]
                if newPlayerVal2 > 21:
                    print("bust")
                    contin()
    else:
        print("Dealer cards: ", dealerUp[0],";", dealerDown[0],"\nPlayer cards: ", player1[0], ";", player2[0])
        if dealerVal == 21 and playerVal < 21:
            print("Blackjack!, dealer wins.")
        elif dealerVal < 17:
            dealer3 = randomcard()
            newDealerVal = dealerVal + dealer3[1]
            time.sleep(0.5)
            print("Dealer cards: ", dealerUp[0], ";", dealerDown[0], ";", dealer3[0], "\nPlayer cards: ", player1[0], ";", player2[0])
            if newDealerVal > 21:
                print("Dealer is bust, Player wins")
            elif newDealerVal < 17:
                dealer4 = randomcard()
                newDealerVal2 = dealerVal + dealer3[1]
                time.sleep(0.5)
                print("Dealer cards: ", dealerUp[0], ";", dealerDown[0], ";", dealer3[0], ";",dealer4[0], "\nPlayer cards: ",player1[0], ";", player2[0])
                if newDealerVal2 > 21:
                    print("Dealer is bust, Player wins")
        else:
            if dealerVal > playerVal:
                print("Dealer wins")

def contin():
    ask = input("play again?")
    if ask == "Y" or ask == "y":
        play()
    else:
        pass
play()
