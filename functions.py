import string
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

def enter_prize(x:str)->int:
    if x=='coin5':
        enter=5
    elif x=='coin10':
        enter=10
    elif x=='coin25':
        enter=25
    elif x=='coin50':
        enter=50
    elif x=='coin100':
        enter=100
    return enter

def single_bet(number:str, x:str)->dict: # returns dictionary with single bet
    return {f'{number}':enter_prize(x)}

def bet_position(list:list)->dict: # returns overall bet on single position
    dictionary={}
    for single_dict in list:
        for key, value in single_dict.items():
            if key in dictionary:
                dictionary[key]+=value
            else:
                dictionary[key]=value
    return dictionary

# lista=[{'d36':5}, {'s25':10}, {'t123':10}, {'d36':10}, {'d36':25}, {'t123': 25}]
# print(bet_position(lista))