'''
Make by HSC

Create PCV_1 in 15 of May, 2024. 
-- Basic Random number 
-- Win and lost calculation 
-- Action of Hit, Stand and Double

Update to PCV_2 in 21 of May, 2024. 
-- Suits and ranks separate random 
-- Bug: "A" = 1/11. Use the biggest amount

Update to PCV_3 in 24 of May, 2024. 
-- If dealer get "A" in his face-up card, allow player to buy insurance.

Update to PCV_4 in 02 of June, 2024. 
-- If player get 21 in their hit, automatic jump to dealer's card page.

Update to PCV_5 in 11 of June, 2024. 
-- Bug: If player get Blackjack but dealer get "A",
H                will ask player want to buy insurance or not. 
S		 The correct situation will be asking player
C                want to win 1:1 or 1:1.5 if dealer is not Blackjack.

Update to PCV_6 in 17 of June, 2024. 
-- Create layout to convenient watching.

Create MV_1 in 19 of June, 2024. 
-- More easy to run on the mobile. ~~Testing by Xiaomi 13T pro ~~Using app "Coding python"

Upload MV_1 on FB Group "Python" in 20 of June, 2024. 1901(NZT, GMT+12)
-- Link: https://www.facebook.com/groups/python (Update: Post delete)

Upload MV_1 on GitHub in 20 of June, 2024. 1925(NZST, GMT+12)

Reupload MV_1 on GitHub in 20 of June, 2024. 2050(NZST, GMT+12)

Upload MV_2 on GitHub in 20 of June, 2024. 2317(NZST, GMT+12)
-- Make the side bet of Perfect Pair(PP), if win, 5:1.
-- When start the program, will ask you do you want to play side-bet.
-- Fix the UI problem
-- Because original PP is using 208 card but this program using 52 cards,
                          25:1 of same suits and same ranks NOT AVAILABLE
-- To optimization: If player get same colour of PP, 12:1

Upload PCV_7 on GitHub in 21 of June, 2024. 0000(NZST, GMT+12)

Upload MV_2.1 on GitHub in 21 of June, 2024. 0925(NZST, GMT+12)
-- PCV_7,1 will be update soon.
-- Player get same colour of PP, 12:1 available.

Upload PCV_7.1 on GitHub in 21 of June, 2024. 0937(NZST, GMT+12)
-- Function as same as MV_2.1

Upload PCV_7.2 on GitHub in 21 of June, 2024. 1450(NZST, GMT+12)
-- Make the side bet of 21+3
-- Allow player to choose Side bet type: No side bet,
                             Perfect Pair and/or 21+3
-- MV_2.2 will be update soon.

Update MV_2.2 on GitHub in 21 of June, 2024. 1510(NZST, GMT+12)
-- Function as same as MV_2.2
-- Fix the UI problem
-- Fix the bug of side-bet reset problem

MV_2.2 and PCV_7.2 update
-- 21+3 side bet add "Three of King"
-- UI update

MV_2.3
-- Change the Side-Bet entering answer
-- Royal Match side bet
-- Confirm PCV_7.2 is the last system update

MV_2.4 on GitHub in 23 of September, 2024. 2320(NZST, GMT+12)
-- Dealer Bust side bet
=========================================================================
Stop support version from:  MV_2.3    PCV_7.2(Last update)
=========================================================================
The latest version:  MV_2.4    PCV_7.2
'''

import random

# Define card suits and ranks
suits = ['♥', '♦', '♣', '♠']
##suits = ['♥', '♦']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
##ranks = ['K', 'Q']

# Define card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # Initially return 11; adjust dynamically in the game logic
        else:
            return int(self.rank)
        
    def adjust_ace_value(self, current_hand_value):
        if self.rank == 'A' and current_hand_value > 21:
            return 1
        return self.get_value()

# Card display (dealer)
def dealer_display(dealer_first_card):
    print(f"Dealer's Hand: [{str(dealer_first_card)} ,??]")
    return

# Block
def block():
    print("========================================")
def block_end():
    print("=======================END==GAME========")

# Result of card
def showing_result(player, dealer):
    block()
    print("||>\tPlayer    <|> \t  Dealer     <||\n||>\t ",
          player,"\t  <|> \t   ",dealer,"\t     <||")
    block()

# Extract the unique digits
def extract_unique_digits(numbers):
    unique_digits = set()
    approve_digits = {'0' ,'1', '2', '3', '4'}
    
    for char in numbers:
        if char in approve_digits:
            unique_digits.add(char)
            
    return sorted(map(int, unique_digits))

# Define deck class
class Deck:
    def __init__(self):
        self.cards = []
        self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Define player class
class Player:
    def __init__(self, name, initial_money=500):
        self.name = name
        self.money = int(initial_money)
        self.hand = []
        self.current_bet = 0
        self.current_pp = 0
        self.current_21_p_3 = 0 
        self.insurance_bet = 0
        self.current_royal = 0
        self.current_bust_amount = 0

    def place_bet(self, amount, pp_amount, twenty_four_amount, royal_match_amount, too_many_amount):
        self.current_bet = 0
        self.current_pp = 0
        self.current_21_p_3 = 0
        self.current_royal = 0
        self.current_bust_amount = 0
        T_bet = 0
        T_bet = amount + pp_amount + twenty_four_amount + royal_match_amount + too_many_amount
        if T_bet > self.money:
            print("Insufficient funds!")
            return False
        self.current_bet += amount
        self.current_pp += pp_amount
        self.current_21_p_3 += twenty_four_amount
        self.current_royal += royal_match_amount
        self.current_bust_amount += too_many_amount
        self.money -= amount
        self.money -= pp_amount
        self.money -= twenty_four_amount
        self.money -= royal_match_amount
        self.money -= too_many_amount
        return True

    def clear_hand(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        hand_value = sum(card.get_value() for card in self.hand)
        num_aces = sum(1 for card in self.hand if card.rank == 'A')

        # Adjust for Aces
        while hand_value > 21 and num_aces > 0:
            hand_value -= 10
            num_aces -= 1

        return hand_value

# Define dealer class
class Dealer:
    def __init__(self):
        self.hand = []

    def clear_hand(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        if not self.hand:
            return 0

        hand_value = sum(card.get_value() for card in self.hand)
        num_aces = sum(1 for card in self.hand if card.rank == 'A')

        # Adjust for Aces
        while hand_value > 21 and num_aces > 0:
            hand_value -= 10
            num_aces -= 1

        return hand_value

    def should_hit(self):
        return self.get_hand_value() < 17

# Define blackjack game class
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player", initial_money=500)
        self.dealer = Dealer()

    def reset_game(self):
        self.deck = Deck()
        self.player.clear_hand()
        self.dealer.clear_hand()

    def deal_initial_cards(self):
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

    def player_turn(self, dealer_first_card):
        block(), block()
        print(f"Player's Hand: {[str(card) for card in self.player.hand]} Total: {self.player.get_hand_value()}") 
        double_surrender_allow = True
        while True:
            if self.player.hand[1].rank == 'A' and self.player.hand[0].get_value() == 10 or self.player.hand[0].rank == 'A' and self.player.hand[1].get_value() == 10:
                return 2
            else:
                if self.player.get_hand_value() == 21:
                    break
                else:
                    if double_surrender_allow == True:
                        dealer_display(dealer_first_card)
                        action = input("Choose action (H, S, D, SR): ").lower()
                    else:
                        dealer_display(dealer_first_card)
                        action = input("Choose action (Hit or Stand): ").lower()
                        
            if action == "hit" or action == "h":
                double_surrender_allow = False
                self.player.add_card(self.deck.deal_card())
                hand_value = self.player.get_hand_value()

                block()
                print(f"P Hit: {[str(card) for card in self.player.hand]} T: {hand_value}")

                if hand_value > 21:
                    return -1  # Player busts

            elif action == "stand" or action == "s":
                break

            elif action == "double" or action == "d" and double_surrender_allow == True:
                if self.player.money >= self.player.current_bet:
                    self.player.money -= self.player.current_bet
                    self.player.current_bet *= 2
                    self.player.add_card(self.deck.deal_card())
                    block()
                    print(f"P D: {[str(card) for card in self.player.hand]} Total: {self.player.get_hand_value()}")
                    if self.player.get_hand_value() > 21:
                        return -1  # Player bustsbreak
                    else:
                        break
                else:
                    print("Insufficient funds to double down!")

            elif action == "surrender" or action == "sr" and double_surrender_allow == True:
                self.player.money += self.player.current_bet / 2
                block()
                print("Player surrenders.")
                return -0.5  # Player surrenders

            else:
                block()
                if double_surrender_allow == True:                    
                    print("Invalid input. Choose Hit, Stand, Double, or Surrender.")
                else:
                    if action == "surrender" or action == "sr":          
                        print("Not allow Surrender. Choose Hit or Stand")
                    elif action == "double" or action == "d":
                        print("Not allow Double. Choose Hit or Stand")
                    else:
                        print("Invalid input. Choose Hit or Stand.")
                block()
                print(f"P Hand: {[str(card) for card in self.player.hand]} Total: {self.player.get_hand_value()}")

        return 0  # Player stands

    def dealer_turn(self):
        block(), block()
        print(f"D Hand: {[str(card) for card in self.dealer.hand]} Total: {self.dealer.get_hand_value()}")
        while self.dealer.should_hit():
            self.dealer.add_card(self.deck.deal_card())
            block()
            print(f"D Hits: {[str(card) for card in self.dealer.hand]} Total: {self.dealer.get_hand_value()}")

    def settle_bets(self, result):
        player_hand_value = self.player.get_hand_value()
        dealer_hand_value = self.dealer.get_hand_value()
        dealer_card_count = len(self.dealer.hand)
        if result == -1:  # Player busts
            block(), block()
            print(f"D Hand: {[str(card) for card in self.dealer.hand]} Total: {self.dealer.get_hand_value()}")
            showing_result(player_hand_value, dealer_hand_value)
            print("Player busts! Dealer wins.")
        elif result == -0.5:  # Player surrenders
            block(), block()
            print(f"D Hand: {[str(card) for card in self.dealer.hand]} Total: {self.dealer.get_hand_value()}")
            showing_result(player_hand_value, dealer_hand_value)
            print("Player surrenders.")
        elif result == 2:  # Player Blackjack
            block()
            showing_result("BJ", dealer_hand_value)
            print("\n\tPlayer win Blackjack!\n")
            self.player.money += self.player.current_bet * 2.5
        else:
            if dealer_hand_value > 21:
                showing_result(player_hand_value, dealer_hand_value)
                print("Dealer busts! Player wins.")
                self.player.money += self.player.current_bet * 2
            elif player_hand_value > dealer_hand_value:
                showing_result(player_hand_value, dealer_hand_value)
                print("Player wins")
                self.player.money += self.player.current_bet * 2
            elif player_hand_value < dealer_hand_value:
                showing_result(player_hand_value, dealer_hand_value)
                print("Dealer wins")
            else:
                showing_result(player_hand_value, dealer_hand_value)
                print("Push (Tie).")
                self.player.money += self.player.current_bet
        if dealer_hand_value > 21:
            multiplier = {
                3: 2,
                4: 3,
                5: 11,
                6: 51,
                7: 101
            }

            self.player.money += self.player.current_bust_amount * multiplier.get(dealer_card_count, 251)
            block()
            print("Congratulations! Dealer Bust!!")
            print(f"Pay {multiplier.get(dealer_card_count, 251) - 1} : 1. You win: {self.player.current_bust_amount * multiplier.get(dealer_card_count, 251)}")

            '''
            if too_many_amount != 0:
                if dealer_card_count == 3:
                    self.player.current_bust_amount *= 2
                elif dealer_card_count == 4:
                    self.player.money += self.player.current_bust_amount * 3
                elif dealer_card_count == 5:
                    self.player.money += self.player.current_bust_amount * 10
                elif dealer_card_count == 6:
                    self.player.money += self.player.current_bust_amount * 51
                elif dealer_card_count == 7:
                    self.player.money += self.player.current_bust_amount * 101
                else:
                    self.player.money += self.player.current_bust_amount * 251
            '''

        # Clear current bet after settling
        self.player.current_bet = 0
        block_end(), block()


    def play_round(self):
        self.reset_game()
        self.deal_initial_cards()

        player_hand_value = self.player.get_hand_value()
        dealer_hand_value = self.dealer.get_hand_value()

        ## Side-bet  Perfect pair
        if self.player.current_pp != 0:
            if self.player.hand[0].rank == self.player.hand[1].rank:
                block()
                if self.player.hand[0].suit == "♥" and self.player.hand[1].suit == "♦" or self.player.hand[0].suit == "♦" and self.player.hand[1].suit == "♥" or self.player.hand[0].suit == '♠' and self.player.hand[1].suit == '♣' or self.player.hand[0].suit == '♣' and self.player.hand[1].suit == '♠':
                    print("Congratulation! You get a Perfect Pair!\nPay 12 to 1. You win:",self.player.current_pp*12)
                    self.player.money += self.player.current_pp*25
                else:
                    print("Congratulation! You get a Pair!\nPay 5 to 1. You win:",self.player.current_pp*5)
                    self.player.money += self.player.current_pp*5

        ## Side-bet  21+3
        if self.player.current_21_p_3 != 0:
            straight = False
            suit = False
            
            ranks = [self.player.hand[0].rank, self.player.hand[1].rank, self.dealer.hand[0].rank]
            ranks.sort()

            valid_straights = {
                ('10', 'J', 'Q'),
                ('J', 'Q', 'K'),
                ('A', '2', '3'),
                ('2', '3', '4'),
                ('3', '4', '5'),
                ('4', '5', '6'),
                ('5', '6', '7'),
                ('6', '7', '8'),
                ('7', '8', '9'),
                ('8', '9', '10'),
                ('9', '10', 'J'),
                ('10', 'J', 'Q'),
                ('J', 'K', 'Q'),
                ('A', 'Q', 'K')
            }

            if any(tuple(ranks[i:i+3]) in valid_straights for i in range(len(ranks)-2)):
                straight = True

            if self.player.hand[0].suit == self.player.hand[1].suit == self.dealer.hand[0].suit:
                suit = True

            if straight and suit:
                block()
                print("Congratulation! You win 21+3! (Straight flush)\nPay 40 to 1. You win: ",self.player.current_21_p_3*40)
                self.player.money += self.player.current_21_p_3 * 40
            elif suit:
                block()
                print("Congratulation! You win 21+3! (Flush)\nPay 5 to 1. You win: ",self.player.current_21_p_3*5)
                self.player.money += self.player.current_21_p_3 * 5
            elif straight:
                block()
                print("Congratulation! You win 21+3! (Straight)\nPay 10 to 1. You win: ",self.player.current_21_p_3*10)
                self.player.money += self.player.current_21_p_3 * 10

            if self.player.hand[0].rank == self.player.hand[1].rank == self.dealer.hand[0].rank:
                block()
                print("Congratulation! You win 21+3! (Three of a kind)\nPay 30 to 1. You win: ",self.player.current_21_p_3*30)
                self.player.money += self.player.current_21_p_3 * 30

        ## Side-bet  Royal Match
        if self.player.current_royal != 0:
            if self.player.hand[0].suit == self.player.hand[1].suit:
                block()
                if self.player.hand[0].rank == "Q" and self.player.hand[1].rank == "K" or self.player.hand[1].rank == "Q" and self.player.hand[0].rank == "K":
                    winning_royal = self.player.current_royal*25
                    print("||\t\t\t\t      ||\n||   You have same flush of Q & K!    ||")
                    if winning_royal >= 1000000000:
                        winning_royal = winning_royal/1000000000
                        block()
                        print("Congratulation! You win: {:.1f}B!".format(winning_royal))
                        print("||\t\t\t\t      ||")
                    elif winning_royal >= 1000000:
                        winning_royal = winning_royal/1000000
                        print("||\tPay 25 to 1. Win:{:.1f}M\t      ||\n||\t\t\t\t      ||".format(winning_royal))
                    elif winning_royal >= 10000:
                        winning_royal = winning_royal/1000
                        print("||\tPay 25 to 1. Win:{:.1f}K\t      ||\n||\t\t\t\t      ||".format(winning_royal))
                    else:
                        print("||\tPay 25 to 1. Win:",winning_royal,"\t      ||\n||\t\t\t\t      ||")
                    self.player.money += self.player.current_royal * 25
                else:
                    print("Congratulation! You win Royal Match! \n(Flush)Pay 5 to 2. You win:",self.player.current_royal*2.5)
                    self.player.money += self.player.current_royal * 2.5
            

        # Check for dealer blackjack immediately after dealing initial cards
        if self.dealer.hand[1].rank == 'A' and self.dealer.hand[0].get_value() == 10:
            block()
            print(f"P Hand: {[str(card) for card in self.player.hand]} Total: {self.player.get_hand_value()}")
            print(f"D Hand: {[str(card) for card in self.dealer.hand]} Total: {self.dealer.get_hand_value()}")

            if self.player.get_hand_value() == 21:
                showing_result("BJ", "BJ")
                print("Player and Dealer are Blackjack! \nIts a Push (Tie).")
                self.player.money += self.player.current_bet
            else:
                showing_result(player_hand_value, "BJ")
                block()
                print("\n\tDealer win Blackjack!\n")
            block_end(), block()
            return
        
        choice_bj = "no"
        self.player.insurance_bet = 0
        
        if self.dealer.hand[0].rank == 'A' and self.player.get_hand_value() == 21:
            block()
            block()
            choice_bj = "continue"
            block
            print("You get Blackjack! \nBut dealer's face-up card is Ace. Do you")
            choice_bj = input("want to win 1:1 or continue win 1:1.5 if\ndealer is not Blackjack? (win/continue): ").lower()
            if choice_bj == "win" or choice_bj == "w":
                self.player.money += self.player.current_bet * 2
                self.player.current_bet = 0
                if self.dealer.get_hand_value() == 21:
                    showing_result("BJ", "BJ")
                else:
                    showing_result("BJ", dealer_hand_value)
                return
            else:
                choice_bj = "nope"

        if self.dealer.hand[0].rank == 'A' and choice_bj == "no" :
            block()
            block()
            print("Dealer's face-up card is Ace.\nInsurance option available.")
            choice = input("Do you want to buy insurance? (y/n): ").lower()
            if choice == "yes" or choice == "y":
                insurance_amount = self.player.current_bet * (1/2)
                if self.player.money >= insurance_amount:
                    self.player.money -= insurance_amount
                    self.player.insurance_bet = insurance_amount

        if self.dealer.hand[0].rank == 'A' and self.dealer.hand[1].get_value() == 10:
            print(f"P Hand: {[str(card) for card in self.player.hand]} Total: {self.player.get_hand_value()}")
            print(f"D Hand: {[str(card) for card in self.dealer.hand]} Total: {self.dealer.get_hand_value()}")
            block()
            block()
            if self.player.insurance_bet > 0:
                print("\n\tDealer win Blackjack!\n")
                showing_result(player_hand_value, "BJ")
                print("Insurance pays 2:1.")
                self.player.money += self.player.insurance_bet * 2
            elif choice_bj == "nope":
                showing_result("BJ", "BJ")
                print("\nPlayer & Dealer have Blackjack!\n")
                self.player.money += self.player.current_bet
            else:
                print("\n\tDealer win Blackjack!\n")
                showing_result(player_hand_value, "BJ")
                print("Player loses.")
            block_end(), block()
            return

        # Call player_turn with dealer's first card
        player_result = self.player_turn(self.dealer.hand[0])

        if player_result == -1 or player_result == -0.5:
            self.settle_bets(player_result)
            return

        self.dealer_turn()
        self.settle_bets(player_result)
        self.player.current_bet = 0

# Main program loop
if __name__ == "__main__":
    fst_log_in = True
    game = BlackjackGame()
    
    while True:
        if fst_log_in:
            fst_log_in = False
            side_bet_choice = 0
            print("Welcome to BlackJack.\n")
            print("There have 3 choices of Side Bet:")
            print("1)Perfect Pair  2)21+3  \n")
            print("3)Royal Match   4)Dealer Bust\n")
            print("No side bet if not enter anything\n")
            
            while True:
                side_bet_choice = input("Enter the number you choose:  ")
                if side_bet_choice == "":
                    side_bet_choice = "0"
                result = extract_unique_digits(side_bet_choice)
                if result:
                    break
                else:
                    block()
                    print("You must enter valid number: {1, 2, 3, 4}")
                    block()
                    
            print("\n"*20)
            
        print(f"Player's Money: {int(game.player.money)}")
        
        while True:
            try:
                bet_amount = int(input("Place your bet amount (0 to quit): "))
                if bet_amount < 0:
                    block()
                    print("Please enter a positive number.")
                    block()
                else:
                    break  # Valid input, break out of the loop
            except ValueError:
                block()
                print("Invalid input. Enter a valid number.")
                block()

        if bet_amount == 0:
            block()
            block()
            print("Thanks for playing!")
            input("=======================MAKE=BY=HSC======")
            break
                
        ## Side bet 
        if 1 in result:
            while True:
                try:
                    i_pp_amount = 0
                    i_pp_amount = input("Place your Perfect Pair bet: ")

                    ## If user enters nothing, pp_amount = 0
                    if i_pp_amount == "":
                        pp_amount = 0
                    else:
                        pp_amount = int(i_pp_amount)
                        
                    if pp_amount < 0:
                        block()
                        print("Please enter a positive number.")
                        block()
                    else:
                        break  # Valid input, break out of the loop
                except ValueError: 
                    block()
                    print("Invalid input. Enter a valid number.")
                    block()
        else:
            pp_amount = 0

        if 2 in result:
            while True:
                try:
                    i_24_amount = 0
                    Twenty4_amount = 0
                    i_24_amount = input("Place your 21+3 bet: ")
                    
                    ## If user enters nothing, pp_amount = 0
                    if i_24_amount == "":
                        i_24_amount = 0
                    else:
                        Twenty4_amount = int(i_24_amount)
                        
                    if Twenty4_amount < 0:
                        block()
                        print("Please enter a positive number.")
                        block()
                    else:
                        break  # Valid input, break out of the loop
                except ValueError:
                    block()
                    print("Invalid input. Enter a valid number.")
                    block()
        else:
            Twenty4_amount = 0

        if 3 in result:
            while True:
                try:
                    i_royal_match_amount = 0
                    royal_match_amount = 0
                    i_royal_match_amount = input("Place your Royal Match bet: ")
                    
                    ## If user enters nothing, royal_match_amount = 0
                    if i_royal_match_amount == "":
                        i_royal_match_amount = 0
                    else:
                        royal_match_amount = int(i_royal_match_amount)
                        
                    if royal_match_amount < 0:
                        block()
                        print("Please enter a positive number.")
                        block()
                    else:
                        break  # Valid input, break out of the loop
                except ValueError:
                    block()
                    print("Invalid input. Enter a valid number.")
                    block()
        else:
            royal_match_amount = 0

        if 4 in result:
            while True:
                try:
                    i_too_many_amount = 0
                    too_many_amount = 0
                    i_too_many_amount = input("Place your Dealer Bust bet: ")
                    
                    ## If user enters nothing, royal_match_amount = 0
                    if i_too_many_amount == "":
                        i_too_many_amount = 0
                    else:
                        too_many_amount = int(i_too_many_amount)
                        
                    if too_many_amount < 0:
                        block()
                        print("Please enter a positive number.")
                        block()
                    else:
                        break  # Valid input, break out of the loop
                except ValueError:
                    block()
                    print("Invalid input. Enter a valid number.")
                    block()
        else:
            too_many_amount = 0
            
            
        if game.player.place_bet(bet_amount, pp_amount, Twenty4_amount, royal_match_amount, too_many_amount):
            game.play_round()
        else:
            block()
            print("Invalid bet amount. Please try again.")
