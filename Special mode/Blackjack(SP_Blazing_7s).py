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
=========================================================================
This is a special mode of Blackjack. (Remember, update will be available
only in GitHub: https://github.com/MrAnsonC/blackjack/tree/main/Special%20mode)

-- Core MV_2.2, Blazing 7S.
--  If player bet "Blazing 7S", must bet in 5 dollor.

        Only calculate the first two card of player
            and first card of dealer(Exculde situation 6)
                                
        1) If player's own a card "7", win $10.
        2) If player's own a pair of "7", win $125.
        3) If player's own a pair of "7" and dealer
            get "7", win $200
        4) If player's own a pair of "7" with same colour
           suit,win 10% of the total pool.(At least 500)
        5) If player's own a pair of "7" with same colour
           suit and dealer get "7",win 50% of the total
                                      pool.(At least 1000)
        6) If player's own a pair of "7" with same colour
               suit, and dealer also get a pair of "7",
               win 100% of the total pool.(At least 2000)

        **Situation 6 is not the offical winning method.
                That because this program only use 52
                cards and random everytime.
           

Example: Player bet $20 in on normal betting and type
         "Yes" or "Y" on "Blazing 7S".

         The first card player get "7♥".

         Situation 1
         If dealer get "9♦" and your another card get
                              "8♥", you will win $10.
         Situation 2                    
         If dealer get "9♦" and your another card get
                             "7♣", you will win $75.
         Situation 3                    
         If dealer get "7♦" and your another card get
                             "7♣", you will win $150.
         Situation 4                    
         If dealer get "9♦" and your another card get
                             "7♦", you will win $150
                                or 10% of total pool.
         Situation 5                   
         If dealer get "7♣" and your another card get
                             "7♦", you will win $600
                                or 50% of total pool.
         Situation 6                   
         If dealer get a pair of "7"and your another
                   card get "7♦", you will win $1200
                                or 100% of total pool.
=========================================================================
Stop support version from:  MV_2.1    PCV_7.1
=========================================================================
The latest version:  MV_2.2    PCV_7.2
'''

import random

# Define card suits and ranks
suits = ['♥', '♦', '♣', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
##ranks = ['7', '8' ]

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
def block2():
    print("||||||||||||||||||||||||||||||||||||||||")
def block_end():
    print("=======================END==GAME========")

# Result of card
def showing_result(player, dealer):
    block()
    print("\tPlayer   |||   \tDealer\n\t ",
          player,"\t |||\t ",dealer)
    block()

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
    def __init__(self, name, int_money, int_jackpot):
        self.name = name
        self.money = int(int_money)
        self.jackpot = int(int_jackpot)
        self.hand = []
        self.current_bet = 0
        self.current_pp = 0
        self.current_21_p_3 = 0
        self.current_bz7 = 0
        self.insurance_bet = 0

    def place_bet(self, amount, pp_amount, twenty_four_amount, bz7_amount):
        self.current_bet = 0
        self.current_pp = 0
        self.current_21_p_3 = 0
        self.current_bz7 = 0
        
        T_bet = 0
        T_bet = amount + pp_amount + twenty_four_amount + bz7_amount
        if T_bet > self.money:
            print("Insufficient funds!")
            return False
        self.current_bet += amount
        self.current_pp += pp_amount
        self.current_21_p_3 += twenty_four_amount
        self.current_bz7 += bz7_amount
        self.money -= T_bet
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
        self.player = Player("Player", int_money=500, int_jackpot=1000)
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
        if result == -1:  # Player busts
            block(), block()
            print(f"D Hand: {[str(card) for card in self.dealer.hand]} Total: {self.dealer.get_hand_value()}")
            showing_result(player_hand_value, dealer_hand_value)
            print("Player busts! Dealer wins.")
            block(), block()
        elif result == -0.5:  # Player surrenders
            block(), block()
            print(f"D Hand: {[str(card) for card in self.dealer.hand]} Total: {self.dealer.get_hand_value()}")
            showing_result(player_hand_value, dealer_hand_value)
            print("Player surrenders.")
            block_end(), block()
        elif result == 2:  # Player Blackjack
            block()
            showing_result("BJ", dealer_hand_value)
            print("\n\tPlayer win Blackjack!\n")
            self.player.money += self.player.current_bet * 2.5
            block_end(), block()
        else:
            if dealer_hand_value > 21:
                showing_result(player_hand_value, dealer_hand_value)
                print("Dealer busts! Player wins.")
                block_end(), block()
                self.player.money += self.player.current_bet * 2
            elif player_hand_value > dealer_hand_value:
                showing_result(player_hand_value, dealer_hand_value)
                print("Player wins")
                block_end(), block()
                self.player.money += self.player.current_bet * 2
            elif player_hand_value < dealer_hand_value:
                showing_result(player_hand_value, dealer_hand_value)
                print("Dealer wins")
                block_end(), block()
            else:
                showing_result(player_hand_value, dealer_hand_value)
                print("Push (Tie).")
                block_end(), block()
                self.player.money += self.player.current_bet

        # Clear current bet after settling
        self.player.current_bet = 0


    def play_round(self):
        self.reset_game()
        self.deal_initial_cards()

        player_hand_value = self.player.get_hand_value()
        dealer_hand_value = self.dealer.get_hand_value()

        ## Special mode bet -- Blazing 7S!!!!!!!!!!!!
        if self.player.current_bz7 != 0:
            player_have_a_pair_of_seven = False
            player_hand_one_is_seven = False
            player_hand_two_is_seven = False
            dealer_hand_one_is_seven = False
            dealer_hand_two_is_seven = False
            dealer_hand_one_is_seven_suit = False
            player_suit_of_7 = False
                
            if self.player.hand[0].rank == "7":
                player_hand_one_is_seven = True
            if self.player.hand[1].rank == "7":
                player_hand_two_is_seven = True
            if self.dealer.hand[0].rank == "7":
                dealer_hand_one_is_seven = True
                
            if player_hand_one_is_seven == True and player_hand_two_is_seven == True:
                if self.player.hand[0].suit == "♥" and self.player.hand[1].suit == "♦" or self.player.hand[0].suit == "♦" and self.player.hand[1].suit == "♥" or self.player.hand[0].suit == '♠' and self.player.hand[1].suit == '♣' or self.player.hand[0].suit == '♣' and self.player.hand[1].suit == '♠':
                    player_suit_of_7 = True
                    if (dealer_hand_one_is_seven):
                        dealer_hand_one_is_seven_suit = True
                        if self.dealer.hand[1].rank == "7":
                            dealer_hand_two_is_seven = True
                else:
                    player_have_a_pair_of_seven = True
            elif self.dealer.hand[0].rank == "7":
                dealer_hand_one_is_seven = False

            if dealer_hand_two_is_seven == True:
                block()
                print("  Congratulation! You win BLAZING 7S!!")
                block2()
                print("\t  Player and Dealer \n    Have a pair of same colour suit!")
                print("   You WIN 100% of the pool or $2000")
                self.player.money += max(self.player.jackpot, 1200)
                self.player.jackpot = max(self.player.jackpot - 1300, 1000)
            elif dealer_hand_one_is_seven_suit == True:
                block()
                print("  Congratulation! You win BLAZING 7S!!")
                block2()
                print("  Player have a pair of same colour suit!")
                print("    Dealer also get a 7!")
                block()
                print("  You WIN 50% of the pool or $1000")
                self.player.money += max(self.player.jackpot*0.5, 600)
                self.player.jackpot = max(1000, self.player.jackpot*0.43)
            elif player_suit_of_7 == True:
                block()
                print("  Congratulation! You win BLAZING 7S!!")
                block2()
                print("Player have a pair of same colour suit!")
                block()
                print("    You WIN 10% of the pool or $150")
                self.player.money += max(self.player.jackpot*0.1, 150)
                self.player.jackpot = max(1000, self.player.jackpot*0.87)
            elif dealer_hand_one_is_seven == True:
                block()
                print("  Congratulation! You win BLAZING 7S!!")
                block2()
                print(" Player have a pair of \"7\" and dealer's \n      face-up is \"7\"! You WIN $150")
                self.player.money += 150
            elif player_have_a_pair_of_seven == True:
                block()
                print("  Congratulation! You win BLAZING 7S!!")
                block2()
                print("Player have a pair of \"7\". You WIN $75")
                self.player.money += 75
            elif player_hand_two_is_seven == True or player_hand_one_is_seven == True:
                block()
                print("  Congratulation! You win BLAZING 7S!!")
                print("     Player have a \"7\". You WIN $10")
                self.player.money += 10
                
        # Blazing 7S Jackpot 
        self.player.jackpot += self.player.current_bet*0.4 + (self.player.current_bz7 - 3)
            
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
            choice_bj = input("want to win 1:1 or continue win 1:1.5 \nif dealer is not Blackjack? (win/continue): ").lower()
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
            print("Welcome to BJ.\n")
            print("There have 4 choices of Side Bet:")
            print("1. No Side-Bet    3. Perfect Pair  \n2. 21+3   \t  4. 21+3 & PP")
            side_bet_choice = input("Enter the number you choose:  ")
            if side_bet_choice not in ["2", "3", "4"]:
                side_bet_choice = "1"
            block(),block(),block(),block(),block()

        block()
        print(f"||\t  Blazing Jackpot: {int(game.player.jackpot)}\t      ||")
        block()
        print(f"Player's Money: {int(game.player.money)}")
        
        while True:
            try:
                block()
                bet_amount = int(input("Place your bet amount (0 to quit): "))
                if bet_amount < 0:
                    block()
                    print("Please enter a positive number.")
                else:
                    break  # Valid input, break out of the loop
            except ValueError:
                block()
                print("Invalid input. Enter a valid number.")

        ## Special mode bet -- Blazing 7S!!!!!!!!!!!!
        i_bz7_amount = 0
        bz7_amount = 0
                
        i_bz7_amount = input("$5 to play Blazing 7S amount? (Y/N) ").lower()
        if i_bz7_amount == "y" or i_bz7_amount == "yes":
            bz7_amount = 5
        else:
            bz7_amount = 0

        ## Side bet 
        if side_bet_choice == "3" or side_bet_choice == "4":
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
                        print("Please enter a positive number.")
                    else:
                        break  # Valid input, break out of the loop
                except ValueError:
                    print("Invalid input. Enter a valid number.")

        if side_bet_choice == "2" or side_bet_choice == "4":
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
                        print("Please enter a positive number.")
                    else:
                        break  # Valid input, break out of the loop
                except ValueError:
                    print("Invalid input. Enter a valid number.")
                    
        if side_bet_choice == "1":
            pp_amount = 0
            Twenty4_amount = 0

        if side_bet_choice == "2":
            pp_amount = 0

        if side_bet_choice == "3":
            Twenty4_amount = 0

        if bet_amount == 0:
            print("Thanks for playing!")
            break
            
        if game.player.place_bet(bet_amount, pp_amount, Twenty4_amount, bz7_amount):
            game.play_round()
        else:
            print("Invalid bet amount. Please try again.")

