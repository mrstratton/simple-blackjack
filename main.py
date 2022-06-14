import random

import time

 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

 

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',

         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

 

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,

          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

 

class Card:

 

    def __init__(self, suit, rank):

        self.suit = suit

        self.rank = rank

        self.value = values[rank]

 

    def __str__(self):

        return self.rank + ' of ' + self.suit

 

class Deck:

 

    def __init__(self):

 

        self.all_cards = []

 

        for suit in suits:

            for rank in ranks:

                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

 

    def shuffle(self):

 

        random.shuffle(self.all_cards)

 

    def deal_one(self):

 

        return self.all_cards.pop()

 

class Player:

    available_credits: int

 

    def __init__(self, name, available_credits=0):

 

        self.name = name

        self.available_credits = available_credits

        self.hand = []

        self.extended_hand = []

        self.current_bet = 0

        self.hand_value = 0

        self.added_cash = 0

        self.gain_loss = 0

        self.aces_in_hand = 0

        self.counted_cards = []

 

    def __str__(self):

 

        return f'{self.name}'

 

    def player_hand_add_cards(self, dealt_cards):

        self.hand.append(dealt_cards)

 

    def credit_update(self, credit_update=0):

        if credit_update > 0:

            self.available_credits += credit_update

        else:

            try:

                bank_update = int(input('Cash to Enter: '))

                self.available_credits += bank_update

                self.added_cash += bank_update

            except ValueError:

                print('Not a number.')

 

    def player_bet(self):

        active_bet = True

        while active_bet:

            if self.available_credits != 0:

                try:

                    print(f'Available Cash: ${self.available_credits}')

                    place_a_bet = round(int(input('Place a bet (10% minimum) : ')))

                    while place_a_bet > self.available_credits:

                        print('Not enough cash to place that bet.')

                        place_a_bet = round(int(input('Place a bet (10% minimum) : ')))

                    while place_a_bet < self.available_credits * .1:

                        print(f'Minimum bet is ${int(self.available_credits * .1)} (10% of your available $$).')

                        place_a_bet = round(int(input('Place a bet (10% minimum) : ')))

                    if self.available_credits >= place_a_bet >= round(self.available_credits * .1):

                        self.current_bet += place_a_bet

                        self.available_credits -= place_a_bet

                        active_bet = False

                except ValueError:

                    print('Not a number.')

 

            else:

                print('You\'re out of cash!!')

                try:

                    bank_update = int(input('Cash to Enter: '))

                    self.available_credits += bank_update

                    self.added_cash += bank_update

                    print(' ')

                except ValueError:

                    print('Not a number.')

 

    def hand_in_play(self):

 

        for card in self.hand:

            if card not in self.counted_cards:

                time.sleep(.5)

            print(f'__ {card} __')

            if card not in self.counted_cards:

                self.hand_value += card.value

                self.counted_cards.append(card)

                if card.rank == 'Ace':

                    self.aces_in_hand += 1

 

        while self.hand_value > 21 and self.aces_in_hand > 0:

            self.hand_value -= 10

            self.aces_in_hand -= 1

            print('ace accounted for')

        print(f'Hand value: {self.hand_value}')

 

    def player_gain_loss(self):

        self.gain_loss = self.available_credits - self.added_cash - 100

        if self.gain_loss > 0:

            print(f'Your net gain is ${self.gain_loss}.')

        if self.gain_loss < 0:

            print(f'Your net loss is ${self.gain_loss}.')

        if self.gain_loss == 0:

            print(f'You are net even.')

 

def hit_or_stand(player_one_initial_hand_value):

    while player_one_initial_hand_value != 21:

        user_choice = input('Hit or Stand?: ').lower()

        acceptable_input = ['hit', 'stand']

        while user_choice not in acceptable_input:

            print('Invalid Input')

            user_choice = input('Hit or Stand?: ').lower()

        if user_choice == 'hit':

            print('HIT ME!')

            time.sleep(1)

            return 'hit'

        if user_choice == 'stand':

            print('STAND')

            time.sleep(1)

            return 'stand'

    if player_one_initial_hand_value == 21:

        print('BLACKJACK!')

 

def play_action(player, player_play):

    if player_play == 'hit':

        player.extended_hand.append(new_deck.deal_one())

        for card in player.extended_hand:

            if card not in player.hand:

                player.hand.append(card)

        player.hand_in_play()

        return True

    if player_play == 'stand':

        print(f'Hand Value for {player}: {player.hand_value}')

        return False

 

def dealer_move():

    print(' ')

    print('Dealing card...')

    time.sleep(1)

    dealer_1.extended_hand.append(new_deck.deal_one())

    for card in dealer_1.extended_hand:

        if card not in dealer_1.hand:

            dealer_1.hand.append(card)  # deal card to hand

    dealer_1.hand_in_play()  # print dealer hand and add values to dealer_1.hand_value

 

def player_one_win():

    player_1.credit_update(player_1.current_bet * 2)

 

def player_one_tie():

    player_1.credit_update(player_1.current_bet)

 

def player_one_lose():

    dealer_1.credit_update(player_1.current_bet)

 

def play_again():

    """

    simple true/false for starting a new round

    """

 

    user_input = input('Deal again/end game/add cash? (y/n/a): ').lower()

    acceptable_input = ['y', 'n', 'a']

    while user_input not in acceptable_input:

        print('Try again')

        user_input = input('Deal again/end game/add cash? (y/n/a): ').lower()

    if user_input == 'a':

        player_1.credit_update()

        return True

    if user_input == 'y':

        return True

    if user_input == 'n':

        return False

 

def reset_hand():

    player_1.hand = []

    dealer_1.hand = []

    player_1.hand_value = 0

    dealer_1.hand_value = 0

    player_1.current_bet = 0

    player_1.aces_in_hand = 0

    dealer_1.aces_in_hand = 0

    player_1.extended_hand = []

    dealer_1.extended_hand = []

 

def print_blackjack():

    x = 'LET\'S PLAY BLACKJACK!'

    for letters in x:

        print(letters, end='')

        time.sleep(.25)

    print(' ')

    print(' ')

 

if __name__ == '__main__':

    playing_blackjack = True

 

    while playing_blackjack:

 

        user_input = input('Play new game? (y/n): ').lower()

        acceptable_input = ['y', 'n']

        while user_input not in acceptable_input:

            print('Try again')

            user_input = input('Play new game? (y/n): ').lower()

        if user_input == 'n':

            print(':)')

            playing_blackjack = False

        if user_input == 'y':

            '''

            Start game / create player and dealer

            '''

            print(' ')

            print_blackjack()

            time.sleep(1)

            player_1 = Player(input('Enter your name: '), 100)  # make player 1

            print(f'Player \'{player_1.name}\' has ${player_1.available_credits}.')

            print(' ')

            dealer_1 = Player('Dealer', 0)  # make dealer
            
            time.sleep(1)

 

            game_time = True

 

            while game_time:

 

                new_deck = Deck()  # make new deck

                new_deck.shuffle()  # shuffle new deck

 

                '''

                place a bet

                '''

                player_1.player_bet()

                time.sleep(1)

                print(' ')

                print(f'{player_1.name}\'s bet: ${player_1.current_bet}')

                time.sleep(.5)

                print(f'Available $$: ${player_1.available_credits}')

                time.sleep(1)

                print(' ')

 

                for i in range(2):  # deal 2 cards to player and dealer

                    player_1.player_hand_add_cards(new_deck.deal_one())

                    dealer_1.player_hand_add_cards(new_deck.deal_one())

 

                # two card in self.hand for both player and dealer

 

                '''

                        print player hand and card value

                        print dealer first card

                        '''

 

                print('- Dealer Hand -')

                print(f'__{dealer_1.hand[0]}__')

                print(' ')

                print(f'- {player_1.name}\'s Hand -')  # print & append player cards and first dealer card

                player_1.hand_in_play()

                print(' ')

 

                # begin player_1 turn

 

                print('Your Turn')

                dealer_turn = False

                p1turn = True

 

                # check for natty blackjacks

                if player_1.hand_value == 21:

                    if dealer_1.hand_value != 21:

                        print(' ')

                        print('BLACKJACK!')

                        print(' ')

                        print('- Dealer Hand - ')

                        dealer_1.hand_in_play()

                        print('You win!')

                        player_one_win()

                        p1turn = False

                        if play_again():

                            reset_hand()

                        else:

                            game_time = False

                    elif dealer_1.hand_value == 21:

                        print('- Dealer Hand - ')

                        dealer_1.hand_in_play()

                        print('Dealer BLACKJACK! It\'s a tie!')

                        player_one_tie()

                        p1turn = False

                        if play_again():

                            reset_hand()

                        else:

                            game_time = False

 

                # begin p1turn

                while p1turn:

 

                    #  decision = false if player stands, true while player hits.

                    decision = play_action(player_1, hit_or_stand(player_1.hand_value))

 

                    if not decision:

                        p1turn = False

                        print(' ')

                        print('Dealer\'s Turn.')

                        dealer_turn = True

 

                    if player_1.hand_value > 21:

                        print('That\'s a BUST! Dealer wins!')

                        player_one_lose()

                        p1turn = False

                        if play_again():

                            reset_hand()

                        else:

                            game_time = False

 

                    if player_1.hand_value == 21:

                        print('Max Value!')

                        print(' ')

                        print('Dealer\'s Turn.')

                        p1turn = False

                        dealer_turn = True

 

                while dealer_turn:

 

                    turn = 0

                    while turn == 0:

                        turn += 1

                        print('- Dealer Hand - ')

                        dealer_1.hand_in_play()

                        if dealer_1.hand_value == 21:

                            print('Dealer BLACKJACK! Dealer Wins!')

                            player_one_lose()

                            dealer_turn = False

                            if play_again():

                                reset_hand()

                            else:

                                game_time = False

 

                    # check for win conditions

 

                    while dealer_1.hand_value < 17 or dealer_1.hand_value < player_1.hand_value:

                        dealer_move()

 

                    if dealer_1.hand_value > 21:

                        print('Dealer BUST!')

                        print('Player One Wins!')

                        player_one_win()

                        dealer_turn = False

                        if play_again():

                            reset_hand()

                        else:

                            game_time = False

 

                    elif 17 <= dealer_1.hand_value < 22 and dealer_1.hand_value > player_1.hand_value:

                        print(f'{dealer_1.hand_value} beats {player_1.hand_value}, dealer wins!')

                        player_one_lose()

                        dealer_turn = False

                        if play_again():

                            reset_hand()

                        else:

                            game_time = False

 

                    elif 17 <= dealer_1.hand_value < 22 and dealer_1.hand_value == player_1.hand_value:

                        print(f'{dealer_1.hand_value} ties {player_1.hand_value}')

                        player_one_tie()

                        dealer_turn = False

                        if play_again():

                            reset_hand()

                        else:

                            game_time = False

 

                print(' ')

                print(f'In total you have added {player_1.added_cash} to your account.')

                player_1.player_gain_loss()

                print(' ')
