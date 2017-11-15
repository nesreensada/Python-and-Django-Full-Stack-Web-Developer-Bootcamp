#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        'creating Deck'
        self.items = [(s,r) for s in SUITE for r in RANKS ]

    def shuffle_deck(self):
        print 'shuffle cards'
        shuffle(self.items)

    def split_deck(self):
        print 'split Deck'
        return (self.items[:26],self.items[26:])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards=cards

    def add_card(self,card):
        print 'add a card to deck'
        self.cards.extend(card)

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand

    def play_card(self):
        card=self.hand.remove_card()
        print ('{} card to be played by {}'.format(card,self.name))
        return card

    def cards_for_war(self):
        war_cards=[]
        if len(self.hand.cards)<3:
            return war_cards
        else:
            for i in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards)!=0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
deck=Deck()
deck.shuffle_deck()
name=input("What is your name? ")
half1,half2=deck.split_deck()

player_comp=Player('computer',Hand(half1))
player_user=Player(name,Hand(half2))


war_count=0
rounds=0
while(player_comp.still_has_cards() and player_user.still_has_cards()):

    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(player_user.name+" count: "+str(len(player_user.hand.cards)))
    print(player_comp.name+" count: "+str(len(player_comp.hand.cards)))
    print("Both players play a card!")
    print('\n')

    rounds+=1
    card_user=player_user.play_card()
    card_comp=player_comp.play_card()

    #comparing both
    table_cards=[]

    table_cards.append(card_comp)
    table_cards.append(card_user)

    if card_comp[1]==card_user[1]:
        war_count+=1

        print 'war'

        table_cards.extend(player_user.cards_for_war())
        table_cards.extend(player_comp.cards_for_war())

        if RANKS.index(card_comp[1])<RANKS.index(card_user[1]):
            player_user.hand.add_card(table_cards)
        else:
            player_comp.hand.add_card(table_cards)
    else:

        if RANKS.index(card_comp[1])<RANKS.index(card_user[1]):
            player_user.hand.add_card(table_cards)
        else:
            player_comp.hand.add_card(table_cards)

print ('rounds were '+ str(rounds))
print ('wars were '+ str(war_count))
