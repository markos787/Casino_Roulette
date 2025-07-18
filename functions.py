import numpy as np
import random
import time

def draw(list:list)->int: # returns number as a result of a roulette draw and appends it to list of previous numbers
    x=random.randint(0,36)
    list.append(x)
    return x

def prev_numbers(list:list,step:int)->str: # returns previously drawn number where step is number of draw
    if step>0:
        try:
            x=list[step-1]
        except:
            x='--'
    else:
        x='--'
    return x

def enter_prize(x:str)->int: # returns value of enter prize depending on chosen coin
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

def single_bet(position:str, x:int)->dict: # returns dictionary with single bet
    return {f'{position}':x}

def bet_position(list:list)->dict: # returns all bets divided between single positions
    dictionary={}
    for single_dict in list:
        for key, value in single_dict.items():
            if key in dictionary:
                dictionary[key]+=value
            else:
                dictionary[key]=value
    return dictionary

def overall_bet(dict:dict)->str: # returns overall value of all bets on table
    list=[]
    for key, value in dict.items():
        list.append(int(value))
    all=str(sum(list))
    return all

def draw_result(x:int)->list: # returns list of possible bet wins depending on drawn number
    match x:
        case 0: return ['serie023', 'spiel', 'n26', 'n0', 'n32', 'n15', 'n3', 'o0', 'd01', 'd02', 'd03', 't012', 't023', 'q0123']
        case 1: return ['orphelins', 'n16', 'n33', 'n1', 'n20', 'n14', 'o1', 'd01', 'd14', 'd12', 't012', 'q0123', 't123', 'q1245', 's123456', 'doz112', 'col134', 'red']
        case 2: return ['serie023', 'n4', 'n21', 'n2', 'n25', 'n17', 'o2', 'd02', 'd25', 'd12', 'd23', 't012', 't023', 'q0123', 't123', 'q1245', 'q2356', 's123456', 'col235', 'doz112', 'black']
        case 3: return ['serie023', 'spiel', 'n26', 'n0', 'n12', 'n35', 'n3', 'o3', 'd03', 'd36', 'd23', 't023', 'q0123', 't123', 'q2356', 's123456', 'col336', 'doz112', 'red']
        case 4: return ['serie023', 'n15', 'n19', 'n4', 'n21', 'n2', 'o4', 'd14', 'd47', 'd45', 't456', 'q1245', 'q4578', 's123456', 's456789', 'doz112', 'col134', 'black']
        case 5: return ['serie58', 'n23', 'n10', 'n5', 'n24', 'n16', 'o5', 'd25', 'd58', 'd45', 'd56', 't456', 'q1245', 'q2356', 'q4578', 'q5689', 's123456', 's456789', 'doz112', 'col235', 'red']
        case 6: return ['orphelins', 'n17', 'n34', 'n6', 'n27', 'n13', 'o6', 'd36', 'd69', 'd56', 't456', 'q2356', 'q5689', 's123456', 's456789', 'doz112', 'col336', 'black']
        case 7: return ['serie023', 'n18', 'n29', 'n7', 'n28', 'n12', 'o7', 'd47', 'd710', 'd78', 't789', 'q4578', 'q781011', 's456789', 's789101112', 'doz112', 'col134', 'red']
        case 8: return ['serie58', 'n11', 'n30', 'n8', 'n23', 'n10', 'o8', 'd58', 'd811', 'd78', 'd89', 't789', 'q4578', 'q5689', 'q781011', 'q891112', 's456789', 's789101112', 'doz112', 'col235', 'black']
        case 9: return ['orphelins', 'n14', 'n31', 'n9', 'n22', 'n18', 'o9', 'd69', 'd912', 'd89', 't789', 'q5689', 'q891112', 's456789', 's789101112', 'doz112', 'col336', 'red']
        case 10: return ['serie58', 'n8', 'n23', 'n10', 'n5', 'n24', 'o10', 'd710', 'd1013', 'd1011', 't101112', 'q781011', 'q10111314', 's789101112', 's101112131415', 'doz112', 'col134', 'black']
        case 11: return ['serie58', 'n13', 'n36', 'n11', 'n30', 'n8', 'o11', 'd811', 'd1114', 'd1011', 'd1112', 't101112', 'q781011', 'q891112', 'q10111314', 'q11121415', 's789101112', 's101112131415', 'doz112', 'col235', 'black']
        case 12: return ['serie023', 'spiel', 'n7', 'n28', 'n12', 'n35', 'n3', 'o12', 'd912', 'd1215', 'd1112', 't101112', 'q891112', 'q11121415', 's789101112', 's101112131415', 'doz112', 'col336', 'red']
        case 13: return ['serie58', 'n6', 'n27', 'n13', 'n36', 'n11', 'o13', 'd1013', 'd1316', 'd1314', 't131415', 'q10111314', 'q13141617', 's101112131415', 's131415161718', 'doz1324', 'col134', 'black']
        case 14: return ['orphelins', 'n1', 'n20', 'n14', 'n31', 'n9', 'o14', 'd1114', 'd1417', 'd1314', 'd1415', 't131415', 'q10111314', 'q11121415', 'q13141617', 'q14151718', 's101112131415', 's131415161718', 'doz1324', 'col235', 'red']
        case 15: return ['serie023', 'spiel', 'n0', 'n32', 'n15', 'n19', 'n4', 'o15', 'd1215', 'd1518', 'd1415', 't131415', 'q11121415', 'q14151718', 's101112131415', 's131415161718', 'doz1324', 'col336', 'black']
        case 16: return ['serie58', 'n5', 'n24', 'n16', 'n33', 'n1', 'o16', 'd1316', 'd1619', 'd1617', 't161718', 'q13141617', 'q16171920', 's131415161718', 's161718192021', 'doz1324', 'col134', 'red']
        case 17: return ['orphelins', 'n2', 'n25', 'n17', 'n34', 'n6', 'o17', 'd1417', 'd1720', 'd1617', 'd1718', 't161718', 'q13141617', 'q14151718', 'q16171920', 'q17182021', 's131415161718', 's161718192021', 'doz1324', 'col235', 'black']
        case 18: return ['serie023', 'n9', 'n22', 'n18', 'n29', 'n7', 'o18', 'd1518', 'd1821', 'd1718', 't161718', 'q14151718', 'q17182021', 's131415161718', 's161718192021', 'doz1324', 'col336', 'red']
        case 19: return ['serie023', 'n32', 'n15', 'n19', 'n4', 'n21', 'o19', 'd1619', 'd1922', 'd1920', 't192021', 'q16171920', 'q19202223', 's161718192021', 's192021222324', 'doz1324', 'col134', 'red']
        case 20: return ['orphelins', 'n33', 'n1', 'n20', 'n14', 'n31', 'o20', 'd1720', 'd2023', 'd1920', 'd2021', 't192021', 'q16171920', 'q17182021', 'q19202223', 'q20212324', 's161718192021', 's192021222324', 'doz1324', 'col235', 'black']
        case 21: return ['serie023', 'n19', 'n4', 'n21', 'n2', 'n25', 'o21', 'd1821', 'd2124', 'd2021', 't192021', 'q17182021', 'q20212324', 's161718192021', 's192021222324', 'doz1324', 'col336', 'red']
        case 22: return ['serie023', 'n31', 'n9', 'n22', 'n18', 'n29', 'o22', 'd1922', 'd2225', 'd2223', 't222324', 'q19202223', 'q22232526', 's192021222324', 's222324252627', 'doz1324', 'col134', 'black']
        case 23: return ['serie58', 'n30', 'n8', 'n23', 'n10', 'n5', 'o23', 'd2023', 'd2326', 'd2223', 'd2324', 't222324', 'q19202223', 'q20212324', 'q22232526', 'q23242627', 's192021222324', 's222324252627', 'doz1324', 'col235', 'red']
        case 24: return ['serie58', 'n10', 'n5', 'n24', 'n16', 'n33', 'o24', 'd2124', 'd2427', 'd2324', 't222324', 'q20212324', 'q23242627', 's192021222324', 's222324252627', 'doz1324', 'col336', 'black']
        case 25: return ['serie023', 'n21', 'n2', 'n25', 'n17', 'n34', 'o25', 'd2225', 'd2528', 'd2526', 't252627', 'q22232526', 'q25262829', 's222324252627', 's252627282930', 'doz2536', 'col134', 'red']
        case 26: return ['serie023', 'spiel', 'n26', 'n0', 'n32', 'n35', 'n3', 'o26', 'd2326', 'd2629', 'd2526', 'd2627', 't252627', 'q22232526', 'q23242627', 'q25262829', 'q26272930', 's222324252627', 's252627282930', 'doz2536', 'col235', 'black']
        case 27: return ['serie58', 'n34', 'n6', 'n27', 'n13', 'n36', 'o27', 'd2427', 'd2730', 'd2627', 't252627', 'q23242627', 'q26272930', 's222324252627', 's252627282930', 'doz2536', 'col336', 'red']
        case 28: return ['serie023', 'n29', 'n7', 'n28', 'n12', 'n35', 'o28', 'd2528', 'd2831', 'd2829', 't282930', 'q25262829', 'q28293132', 's252627282930', 's282930313233', 'doz2536', 'col134', 'black']
        case 29: return ['serie023', 'n22', 'n18', 'n29', 'n7', 'n28', 'o29', 'd2629', 'd2932', 'd2829', 'd2930', 't282930', 'q25262829', 'q26272930', 'q28293132', 'q29303233', 's252627282930', 's282930313233', 'doz2536', 'col235', 'black']
        case 30: return ['serie58', 'n36', 'n11', 'n30', 'n8', 'n23', 'o30', 'd2730', 'd3033', 'd2930', 't282930', 'q26272930', 'q29303233', 's252627282930', 's282930313233', 'doz2536', 'col336', 'red']
        case 31: return ['orphelins', 'n20', 'n14', 'n31', 'n9', 'n22', 'o31', 'd2831', 'd3134', 'd3132', 't313233', 'q28293132', 'q31323435', 's282930313233', 's313233343536', 'doz2536', 'col134', 'black']
        case 32: return ['serie023', 'spiel', 'n26', 'n0', 'n32', 'n15', 'n19', 'o32', 'd2932', 'd3235', 'd3132', 'd3233', 't313233', 'q28293132', 'q29303233', 'q31323435', 'q32333536', 's282930313233', 's313233343536', 'doz2536', 'col235', 'red']
        case 33: return ['serie58', 'n24', 'n16', 'n33', 'n1', 'n20', 'o33', 'd3033', 'd3336', 'd3233', 't313233', 'q29303233', 'q32333536', 's282930313233', 's313233343536', 'doz2536', 'col336', 'black']
        case 34: return ['orphelins', 'n25', 'n17', 'n34', 'n6', 'n27', 'o34', 'd3134', 'd3435', 't343536', 'q31323435', 's313233343536', 'doz2536', 'col134', 'red']
        case 35: return ['serie023', 'spiel', 'n26', 'n28', 'n12', 'n35', 'n3', 'o35', 'd3235', 'd3435', 'd3536', 't343536', 'q31323435', 'q32333536', 's313233343536', 'col235', 'doz2536', 'black']
        case 36: return ['serie58', 'n27', 'n13', 'n36', 'n11', 'n30', 'o36', 'd3336', 'd3536', 't343536', 'q32333536', 's313233343536', 'doz2536', 'col336', 'red']
        case _: return []

def bet_result(x:int, list:list, dict:dict)->int: # returns money won (if any) in a single draw
    result={}
    for key, value in dict.items():
        if key in list:
            result[key]=value
    
    result2={}
    for key2, value2 in result.items():
        if str(key2).startswith('o') and len(str(key2))<4:
            result2[key2]=value2*36
        elif str(key2).startswith('d') and str(key2)!='doz112' and str(key2)!='doz1324' and str(key2)!='doz2536':
            result2[key2]=value2*18
        elif str(key2).startswith('t'):
            result2[key2]=value2*12
        elif str(key2).startswith('q'):
            result2[key2]=value2*9
        elif str(key2).startswith('s') and str(key2)!='spiel' and str(key2)!='serie023' and str(key2)!='serie58':
            result2[key2]=value2*6
        elif str(key2).startswith('col') or str(key2).startswith('doz'):
            result2[key2]=value2*3
        elif str(key2).startswith('red') or str(key2).startswith('black'):
            result2[key2]=value2*2
        elif str(key2).startswith('n'):
            result2[key2]=value2*36/5
        elif str(key2).startswith('sp'):
            if x==26:
                result2[key2]=value2*36/4
            else:
                result2[key2]=value2*18/4
        elif str(key2).startswith('orp'):
            if x==1 or x==17:
                result2[key2]=value2*36/5
            else:
                result2[key2]=value2*18/5
        elif str(key2).startswith('serie023'):
            if x==25 or x==26 or x==28 or x==29:
                result2[key2]=value2*9/9
            elif x==0 or x==2 or x==3:
                result2[key2]=value2*12/9
            else:
                result2[key2]=value2*18/9
        elif str(key2).startswith('serie58'):
            result2[key2]=value2*18/6
        
    sum_values=int(sum(result2.values()))

    return sum_values

def balance(before:list, bet:int, prize:int)->list: # returns overall money owned by a player
    outcome=before[-1]+prize-bet
    before.append(outcome)
    return before

def chances(dict:dict)->str: # returns percentage of chances to win anything from a bet
    o0 = [0]
    o1 = [1]
    o2 = [2]
    o3 = [3]
    o4 = [4]
    o5 = [5]
    o6 = [6]
    o7 = [7]
    o8 = [8]
    o9 = [9]
    o10 = [10]
    o11 = [11]
    o12 = [12]
    o13 = [13]
    o14 = [14]
    o15 = [15]
    o16 = [16]
    o17 = [17]
    o18 = [18]
    o19 = [19]
    o20 = [20]
    o21 = [21]
    o22 = [22]
    o23 = [23]
    o24 = [24]
    o25 = [25]
    o26 = [26]
    o27 = [27]
    o28 = [28]
    o29 = [29]
    o30 = [30]
    o31 = [31]
    o32 = [32]
    o33 = [33]
    o34 = [34]
    o35 = [35]
    o36 = [36]
    d01 = [0,1]
    d02 = [0,2]
    d03 = [0,3]
    d14 = [1,4]
    d25 = [2,5]
    d36 = [3,6]
    d47 = [4,7]
    d58 = [5,8]
    d69 = [6,9]
    d710 = [7,10]
    d811 = [8,11]
    d912 = [9,12]
    d1013 = [10,13]
    d1114 = [11,14]
    d1215 = [12,15]
    d1316 = [13,16]
    d1417 = [14,17]
    d1518 = [15,18]
    d1619 = [16,19]
    d1720 = [17,20]
    d1821 = [18,21]
    d1922 = [19,22]
    d2023 = [20,23]
    d2124 = [21,24]
    d2225 = [22,25]
    d2326 = [23,26]
    d2427 = [24,27]
    d2528 = [25,28]
    d2629 = [26,29]
    d2730 = [27,30]
    d2831 = [28,31]
    d2932 = [29,32]
    d3033 = [30,33]
    d3134 = [31,34]
    d3235 = [32,35]
    d3336 = [33,36]
    d12 = [1,2]
    d23 = [2,3]
    d45 = [4,5]
    d56 = [5,6]
    d78 = [7,8]
    d89 = [8,9]
    d1011 = [10,11]
    d1112 = [11,12]
    d1314 = [13,14]
    d1415 = [14,15]
    d1617 = [16,17]
    d1718 = [17,18]
    d1920 = [19,20]
    d2021 = [20,21]
    d2223 = [22,23]
    d2324 = [23,24]
    d2526 = [25,26]
    d2627 = [26,27]
    d2829 = [28,29]
    d2930 = [29,30]
    d3132 = [31,32]
    d3233 = [32,33]
    d3435 = [34,35]
    d3536 = [35,36]
    t012 = [0,1,2]
    t023 = [0,2,3]
    q0123 = [0,1,2,3]
    t123 = [1,2,3]
    t456 = [4,5,6]
    t789 = [7,8,9]
    t101112 = [10,11,12]
    t131415 = [13,14,15]
    t161718 = [16,17,18]
    t192021 = [19,20,21]
    t222324 = [22,23,24]
    t252627 = [25,26,27]
    t282930 = [28,29,30]
    t313233 = [31,32,33]
    t343536 = [34,35,36]
    q1245 = [1,2,4,5]
    q2356 = [2,3,5,6]
    q4578 = [4,5,7,8]
    q5689 = [5,6,8,9]
    q781011 = [7,8,10,11]
    q891112 = [8,9,11,12]
    q10111314 = [10,11,13,14]
    q11121415 = [11,12,14,15]
    q13141617 = [13,14,16,17]
    q14151718 = [14,15,17,18]
    q16171920 = [16,17,19,20]
    q17182021 = [17,18,20,21]
    q19202223 = [19,20,22,23]
    q20212324 = [20,21,23,24]
    q22232526 = [22,23,25,26]
    q23242627 = [23,24,26,27]
    q25262829 = [25,26,28,29]
    q26272930 = [26,27,29,30]
    q28293132 = [28,29,31,32]
    q29303233 = [29,30,32,33]
    q31323435 = [31,32,34,35]
    q32333536 = [32,33,35,36]
    s123456 = [1,2,3,4,5,6]
    s456789 = [4,5,6,7,8,9]
    s789101112 = [7,8,9,10,11,12]
    s101112131415 = [10,11,12,13,14,15]
    s131415161718 = [13,14,15,16,17,18]
    s161718192021 = [16,17,18,19,20,21]
    s192021222324 = [19,20,21,22,23,24]
    s222324252627 = [22,23,24,25,26,27]
    s252627282930 = [25,26,27,28,29,30]
    s282930313233 = [28,29,30,31,32,33]
    s313233343536 = [31,32,33,34,35,36]
    doz112 = [1,2,3,4,5,6,7,8,9,10,11,12]
    doz1324 = [13,14,15,16,17,18,19,20,21,22,23,24]
    doz2536 = [25,26,27,28,29,30,31,32,33,34,35,36]
    col134 = [1,4,7,10,13,16,19,22,25,28,31,34]
    col235 = [2,5,8,11,14,17,20,23,26,29,32,35]
    col336 = [3,6,9,12,15,18,21,24,27,30,33,36]
    red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    n26 = [32,0,26,3,35]
    n3 = [0,26,3,25,12]
    n35 = [26,3,35,12,28]
    n12 = [3,35,12,28,7]
    n28 = [35,12,28,7,29]
    n7 = [12,18,7,29,18]
    n29 = [28,7,29,18,22]
    n18 = [7,29,18,22,9]
    n22 = [29,18,22,9,31]
    n9 = [18,22,9,31,14]
    n31 = [22,9,31,14,20]
    n14 = [9,31,14,20,1]
    n20 = [31,14,20,1,33]
    n1 = [14,20,1,33,16]
    n33 = [20,1,33,16,24]
    n16 = [1,33,16,24,5]
    n24 = [33,16,24,5,10]
    n5 = [16,24,5,10,23]
    n10 = [24,5,10,23,8]
    n23 = [5,10,23,8,30]
    n0 = [3,26,0,32,15]
    n32 = [26,0,32,15,19]
    n15 = [0,32,15,19,4]
    n19 = [32,15,19,4,21]
    n4 = [15,19,4,21,2]
    n21 = [19,4,21,2,25]
    n2 = [4,21,2,25,17]
    n25 = [21,2,25,17,34]
    n17 = [2,25,17,34,6]
    n34 = [25,17,34,6,27]
    n6 = [17,34,6,27,13]
    n27 = [34,6,27,13,36]
    n13 = [6,27,13,36,11]
    n36 = [27,13,36,11,30]
    n11 = [13,36,11,30,8]
    n30 = [36,11,30,8,23]
    n8 = [11,30,8,23,10]
    spiel = [15,32,0,26,3,35,12]
    serie023 = [15,32,0,26,3,35,12,28,7,29,18,22,25,2,21,4,19]
    orphelins = [9,31,14,20,1,6,34,17]
    serie58 = [33,16,24,5,10,23,8,30,11,36,13,27]

    bets_values=[o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16,o17,o18,o19,o20,o21,o22,o23,o24,o25,o26,o27,o28,o29,o30,o31,o32,o33,o34,o35,o36,d01,d02,d03,d14,d25,d36,d47,d58,d69,d710,d811,d912,d1013,d1114,d1215,d1316,d1417,d1518,d1619,d1720,d1821,d1922,d2023,d2124,d2225,d2326,d2427,d2528,d2629,d2730,d2831,d2932,d3033,d3134,d3235,d3336,d12,d23,d45,d56,d78,d89,d1011,d1112,d1314,d1415,d1617,d1718,d1920,d2021,d2223,d2324,d2526,d2627,d2829,d2930,d3132,d3233,d3435,d3536,t012,t023,q0123,t123,t456,t789,t101112,t131415,t161718,t192021,t222324,t252627,t282930,t313233,t343536,q1245,q2356,q4578,q5689,q781011,q891112,q10111314,q11121415,q13141617,q14151718,q16171920,q17182021,q19202223,q20212324,q22232526,q23242627,q25262829,q26272930,q28293132,q29303233,q31323435,q32333536,s123456,s456789,s789101112,s101112131415,s131415161718,s161718192021,s192021222324,s222324252627,s252627282930,s282930313233,s313233343536,doz112,doz1324,doz2536,col134,col235,col336,red,black,n26,n3,n35,n12,n28,n7,n29,n18,n22,n9,n31,n14,n20,n1,n33,n16,n24,n5,n10,n23,n0,n32,n15,n19,n4,n21,n2,n25,n17,n34,n6,n27,n13,n36,n11,n30,n8,spiel,serie023,orphelins,serie58]
    bets_keys=['o0','o1','o2','o3','o4','o5','o6','o7','o8','o9','o10','o11','o12','o13','o14','o15','o16','o17','o18','o19','o20','o21','o22','o23','o24','o25','o26','o27','o28','o29','o30','o31','o32','o33','o34','o35','o36','d01','d02','d03','d14','d25','d36','d47','d58','d69','d710','d811','d912','d1013','d1114','d1215','d1316','d1417','d1518','d1619','d1720','d1821','d1922','d2023','d2124','d2225','d2326','d2427','d2528','d2629','d2730','d2831','d2932','d3033','d3134','d3235','d3336','d12','d23','d45','d56','d78','d89','d1011','d1112','d1314','d1415','d1617','d1718','d1920','d2021','d2223','d2324','d2526','d2627','d2829','d2930','d3132','d3233','d3435','d3536','t012','t023','q0123','t123','t456','t789','t101112','t131415','t161718','t192021','t222324','t252627','t282930','t313233','t343536','q1245','q2356','q4578','q5689','q781011','q891112','q10111314','q11121415','q13141617','q14151718','q16171920','q17182021','q19202223','q20212324','q22232526','q23242627','q25262829','q26272930','q28293132','q29303233','q31323435','q32333536','s123456','s456789','s789101112','s101112131415','s131415161718','s161718192021','s192021222324','s222324252627','s252627282930','s282930313233','s313233343536','doz112','doz1324','doz2536','col134','col235','col336','red','black','n26','n3','n35','n12','n28','n7','n29','n18','n22','n9','n31','n14','n20','n1','n33','n16','n24','n5','n10','n23','n0','n32','n15','n19','n4','n21','n2','n25','n17','n34','n6','n27','n13','n36','n11','n30','n8','spiel','serie023','orphelins','serie58']
    bets={}
    for i in range(len(bets_keys)):
        bets[bets_keys[i]]=bets_values[i]

    made_bets=[]
    for key, value in dict.items():
        made_bets.append(key)
    
    list_numbers_on_bet=[]
    for key, value in bets.items():
        if key in made_bets:
            list_numbers_on_bet.append(value)
        else:
            continue
    
    numbers_on_bet=[]
    for item in list_numbers_on_bet:
        numbers_on_bet.extend(item)

    single_numbers=[]
    for item in numbers_on_bet:
        if item in single_numbers:
            continue
        else:
            single_numbers.append(item)
    
    chance=f'{round(100*len(single_numbers)/37, 2)}%'
        
    return chance

def rotation_angle(result):
    angle=0
    result_int=int(result)
    if result_int==34:
        angle=0
    elif result_int==17:
        angle=(360/37)*1+3
    elif result_int==25:
        angle=(360/37)*2+3
    elif result_int==2:
        angle=(360/37)*3+3
    elif result_int==21:
        angle=(360/37)*4+3
    elif result_int==4:
        angle=(360/37)*5+3
    elif result_int==19:
        angle=(360/37)*6+3
    elif result_int==15:
        angle=(360/37)*7+3
    elif result_int==32:
        angle=(360/37)*8+3
    elif result_int==0:
        angle=(360/37)*9+3
    elif result_int==26:
        angle=(360/37)*10+3
    elif result_int==3:
        angle=(360/37)*11+3
    elif result_int==35:
        angle=(360/37)*12+3
    elif result_int==12:
        angle=(360/37)*13+3
    elif result_int==28:
        angle=(360/37)*14+3
    elif result_int==7:
        angle=(360/37)*15+3
    elif result_int==29:
        angle=(360/37)*16+3
    elif result_int==18:
        angle=(360/37)*17+3
    elif result_int==22:
        angle=(360/37)*18+3
    elif result_int==9:
        angle=(360/37)*19+3
    elif result_int==31:
        angle=(360/37)*20+3
    elif result_int==14:
        angle=(360/37)*21+3
    elif result_int==20:
        angle=(360/37)*22+3
    elif result_int==1:
        angle=(360/37)*23+3
    elif result_int==33:
        angle=(360/37)*24+3
    elif result_int==16:
        angle=(360/37)*25+3
    elif result_int==24:
        angle=(360/37)*26+3
    elif result_int==5:
        angle=(360/37)*27+3
    elif result_int==10:
        angle=(360/37)*28+3
    elif result_int==23:
        angle=(360/37)*29+3
    elif result_int==8:
        angle=(360/37)*30+3
    elif result_int==30:
        angle=(360/37)*31+3
    elif result_int==11:
        angle=(360/37)*32+3
    elif result_int==36:
        angle=(360/37)*33+3
    elif result_int==13:
        angle=(360/37)*34+3
    elif result_int==27:
        angle=(360/37)*35+3
    elif result_int==6:
        angle=(360/37)*36+3
    return angle


# lista=[{'d36':5}, {'n25':10}, {'t123':10}, {'d36':10}, {'d36':25}, {'t123': 25}]
# diction={'d36': 40, 'n25': 10, 't123': 35}
# print(chances(diction))
# chances({'o0':20, 'd12':35, 'spiel':20})