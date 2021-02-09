#Elaine Wilde 1671617

lemon_cup = float(input('Enter amount of lemon juice (in cups):\n'))
water_cup = float(input('Enter amount of water (in cups):\n'))
agave_cup = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print()
print('Lemonade ingredients - yields' ,'{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon_cup), 'cup(s) lemon juice')
print('{:.2f}'.format(water_cup), 'cup(s) water')
print('{:.2f}'.format(agave_cup), 'cup(s) agave nectar\n')

total_servings = float(input('How many servings would you like to make?\n'))
print()
multiply_by = total_servings / servings
total_lemon = multiply_by * lemon_cup
total_water = multiply_by * water_cup
total_agave = multiply_by * agave_cup

print('Lemonade ingredients - yields', '{:.2f}'.format(total_servings), 'servings')
print('{:.2f}'.format(total_lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(total_water), 'cup(s) water')
print('{:.2f}'.format(total_agave), 'cup(s) agave nectar')
print()

lemon_gal = total_lemon * (1/16)
water_gal = total_water * (1/16)
agave_gal = total_agave * (1/16)

print('Lemonade ingredients - yields', '{:.2f}'.format(total_servings), 'servings')
print('{:.2f}'.format(lemon_gal), 'gallon(s) lemon juice')
print('{:.2f}'.format(water_gal), 'gallon(s) water')
print('{:.2f}'.format(agave_gal), 'gallon(s) agave nectar')




