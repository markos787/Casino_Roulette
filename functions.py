from unittest import result
import numpy as np
import random
import time

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

def single_bet(position:str, x:str, list:list)->dict: # returns dictionary with single bet
    return {f'{position}':enter_prize(x)}

def bet_position(list:list)->dict: # returns overall bet on single position
    dictionary={}
    for single_dict in list:
        for key, value in single_dict.items():
            if key in dictionary:
                dictionary[key]+=value
            else:
                dictionary[key]=value
    return dictionary

def overall_bet(dict:dict)->str:
    list=[]
    for key, value in dict.items():
        list.append(int(value))
    all=str(sum(list))
    return all

def draw_result(x:int)->list:
    match x:
        case 0: return ['spiel', 'n26', 'n0', 'n32', 'n15', 'n3', 'o_0_', 'd_0_1_', 'd_0_2_', 'd_0_3_', 't_0_1_2_', 't_0_2_3_', 'q_0_1_2_3_']
        case 1: return ['orphelins', 'n16', 'n33', 'n1', 'n20', 'n14', 'o_1_', 'd_0_1_', 'd_1_4_', 'd_1_2_', 't_0_1_2_', 'q_0_1_2_3_', 't_1_2_3_', 'q_1_2_4_5_', 's_1_2_3_4_5_6_', 'doz_1_12_', 'col_1_34_', 'red']
        case 2: return ['serie023', 'n4', 'n21', 'n2', 'n25', 'n17', 'o_2_', 'd_0_2_', 'd_2_5_', 'd_1_2_', 'd_2_3_', 't_0_1_2_', 't_0_2_3_', 'q_0_1_2_3_', 't_1_2_3_', 'q_1_2_4_5_', 'q_2_3_5_6_', 's_1_2_3_4_5_6_', 'col_2_35_', 'doz_1_12_', 'black']
        case 3: return ['spiel', 'n26', 'n0', 'n12', 'n35', 'n3', 'o_3_', 'd_0_3_', 'd_3_6_', 'd_2_3_', 't_0_2_3_', 'q_0_1_2_3_', 't_1_2_3_', 'q_2_3_5_6_', 's_1_2_3_4_5_6_', 'col_3_36_', 'doz_1_12_', 'red']
        case 4: return ['serie023', 'n15', 'n19', 'n4', 'n21', 'n2', 'o_4_', 'd_1_4_', 'd_4_7_', 'd_4_5_', 't_4_5_6_', 'q_1_2_4_5_', 'q_4_5_7_8_', 's_1_2_3_4_5_6_', 's_4_5_6_7_8_9_', 'doz_1_12_', 'col_1_34_', 'black']
        case 5: return ['serie58', 'n23', 'n10', 'n5', 'n24', 'n16', 'o_5_', 'd_2_5_', 'd_5_8_', 'd_4_5_', 'd_5_6_', 't_4_5_6_', 'q_1_2_4_5_', 'q_2_3_5_6_', 'q_4_5_7_8_', 'q_5_6_8_9_', 's_1_2_3_4_5_6_', 's_4_5_6_7_8_9_', 'doz_1_12_', 'col_2_35_', 'red']
        case 6: return ['orphelins', 'n17', 'n34', 'n6', 'n27', 'n13', 'o_6_', 'd_3_6_', 'd_6_9_', 'd_5_6_', 't_4_5_6_', 'q_2_3_5_6_', 'q_5_6_8_9_', 's_1_2_3_4_5_6_', 's_4_5_6_7_8_9_', 'doz_1_12_', 'col_3_36_', 'black']
        case 7: return ['serie023', 'n18', 'n29', 'n7', 'n28', 'n12', 'o_7_', 'd_4_7_', 'd_7_10_', 'd_7_8_', 't_7_8_9_', 'q_4_5_7_8_', 'q_7_8_10_11_', 's_4_5_6_7_8_9_', 's_7_8_9_10_11_12_', 'doz_1_12_', 'col_1_34_', 'red']
        case 8: return ['serie58', 'n11', 'n30', 'n8', 'n23', 'n10', 'o_8_', 'd_5_8_', 'd_8_11_', 'd_7_8_', 'd_8_9_', 't_7_8_9_', 'q_4_5_7_8_', 'q_5_6_8_9_', 'q_7_8_10_11_', 'q_8_9_11_12_', 's_4_5_6_7_8_9_', 's_7_8_9_10_11_12_', 'doz_1_12_', 'col_2_35_', 'black']
        case 9: return ['orphelins', 'n14', 'n31', 'n9', 'n22', 'n18', 'o_9_', 'd_6_9_', 'd_9_12_', 'd_8_9_', 't_7_8_9_', 'q_5_6_8_9_', 'q_8_9_11_12_', 's_4_5_6_7_8_9_', 's_7_8_9_10_11_12_', 'doz_1_12_', 'col_3_36_', 'red']
        case 10: return ['serie58', 'n8', 'n23', 'n10', 'n5', 'n24', 'o_10_', 'd_7_10_', 'd_10_13_', 'd_10_11_', 't_10_11_12_', 'q_7_8_10_11_', 'q_10_11_13_14_', 's_7_8_9_10_11_12_', 's_10_11_12_13_14_15_', 'doz_1_12_', 'col_1_34_', 'black']
        case 11: return ['serie58', 'n13', 'n36', 'n11', 'n30', 'n8', 'o_11_', 'd_8_11_', 'd_11_14_', 'd_10_11_', 'd_11_12_', 't_10_11_12_', 'q_7_8_10_11_', 'q_8_9_11_12_', 'q_10_11_13_14_', 'q_11_12_14_15_', 's_7_8_9_10_11_12_', 's_10_11_12_13_14_15_', 'doz_1_12_', 'col_2_35_', 'black']
        case 12: return ['spiel', 'n7', 'n28', 'n12', 'n35', 'n3', 'o_12_', 'd_9_12_', 'd_12_15_', 'd_11_12_', 't_10_11_12_', 'q_8_9_11_12_', 'q_11_12_14_15_', 's_7_8_9_10_11_12_', 's_10_11_12_13_14_15_', 'doz_1_12_', 'col_3_36_', 'red']
        case 13: return ['serie58', 'n6', 'n27', 'n13', 'n36', 'n11', 'o_13_', 'd_10_13_', 'd_13_16_', 'd_13_14_', 't_13_14_15_', 'q_10_11_13_14_', 'q_13_14_16_17_', 's_10_11_12_13_14_15_', 's_13_14_15_16_17_18_', 'doz_13_24_', 'col_1_34_', 'black']
        case 14: return ['orphelins', 'n1', 'n20', 'n14', 'n31', 'n9', 'o_14_', 'd_11_14_', 'd_14_17_', 'd_13_14_', 'd_14_15_', 't_13_14_15_', 'q_10_11_13_14_', 'q_11_12_14_15_', 'q_13_14_16_17_', 'q_14_15_17_18_', 's_10_11_12_13_14_15_', 's_13_14_15_16_17_18_', 'doz_13_24_', 'col_2_35_', 'red']
        case 15: return ['spiel', 'n0', 'n32', 'n15', 'n19', 'n4', 'o_15_', 'd_12_15_', 'd_15_18_', 'd_14_15_', 't_13_14_15_', 'q_11_12_14_15_', 'q_14_15_17_18_', 's_10_11_12_13_14_15_', 's_13_14_15_16_17_18_', 'doz_13_24_', 'col_3_36_', 'black']
        case 16: return ['serie58', 'n5', 'n24', 'n16', 'n33', 'n1', 'o_16_', 'd_13_16_', 'd_16_19_', 'd_16_17_', 't_16_17_18_', 'q_13_14_16_17_', 'q_16_17_19_20_', 's_13_14_15_16_17_18_', 's_16_17_18_19_20_21_', 'doz_13_24_', 'col_1_34_', 'red']
        case 17: return ['orphelins', 'n2', 'n25', 'n17', 'n34', 'n6', 'o_17_', 'd_14_17_', 'd_17_20_', 'd_16_17_', 'd_17_18_', 't_16_17_18_', 'q_13_14_16_17_', 'q_14_15_17_18_', 'q_16_17_19_20_', 'q_17_18_20_21_', 's_13_14_15_16_17_18_', 's_16_17_18_19_20_21_', 'doz_13_24_', 'col_2_35_', 'black']
        case 18: return ['serie023', 'n9', 'n22', 'n18', 'n29', 'n7', 'o_18_', 'd_15_18_', 'd_18_21_', 'd_17_18_', 't_16_17_18_', 'q_14_15_17_18_', 'q_17_18_20_21_', 's_13_14_15_16_17_18_', 's_16_17_18_19_20_21_', 'doz_13_24_', 'col_3_36_', 'red']
        case 19: return ['serie023', 'n32', 'n15', 'n19', 'n4', 'n21', 'o_19_', 'd_16_19_', 'd_19_22_', 'd_19_20_', 't_19_20_21_', 'q_16_17_19_20_', 'q_19_20_22_23_', 's_16_17_18_19_20_21_', 's_19_20_21_22_23_24_', 'doz_13_24_', 'col_1_34_', 'red']
        case 20: return ['orphelins', 'n33', 'n1', 'n20', 'n14', 'n31', 'o_20_', 'd_17_20_', 'd_20_23_', 'd_19_20_', 'd_20_21_', 't_19_20_21_', 'q_16_17_19_20_', 'q_17_18_20_21_', 'q_19_20_22_23_', 'q_20_21_23_24_', 's_16_17_18_19_20_21_', 's_19_20_21_22_23_24_', 'doz_13_24_', 'col_2_35_', 'black']
        case 21: return ['serie023', 'n19', 'n4', 'n21', 'n2', 'n25', 'o_21_', 'd_18_21_', 'd_21_24_', 'd_20_21_', 't_19_20_21_', 'q_17_18_20_21_', 'q_20_21_23_24_', 's_16_17_18_19_20_21_', 's_19_20_21_22_23_24_', 'doz_13_24_', 'col_3_36_', 'red']
        case 22: return ['serie023', 'n31', 'n9', 'n22', 'n18', 'n29', 'o_22_', 'd_19_22_', 'd_22_25_', 'd_22_23_', 't_22_23_24_', 'q_19_20_22_23_', 'q_22_23_25_26_', 's_19_20_21_22_23_24_', 's_22_23_24_25_26_27_', 'doz_13_24_', 'col_1_34_', 'black']
        case 23: return ['serie58', 'n30', 'n8', 'n23', 'n10', 'n5', 'o_23_', 'd_20_23_', 'd_23_26_', 'd_22_23_', 'd_23_24_', 't_22_23_24_', 'q_19_20_22_23_', 'q_20_21_23_24_', 'q_22_23_25_26_', 'q_23_24_26_27_', 's_19_20_21_22_23_24_', 's_22_23_24_25_26_27_', 'doz_13_24_', 'col_2_35_', 'red']
        case 24: return ['serie58', 'n10', 'n5', 'n24', 'n16', 'n33', 'o_24_', 'd_21_24_', 'd_24_27_', 'd_23_24_', 't_22_23_24_', 'q_20_21_23_24_', 'q_23_24_26_27_', 's_19_20_21_22_23_24_', 's_22_23_24_25_26_27_', 'doz_13_24_', 'col_3_36_', 'black']
        case 25: return ['serie023', 'n21', 'n2', 'n25', 'n17', 'n34', 'o_25_', 'd_22_25_', 'd_25_28_', 'd_25_26_', 't_25_26_27_', 'q_22_23_25_26_', 'q_25_26_28_29_', 's_22_23_24_25_26_27_', 's_25_26_27_28_29_30_', 'doz_25_36_', 'col_1_34_', 'red']
        case 26: return ['spiel', 'n26', 'n0', 'n32', 'n35', 'n3', 'o_26_', 'd_23_26_', 'd_26_29_', 'd_25_26_', 'd_26_27_', 't_25_26_27_', 'q_22_23_25_26_', 'q_23_24_26_27_', 'q_25_26_28_29_', 'q_26_27_29_30_', 's_22_23_24_25_26_27_', 's_25_26_27_28_29_30_', 'doz_25_36_', 'col_2_35_', 'black']
        case 27: return ['serie58', 'n34', 'n6', 'n27', 'n13', 'n36', 'o_27_', 'd_24_27_', 'd_27_30_', 'd_26_27_', 't_25_26_27_', 'q_23_24_26_27_', 'q_26_27_29_30_', 's_22_23_24_25_26_27_', 's_25_26_27_28_29_30_', 'doz_25_36_', 'col_3_36_', 'red']
        case 28: return ['serie023', 'n29', 'n7', 'n28', 'n12', 'n35', 'o_28_', 'd_25_28_', 'd_28_31_', 'd_28_29_', 't_28_29_30_', 'q_25_26_28_29_', 'q_28_29_31_32_', 's_25_26_27_28_29_30_', 's_28_29_30_31_32_33_', 'doz_25_36_', 'col_1_34_', 'black']
        case 29: return ['serie023', 'n22', 'n18', 'n29', 'n7', 'n28', 'o_29_', 'd_26_29_', 'd_29_32_', 'd_28_29_', 'd_29_30_', 't_28_29_30_', 'q_25_26_28_29_', 'q_26_27_29_30_', 'q_28_29_31_32_', 'q_29_30_32_33_', 's_25_26_27_28_29_30_', 's_28_29_30_31_32_33_', 'doz_25_36_', 'col_2_35_', 'black']
        case 30: return ['serie58', 'n36', 'n11', 'n30', 'n8', 'n23', 'o_30_', 'd_27_30_', 'd_30_33_', 'd_29_30_', 't_28_29_30_', 'q_26_27_29_30_', 'q_29_30_32_33_', 's_25_26_27_28_29_30_', 's_28_29_30_31_32_33_', 'doz_25_36_', 'col_3_36_', 'red']
        case 31: return ['orphelins', 'n20', 'n14', 'n31', 'n9', 'n22', 'o_31_', 'd_28_31_', 'd_31_34_', 'd_31_32_', 't_31_32_33_', 'q_28_29_31_32_', 'q_31_32_34_35_', 's_28_29_30_31_32_33_', 's_31_32_33_34_35_36_', 'doz_25_36_', 'col_1_34_', 'black']
        case 32: return ['spiel', 'n26', 'n0', 'n32', 'n15', 'n19', 'o_32_', 'd_29_32_', 'd_32_35_', 'd_31_32_', 'd_32_33_', 't_31_32_33_', 'q_28_29_31_32_', 'q_29_30_32_33_', 'q_31_32_34_35_', 'q_32_33_35_36_', 's_28_29_30_31_32_33_', 's_31_32_33_34_35_36_', 'doz_25_36_', 'col_2_35_', 'red']
        case 33: return ['serie58', 'n24', 'n16', 'n33', 'n1', 'n20', 'o_33_', 'd_30_33_', 'd_33_36_', 'd_32_33_', 't_31_32_33_', 'q_29_30_32_33_', 'q_32_33_35_36_', 's_28_29_30_31_32_33_', 's_31_32_33_34_35_36_', 'doz_25_36_', 'col_3_36_', 'black']
        case 34: return ['orphelins', 'n25', 'n17', 'n34', 'n6', 'n27', 'o_34_', 'd_31_34_', 'd_34_35_', 't_34_35_36_', 'q_31_32_34_35_', 's_31_32_33_34_35_36_', 'doz_25_36_', 'col_1_34_', 'red']
        case 35: return ['spiel', 'n26', 'n28', 'n12', 'n35', 'n3', 'o_35_', 'd_32_35_', 'd_34_35_', 'd_35_36_', 't_34_35_36_', 'q_31_32_34_35_', 'q_32_33_35_36_', 's_31_32_33_34_35_36_', 'col_2_35_', 'doz_25_36_', 'black']
        case 36: return ['serie58', 'n27', 'n13', 'n36', 'n11', 'n30', 'o_36_', 'd_33_36_', 'd_35_36_', 't_34_35_36_', 'q_32_33_35_36_', 's_31_32_33_34_35_36_', 'doz_25_36_', 'col_3_36_', 'red']
        case _: return []

def bet_result(x:int, list:list, dict:dict)->int: # returns money won/lost in a single draw

    result={}
    for key, value in dict.items():
        if key in list:
            result[key]=value
    
    result2={}
    for key2, value2 in result.items():
        if str(key2).startswith('o') and len(str(key2))<4:
            result2[key2]=value2*36
        elif str(key2).startswith('d'):
            result2[key2]=value2*18
        elif str(key2).startswith('t'):
            result2[key2]=value2*12
        elif str(key2).startswith('q'):
            result2[key2]=value2*9
        elif str(key2).startswith(r'^s\d'):
            result2[key2]=value2*6
        elif str(key2).startswith('col') or str(key2).startswith('doz'):
            result2[key2]=value2*3
        elif str(key2).startswith('red') or str(key2).startswith('black'):
            result2[key2]=value2*2
        elif str(key2).startswith('n'):
            result2[key2]=value2*36
        elif str(key2).startswith('sp'):
            if x==26:
                result2[key2]=value2*36
            else:
                result2[key2]=value2*18
        elif str(key2).startswith('orp'):
            if x==1 or x==17:
                result2[key2]=value2*36
            else:
                result2[key2]=value2*18
        elif str(key2).startswith('serie023'):
            if x==25 or x==26 or x==28 or x==29:
                result2[key2]=value2*9
            elif x==0 or x==2 or x==3:
                result2[key2]=value2*12
            else:
                result2[key2]=value2*18
        elif str(key2).startswith('serie58'):
            result2[key2]=value2*18
        
    sum_values=int(sum(result2.values()))

    return sum_values

def balance(before:list, bet:int, prize:int)->list: # returns overall money owned by a player
    outcome=before[-1]+prize-bet
    before.append(outcome)
    return before

def chances(dict:dict)->str: # returns percentage of chances to win anything from a bet
#  TODO make lists of numbers that are associated with a position, concat lists that are on the bet, keep only numbers that does not repeat and calculate chances, make it after every bet

# lista=[{'d36':5}, {'s25':10}, {'t123':10}, {'d36':10}, {'d36':25}, {'t123': 25}]
# print(bet_position(lista))