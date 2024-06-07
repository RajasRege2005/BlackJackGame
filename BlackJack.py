import random
from artbj import logo
print(logo)
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer=[]
player=[]
def compare(player_score,dealer_score):
    if player_score==dealer_score:
        print("It's a draw.")
    elif dealer_score==0 or player_score>21:
        print("Computer wins.") 
    elif player_score==0 or dealer_score>21:
        print("Player wins.")
    else:
        if(player_score>dealer_score):
            print("User wins.")
        else:
            print("Computer wins")               
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0 
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def dealer_card():
    dealer_cards=random.choice(cards)
    return dealer_cards
for _ in range(2):
    player.append(dealer_card())
    dealer.append(dealer_card())
game_end=False    
while not game_end:    
    player_score=calculate_score(player)
    dealer_score=calculate_score(dealer)
    print(f"Your cards:{player} ,current score={player_score}")
    print(f"Dealer's first card:{dealer[0]}")
    if player_score==0 or dealer_score==0 or player_score>21:
        game_end=True
    else:
        choice=input("Type 'y' for adding another card or 'n' to pass:")
        if choice=="y":
            player.append(dealer_card())
        else:
            game_end=True    
while dealer_score!=0 and dealer_score<17:
    dealer.append(dealer_card())
    dealer_score=calculate_score(dealer) 
print(f"Player's final cards:{player}, score={player_score}")
print(f"Dealer's final cards:{dealer}, score={dealer_score}")    
compare(player_score,dealer_score)     
          