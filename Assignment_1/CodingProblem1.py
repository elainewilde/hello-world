#Elaine Wilde 1671617

print('Birthday Calculator')
print('Current Day')
current_month = int(input('Month:'))
current_day = int(input('Day:'))
current_year = int(input('Year:'))
print('Birthday')
bday_month = int(input('Month:'))
bday_day = int(input('Day:'))
bday_year = int(input('Year:'))

delta_month = current_month - bday_month
delta_day = current_day - bday_day
delta_year = current_year - bday_year

if delta_month>0:
    print('You are', delta_year, "years old.")
if delta_month<0:
    print('You are', delta_year - 1, "years old.")
if delta_month==0:
    if delta_day >0:
        print('You are', delta_year, 'years old.')
    if delta_day <0:
        print('You are', delta_year - 1, 'years old.')
    if delta_day ==0:
        print('Happy birthday!')