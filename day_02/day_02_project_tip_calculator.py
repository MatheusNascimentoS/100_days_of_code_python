print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = float(input('What percentage tip would you like to give? 10%, 12% or 15% ')) / 100
n_people = int(input('How many people to split the bill? '))
bill_person = (bill + bill *  tip) / n_people
print(f'Each person should pay ${bill_person:.2f}')
