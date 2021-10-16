import pandas



nato = pandas.read_csv(r"day_26\nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}

while True:
    word_to_spell = input("Enter a word: ").upper()
    try:
        nato_word = [nato_dict[letter] for letter in word_to_spell]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        break

print(nato_word)

