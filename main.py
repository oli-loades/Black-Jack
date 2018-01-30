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
        """ uses the random shuffle function to shuffle the created deck """
        random.shuffle(self.deck)

    def draw(self):
        """ selects the next card in the deck """
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
        self.gotBlackJack = False

    def printHand(self):
        """
            shows players hand
        """
        print "Player " + str(self.num) + " hand: " + self.hand.getHand()

    def wins(self):
        """
            returns winnings //not fully implemented
        """
        print "player " + str(self.num) + " wins"
        self.printScore()

    def loses(self):
        """
            removes the tokens from the player
        """
        self.num = num  #used to show which player is selected
        self.hasBlackJack = False



    def printScore(self):
"""
    def makeBet(self):
        #checks if bet is ok
"""


class Hand:
    def __init__(self,deck):
        self.deck = deck
        self.cards = []

        self.highAce = False

        for i in range(0,2):
            self.draw()
        self.score = 0
        self.calcScore()
        self.bust = False

        self.values = ["","Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]


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
        if self.highAce == True:
            self.score = self.score + 10"""

    def getHand(self):
        """
            shows the players cards
        """
        s = ""
        for x in range(len(self.cards)):
            if x == (len(self.cards)-1):
                s = s + self.values[self.cards[x][1]] + " of " +self.cards[x][0]

    def draw(self):
        """ gives a player a cards from the deck """
        self.cards.append(self.deck.draw()) #adds a card to the hand from the deck

    def newHand(self):
        """ gives player 2 new cards """
        self.cards = []
        self.highAce = False
        self.bust = False
        for i in range(0,2): #takes 2 cards
            self.draw()

    def hit(self):
        """
            give another card and checks if they have gone over 21
        """
        self.draw()

        print "Card: " + self.values[self.cards[-1][1]] + " of " +self.cards[-1][0]
        self.calcScore()
        if self.score > 21:
            self.busted()


    def busted(self):
        """
            if the player goes over 21
        """
        self.bust = True
        print "you have gone bust, you lose"

    def ace(self):
        """sets ace to be scored as 11 """
        self.highAce = True
        self.calcScore()

    def getScore(self):

        """ returns score """
        self.calcScore()
        return self.score

    def hasAce(self):
        """ checks whether the player has an ace or not """
        if len(self.cards) == 2: #if checking at the start of the game
            if self.cards[0][1] == 1 or self.cards[1][1] == 1: #if either card is an ace
                return True
            else:
                return False
        else: #if player has hit
            if self.cards[-1][1] == 1: #if the new card is an ace
                return True
            else:
                return False

    def blackJack(self):
        """checks if the player has black jack """
        if self.hasAce() == True: #if player has an ace
            self.ace() #high ace
            if self.score == 21:
                return True
            else:
                return False
        else:
            return False


class Dealer(Hand):
    def __init__(self, deck):
        Hand.__init__(self,deck)
        self.blackJackWin = False


    def showCard(self):

        """ shows the first card """
        print "Dealers card: " +  self.values[self.cards[0][1]] + " of " + self.cards[0][0]

    def showHand(self):
        """ prints full hand """
        print "Dealers hand: " + self.getHand()

    def play(self):
        """ dealers logic """
        stick = False
        while stick == False and self.bust == False: #loop until dealer sticks or busts
            if self.hasAce() == True:#if dealer has ace
                if (self.score + 10) < 21: #if choosing high ace doesn't bust hand
                    self.ace() #creates high ace
            if self.score < 17: #dealer can only stick if thier score is over 17
                print "dealer chooses to hit"
                self.hit() #gets another card
            else:
                stick = True
                print "Dealer has choosen to stick"
        self.showHand() #shows dealers hand

    def busted(self):
        """ if the dealer busts """
        self.bust = True
        print "Dealer has gone bust"

    def gotBlackJack(self):
        if self.blackJack() == True:
            self.blackJackWin = True

def isAce(players,i):
    """lets the player choose if ace is sored as 1 or 11 """
    if players[i].hand.hasAce() == True:
        a = validate("player " + str(i+1) + " got an ace, do you want it to be scored as 11, 1 = yes, 0 = no ") #checks user input and allows it if it is a number
        valid = False
        while valid == False: #loop until input is 1 or 0
            if a == 1: #if player chooses ace to be scored as 11
                valid = True
                players[i].hand.ace() #set ace to 11
            elif a == 0:
                valid = True
            else: #if 0 or 1 is not entered
                print "Error - enter 1 or 0"

def isBlackJack(players,i):
    """ cheks if s player has black jack """
    if players[i].hand.blackJack() == True:
        players[i].printHand()
        players[i].hasBlackJack = True
        return True
    return False

def validate(msg):
    """

        catches errors if the user doesn't enter a number
    """

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


def win(players,house):
    """ decides which players win """
    for i in range(0,len(players)):#loop through each player
        if players[i].hasBlackJack == False: #if player does not have black jack
            if house.bust == False: #if dealer is not bust
                if players[i].hand.bust == False: #if player is not bust
                    if players[i].hand.score > house.score: #if players score is higher than dealers
                        players[i].wins()
                    else:
                        players[i].loses()
                else: #if player went bust
                    players[i].loses()
            else:#if dealer went bust
                if players[i].hand.bust == False:
                    players[i].wins()
        else: #if player got black jack
            if house.gotBlackJack() == True:
                players[i].loses()
            else:
                players[i].wins()




def hitOrStick(players,i):
    """
        lets the players choose to hit or stick
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
    stick = False
    while stick == False and players[i].hand.bust == False:
        valid = False
        while valid == False:
            hit = validate("Player " + str(i+1) +" do you want to hit? 1 = yes, 0 = no ")
            if hit == 1:
                valid = True
                players[i].hand.hit()
                players[i].printHand()
                isAce(players, i)
                players[i].printScore()
            elif hit == 0:
                stick = True
                valid = True
                print "you have choosen to stick"
            else:
                print "Error - enter 1 or 0"


def play(players, house):
    numPlayers = len(players) #sets number of players
    house.showCard() #shows one of the dealers cards
    for i in range(0,numPlayers): #loop through each player
        if isBlackJack(players,i) == False: #if the player has not go black jack
            players[i].printHand() #show hand
            isAce(players, i) #check if its an ace
            players[i].printScore() #shows score
    for i in range(0,numPlayers):
        if players[i].hasBlackJack == False:
            hitOrStick(players,i) #lets player choose to hit or stick
    house.play() #dealer AI plays
    win(players,house) #Decides who wins

def main():
    """ allows the player to play black jack """
    valid = False

    deck = Deck() #Creates new deck
    house = Dealer(deck) #cretaes new dealer hand
    numPlayers = validate("enter the number of players ") #checks if user has entered a number
    players = [] #list used to stroe players
    end = False #used to stroe whether the player wants to stop playing
    for i in range(0,numPlayers): #loop through eahc player
        players.append(Player(500,deck,i+1)) #crete new player
    play(players,house) #play game
    while valid == False or end == False: #loop until player chooses to end
        valid = False
        p = validate("would you like to play again? 1 = yes, 0 = no ")
        if p == 1:#if player wants to play again
            valid = True
            house.newHand() #dealer new hand
            for i in range(0,numPlayers):
                players[i].hand.newHand() #players new hand
            play(players,house)
        elif p == 0: #ends game
            valid = True
            end = True
            print "game ended"
        else: #if player does not enter 1 or 0
            valid = False
            print "error enter an option from the menu"


if __name__ == "__main__":
    main()
