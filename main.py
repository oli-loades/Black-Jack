import random

class Deck:
    def __init__(self):
        self.deckPos = 0
        self.deck = []
        self.createDeck()
        self.shuffle()

    def createDeck(self):
        """
            creates a nomal deck
        """
        suit = ["Hearts","Spades","Clubs","Diamonds"]
        card = []
        for s in range(len(suit)):
            for x in range(1,14):
                card = [suit[s],x]
                self.deck.append(card)

    def shuffle(self):
        """
            uses the random shuffle function to shuffle the created deck
        """
        random.shuffle(self.deck)

    def draw(self):
        """selects the next card in the deck"""
        temp = []
        temp = self.deck[self.deckPos]
        self.deckPos+=1 #tracks the next card
        return temp

class Player:
    def __init__(self,tokens,deck,num):
        self.hand = Hand(deck)
        #self.bet = 0
        self.tokens = tokens #tracks the players tokens used to bet
        self.num = num #possible pointless variable, can be used to show which player is selected eg. "player ""+ self.num + " winsW

    def printHand(self):
        if self.num == 0:
            print "Dealers hand: " + self.hand.printHand()
        else:
            print "Player " + str(self.num) + " hand: " + self.hand.printHand()
"""
    def makeBet(self):
        #checks if bet is ok
"""

class Hand:
    def __init__(self,deck):
        self.deck = deck
        self.cards = []
        for i in range(0,2):
            self.draw()
        self.score = 0
        self.calcScore()
        self.bust = False


    def draw(self):
        """
            gives a player a cards from the deck
        """
        self.cards.append(self.deck.draw())


    def calcScore(self):
        """
            calcukates the total score of the hand
        """
        self.score = 0
        for x in range(len(self.cards)):
            if self.cards[x][1] >= 10:
                self.score = self.score + 10
            else:
                self.score = self.score + self.cards[x][1]

    def printHand(self):
        s = ""
        values = ["","Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for x in range(len(self.cards)):
            if x == (len(self.cards)-1):
                s = s + values[self.cards[x][1]] + " of " +self.cards[x][0]
            else:
                s = s + values[self.cards[x][1]] + " of " +self.cards[x][0] + " and "
        return s

    def hit(self):
        self.draw()
        self.calcScore()
        if self.score > 21:
            self.busted()



    def busted(self):
        self.bust = True
        print "you have gone bust, you lose"


    """
    def ace(self):
        #allows player to choose whether an ace is scored as 1 or 11

    def hitOrStick(self):
        #allows player to hit or stick

    def split(self):
        #creates a new hand
    """
def validate(msg):
    num = False
    while num == False:
        try:
            val = input(msg)
            num = True
        except:
            print "Error - enter a number"
    return val

def menu():
    print "Option 1 - Play"
    print "Option 2 - View Tokens"
    print "Option 3 - Save"
    print "Option 4 - Load"
    print "Option 0 - Exit"

def game():

    """
        allows the player to play black jack
    """
    valid = False
    deck = Deck()
    house = Player(1000,deck,0)
    numPlayers = validate("enter the number of players ")
    players = []
    house.printHand()
    for i in range(0,numPlayers):
        players.append(Player(500,deck,i+1))
        #print players[i].hand.cards #prints the cards ech player has been dealt
        players[i].printHand()
    for i in range(0,numPlayers):
        valid = False
        while valid == False:
            hit = validate("Player " + str(i+1) +" do you want to hit? 1 = yes, 0 = no ")
            if hit == 1:
                valid = True
                players[i].hand.hit()
                players[i].printHand()
            elif hit == 0:
                valid = True
                print "you have choosen to stick"
            else:
                print "Error - enter 1 or 0"


    #hit or stick

def main():
    """
        used to show the menu and allows the user to select different options
    """
    menu()
    #game()
    #if the user makes a mistake it does not crash
    valid = False
    m = validate("Enter an option from the menu ")
    while valid == False:
        if m >= 0 and m <= 4:
            valid = True
            if m == 1:
                game()
            elif m == 2:
                print "not yet implemented"
                #print player.tokens
            elif m == 3:
                print "not yet implemented"
                #save()
            elif m == 4:
                print "not yet implemented"
                #load()
            else:
                print "exit"
        else:
            m = input("Error - Enter an option from the menu ")


if __name__ == "__main__":
    main()
