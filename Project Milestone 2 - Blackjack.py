# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:08:30 2020

@author: Lisandro Cocca
"""
# Modules and Packages
import random

# Definition of classes
class Card():
    
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits
    
    def __str__(self):
        return f"{self.ranks} of {self.suits}"
    
class Deck():
    
    def __init__(self):
        self.deck = []
        self.size = 52
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))
                
    def __str__(self):
        # En la solucion explica bien como usar el object.__str__! Puede mejorarse
        return f"The deck has currently {self.size} cards!"
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        self.size -= 1
        return self.deck.pop()
    
class Hand():
    
    def __init__(self):
        self.cards = []     # Cards in hand
        self.value = 0      # Value of hand
        self.aces = 0       # Quantity of Aces
    
    def __str__(self):
        return f"The hand's value is {self.value}"
        
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.ranks]
        
    def adjust_aces(self):
        
        # Puede hacerse tambien en add_card, obviando el for!
        for k in self.cards:
            if k.ranks == 'Ace':
                self.aces += 1
        
        # Separe la condicion > 21 con el llamado, vale!
        if self.aces:
            self.aces -= 1
            self.value -= 10
            print(f"The new hand value is {self.value}")

                
class Chips():
    
    def __init__(self):
        self.total = 100
        self.bet = 0
     
    def __str__(self):
        return f"Your bank account currently has ${self.total}"
      
    # Es programada por separado en la solucion! Me gusta que sea parte de la clase?   
    def add_bet(self):
        
        while True:
            try:
                choice = int(input("How much would you like to bet?: "))
                
                # Puede ir en un else despues del except tambien, para ser mas claro!
                if choice > self.total:
                    print("Sorry man you arent that rich!\n")
                else:
                    break
            except:
                print("Whoops that is not a number!\n")
                
        self.bet = choice
        print("")

        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
    

def hand_fdisplay(hand):
    for item in hand.cards:
        print(item)
    print(hand)
    print("\n-------------\n")

def hand_sdisplay(hand):
    print(hand.cards[0])
    print("Mysterious Card")
    print("The hand's value is unkwown!")
    print("\n-------------\n")   

def hit_or_stay():
    choice = 'Wrong'
    
    while choice not in ['Y', 'N']:
        choice = input("Dear player, do you want to hit? (Y,N): ")
                
        if choice not in ['Y', 'N']:
            print("Sorry you have to choose Y or N!\n")
    
    print("")
    return choice == 'Y'

def busted_check(hand):
    
    if hand.value > 21:
        if hand.aces == 0:
            return True
        else:
            hand.adjust_aces()
            return False
        
def computer_decision(hand):
    return hand.value <= 17

def computer_win(handC, handP):
    return handC.value >= handP.value

def replay_ask():
    choice = 'Wrong'
    
    while choice not in ['Y', 'N']:
        choice = input("Dear player, do you want to play another game? (Y,N): ")
                
        if choice not in ['Y', 'N']:
            print("Sorry you have to choose Y or N!\n")
    
    print("")
    return choice == 'Y'
    
      
     
 ## Variable Definition
ranks = ('Two', 'Three', 'Four', 'Five', 'Six',
         'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 
          'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
          'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Bank account
bank = Chips()

# Replay boolean
replay = True

while replay:
       
    # Creating a Deck
    test_deck = Deck()
    
    # Shuffling the deck
    test_deck.shuffle()
    
    # Creating both Player and Computer hands
    player_hand = Hand()
    computer_hand = Hand()
    
    # Initial dealing
    for i in range(0, 2):
        computer_hand.add_card(test_deck.deal())
        player_hand.add_card(test_deck.deal())
    
    # Displaying Player hand
    print("\nPlayer's Hand \n")
    hand_fdisplay(player_hand)
    
    # Displaying Computer hand
    print("Computer's Hand!\n")
    hand_sdisplay(computer_hand)
    
    ### PLAYER 1 TURN
    # Asking for bets
    print(bank)
    bank.add_bet()
    
    # Asking if hitting
    while hit_or_stay():
    
        # If hit, add new card
        player_hand.add_card(test_deck.deal())
                
        # Display player hand
        print("Player's Hand \n")
        hand_fdisplay(player_hand)
        
        # Checking if Player busted
        if busted_check(player_hand):
            print("Sry bro u screwed as fuck!")
            bank.lose_bet()
            break
    
    if not busted_check(player_hand):
        ### COMPUTER TURN
        # Revealing computers hand and calculating value
        print("Computer's Hand \n")
        hand_fdisplay(computer_hand)
        
        # Deciding wether hit or stay
        while computer_decision(computer_hand):
            
            # If hit, add new card
            computer_hand.add_card(test_deck.deal())
    
            # Display computer hand
            print("Computer's Hand \n")
            hand_fdisplay(computer_hand)
        
            # Checking if Computer busted
            if busted_check(computer_hand):
                print("Computer busted :D ")
                bank.win_bet()
                break
    
        if not busted_check(computer_hand):     
            # Checking if Computer beated player
            if computer_win(computer_hand, player_hand):
                print(f"Computer won with a result of {computer_hand.value} to {player_hand.value}")
                bank.lose_bet()
            else:
                print(f"Player won with a result of {player_hand.value} to {computer_hand.value}")
                bank.win_bet()
    
    # Showing current account balance
    print(bank)

    ### ASKING FOR REPLAY
    replay = replay_ask()
    