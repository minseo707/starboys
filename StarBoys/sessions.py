# Previous Update # 존댓말 (높임표현)
from random import *
from datas import *

session = 0
start = False # False -> veg / True -> user

# Condition

def water(input): 
    if input >= 80:
        value = choice(water1) # Hash Data
    elif input >= 50:
        value = choice(water2)
    else:
        value = choice(water3)
    return value

def temp(input): 
    if input >= 33:
        value = choice(temp1) # Hash Data
    elif input >= 18:
        value = choice(temp2)
    else:
        value = choice(temp3)
    return value

def light(input): 
    if input >= 7:
        value = choice(light1) # Hash Data
    elif input >= 5:
        value = choice(light2)
    else:
        value = choice(light3)
    return value

def todayConditon(input1, input2, input3):
    score = 0
    if input1 >= 80:
        score += 1
    elif input1 >= 50:
        score += 3
    else:
        score += 0

    if input2 >= 33:
        score += 1
    elif input2 >= 18:
        score += 3
    else:
        score += 0

    if input3 >= 7:
        score += 5
    elif input3 >= 5:
        score += 3
    else:
        score += 0

    if score >= 9:
        value = choice(todayConditon1)
    elif score >= 6:
        value = choice(todayConditon2)
    else:
        value = choice(todayConditon3)

    return value

def whenGrow(input):
    value = randint(3, 25)
    value *= 5
    return f'다 자라기 까지 약 {value}일 남았어요!'

def simsim(input):
    value = randint(1, 4)
    pass

def thanks(input):
    pass

def wantFriend(input):
    pass

def what(input): # 뭐하고 있어?
    pass

# 알고리즘

def veg(input):
    global session
    session += 1
    pass

def user(input):
    global session
    session += 1
    pass

# Start
story = randint(1, 4)

de_water = randint(1, 10)*10
de_temp = randint(0, 35)
de_light = randint(1, 10)

if True:
# if story == 1:
    print("주인 : \"습도는 어때?\"")
    print("식물 : " + f"\"{water(de_water)}\"")
# elif story == 2:
    print("주인 : \"온도는 어때?\"")
    print("식물 : " + f'"{temp(de_temp)}"')
# elif story == 3:
    print("주인 : \"조도는 어때?\"")
    print("식물 : " + f'"{light(de_light)}"')
# elif story == 4:
    print("주인 : \"오늘 하루는 어때?\"")
    print("식물 : " + f'"{todayConditon(de_water, de_temp, de_light)}"')

print(de_water, de_temp, de_light)


# Data Save

