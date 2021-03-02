#Elaine Wilde 1671617

import math

def exact_change(change):
    def num_dollars(totalchange):
        num_dollars = math.floor(totalchange / 100)#num_dollar
        remainder_dollar = totalchange - num_dollars * 100
        #print(remainder_dollar, 'rem dollars')
        return num_dollars, remainder_dollar

    def num_quarters(remainder_dollar):
        num_quarters = math.floor(remainder_dollar / 25) #num_quarter
        remainder = remainder_dollar - num_quarters * 25
        return num_quarters, remainder

    def num_dimes(a_few_cents):
        num_dimes = math.floor(a_few_cents/10)
        leftover = a_few_cents - num_dimes *10
        return num_dimes,leftover

    def num_nickels(a_few_nic):
        num_nickels = math.floor(a_few_nic/5)
        leftovers = a_few_nic - num_nickels *5
        return num_nickels, leftovers

    def num_pennies(a_few_pen):
        num_pennies = math.floor(a_few_pen/1)
        pleftover = a_few_pen - num_pennies * 1
        return num_pennies, pleftover


    #input the amount
    exact_change = change

    dollars,dol_remainder = num_dollars(exact_change)
    quarters,quar_remainder = num_quarters(dol_remainder)
    dimes, dime_remainder = num_dimes(quar_remainder)
    nickels, nickel_remainder = num_nickels(dime_remainder)
    pennies, penny_remainder = num_pennies(nickel_remainder)

    #print(dollars, "dollars") if dollars > 1 else print(dollars, "dollar")

    (print(dollars, "dollars") if dollars > 1 else print(dollars, "dollar")) if dollars > 0 else print(end='')
    (print(quarters, "quarters") if quarters > 1 else print(quarters, "quarter")) if quarters > 0 else print(end='')
    (print(dimes, "dimes") if dimes > 1 else print(dimes, "dime")) if dimes > 0 else print(end='')
    (print(nickels, "nickels") if nickels > 1 else print(nickels, "nickel")) if nickels > 0 else print(end='')
    (print(pennies, "pennies") if pennies > 1 else print(pennies, "penny")) if pennies > 0 else print(end='')

    if exact_change <= 0:
        print("no change")

    return dollars, quarters, dimes, nickels, pennies


if __name__ == '__main__':
    # __ is 'dunder' or special, in this case __name__ means name of file
    # https://levelup.gitconnected.com/python-dunder-methods-ea98ceabad15
    #'__main__' is a special string for main.py
    #use this for actions run on unit tests in zybooks
    inputval = int(input())
    numdollars, numquarters, numdimes, numnickels, numpennies = exact_change(inputval)


