#Elaine Wilde 1671617

def quicksort(arr):
    arr.sort()
    return arr

sorting_list = []

while True:
    input_info = input()
    if input_info == '-1':
        break
    sorting_list.append(input_info)

sorted_list = quicksort(sorting_list)

print(sorted_list)