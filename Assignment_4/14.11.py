#Elaine Wilde 1671617

def print_output(arr):
    for i in arr:
        print(i + ' ', end='')
    print()

def selection_sort_descend_trace(num_list):
    for i in range(len(num_list)):
        max_idx = i
        for j in range(i + 1, len(num_list)):
            if num_list[max_idx] < num_list[j]:
                max_idx = j
        num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]
        print_output(num_list)

if __name__ == '__main__':

    input_nums = input()
    num_list = input_nums.split()
    selection_sort_descend_trace(num_list)