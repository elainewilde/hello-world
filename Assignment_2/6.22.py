#Elaine Wilde 1671617

#First equation variables
a = int(input())
b = int(input())
c = int(input())
#Second equation variables
d = int(input())
e = int(input())
f = int(input())

#defining the ranges first with for loops, and then typing out equation to test condition with if statement
flag = False

for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
        if a * x + b * y == c and d * x + e * y == f:
            flag = True
            print(x,y)
if flag == False:
    print("No solution")