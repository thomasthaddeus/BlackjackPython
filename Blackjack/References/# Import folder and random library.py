# Import folder and random library
import playing_cards
import random
# Function to deal one cand
# Parameters: No parameters
# Returns: A string containing two characters) representing
# the card delt, i.e. 2H' meaning 2 of Hearts
def deal_one_card():
    # Create an empty list for player hand and dealer hand.
    player_hand = []
    dealer_hand = []
    #define variables
    play_choice == 'y'
    win = 0
    draw = 0
    lose = 0
    game_count = 0
    # Prompt text to ask user on game play.
    prompt_text = input("\nWould you like to play BlackJack [y]n]?')
    while prompt_text !='n' and prompt_text !='y': 
        prompt_text = get_play_choice ("\nPlay again [yn]?) # If statement if user selects no. if prompt_text == print("Goodbye') print('You played win, games!") print('-> Won: win) print("--> Lost: lose) print('-> Drawn: ', draw) elif prompt_text # Deal first card for player. card = playing_cards.deal_one_card() # Append it to the player hand. player_hand.append(card) # Deal second card for player. card = playing_cards.deal_one_card() # Append it to the player_hand. player_hand.append(card) # Deal first care for dealer. card = playing_cards.deal_one_card() # Append it to the dealer hand. dealer_hand.append(card) .
30
31
32
33
34
35
36
37
38
39
40
41
42
43 HDD D D D D D D D ) # Deal second card for dealer. card = playing_cards.deal_one_card() # Append it to the dealer_hand. dealer_hand.append (card) # Display the player's hand and dealer's hand to the # screen calling functions. display_hand("\nDealer\'s hand is ', dealer_hand) display_hand("\nPlayer\'s hand is" player_hand) dealer_total= get_hand_total (dealer_hand) player_total= get_hand_total (player_hand) # If player and dealer's hand 21 count as draw.
if player_total == 21 and dealer_total == 21:
    print("*** Blackjack --")
    display_hand("\nDealer\'s hand is" , dealer_hand)
    display_hand("\nPlayer\'s hand is ', player_hand)
    print("*** Blackjack! Push no winners! ***")
    print("\n---- END GAME print("\nThas was fun!')
    draw += 1
    game count += 1
    lose COCOCOON N9 H Ở LÊN CỦ - ỞI Ấn 5 LÀ NỤ H Ở get_play_choice () # If user inputs no, provide summary details. if prompt text == 'n': print('Goodbye') print('You played', win, games!') print("-> Won: win) print('.-> Lost: print('-> Drawn : , draw) # If player_total 1s 21 and dealer_total Won: 'win) print('-> Lost: lose) print('-> Drawn: # If player total total is not 21 and dealer total is = 21, dealer wins. elif player_total != 21 and dealer_total == 21 : display_hand("\nDealer\'s hand is ', dealer_hand) print("*** Blackjack! Dealer Wins! ****) . print("\n---- print("\nThas was fun!') lose += END GAME 91 1 93 game count += 1 get_play_c 96 . a 100 lose) 101 102 100 103 yet _choice () user inputs no, provide summary details. if play_again_choice == 'n': print("Goodbye') print('You played , win, ! games!') print(" -> Won: ', win) print('-> Lost: print('-> Drawn: 'draw) else : play_player_hand (player_hand) play_dealer hand (dealer hand) player-total = get_hand total (player_hand) dealer_total = get_hand total (dealer_hand) Eween 15 and 21 for player and 17 and 21, whichever is greater, determines winner. if player yer_total >= 15 and and player_total = 21 and dealer_total >= 17 and dealer_total dealer_total : printi' --- Dealer: 7 dealer_total,' Player: ', player_total ,'-> Player Wins! ---') 104 105 106 107 108 109 if player 110 211 print("\n- END GAME ') 112 print("\nThat was fun!') win += 1 113 11 114 *** 115 += game_count 116 117 118 119 get_play_choice () user inputs no, provide summary details if prompt_text == 'n': print('Goodbye') print('You played win, I games!') print('-> Won: 'win) 
                 print('-> Lost: ! lose) 
                 print('-> Drawn: ', draw)
                 elif player_total Drawn: draw) # If dealer total 19 more than 21 then dealer loses. elif player_total >= 15 and player_total = 21 : print('--- Dealer:", dealer_total,' Player: • player_total '-> Player Wins! print("\n----- -') print("\nThat was fun!') 168 ---') 1 169 END GAME 170 171 win += 1 172 173 174 175 176 177 178 game_count += 1 get_play_choice () # If user inputs no, provide summary details. if prompt text == 'n': print('Goodbye') print("You played', win, games!') print('-> Won: win) print('-> Lost: ', lose) print('-> Drawn: ', draw) # If the afommentioned didn't meet the arguments, then it's a draw. else : print('--- Dealer: ', dealer_total,' Player: ', player_total , 'Push - no winners! print("\n--- END GAME print("\nThat was fun!') 179 180 181 182 183 ---') 184 185 186 draw += 1 187 game_count += 1 188 189 190 191 192 get_play_choice () # If user inputs no, provide summary details. if prompt text == 'n': print('Goodbye') print('You played', win, games!') print("-> Won: print("-> Lost: ', lose) print('-> Drawn: ', draw) return player_hand, dealer_hand 193 win) 194 195 196 197 199 200 11 201 198 fief get_hit_choice(): #define string variable hit_choice = # Create a while loop to validate data on hit or stand. while hit_choice != 's' or hit_choice != 'h': hit choice = input('\nPlease enter h or s (n = Hit, s= Stand): ') return hit choice 202 203 204 205
211 212 216 206 def get_play_choice (prompt_text): 207 # create play_choice string variable 208 play_choice 209 # Create a while loop to validate user input on whether they would like to play again. 210 while play_choice != 'y' or play_choice != 'n': play_choice = input (prompt_text) return play_choice 213 214 def display_hand (hand_text, hand) : 215 # call get_hand total function total = str (get_hand_total (hand)) 217 # Create a deck string variable. deck = 1 # Replace lettering with suit names and append to hand. for card_name in enumerate (hand) : card_name = card_name.replace('C', 'of Clubs') card_name = card_name.replace('D', 'of Diamonds') card_name = card_name.replace(':', 'of Hearts') card_name = card_name.replace('s', 'of Spades') # Card name is replaced to deck string: deck += card_name + 'T print (hand_text + total + ':' + deck[:-3]) return deck 218 219 220 221 222 223 224 225 226 227 228 229 230 def get_hand_total (hand) : # Define Points accumulator 231 232 total = 0 233 234 235 # Create a for loop to start at 0 and the cards that are drawn. for card in hand: # Create if-elif-else statements to determine suitable points for KQ. Jor Ten. 'K' or card == 'Q' or card == # Accumulate 10 points. 236 if card == "J': 237 238 total += 10 239 # Else if Ace drawn will add 11 otherwise if more than 21 will only add 1 point. 240 elif card == 'A': 241 if Points > 11: 242 total += 1 243 else: 244 total += 11 245 # Else, if any of the cards are anything, then will add chose points to the variable. 246 else:
247 total += card 
248 # If the draw of hand deals either I. K. 0. J then 21 points is given and Blackjack. 
if hand > 1: 
249 
250 if card == 'K' or card == 'Q' or card == 'J': 
251 total = 21 252 # Return the function return total 253 254 257 bust = False 259 255 def play_player_hand (player_hand) : 256 # define variables including bust and hit_choice (hit or stand) hit choice = 1 258 # Call get_hand_total function player_total = get_hand_total (player_hand) #while user bust 13 False while bust == False: # Call get hit_choice function. hit_choice = get_hit_choice ()
260
261
262
263
264
265 if hit choice == 'h': 
266
267
268
269
270 # Import playing_card file to hand and call deal_one_card Iunction card = playing_card.deal_one_card() # Call display_hand Iunction. display_hand('\nPlayer\'s hand is', player_hand) # Call ger_hand_total function player_total = get_hand_total (player_hand) # If player score is 21 or greater and choice is hic, print player busts. if player_total >= 21 and hit_choice == 'n': bust = True 271 272 273 274 275 276 277 print('--> Player busts!') # Else le choice is stand and greater than 15 then hit_choice is true. elif hit_choice == 's' and player_total >= 15: hit_choice = True # IF user selects stand and score is less than 15 print error and add one card to hand. 278 279 280 else: 281 282 283 284 hit_choice == 's' and player_total Dealer busts!') return dealer total 
296 card = 
297 
298
299
300
301
302
303
304
305
