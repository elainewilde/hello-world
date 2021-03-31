#Elaine Wilde 1671617

lst = []

string1 = input()

split_string= string1.split(" ")

new_list = []
for i in split_string:
    new_list.append(int(i))

new_list.sort()

for i in new_list:
    if i >= 0:
        print(i,end=" ")
    else: pass
