import random

# Define card suits and ranks
suits = ['♥', '♦', '♣', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
##ranks = ['K', 'A']

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
    def __init__(self, name, initial_money=500):
        self.name = name
        self.money = int(initial_money)
        self.hand = []
        self.current_bet = 0
        self.insurance_bet = 0

    def place_bet(self, amount):
        self.current_bet = 0
        if amount > self.money:
            print("Insufficient funds!")
            return False
        self.current_bet += amount
        self.money -= amount
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
                        print("Not allow Surrender. Choose Hit or Stand.")
                    elif action == "double" or action == "d":
                        print("Not allow Double. Choose Hit or Stand.")
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
            print("\n\t   Player wins Blackjack!\n")
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

        # Check for dealer blackjack immediately after dealing initial cards
        if self.dealer.hand[1].rank == 'A' and self.dealer.hand[0].get_value() == 10:
            block()
            print("Dealer has Blackjack!")
            
            if self.player.get_hand_value() == 21:
                print(f"P Hand: {[str(card) for card in self.player.hand]} Total: {self.player.get_hand_value()}")
                print(f"D Hand: {[str(card) for card in self.dealer.hand]} Total: {self.dealer.get_hand_value()}")
                showing_result("BJ", "BJ")
                print("Player and Dealer is Blackjack! Push (Tie).")
                block_end(), block()
                self.player.money += self.player.current_bet
            else:
                block()
                print(f"P Hand: {[str(card) for card in self.player.hand]} Total: {self.player.get_hand_value()}")
                print(f"D Hand: {[str(card) for card in self.dealer.hand]} Total: {self.dealer.get_hand_value()}")
                showing_result(player_hand_value, "BJ")
                print("Dealer win! Player loses!")
            return
        
        choice_bj = "no"
        self.player.insurance_bet = 0
        
        if self.dealer.hand[0].rank == 'A' and self.player.get_hand_value() == 21:
            block()
            block()
            choice_bj = "continue"
            block
            print("You get Blackjack! \nBut dealer's face-up card is Ace")
            choice_bj = input("Do you want to win 1:1 or win 1:1.5 \nif dealer is not Blackjack? (win/continue): ").lower()
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
                print("\n\t   Dealer has Blackjack!")
                showing_result(player_hand_value, "BJ")
                print("Insurance pays 2:1.")
                self.player.money += self.player.insurance_bet * 2
            elif choice_bj == "nope":
                showing_result("BJ", "BJ")
                print("Dealer has Blackjack. Its a Push (Tie).")
                self.player.money += self.player.current_bet
            else:
                print("Dealer has Blackjack!")
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
    game = BlackjackGame()

    while True:
        print(f"Player's Money: {int(game.player.money)}")
        while True:
            try:
                bet_amount = int(input("Place your bet amount (0 to quit): "))
                if bet_amount < 0:
                    print("Please enter a positive number.")
                else:
                    break  # Valid input, break out of the loop
            except ValueError:
                print("Invalid input. Enter a valid number.")
                block()

        if bet_amount == 0:
            print("Thanks for playing!")
            break
            
        if game.player.place_bet(bet_amount):
            game.play_round()
        else:
            print("Invalid bet amount. Please try again.")
            block()
