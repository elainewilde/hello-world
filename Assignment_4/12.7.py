#Elaine Wilde 1671617

if __name__ == '__main__':
    user_input = ' '

    try:
        age = int(input('Enter age here'))
        if ( age <18 or age > 75):
            raise ValueError;
        burning_rate = (220 - age) * .7
        print('Fat burning heart rate for a' + str(age) + 'year-old: ' + str(burning_rate) + 'bpm')

    except ValueError:
        print('Invalid age.')
        print('Could not calculate heart rate info')