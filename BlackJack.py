import random

def createDeck():
    deck = []
    suit = ["H","S","C","D"]
    card = []
    for s in range(len(suit)):
        for x in range(0,14):
            card = [suit[s],x]
            deck.append(card)
    return deck

def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

def deal(deckPos, deck):
    score = 0
    score = deck[deckPos][1]
    if score > 10: #if the card is a picture card
        score = 10
    if score == 1:
        score = ace()
    print "score: " + str(score)
    return score

def ace():
    yn = ""
    while yn != "y" or yn != "n":
        yn = input("you got an ace, do you want to it to count as 11 [y/n]?")
        if yn == "y":
            return 11
        elif yn == "n":
            return 1
        
def displayMenu():
    print "Option 1 - Play BlackJack"
    print "Option 2 - View Tokens"
    print "Option 3 - Save"
    print "Option 4 - Load"																																																																										
    print "Option 0 - Exit"

def game():
    deckPos = 0 #removes the need to remove cards from the deck array
    pTotal = 0
    dTotal = 0;
    deck = []
    hitOrStick = ""
    deck = createDeck()

    deck = shuffleDeck(deck)
    for i in range(0,2):
        score = deal(deckPos, deck)
        pTotal = pTotal + score
        deckPos+=1

        score = deal(deckPos, deck)
        dTotal = dTotal + score
        deckPos+=1

    print "players score total:" + str(pTotal)
    print "dealers score total:" + str(dTotal)

    #did they get blackjack?
    #if not
    #ask user if teh ywant to stick or hit
    #repeat until user goes above 21 or chooses to stick

def main():
    userOption = -1
    while userOption != 0:
        userOption = input("enter an option from the menu")
        displayMenu()
        if userOption == 1:
            game();
    
    
if __name__ == "__main__":
	while True:
            main()
