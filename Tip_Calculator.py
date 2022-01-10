print('Welcome to the tip calculator!')
bill_amount = float(input('What was the total bill?\nRs '))
No_of_persons =int(input('How many people are to split the bill?\n'))
tip_percentage =int(input('What percentage of tip would you like to give?\n'))
tip_amount = ((bill_amount/100)*tip_percentage)
total_amount = bill_amount + tip_amount
individual_amount = total_amount/No_of_persons
print(f"Each person has to pay: Rs {round(individual_amount,2)}")
