from art import logo
from art import vs
from data_game import data
from random import choice
import os
clear = lambda: os. system('cls')

def new_instagram():
    return choice(data)

def instagram_to_compare(insta_1, a, insta_2, b):
    print(f"Compare {a}: {insta_1['name']}, {insta_1['description']}, from {insta_1['country']}.")
#    print(f"dica: {insta_1['follower_count']}")
    print(vs)
#    print(f"dica: {insta_2['follower_count']}")
    print(f"Compare {b}: {insta_2['name']}, {insta_2['description']}, from {insta_2['country']}. ")

a = new_instagram()
b = new_instagram()
if a == b:
    b = new_instagram()

score = 0
end_game = False
while not end_game:
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    instagram_to_compare(a, "A", b,"B")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if a['follower_count'] >= b['follower_count']:
        if guess in "Aa":
            a = b
            b = new_instagram()
            if a == b:
                b = new_instagram()
            score += 1
        else:
            end_game = True
    else:
        if guess in "Bb":
            a = b
            b = new_instagram()
            if a == b:
                b = new_instagram()
            score += 1
        else:
            end_game = True
    clear()
print(logo)
print(f"Sorry, That's wrong. Final score: {score}.")