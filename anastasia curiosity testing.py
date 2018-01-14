import time
import random
print("hello, welcome to my quiz!")

possible_choices = {(0,0,0) : False, (1,0,0): False, (0,1,0): False, (1,1,0): False, \
(0,0,1): False, (1,0,1): False, (0,1,1): False, (1,1,1): False}

mykeys = possible_choices.keys()
length = len(mykeys) - 1

r1 = random.randint(0,length)

while(possible_choices[mykeys[r1]] == True):
    r1 = random.randint(0,length)
my_vars = mykeys[r1]
possible_choices[my_vars] = True
print(my_vars)
c1 = my_vars[0]
d1 = my_vars[1]
t1 = my_vars[2]

r2 = random.randint(0,length)
while(possible_choices[mykeys[r2]] == True):
    r2 = random.randint(0,length)
my_vars2 = mykeys[r2]
possible_choices[my_vars2] = True
print(my_vars2)
c2 = my_vars2[0]
d2 = my_vars2[1]
t2 = my_vars2[2]
# print("rgn has produced: c = " + str(c) + " d = " + str(d) + " t = " + str(t))

r3 = random.randint(0,length)
while(possible_choices[mykeys[r3]] == True):
    r3 = random.randint(0,length)
my_vars3 = mykeys[r3]
possible_choices[my_vars3] = True
print(my_vars3)
c3 = my_vars3[0]
d3 = my_vars3[1]
t3 = my_vars3[2]

r4 = random.randint(0,length)
while(possible_choices[mykeys[r4]] == True):
    r4 = random.randint(0,length)
my_vars4 = mykeys[r4]
possible_choices[my_vars4] = True
print(my_vars4)
c4 = my_vars4[0]
d4 = my_vars4[1]
t4 = my_vars4[2]

print("1: c = " + str(c1) + " d = " + str(d1) + " t = " + str(t1))
print("2: c = " + str(c2) + " d = " + str(d2) + " t = " + str(t2))
print("3: c = " + str(c3) + " d = " + str(d3) + " t = " + str(t3))
print("4: c = " + str(c4) + " d = " + str(d4) + " t = " + str(t4))


print("setup complete")

s_color = ""
if c1:
    s_color = "black"
else:
    s_color = "white"

s_drink = ""
if d1:
    s_drink = "wine"
else:
    s_drink = "water"

s_trans = ""
if t1:
    s_trans = "train"
else:
    s_trans = "boat"

def ask_continue():
    print("Do you want to continue?")
    cont = raw_input("type 'y' to continue 'n' to skip: ")
    if cont == 'n':
        return 0
    else:
        return 1

go = 1

print("It was one of those eerie Mondays in August, a particularly strange day as everything was tinted " + s_color)
time.sleep(1)
go = ask_continue()
if go:
    print("Unable to take it anymore, Amelia reached for her glass of " + s_drink)
    time.sleep(1)
    go = ask_continue()
    if go:
        print("She would not stay here a moment longer. Her bags were packed, and the " + s_trans + " was waiting.")





#
#
# print("Do you prefer black or white?")
#
# color = raw_input("type 'b' for black 'w' for white: ")
# while(color != 'b' and color != 'w'):
#     color = raw_input("Invalid Input: (type 'b' or 'w'): ")
#
# black = 0;
# if color == 'b':
#     print("Thanks you chose black")
#     black = 1
# else:
#     print("Thanks you chose white")
#
#
# time.sleep(1)
#
# print("Do you prefer wine or water?")
# drink = raw_input("type '1' for wine '2' for water: ")
# while(drink != '1' and drink != '2'):
#     drink = raw_input("Invalid Input: (type '1' or '2'): ")
#
# wine = 0;
# if drink == '1':
#     print("Thanks you chose wine")
#     black = 1
# else:
#     print("Thanks you chose water")
#
# time.sleep(1)
# print("Do you prefer trains or boats?")
# trans = raw_input("type 't' for trains 'b' for boats: ")
# while(trans != 't' and trans != 'b'):
#     trans = raw_input("Invalid Input: (type '1' or '2'): ")
#
# train = 0;
# if trans == 't':
#     print("Thanks you chose trains")
#     train = 1
# else:
#     print("Thanks you chose boats")
