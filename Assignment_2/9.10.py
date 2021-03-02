#Elaine Wilde 1671617

import csv

file = input()
initial_file = open(file)
csvreader = csv.reader(initial_file)

frequency = {}

data_list = list(csvreader)
for i in data_list:
    pass


empty={}

data_list = data_list[0]
for item in data_list:
    var = item
    if empty.get(var) == None:
        empty[var] = 1

    else:
        temp=empty[var] +1
        empty[var] =temp



for item in empty:
    print(item, empty[item])
