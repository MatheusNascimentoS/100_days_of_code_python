from random import choice
def deal_card(user):
    card = choice(deck_of_cards)
    user.append(card)
    index_card = deck_of_cards.index(card)
    del(deck_of_cards[index_card])

def check_sum():
    global sum_player 
    global sum_dealer
    global end_game
    sum_player = sum_dealer = 0
    for hand in players_cards:
        sum_player += hand
    for hand in dealers_cards:
        sum_dealer += hand
    if 11 in players_cards and sum_player > 21:
        sum_player -= 10
    if 11 in dealers_cards and sum_dealer > 21:
        sum_dealer -= 10
    if sum_player > 21 or sum_dealer == 21:
        end_game = True
        print("Dealer Wins.1")
    elif sum_dealer > 21 or sum_player == 21:
        end_game = True
        print("Player Wins.1")
    
deck_of_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10]
players_cards = []
dealers_cards = []
sum_player = sum_dealer = 0

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
deal_card(players_cards)
deal_card(dealers_cards)
deal_card(players_cards)
deal_card(dealers_cards)
print(f"Your cards: {players_cards}")
print(f"Dealer's first card: {dealers_cards[0]}")
end_game = False
check_sum()
while not end_game: 
    hit_or_stand = input("Type 'h' to another card or 's' to stand: ")
    
    if hit_or_stand == "s":
        print(f"Dealer's cards: {dealers_cards}. Current score: {sum_dealer}")
        while True:
            if sum_dealer > sum_player:
                print("Dealer Wins.2")
                end_game = True
                break
            elif sum_player > sum_dealer and sum_dealer < 17:
                deal_card(dealers_cards)
                check_sum()
                print(f"Dealer's cards: {dealers_cards}. Current score: {sum_dealer}")
            elif sum_player > sum_dealer and sum_dealer >= 17:
                print("Player Wins.2")
                end_game = True
                break
    
    if hit_or_stand == "h":
        deal_card(players_cards)
        check_sum()
        print(f"Your cards: {players_cards}. Current score: {sum_player}")
        
    


