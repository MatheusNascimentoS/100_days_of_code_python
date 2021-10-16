def caeser(direction, text_caeser, shift_amount):
    for letter in text_caeser:
        if letter in alphabet:    
            index_letter = alphabet.index(letter)
            
            if direction == "encode":
                if index_letter + shift_amount > len(alphabet)-1:
                    new_index_letter = index_letter + shift_amount - len(alphabet)
                else:
                    new_index_letter = index_letter + shift_amount

            elif direction == "decode":
                if index_letter - shift_amount < 0:
                    new_index_letter = index_letter - shift_amount + len(alphabet)
                else:
                    new_index_letter = index_letter - shift_amount

            print(alphabet[new_index_letter], end="")
        else:
            print(letter, end="")

# def encrypt(plain_text, shift_amount):
#     for letter in plain_text:
#         if letter in alphabet:
#             index_letter = alphabet.index(letter)
#             if index_letter + shift_amount > len(alphabet)-1:
#                 new_index_letter = index_letter + shift_amount - len(alphabet)
#             else:
#                 new_index_letter = index_letter + shift_amount
#             print(alphabet[new_index_letter],end='')
#         else:
#             print(letter, end='')

# def decrypt(plain_text, shift_amount):
#     for letter in plain_text:    
#         if letter in alphabet:
#             index_letter = alphabet.index(letter)
#             if index_letter - shift_amount < 0:
#                 new_index_letter = index_letter - shift_amount + len(alphabet)
#             else:
#                 new_index_letter = index_letter - shift_amount
#             print(alphabet[new_index_letter],end='')
#         else:
#             print(letter, end='')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))
if shift > len(alphabet):
    shift = shift % len(alphabet)

caeser(direction, text, shift)

# if direction == 'encode':
#     encrypt(text, shift)
# elif direction == 'decode':
#     decrypt(text, shift)