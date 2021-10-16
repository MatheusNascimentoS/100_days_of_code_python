from art import logo
import os
clear = lambda: os. system('cls')

def new_bidder():
    global greater_bid
    bidder = input("What's your name?: ")
    bid = int(input("What's your bid?: "))
    new_bidder_dict = {"Bidder": bidder, "Bid": bid}
    if bid > greater_bid["Bid"]: 
        greater_bid = new_bidder_dict
    
    bids_dictionary[len(bids_dictionary)+1] = new_bidder_dict

print(logo)
bids_dictionary = {}
greater_bid = {"Bidder": "Start", "Bid": 0}
while True:
    new_bidder()
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")
    clear()
    if other_bidder == "no":
        break
print(f'The winner is {greater_bid["Bidder"]} with a bid of ${greater_bid["Bid"]}.')
