# Init main file commit
import random


class Player:
    def __init__(self, ID, card_deck):
        self.ID = ID
        self.card_deck = card_deck

    @property
    def card_deck(self):
        return self._card_deck

    @card_deck.setter
    def card_deck(self, card_deck):
        self._card_deck = card_deck

    def draw_card(self, card_deck, n=0):
        try:
            self.card_deck = card_deck
            return card_deck[n]
        except IndexError:
            print("No more cards to play")

    def remove_card_from_deck(self, card_deck):
        try:
            self.card_deck = card_deck
            card_deck.pop(0)
        except IndexError:
            pass

    def take_cards(self, card_deck, cards_to_take):
        self.card_deck = card_deck
        self.cards_to_take = cards_to_take
        card_deck.append(cards_to_take)


class Referee:
    counter = 0

    def __init__(self, card_deck):
        self.card_deck = card_deck

    def shuffle(self):
        deck = self.card_deck
        card_list = []
        for i in deck:
            card_list.append(list(i.keys()))

        random.shuffle(card_list)
        mixed_card_deck = []

        for shuffeled_card in card_list:
            for card in deck:
                if list(card.keys()) == shuffeled_card:
                    mixed_card_deck.append(card)

        return mixed_card_deck

    def split_deck(self, mixed_card_deck):
        self.mixed_card_deck = mixed_card_deck
        deck1 = mixed_card_deck[0:26]
        deck2 = mixed_card_deck[26:]

        return deck1, deck2

    def declare_winner(self, card_player, card_computer):
        self.card_player = card_player
        self.card_computer = card_computer

        if list(card_player.values()) > list(card_computer.values()):
            return "Player"
        elif list(card_player.values()) < list(card_computer.values()):
            return "Computer"
        else:
            return "Draw"


def main():
    card_deck = [
        {"As": 14},
        {"Ah": 14},
        {"Ac": 14},
        {"Ad": 14},
        {"Ks": 13},
        {"Kh": 13},
        {"Kc": 13},
        {"Kd": 13},
        {"Qs": 12},
        {"Qh": 12},
        {"Qc": 12},
        {"Qd": 12},
        {"Js": 11},
        {"Jh": 11},
        {"Jc": 11},
        {"Jd": 11},
        {"10s": 10},
        {"10h": 10},
        {"10c": 10},
        {"10d": 10},
        {"9s": 9},
        {"9h": 9},
        {"9c": 9},
        {"9d": 9},
        {"8s": 8},
        {"8h": 8},
        {"8c": 8},
        {"8d": 8},
        {"7s": 7},
        {"7h": 7},
        {"7c": 7},
        {"7d": 7},
        {"6s": 6},
        {"6h": 6},
        {"6c": 6},
        {"6d": 6},
        {"5s": 5},
        {"5h": 5},
        {"5c": 5},
        {"5d": 5},
        {"4s": 4},
        {"4h": 4},
        {"4c": 4},
        {"4d": 4},
        {"3s": 3},
        {"3h": 3},
        {"3c": 3},
        {"3d": 3},
        {"2s": 2},
        {"2h": 2},
        {"2c": 2},
        {"2d": 2},
    ]

    referee = Referee(card_deck)
    # print(test.card_deck)
    deck = referee.shuffle()
    player_deck, computer_deck = referee.split_deck(deck)

    player = Player("player", player_deck)
    computer = Player("computer", computer_deck)
    winner = ""
    table_cards = []
    # print("Player deck", player_deck)
    while True:
        print(f"Player deck: {len(player_deck)}. Computer deck: {len(computer_deck)}")
        if len(player_deck) != 0 or len(computer_deck) != 0:
            if winner == "Player":
                for card in table_cards:
                    player.take_cards(player_deck, card)
                table_cards = []
                winner = ""
            elif winner == "Computer":
                for card in table_cards:
                    computer.take_cards(computer_deck, card)
                table_cards = []
                winner = ""
            elif winner == "Draw":
                player_card = player.draw_card(player_deck, 1)
                player.remove_card_from_deck(player_deck)
                computer_card = computer.draw_card(computer_deck, 1)
                computer.remove_card_from_deck(computer_deck)

                table_cards.append(player_card)
                table_cards.append(computer_card)
                winner = ""

            else:
                player_card = player.draw_card(player_deck)
                player.remove_card_from_deck(player_deck)
                computer_card = computer.draw_card(computer_deck)
                computer.remove_card_from_deck(computer_deck)
                # print("Player deck after", player_deck)

                # print(player_card)
                # print(computer_card)

                winner = referee.declare_winner(player_card, computer_card)
                print(winner)

                table_cards.append(player_card)
                table_cards.append(computer_card)
                # print(table_cards)

            # print(player_deck)
        elif len(player_deck) == 0:
            print("Computer won the war")
            break
        elif len(computer_deck) == 0:
            print("Player won the war")
            break


main()


"""
Computer and user have the same class == Player

class Player:
ATTRIBUTE:
        ******* have to have getters and setters ******
    - stores its own deck which is provided by ???
    - player ID
        
METHOD:
    1. draw random card
        1.1. populate global variable called maybe TABLE?????
        1.2. take out card from deck list 
  
      
        if declared winner
    2. take cards
        2.1 take cards from global variable TABLE and append to card deck list
        
    
        if declared draw???
    3. 
    
   
   
    
class Referee:
ATTRIBUTE:
    - whole card deck as a list?
    - counter.


METHOD:
    1. shuffle_deck - randomly shuffles whole card deck
    
    
    
    2. split_deck - give card decks to each player
    
    
    
    
    
    3. declare_winner:
        3.1 compare two cards
        3.2 declare winner 
"""


# how to code which card beats which?


""" 
    1. start game - create both players
    
    2. create Referee
        2.1 shuffle cards
        2.2 give stacks of cards to each player
        
    3. computer draws card --- NO IDEA WHERE TO SAVE BOTH PLAYERS CARD. MAYBE ANOTHER class Board?????
    4. player draws card
    
    5. Referee declares winner:
        5.1  compares values of both cards
        5.2  declares winner
    
    6. winner takes both cards to separate won card stack
    
    7. repeat step 3-6.
"""
