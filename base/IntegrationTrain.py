a_list = [1,2,3]
print(sum(a_list))

import random

proint1 = random.randrange(1,7)
proint2 = random.randrange(1,7)
proint3 = random.randrange(1,7)
print(proint1,proint2,proint3)

def roll_dice(numbers=3,points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points=[]
    while numbers>0:
        points.append(random.randrange(1,7))
        numbers = numbers-1
    return points
def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'
def start_game():
    print('<<<<<< GAME START >>>>>>')
    choices = ['Big','Small']
    your_choices = input('Big or Small')
    print('How much do wanna bet ?-')
    cash = 1000
    bet = input()
    if your_choices in choices:
        points =roll_dice()
        total = sum(points)
        youwin=your_choices==roll_result(total)
        if youwin:
            cash=cash+bet
            print('The points are',points,'You Win!')
            print('You gained',bet,'you have',cash)
        else:
            cash=cash-bet
            print('The points are',points,'You Lost!')
            print('You lost',bet,'you have',cash)
    else:
        print('Invalid Worlds')
        start_game()

start_game()
