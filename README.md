PCV means Personal Computer Version   |||   MV means Mobile Version

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
-- Bug: If player get Blackjack but dealer get "A", will ask player want to buy insurance or not. 
		The correct situation will be asking player want to win 1:1 or 1:1.5 if dealer is not Blackjack.

Update to PCV_6 in 17 of June, 2024. 
-- Create layout to convenient watching.

Create MV_1 in 19 of June, 2024. 
-- More easy to run on the mobile. ~~Testing by Xiaomi 13T pro ~~Using app "Coding python"

Upload MV_1 on FB Group "Python" in 20 of June, 2024. 1901(NZT, GMT+12) Link: https://www.facebook.com/groups/python
								(				Update: Post delete)

Upload MV_1 on GitHub in 20 of June, 2024. 1925(NZT, GMT+12)

Reupload MV_1 on GitHub in 20 of June, 2024. 2050(NZT, GMT+12)

Upload MV_2 on GitHub in 20 of June, 2024. 2319(NZST, GMT+12)
-- Make the side bet of Perfect Pair(PP), if win, 5:1.
-- When start the program, will ask you do you want to play side-bet.
-- Fix the UI problem
-- Because original PP is using 208 card but this program using 52 cards,
                          25:1 of same suits and same ranks NOT AVAILABLE
-- To optimization: If player get same colour of PP, 12:1

Upload PCV_7 on GitHub in 21 of June, 2024. 0000(NZST, GMT+12)

Upload MV_2.1 on GitHub in 21 of June, 2024. 0925(NZST, GMT+12)
-- PCV_7 will be update soon.
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

                Side bet odds:
Perfect Pair:
Getting same colour Pair:           1 : 12
Pair:                               1 : 5

21+3:
Player and Dealer Straight Flush:   1 : 40
Three of a kind:                    1 : 30
Player and Dealer Straight:         1 : 10
Player and Dealer Flush:            1 : 5

Royal Match:
Player suit and get "Q"&"K":        1 : 25
Player Flush:                       2 : 5

Dealer Bust:
Dealer get 3 cards and bust:        1 : 1
Dealer get 4 cards and bust:        1 : 2
Dealer get 5 cards and bust:        1 : 10
Dealer get 6 cards and bust:        1 : 50
Dealer get 7 cards and bust:        1 : 100
Dealer get 8+ cards and bust:       1 : 250

=========================================================================

Special mode: SP_War_of_Casino(Core MV_2.2)
Special mode: SP_Blazing_7s(Core MV_2.2)

Stop support version from:  MV_2.3    PCV_7.2

=========================================================================

The latest version:  MV_2.4    PCV_7.2

=========================================================================
Future target:
1. Make the "Split" function
2. Accept special side-bet. Match with dealer(MWD)
3. Make some special mode......
4. Make the GUI version
5. Make it in java and C++
