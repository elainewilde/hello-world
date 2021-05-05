#Elaine Wilde 1671617

full_list = []

while True:
    input_info = input()
    if input_info == '-1':
        break
    name_list = input_info.split()
    try:
        int(name_list[1])
    except ValueError:
        print('FIXME')
        input_info = input()
        name_list = input_info.split()
        name_list[1] = -1

    full_list.append(name_list)

clean_list = []

for a in full_list:
    last_index = len(a) -1
    reformat_num = str(int(a[last_index]) + 1)
    clean_string = a[0] + ' ' + reformat_num
    clean_list.append(clean_string)

for i in clean_list:
    print(i)
