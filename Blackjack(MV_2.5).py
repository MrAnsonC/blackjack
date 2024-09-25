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
-- Fire 21

MV_2.5 on GitHub in 24 of September, 2024. 2329(NZST, GMT+12)
-- 4 Decks in games
-- Add the side bet odds

=========================================================================
    Type of Side bet                |     Odds
==================================================
Perfect Pair:                       |
--------------------------------------------------
Mixed Pair                          |    1 : 4
Colour Pair                         |    1 : 6
Perfect Pair                        |    1 : 10
Perfect Aces                        |    1 : 50 
==================================================
21+3:                               |
--------------------------------------------------
Flush                               |    1 : 5
Straight                            |    1 : 10
Three of a King (Same Ranks)        |    1 : 30
Straight Flush                      |    1 : 40
Suired Three of a King (Same Suits) |    1 : 100
==================================================
Royal Match:                        |
--------------------------------------------------
Player Flush                        |    2 : 5
Player suit and get "Q"&"K"         |    1 : 25
==================================================
Dealer Bust:                        |
--------------------------------------------------
Dealer get 3 cards and bust         |    1 : 1
Dealer get 4 cards and bust         |    1 : 2
Dealer get 5 cards and bust         |    1 : 10
Dealer get 6 cards and bust         |    1 : 50
Dealer get 7 cards and bust         |    1 : 100
Dealer get 8+ cards and bust        |    1 : 250
==================================================
Fire 21:  (Original 3 cards)        |
--------------------------------------------------
First 3 cards = 19                  |    1 : 1
First 3 cards = 20                  |    1 : 2
First 3 cards = 21                  |    1 : 4
  |-> With same flush               |    1 : 20
  --> 3 Cards are 7                 |    1 : 100
=========================================================================
Stop support version from:  MV_2.4    PCV_7.2(Last update)
=========================================================================
The latest version:  MV_2.5
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

# Side bet input
def get_side_bet_input(message):
    while True:
        try:
            amount = input(message)
            if amount == "":
                return 0
            amount = int(amount)
            if amount < 0:
                block()
                print("Please enter a positive number.")
                block()
            else:
                return amount
        except ValueError:
            block()
            print("Invalid input. Enter a valid number.")
            block()


# Result of card
def showing_result(player, dealer):
    block()
    print("||>\tPlayer    <|> \t  Dealer     <||\n||>\t ",
          player,"\t  <|> \t   ",dealer,"\t     <||")
    block()

# Extract the unique digits
def extract_unique_digits(numbers):
    unique_digits = set()
    approve_digits = {'0' ,'1', '2', '3', '4', '5'}
    
    for char in numbers:
        if char in approve_digits:
            unique_digits.add(char)
            
    return sorted(map(int, unique_digits))

# Define deck class
class Deck:
    def __init__(self, num_decks = 4):
        self.num_decks = num_decks
        self.cards = []
        self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        self.cards = [Card(rank, suit) for _ in range(self.num_decks) for suit in suits for rank in ranks]

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
        self.current_fire_3 = 0

    def place_bet(self, amount, pp_amount, twenty_four_amount, royal_match_amount, too_many_amount, fire_3_amount):
        self.current_bet = 0
        self.current_pp = 0
        self.current_21_p_3 = 0
        self.current_royal = 0
        self.current_bust_amount = 0
        self.current_fire_3 = 0
        T_bet = 0
        T_bet = amount + pp_amount + twenty_four_amount + royal_match_amount + too_many_amount + fire_3_amount
        if T_bet > self.money:
            print("Insufficient funds!")
            return False
        self.current_bet += amount
        self.current_pp += pp_amount
        self.current_21_p_3 += twenty_four_amount
        self.current_royal += royal_match_amount
        self.current_bust_amount += too_many_amount
        self.current_fire_3 += fire_3_amount
        self.money -= amount
        self.money -= pp_amount
        self.money -= twenty_four_amount
        self.money -= royal_match_amount
        self.money -= too_many_amount
        self.money -= fire_3_amount
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
            if self.player.current_bust_amount != 0:
                multiplier = {
                    3: 1,
                    4: 2,
                    5: 10,
                    6: 50,
                    7: 100
                }

                # Calculate winnings
                win_multiplier = multiplier.get(dealer_card_count, 250)
                winnings = self.player.current_bust_amount * (win_multiplier + 1)

                # Update player's money
                self.player.money += self.player.current_bust_amount * (win_multiplier + 1)

                # Block and print messages
                block()
                print("Congratulations! Dealer Bust!!")
                print(f"Pay 1 : {win_multiplier}. You win: {winnings}")

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
                if self.player.hand[0].suit == self.player.hand[1].suit:
                    if self.player.hand[0].rank == "A":
                        print("Congratulation! You get a Perfect Aces!\nPay 1 : 50. You win:",self.player.current_pp*50)
                        self.player.money += self.player.current_pp*50
                    else:
                        print("Congratulation! You get a Perfect Pair!\nPay 1 : 10. You win:",self.player.current_pp*10)
                        self.player.money += self.player.current_pp*10
                elif self.player.hand[0].suit == "♥" and self.player.hand[1].suit == "♦" or self.player.hand[0].suit == "♦" and self.player.hand[1].suit == "♥" or self.player.hand[0].suit == '♠' and self.player.hand[1].suit == '♣' or self.player.hand[0].suit == '♣' and self.player.hand[1].suit == '♠':
                    print("Congratulation! You get a Colour Pair!\nPay 1 : 6. You win:",self.player.current_pp*6)
                    self.player.money += self.player.current_pp*25
                else:
                    print("Congratulation! You get a Pair!\nPay 1 : 4. You win:",self.player.current_pp*4)
                    self.player.money += self.player.current_pp*4

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
                print("Congratulation! You win 21+3! (Straight flush)\nPay 1 : 40. You win: ",self.player.current_21_p_3*40)
                self.player.money += self.player.current_21_p_3 * 40
            elif suit:
                block()
                print("Congratulation! You win 21+3! (Flush)\nPay 1 : 5. You win: ",self.player.current_21_p_3*5)
                self.player.money += self.player.current_21_p_3 * 5
            elif straight:
                block()
                print("Congratulation! You win 21+3! (Straight)\nPay 1 : 10. You win: ",self.player.current_21_p_3*10)
                self.player.money += self.player.current_21_p_3 * 10

            if self.player.hand[0].rank == self.player.hand[1].rank == self.dealer.hand[0].rank:
                block()
                if self.player.hand[0].suit == self.player.hand[1].suit == self.dealer.hand[0].suit:
                    print("Congratulation! You win 21+3! (Rank 3 of a kind)\nPay 1 : 100. You win: ",self.player.current_21_p_3*100)
                    self.player.money += self.player.current_21_p_3 * 100
                else:
                    print("Congratulation! You win 21+3! (3 of a kind)\nPay 1 : 30. You win: ",self.player.current_21_p_3*30)
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
                        print("||\tPay 1 : 25. Win:{:.1f}M\t      ||\n||\t\t\t\t      ||".format(winning_royal))
                    elif winning_royal >= 10000:
                        winning_royal = winning_royal/1000
                        print("||\tPay 1 : 25. Win:{:.1f}K\t      ||\n||\t\t\t\t      ||".format(winning_royal))
                    else:
                        print("||\tPay 1 : 25. Win:",winning_royal,"\t      ||\n||\t\t\t\t      ||")
                    self.player.money += self.player.current_royal * 25
                else:
                    print("Congratulation! You win Royal Match! \n(Flush)Pay 2 : 5. You win:",self.player.current_royal*2.5)
                    self.player.money += self.player.current_royal * 2.5

        ##Side bet  Fire 3
        if self.player.current_fire_3 != 0:
            if self.dealer.hand[0].rank == "J" or self.dealer.hand[0].rank == "Q" or self.dealer.hand[0].rank == "K":
                dealer_hand_values = 10
            elif self.dealer.hand[0].rank == "A":
                test_1_or_11 = player_hand_value + 1
                if test_1_or_11 > 18 and test_1_or_11 < 22:
                    dealer_hand_values = 1
                else:
                    dealer_hand_values = 11
            else:
                dealer_hand_values = self.dealer.hand[0].rank
            three_cards_total = player_hand_value + int(dealer_hand_values)
            if three_cards_total > 18 and three_cards_total < 22:
                block()
                if three_cards_total == 19:
                    print("Congratulation! You win Fire 3! (19)\nPay 1 : 1. You win: ",self.player.current_fire_3*2)
                    self.player.money += self.player.current_fire_3*2
                elif three_cards_total == 20:
                    print("Congratulation! You win Fire 3! (20)\nPay 1 : 2. You win: ",self.player.current_fire_3*3)
                    self.player.money += self.player.current_fire_3*3
                else:
                    if self.player.hand[0].suit == self.player.hand[1].suit == self.dealer.hand[0].suit:
                        print("Congratulation! You win Fire 3! (21)\nPay 1 : 20. You win: ",self.player.current_fire_3*20)
                        self.player.money += self.player.current_fire_3*21
                    elif self.player.hand[0].rank == 7 and self.player.hand[1].rank == 7 and self.dealer.hand[0].rank == 7:
                        print("Congratulation! You win Fire 3! (21)\nPay 1 : 100. You win: ",self.player.current_fire_3*100)
                        self.player.money += self.player.current_fire_3*101
                    else:
                        print("Congratulation! You win Fire 3! (21)\nPay 1 : 4. You win: ",self.player.current_fire_3*4)
                        self.player.money += self.player.current_fire_3*4
            
            

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

    def display_deck(self):
        suits = ['♥', '♦', '♣', '♠']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        card_count = {suit: {rank: 0 for rank in ranks} for suit in suits}
        total_count = {rank: 0 for rank in ranks}

        # Count the cards remaining in the deck
        for card in self.deck.cards:
            card_count[card.suit][card.rank] += 1

        for suit in suits:
            for rank in ranks:
                total_count[rank] += card_count[suit][rank]

        # Print table header
        print("\n   A  2  3  4  5  6  7  8  9  X  J  Q  K")
        # print("\n   A  2  3  4  5  6  7  8  9  X  J  Q  K  ||  T")

        # Print each row for suits with counts
        for suit in suits:
            row = [str(card_count[suit][rank]) for rank in ranks]
            total = sum(card_count[suit][rank] for rank in ranks)
            print(f"{suit}  {'  '.join(row)}")
            # print(f"{suit}  {'  '.join(row)}  || {total}")
        # print("================================================")
        block()
        total_row = [f"{total_count[rank]:02}" for rank in ranks]
        total_sum = sum(total_count[rank] for rank in ranks)
        print(f"  {' '.join(total_row)}")
        # print(f"   {' '.join(total_row)} || {total_sum}")
        print()

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
            print("1)Perfect Pair  2)21+3  3)Royal Match")
            print("4)Dealer Bust   5)Fire 3")
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
                    print("You must enter 1, 2, 3, 4, 5")
                    block()
                    
            print("\n"*20)
            
        print(f"Player's Money: {int(game.player.money)}")

        if len(game.deck.cards) < 45:
            print("Card have been reset!")
            game.deck.generate_deck()
            game.deck.shuffle()
        
        while True:
            bet_amount = input("Place your bet amount (0 to quit): ")
            if bet_amount.lower() == "dev":
                game.display_deck()
                continue 
            try:
                bet_amount = int(bet_amount)
                if bet_amount < 0:
                    print("Please enter a positive number.")
                else:
                    break
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
            pp_amount = get_side_bet_input("Place your Perfect Pair bet: ")
        else:
            pp_amount = 0

        if 2 in result:
            Twenty4_amount = get_side_bet_input("Place your 21+3 bet: ")
        else:
            Twenty4_amount = 0

        if 3 in result:
            royal_match_amount = get_side_bet_input("Place your Royal Match bet: ")
        else:
            royal_match_amount = 0

        if 4 in result:
            too_many_amount = get_side_bet_input("Place your Dealer Bust bet: ")
        else:
            too_many_amount = 0

        if 5 in result:
            fire_3_amount = get_side_bet_input("Place your Fire 3 bet: ")
        else:
            fire_3_amount = 0
            
            
        if game.player.place_bet(bet_amount, pp_amount, Twenty4_amount, royal_match_amount, too_many_amount, fire_3_amount):
            game.play_round()
        else:
            block()
            print("Invalid bet amount. Please try again.")
