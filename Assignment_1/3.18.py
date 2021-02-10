#Elaine Wilde 1671617

wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))

wall_area = wall_height * wall_width
paint_needed = wall_area / 350

print('Wall area:', wall_area, 'square feet')
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')

rounded_value = round(paint_needed)
#total_value = rounded_value *

print('Cans needed:', rounded_value, 'can(s)\n')


color_needed = str(input('Choose a color to paint the wall:\n'))

paint_colors = {
    "red":'35',
    "blue":'25',
    "green":'23'
}

red = paint_colors.get('red')
blue = paint_colors.get('blue')
green = paint_colors.get('green')

if color_needed=="red":
    print('Cost of purchasing red paint: $35')
elif color_needed=="blue":
    print('Cost of purchasing blue paint: $25')
elif color_needed=="green":
    print('Cost of purchasing green paint: $23')







