import numpy as np
import random

def draw(list:list)->int:
    x=random.randint(0,36)
    list.append(x)
    return x

def prev_numbers(list:list,step:int)->str: # returns drawn number where step is number of draw
    try:
        x=list[::-1]
        x=x[step-1]
    except:
        x='--'
    return x

def enter_prize(x)->int:
    if x=='d5':
        enter=5
    elif x=='d10':
        enter=10
    elif x=='d50':
        enter=50
    elif x=='d100':
        enter=100
    elif x=='d500':
        enter=500
    elif x=='d1k':
        enter=1000
    elif x=='d5k':
        enter=5000
    return enter

