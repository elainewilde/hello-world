#Elaine Wilde 1671617

def input_proc(count):
    first = get_jersey_num(count)
    second = get_player_rating(count)
    print()
    return first, second

def get_jersey_num(count):
    jersey_number = input("Enter player "+str(count)+ "'s jersey number:\n")
    return jersey_number

def get_player_rating(count):
    player_rating = input("Enter player "+str(count)+ "'s rating:\n")
    return player_rating


def run_menu(this_dict):
    print("MENU")
    print("a - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n\nChoose an option:")
    choice = input()
    if choice == 'a':
        this_dict = add_player(this_dict)
        return True, this_dict
    if choice == 'd':
        this_dict = remove_player(this_dict)
        return True, this_dict
    if choice == 'u':
        this_dict = update_player(this_dict)
        return True, this_dict
    if choice == 'r':
        this_dict = above_rating(this_dict)
        return True, this_dict
    if choice == 'o':
        this_dict = output_roster(this_dict)
        return True, this_dict
    if choice == 'q':
        return False, this_dict


def add_player(thisdict):
    i = len(thisdict)
    jrsynum, plrat = input_proc(i+1)
    player_dict[jrsynum]=plrat
    return thisdict

def remove_player(thisdict):
    number = input()
    del thisdict[number]
    return thisdict


def update_player(thisdict):
    player_num = input()
    new_rating = input("New rating")
    thisdict[player_num]=new_rating
    return thisdict

def above_rating(thisdict):
    num = int(input("ABOVE "))
    for i in thisdict:
        if float(thisdict[i]) > num:
            print("Jersey number: " + str(i) + ", Rating: " + player_dict[i])
            return thisdict


def output_roster(thisdict):
    print('ROSTER')
    array = []
    for i in player_dict:
        array.append(int(i))
    array.sort()
    for i in array:
        print("Jersey number: " + str(i) + ", Rating: " + player_dict[str(i)])
    print()
    return thisdict

if __name__== "__main__":
    player_dict={}
    for i in range(5):
        jrsynum, plrat = input_proc(i+1)
        player_dict[jrsynum]=plrat
    output_roster(player_dict)

    flag = True
    while flag:
        flag, player_dict = run_menu(player_dict)

