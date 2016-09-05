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
        suit = ["H","S","C","D"]
        card = []
        for s in range(len(suit)):
            for x in range(0,14):
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

    def printHnad(self):
        Hand.printHnad()
"""
    def makeBet(self):
        #checks if bet is ok
"""

class Hand:
    def __init__(self,deck):
        self.deck = deck
        self.cards = []
        self.deal()

        #self.score = self.calScore()

    def deal(self):
        """
            gives each player 2 cards
        """
        for i in range(0,2):
            self.cards.append(self.deck.draw())


    def calcScore(self):
        """
            calcukates the total score of the hand
        """
        for x in range(len(self.cards)):
            sum = self.card[x][1]
        return sum

    def printHand(self):
        print "score = " + self.score
    """
    def ace(self):
        #allows player to choose whether an ace is scored as 1 or 11

    def hitOrStick(self):
        #allows player to hit or stick

    def split(self):
        #creates a new hand
    """
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
    deck = Deck()
    numPlayers = input("enter the number of players ")
    players = []
    for i in range(0,numPlayers):
        players.append(Player(500,deck,i))
        print players[i].hand.cards #prints the cards ech player has been dealt

def main():
    """
        used to show the menu and allows the user to select different options
    """
    menu()
    #game()
    #if the user makes a mistake it does not crash
    valid = False
    m = input("Enter an option from the menu ")
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
