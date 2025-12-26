 # Movie Ticket Pricing 
 
age = 2
day = 'WEDNESDAY'

price = 12 if age>= 18 else 8

if day == 'WEDNESDAY':
    price -= 2
    #price = price -2
print("Ticket price for you is $",price)