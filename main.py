from email.mime import image
import re
import functions as ff
import tkinter as tk
from tkinter import IntVar, PhotoImage
import time
from PIL import Image, ImageTk

# main window
root_main=tk.Tk()
root_main.title('Casino Roulette')
root_main.geometry('1530x600')
root_main.resizable(False, False)
root_main.config(bg='green')

# help window
def help_window(event=None):
    root_help=tk.Toplevel()
    root_help.title('Help')
    root_help.geometry('800x400')
    root_help.resizable(False, False)

    root_help.grid_rowconfigure(0, weight=1)
    root_help.grid_columnconfigure(0, weight=1)

    # frame for canvas
    canvas_frame_help=tk.Frame(root_help)
    canvas_frame_help.grid(row=0, column=0)
    canvas_frame_help.grid_rowconfigure(0, weight=1)
    canvas_frame_help.grid_columnconfigure(0, weight=1)

    # canvas
    canvas=tk.Canvas(canvas_frame_help, width=root_help.winfo_width(), height=root_help.winfo_height())
    canvas.grid(row=0, column=0)

    # scrollbar
    scrollbar = tk.Scrollbar(canvas_frame_help, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)

    # help frame
    frame_help=tk.Frame(canvas)
    canvas.create_window((0,0), window=frame_help, anchor='nw')


    # text of help
    label_help_title=tk.Label(frame_help, font=('Times New Roman', 24, 'bold'), wraplength=770, justify='left', text=r'Help')
    label_help_sub1=tk.Label(frame_help, font=('Times New Roman', 14, 'italic'), wraplength=770, justify='left', text=r'1. What is roulette?')
    label_help_txt1=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'French roulette is a game in which players place bets on the outcome of one of 37 numbers drawn from 0 to 36. The roulette wheel is turned by a dealer (throw), who also settles the winnings after the throw. Players can bet not only on individual numbers, but also on their combinations, which will be explained below. The outcome of the throw is completely random. In the computer version, the system plays the role of the dealer, but the outcome is also 100% random.')
    label_help_sub2=tk.Label(frame_help, font=('Times New Roman', 14, 'italic'), wraplength=770, justify='left', text=r'2. What is the maximum bet?')
    label_help_txt2=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'A player can place a maximum of 10,000 on the table at one time.')
    label_help_sub3=tk.Label(frame_help, font=('Times New Roman', 14, 'italic'), wraplength=770, justify='left', text=r'3. What do the individual bets look like?')
    label_help_txt3=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Single - a bet on a single number. The chance of hitting is the smallest, but the winnings are the highest. The player receives 36 times their bet.')
    label_help_txt4=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Two - the player bets on two numbers that are adjacent to each other on the table (not on the wheel). The win is 18 times the bet.')
    label_help_txt5=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Three - a bet on three numbers that are adjacent to each other on the table. The win is 12 times the bet.')
    label_help_txt6=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Four - the player bets on a combination of the four numbers that are closest to each other on the table. The win is 9 times the bet.')
    label_help_txt7=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Six - a bet on the six numbers that are closest to each other on the table. The win is 6 times the bet.')
    label_help_txt8=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Dozen - twelve consecutive numbers according to the table. The win is 3 times the bet. The minimum bet is 25.')
    label_help_txt9=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Column - twelve numbers located in three columns of the table. The win is 3 times the bet. The minimum bet is 25.')
    label_help_txt10=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Color - black or red. The win is 2 times the bet. The minimum bet is 50.')
    label_help_txt11=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Neighbors - when betting on the neighbor of a given number, you bet on that number and two of its neighbors on each side according to the wheel. The win is 31 times the bet. The minimum bet includes 5 tokens.')
    label_help_txt12=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'0 Spiel - in this bet, you bet on the neighbors of the number 0. The bet on the number 26 is a single, and on the numbers 0, 3, 12, 15, 32 and 35 - double. The minimum bet is 4 tokens, so the winnings are either 32 times or 14 times the bet.')
    label_help_txt13=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Series 0/2/3 - bet on the numbers 15, 32, 0, 26, 3, 35, 12, 28, 7, 29, 18, 22, 25, 2, 21, 4 and 19 (i.e. this is an extended 0 Spiel), with the numbers 25, 26, 28 and 29 being double fours, the numbers 0, 2 and 3 being double threes, and the remaining numbers being single twos. The minimum bet is 9 tokens, and the winnings are 9 times, 15 times or also 9 times if a four, three or two is rolled.')
    label_help_txt14=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Orphelins - consists of numbers that neither Series 0/2/3 nor Series 5/8 will cover, i.e. 9, 31, 14, 20, 1, 6, 34 and 17. This is a stake of 5 tokens, one of which is on 1 and then one token each on the twos 6/9, 14/17, 17/20 and 31/34.')
    label_help_txt15=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'Series 5/8 - includes the remaining numbers not listed above, i.e. 33, 16, 24, 5, 10, 23, 8, 30, 11, 36, 13 and 27. All 6 of the minimum chips are placed on the pairs of these numbers, so the winnings are 12 times the bet.')
    label_help_sub4=tk.Label(frame_help, font=('Times New Roman', 14, 'italic'), wraplength=770, justify='left', text=r'4. How to play?')
    label_help_txt16=tk.Label(frame_help, font=('Times New Roman', 12, ), wraplength=770, justify='left', text=r'First, you must make a bet. To do this, click on the icon of the token in question, and then on the button with the number or another bet. This action must be repeated each time for a new bet. The total bet and the chances of hitting the number with the current total bet will be displayed to the left of the tokens. Even further to the left is the balance, which the player starts at 5,000. If the player wants to undo the previous bet, they should click "Back bet" under the roulette wheel, and if they want to bet again - the "Reset bet" button next to it. There is also a place for the last drawn number under the wheel, and a history of the last 10 draws on the left side of the wheel. To spin the wheel, click the "Spin" button.')

    label_help_title.grid(row=0, column=0, sticky='W', padx=370, pady=5)
    label_help_sub1.grid(row=1, column=0, sticky='W', padx=5, pady=(30,0))
    label_help_txt1.grid(row=2, column=0, sticky='W', padx=5)
    label_help_sub2.grid(row=3, column=0, sticky='W', padx=5, pady=(30,0))
    label_help_txt2.grid(row=4, column=0, sticky='W', padx=5)
    label_help_sub3.grid(row=5, column=0, sticky='W', padx=5, pady=(30,0))
    label_help_txt3.grid(row=6, column=0, sticky='W', padx=5, pady=3)
    label_help_txt4.grid(row=7, column=0, sticky='W', padx=5, pady=3)
    label_help_txt5.grid(row=8, column=0, sticky='W', padx=5, pady=3)
    label_help_txt6.grid(row=9, column=0, sticky='W', padx=5, pady=3)
    label_help_txt7.grid(row=10, column=0, sticky='W', padx=5, pady=3)
    label_help_txt8.grid(row=11, column=0, sticky='W', padx=5, pady=3)
    label_help_txt9.grid(row=12, column=0, sticky='W', padx=5, pady=3)
    label_help_txt10.grid(row=13, column=0, sticky='W', padx=5, pady=3)
    label_help_txt11.grid(row=14, column=0, sticky='W', padx=5, pady=3)
    label_help_txt12.grid(row=15, column=0, sticky='W', padx=5, pady=3)
    label_help_txt13.grid(row=16, column=0, sticky='W', padx=5, pady=3)
    label_help_txt14.grid(row=17, column=0, sticky='W', padx=5, pady=3)
    label_help_txt15.grid(row=18, column=0, sticky='W', padx=5, pady=3)
    label_help_sub4.grid(row=19, column=0, sticky='W', padx=5, pady=(30,0))
    label_help_txt16.grid(row=20, column=0, sticky='W', padx=5)

    # scroll with mouse
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    # size of scrollbar window equal to size of the whole window
    def update_canvas_size(event=None):
        width = 800*root_help.winfo_width()
        height = 400*root_help.winfo_height()
        canvas.config(width=width, height=height)
        canvas.config(scrollregion=canvas.bbox("all"))
    
    root_help.bind("<Configure>", update_canvas_size)

    root_help.mainloop()

# definng the list of results
results_list=[]

# defining the list for dictionaries of bets
bets_list=[]

# variable for coin
selected_coin=0

# for operating on radiobuttons
var=IntVar()

# defining the list for money balance
balance_history=[5000]

# functions of choosing coins for a bet
def coin_choose_5(event=None):
    check5.select()
    check10.deselect()
    check25.deselect()
    check50.deselect()
    check100.deselect()
    global selected_coin
    selected_coin = 5

def coin_choose_10(event=None):
    check5.deselect()
    check10.select()
    check25.deselect()
    check50.deselect()
    check100.deselect()
    global selected_coin
    selected_coin = 10

def coin_choose_25(event=None):
    check5.deselect()
    check10.deselect()
    check25.select()
    check50.deselect()
    check100.deselect()
    global selected_coin
    selected_coin = 25

def coin_choose_50(event=None):
    check5.deselect()
    check10.deselect()
    check25.deselect()
    check50.select()
    check100.deselect()
    global selected_coin
    selected_coin = 50

def coin_choose_100(event=None):
    check5.deselect()
    check10.deselect()
    check25.deselect()
    check50.deselect()
    check100.select()
    global selected_coin
    selected_coin = 100

# function operating on bets, balance and chances
def bet(name):
    # making dict of button names so that it could be read properly
    bets_keys=[o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16,o17,o18,o19,o20,o21,o22,o23,o24,o25,o26,o27,o28,o29,o30,o31,o32,o33,o34,o35,o36,d01,d02,d03,d14,d25,d36,d47,d58,d69,d710,d811,d912,d1013,d1114,d1215,d1316,d1417,d1518,d1619,d1720,d1821,d1922,d2023,d2124,d2225,d2326,d2427,d2528,d2629,d2730,d2831,d2932,d3033,d3134,d3235,d3336,d12,d23,d45,d56,d78,d89,d1011,d1112,d1314,d1415,d1617,d1718,d1920,d2021,d2223,d2324,d2526,d2627,d2829,d2930,d3132,d3233,d3435,d3536,t012,t023,q0123,t123,t456,t789,t101112,t131415,t161718,t192021,t222324,t252627,t282930,t313233,t343536,q1245,q2356,q4578,q5689,q781011,q891112,q10111314,q11121415,q13141617,q14151718,q16171920,q17182021,q19202223,q20212324,q22232526,q23242627,q25262829,q26272930,q28293132,q29303233,q31323435,q32333536,s123456,s456789,s789101112,s101112131415,s131415161718,s161718192021,s192021222324,s222324252627,s252627282930,s282930313233,s313233343536,doz112,doz1324,doz2536,col134,col235,col336,red,black,n26,n3,n35,n12,n28,n7,n29,n18,n22,n9,n31,n14,n20,n1,n33,n16,n24,n5,n10,n23,n0,n32,n15,n19,n4,n21,n2,n25,n17,n34,n6,n27,n13,n36,n11,n30,n8,spiel,serie023,orphelins,serie58]
    bets_values=['o0','o1','o2','o3','o4','o5','o6','o7','o8','o9','o10','o11','o12','o13','o14','o15','o16','o17','o18','o19','o20','o21','o22','o23','o24','o25','o26','o27','o28','o29','o30','o31','o32','o33','o34','o35','o36','d01','d02','d03','d14','d25','d36','d47','d58','d69','d710','d811','d912','d1013','d1114','d1215','d1316','d1417','d1518','d1619','d1720','d1821','d1922','d2023','d2124','d2225','d2326','d2427','d2528','d2629','d2730','d2831','d2932','d3033','d3134','d3235','d3336','d12','d23','d45','d56','d78','d89','d1011','d1112','d1314','d1415','d1617','d1718','d1920','d2021','d2223','d2324','d2526','d2627','d2829','d2930','d3132','d3233','d3435','d3536','t012','t023','q0123','t123','t456','t789','t101112','t131415','t161718','t192021','t222324','t252627','t282930','t313233','t343536','q1245','q2356','q4578','q5689','q781011','q891112','q10111314','q11121415','q13141617','q14151718','q16171920','q17182021','q19202223','q20212324','q22232526','q23242627','q25262829','q26272930','q28293132','q29303233','q31323435','q32333536','s123456','s456789','s789101112','s101112131415','s131415161718','s161718192021','s192021222324','s222324252627','s252627282930','s282930313233','s313233343536','doz112','doz1324','doz2536','col134','col235','col336','red','black','n26','n3','n35','n12','n28','n7','n29','n18','n22','n9','n31','n14','n20','n1','n33','n16','n24','n5','n10','n23','n0','n32','n15','n19','n4','n21','n2','n25','n17','n34','n6','n27','n13','n36','n11','n30','n8','spiel','serie023','orphelins','serie58']
    global bets
    bets={}
    for i in range(len(bets_keys)):
        bets[bets_keys[i]]=bets_values[i]

    selected_rb=var.get()
    if selected_rb:
        name_str=bets[name]
        if name_str.startswith('n') or name_str=='orphelins':
            single_bet=ff.single_bet(name_str, 5*selected_coin)
        elif name_str=='spiel':
            single_bet=ff.single_bet(name_str, 4*selected_coin)
        elif name_str=='serie023':
            single_bet=ff.single_bet(name_str, 9*selected_coin)
        elif name_str=='serie58':
            single_bet=ff.single_bet(name_str, 6*selected_coin)
        else:
            single_bet=ff.single_bet(name_str, selected_coin)
        
        bets_list.append(single_bet)
        bet_position=ff.bet_position(bets_list)
        bet_on_number=bet_position[name_str]
        overall_bet=ff.overall_bet(bet_position)
        chance=ff.chances(bet_position)

        if int(overall_bet)>=balance_history[-1]:
            root_er1=tk.Toplevel()
            root_er1.title('Info')
            root_er1.geometry('200x100')
            root_er1.resizable(False, False)

            info_er1=tk.Label(root_er1, text="You cannot make any bigger bet!", anchor='center', font=('Times New Roman', 12), wraplength=180)
            ok_but_er1=tk.Button(root_er1, text='OK', command=root_er1.destroy, width=10)

            info_er1.grid(row=0, column=0, padx=13)
            ok_but_er1.grid(row=1, column=0, padx=30, pady=3)

            root_er1.mainloop()

        elif int(overall_bet)>10000:
            root_er4=tk.Toplevel()
            root_er4.title('Info')
            root_er4.geometry('200x100')
            root_er4.resizable(False, False)

            info_er1=tk.Label(root_er4, text="Maximum bet is 10 000!", anchor='center', font=('Times New Roman', 12), wraplength=180)
            ok_but_er1=tk.Button(root_er4, text='OK', command=root_er4.destroy, width=10)

            info_er1.grid(row=0, column=0, padx=25, pady=10)
            ok_but_er1.grid(row=1, column=0, padx=35, pady=3)

            root_er4.mainloop()

        else:
            name.config(text=bet_on_number, fg='cyan', font=('Calibri', 10, 'bold'))
            balance.config(text=f'{balance_history[-1]-int(overall_bet)}')
            cur_bet.config(text=overall_bet)
            chances.config(text=chance)

    else:
        root_er2=tk.Toplevel()
        root_er2.title('Info')
        root_er2.geometry('200x100')
        root_er2.resizable(False, False)

        info_er1=tk.Label(root_er2, text="Choose a coin before you make a bet!", anchor='center', font=('Times New Roman', 12), wraplength=180)
        ok_but_er1=tk.Button(root_er2, text='OK', command=root_er2.destroy, width=10)

        info_er1.grid(row=0, column=0, padx=20)
        ok_but_er1.grid(row=1, column=0, padx=30, pady=3)

        root_er2.mainloop()

def bet_back(event=None):
    last_one=bets_list[-1]
    key_list=list(last_one.keys())
    number=key_list[0]
    str_number=str(number)
    for key, value in bets.items():
        if value==number:
            name=key

    bets_list.pop()

    bet_position=ff.bet_position(bets_list)
    overall_bet=ff.overall_bet(bet_position)
    chance=ff.chances(bet_position)
    try:
        bet_on_number=bet_position[number]
        name.config(text=bet_on_number, fg='white', font=('Calibri', 10, 'bold'))

    except:
        if str_number.startswith('doz112'):
            name.config(text='1 to 12', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('doz1324'):
            name.config(text='13 to 24', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('doz2536'):
            name.config(text='25 to 36', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('col134'):
            name.config(text='1st 12', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('col235'):
            name.config(text='2nd 12', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('col336'):
            name.config(text='3rd 12', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('spiel'):
            name.config(text='0 SPIEL', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('serie023'):
            name.config(text='SERIE 0/2/3', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('orphelins'):
            name.config(text='ORPHELINS', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('serie58'):
            name.config(text='SERIE 5/8', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('o') or str_number.startswith('n'):
            name.config(text=str_number[1:], fg='white', font=('TkDefaultFont', 9))
        else:
            name.config(text='')

    balance.config(text=f'{balance_history[-1]-int(overall_bet)}')
    cur_bet.config(text=overall_bet)
    chances.config(text=chance)

def bet_reset(event=None):
    for key, value in bets.items():
        str_number=str(value)
        name=key
        if str_number.startswith('doz112'):
            name.config(text='1 to 12', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('doz1324'):
            name.config(text='13 to 24', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('doz2536'):
            name.config(text='25 to 36', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('col134'):
            name.config(text='1st 12', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('col235'):
            name.config(text='2nd 12', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('col336'):
            name.config(text='3rd 12', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('spiel'):
            name.config(text='0 SPIEL', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('serie023'):
            name.config(text='SERIE 0/2/3', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('orphelins'):
            name.config(text='ORPHELINS', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('serie58'):
            name.config(text='SERIE 5/8', fg='white', font=('TkDefaultFont', 9))
        elif str_number.startswith('o') or str_number.startswith('n'):
            name.config(text=str_number[1:], fg='white', font=('TkDefaultFont', 9))
        else:
            name.config(text='')

    balance.config(text=f'{balance_history[-1]}')
    cur_bet.config(text='0')
    chances.config(text='0.00%')
    bets_list.clear()

def spin_check(event=None):
    bet_position=ff.bet_position(bets_list)
    overall_bet=int(ff.overall_bet(bet_position))

    if ('red' in bet_position and bet_position['red']<50) or ('black' in bet_position and bet_position['black']<50) or ('doz112' in bet_position and bet_position['doz112']<25) or ('doz1324' in bet_position and bet_position['doz1324']<25) or ('doz2536' in bet_position and bet_position['doz2536']<25) or ('col134' in bet_position and bet_position['col134']<25) or ('col235' in bet_position and bet_position['col235']<25) or ('col336' in bet_position and bet_position['col336']<25):
        root_er3=tk.Toplevel()
        root_er3.title('Info')
        root_er3.geometry('200x100')
        root_er3.resizable(False, False)

        info_er1=tk.Label(root_er3, text="You have to make bigger bet on dozens, columns or colours!", anchor='center', font=('Times New Roman', 12), wraplength=180)
        ok_but_er1=tk.Button(root_er3, text='OK', command=root_er3.destroy, width=10)

        info_er1.grid(row=0, column=0, padx=10)
        ok_but_er1.grid(row=1, column=0, padx=30, pady=3)

        root_er3.mainloop()
    else:
        pass

    outcome.config(text="Spinning...", font=('TkDefaultFont', 9))
    outcome.update_idletasks()
    
    # rotating image of a roulette circle
    def rotate_image(image_path, image_container, label, result, on_complete, angle_step=5, interval_ms=int(1000/360)):
        angle = 0
        original_image = Image.open(image_path)
        end_angle = -2 * 360 - ff.rotation_angle(result=result)
        def on_finish():
            label.after(100, on_complete)
        def update():
            nonlocal angle
            if angle <= end_angle:
                on_finish()
                return
            rotated = original_image.rotate(angle, resample=Image.BICUBIC, expand=False)
            image_container[0] = ImageTk.PhotoImage(rotated)
            label.config(image=image_container[0])
            angle -= angle_step
            label.after(interval_ms, update)
        update()

    # do it after the circle stops to rotate
    def on_complete():
        result_positions = ff.draw_result(result)
        result_of_bet = ff.bet_result(result, result_positions, bet_position)
        balance_after = ff.balance(balance_history, overall_bet, result_of_bet)
        bet_balance = balance_after[-1] - balance_after[-2]
        plus_minus = '+' if bet_balance >= 0 else ''
        bets_list.clear()

        outcome.config(text=result, font=('TkDefaultFont', 9, 'bold'))

        label1.config(text=ff.prev_numbers(results_list, len(results_list)))
        label2.config(text=ff.prev_numbers(results_list, len(results_list)-1))
        label3.config(text=ff.prev_numbers(results_list, len(results_list)-2))
        label4.config(text=ff.prev_numbers(results_list, len(results_list)-3))
        label5.config(text=ff.prev_numbers(results_list, len(results_list)-4))
        label6.config(text=ff.prev_numbers(results_list, len(results_list)-5))
        label7.config(text=ff.prev_numbers(results_list, len(results_list)-6))
        label8.config(text=ff.prev_numbers(results_list, len(results_list)-7))
        label9.config(text=ff.prev_numbers(results_list, len(results_list)-8))
        label10.config(text=ff.prev_numbers(results_list, len(results_list)-9))
        balance.config(text=f'{balance_after[-1]}')
        cur_bet.config(text='0')
        chances.config(text='0.00%')
        for key, value in bets.items():
            str_number=str(value)
            name=key
            if str_number.startswith('doz112'):
                name.config(text='1 to 12', fg='white', font=('TkDefaultFont', 9))
            elif str_number.startswith('doz1324'):
                name.config(text='13 to 24', fg='white', font=('TkDefaultFont', 9))
            elif str_number.startswith('doz2536'):
                name.config(text='25 to 36', fg='white', font=('TkDefaultFont', 9))
            elif str_number.startswith('col134'):
                name.config(text='1st 12', fg='white', font=('TkDefaultFont', 9))
            elif str_number.startswith('col235'):
                name.config(text='2nd 12', fg='white', font=('TkDefaultFont', 9))
            elif str_number.startswith('col336'):
                name.config(text='3rd 12', fg='white', font=('TkDefaultFont', 9))
            elif str_number.startswith('spiel'):
                name.config(text='0 SPIEL', fg='white', font=('TkDefaultFont', 9))
            elif str_number.startswith('serie023'):
                name.config(text='SERIE 0/2/3', fg='white', font=('TkDefaultFont', 9))
            elif str_number.startswith('orphelins'):
                name.config(text='ORPHELINS', fg='white', font=('TkDefaultFont', 9))
            elif str_number.startswith('serie58'):
                name.config(text='SERIE 5/8', fg='white', font=('TkDefaultFont', 9))
            elif str_number.startswith('o') or str_number.startswith('n'):
                name.config(text=str_number[1:], fg='white', font=('TkDefaultFont', 9))
            else:
                name.config(text='')

        result_name=f'o{result}'
        for key, value in bets.items():
            str_number=str(value)
            name=key
            if str_number==result_name:
                name.config(text='●', font=('Times New Roman', 9, 'bold'), fg='cyan')
                name.update_idletasks()
        
        # root info about the result of a draw
        root_bet_res=tk.Toplevel()
        root_bet_res.title('Info')
        root_bet_res.geometry('200x110')
        root_bet_res.resizable(False, False)
        info_er1=tk.Label(root_bet_res, text=f'Your bet result is:', anchor='center', font=('Times New Roman', 14), wraplength=180)
        info2_er1=tk.Label(root_bet_res, text=f'{plus_minus}{bet_balance}', anchor='center', font=('Times New Roman', 14, 'bold'), wraplength=180)
        ok_but_er1=tk.Button(root_bet_res, text='OK', command=root_bet_res.destroy, width=10)
        info_er1.grid(row=0, column=0, padx=30, pady=(5,0))
        info2_er1.grid(row=1, column=0, padx=40)
        ok_but_er1.grid(row=2, column=0, padx=40, pady=5)
        root_bet_res.mainloop()

    image_var = [None]
    result=ff.draw(results_list)

    rotate_image(circle_path, image_var, circle, result, on_complete)


# the rest of main window
circle_path='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\ruletka_kasyno\\roulette.png'
coin5path='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\ruletka_kasyno\\coin5.png'
coin10path='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\ruletka_kasyno\\coin10.png'
coin25path='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\ruletka_kasyno\\coin25.png'
coin50path='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\ruletka_kasyno\\coin50.png'
coin100path='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\ruletka_kasyno\\coin100.png'
arrowpath='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\ruletka_kasyno\\arrow.png'
circle_img=PhotoImage(file=circle_path)
coin5_img=PhotoImage(file=coin5path)
coin10_img=PhotoImage(file=coin10path)
coin25_img=PhotoImage(file=coin25path)
coin50_img=PhotoImage(file=coin50path)
coin100_img=PhotoImage(file=coin100path)
arrow_img=PhotoImage(file=arrowpath)
arrow_img=arrow_img.subsample(5, 7)


# main frame
frame_main=tk.Frame(root_main, width=(root_main.winfo_width())/2, height=(root_main.winfo_height())/2, bg='green')
frame_main.grid(row=0, column=0)


# sub frames
frame_prev=tk.Frame(frame_main, width=50, bg='green')
frame_circle=tk.Frame(frame_main, bg='green')
frame_bets=tk.Frame(frame_main, bg='green')
frame_neighbours=tk.Frame(frame_main, bg='green')
frame_money=tk.Frame(frame_main, bg='green')

frame_prev.grid(row=0, column=0, rowspan=3, padx=10)
frame_circle.grid(row=0, column=1, rowspan=3, padx=20)
frame_bets.grid(row=0, column=2, padx=80)
frame_neighbours.grid(row=1, column=2)
frame_money.grid(row=2, column=2)


# circle of roulette and play button
circle=tk.Label(frame_circle, image=circle_img, bg='green')
arrow=tk.Label(frame_circle, image=arrow_img, bg='green')
spin=tk.Button(frame_circle, width=4, text='Spin',command=spin_check, bg='grey25', fg='white')
help=tk.Button(frame_circle, width=4, text='Help', command=help_window, bg='grey25', fg='white')
outcome=tk.Label(frame_circle, text='Outcome', background='white', borderwidth=2, relief='solid', width=12, height=2)
outcome_label=tk.Label(frame_circle, text='Outcome', bg='green', fg='white', font=('TkDefaultFont', 10, 'bold'))
back=tk.Button(frame_circle, width=7, text='Back bet', command=bet_back, bg='grey25', fg='white')
reset=tk.Button(frame_circle, width=7, text='Reset bet', command=bet_reset, bg='grey25', fg='white')

circle.grid(row=0, column=0, columnspan=2)
arrow.grid(row=0, column=2, sticky='W')
spin.grid(row=1, column=0)
help.grid(row=1, column=1)
outcome_label.grid(row=1, column=0, columnspan=2, pady=(0,2))
outcome.grid(row=2, column=0, columnspan=2)
back.grid(row=3, column=0)
reset.grid(row=3, column=1)


# list of last numbers
label1=tk.Label(frame_prev, text='--', bg='green', fg='white', font=('TkDefaultFont', 9, 'bold'))
label2=tk.Label(frame_prev, text='--', bg='green', fg='white', font=('TkDefaultFont', 9, 'bold'))
label3=tk.Label(frame_prev, text='--', bg='green', fg='white', font=('TkDefaultFont', 9, 'bold'))
label4=tk.Label(frame_prev, text='--', bg='green', fg='white', font=('TkDefaultFont', 9, 'bold'))
label5=tk.Label(frame_prev, text='--', bg='green', fg='white', font=('TkDefaultFont', 9, 'bold'))
label6=tk.Label(frame_prev, text='--', bg='green', fg='white', font=('TkDefaultFont', 9, 'bold'))
label7=tk.Label(frame_prev, text='--', bg='green', fg='white', font=('TkDefaultFont', 9, 'bold'))
label8=tk.Label(frame_prev, text='--', bg='green', fg='white', font=('TkDefaultFont', 9, 'bold'))
label9=tk.Label(frame_prev, text='--', bg='green', fg='white', font=('TkDefaultFont', 9, 'bold'))
label10=tk.Label(frame_prev, text='--', bg='green', fg='white', font=('TkDefaultFont', 9, 'bold'))

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)
label5.grid(row=4, column=0)
label6.grid(row=5, column=0)
label7.grid(row=6, column=0)
label8.grid(row=7, column=0)
label9.grid(row=8, column=0)
label10.grid(row=9, column=0)


# numbers and bets
# only numbers
o0=tk.Button(frame_bets, width=4, height=11, text='0', command=lambda: bet(o0), bg='green', fg='white')
o1=tk.Button(frame_bets, width=4, height=2, text='1', command=lambda: bet(o1), bg='red', fg='white')
o2=tk.Button(frame_bets, width=4, height=2, text='2', command=lambda: bet(o2), bg='black', fg='white')
o3=tk.Button(frame_bets, width=4, height=2, text='3', command=lambda: bet(o3), bg='red', fg='white')
o4=tk.Button(frame_bets, width=4, height=2, text='4', command=lambda: bet(o4), bg='black', fg='white')
o5=tk.Button(frame_bets, width=4, height=2, text='5', command=lambda: bet(o5), bg='red', fg='white')
o6=tk.Button(frame_bets, width=4, height=2, text='6', command=lambda: bet(o6), bg='black', fg='white')
o7=tk.Button(frame_bets, width=4, height=2, text='7', command=lambda: bet(o7), bg='red', fg='white')
o8=tk.Button(frame_bets, width=4, height=2, text='8', command=lambda: bet(o8), bg='black', fg='white')
o9=tk.Button(frame_bets, width=4, height=2, text='9', command=lambda: bet(o9), bg='red', fg='white')
o10=tk.Button(frame_bets, width=4, height=2, text='10', command=lambda: bet(o10), bg='black', fg='white')
o11=tk.Button(frame_bets, width=4, height=2, text='11', command=lambda: bet(o11), bg='black', fg='white')
o12=tk.Button(frame_bets, width=4, height=2, text='12', command=lambda: bet(o12), bg='red', fg='white')
o13=tk.Button(frame_bets, width=4, height=2, text='13', command=lambda: bet(o13), bg='black', fg='white')
o14=tk.Button(frame_bets, width=4, height=2, text='14', command=lambda: bet(o14), bg='red', fg='white')
o15=tk.Button(frame_bets, width=4, height=2, text='15', command=lambda: bet(o15), bg='black', fg='white')
o16=tk.Button(frame_bets, width=4, height=2, text='16', command=lambda: bet(o16), bg='red', fg='white')
o17=tk.Button(frame_bets, width=4, height=2, text='17', command=lambda: bet(o17), bg='black', fg='white')
o18=tk.Button(frame_bets, width=4, height=2, text='18', command=lambda: bet(o18), bg='red', fg='white')
o19=tk.Button(frame_bets, width=4, height=2, text='19', command=lambda: bet(o19), bg='red', fg='white')
o20=tk.Button(frame_bets, width=4, height=2, text='20', command=lambda: bet(o20), bg='black', fg='white')
o21=tk.Button(frame_bets, width=4, height=2, text='21', command=lambda: bet(o21), bg='red', fg='white')
o22=tk.Button(frame_bets, width=4, height=2, text='22', command=lambda: bet(o22), bg='black', fg='white')
o23=tk.Button(frame_bets, width=4, height=2, text='23', command=lambda: bet(o23), bg='red', fg='white')
o24=tk.Button(frame_bets, width=4, height=2, text='24', command=lambda: bet(o24), bg='black', fg='white')
o25=tk.Button(frame_bets, width=4, height=2, text='25', command=lambda: bet(o25), bg='red', fg='white')
o26=tk.Button(frame_bets, width=4, height=2, text='26', command=lambda: bet(o26), bg='black', fg='white')
o27=tk.Button(frame_bets, width=4, height=2, text='27', command=lambda: bet(o27), bg='red', fg='white')
o28=tk.Button(frame_bets, width=4, height=2, text='28', command=lambda: bet(o28), bg='black', fg='white')
o29=tk.Button(frame_bets, width=4, height=2, text='29', command=lambda: bet(o29), bg='black', fg='white')
o30=tk.Button(frame_bets, width=4, height=2, text='30', command=lambda: bet(o30), bg='red', fg='white')
o31=tk.Button(frame_bets, width=4, height=2, text='31', command=lambda: bet(o31), bg='black', fg='white')
o32=tk.Button(frame_bets, width=4, height=2, text='32', command=lambda: bet(o32), bg='red', fg='white')
o33=tk.Button(frame_bets, width=4, height=2, text='33', command=lambda: bet(o33), bg='black', fg='white')
o34=tk.Button(frame_bets, width=4, height=2, text='34', command=lambda: bet(o34), bg='red', fg='white')
o35=tk.Button(frame_bets, width=4, height=2, text='35', command=lambda: bet(o35), bg='black', fg='white')
o36=tk.Button(frame_bets, width=4, height=2, text='36', command=lambda: bet(o36), bg='red', fg='white')
# double numbers - horizontal
d01=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d01), bg='dark violet')
d02=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d02), bg='dark violet')
d03=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d03), bg='dark violet')
d14=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d14), bg='dark violet')
d25=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d25), bg='dark violet')
d36=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d36), bg='dark violet')
d47=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d47), bg='dark violet')
d58=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d58), bg='dark violet')
d69=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d69), bg='dark violet')
d710=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d710), bg='dark violet')
d811=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d811), bg='dark violet')
d912=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d912), bg='dark violet')
d1013=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d1013), bg='dark violet')
d1114=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d1114), bg='dark violet')
d1215=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d1215), bg='dark violet')
d1316=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d1316), bg='dark violet')
d1417=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d1417), bg='dark violet')
d1518=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d1518), bg='dark violet')
d1619=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d1619), bg='dark violet')
d1720=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d1720), bg='dark violet')
d1821=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d1821), bg='dark violet')
d1922=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d1922), bg='dark violet')
d2023=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d2023), bg='dark violet')
d2124=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d2124), bg='dark violet')
d2225=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d2225), bg='dark violet')
d2326=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d2326), bg='dark violet')
d2427=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d2427), bg='dark violet')
d2528=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d2528), bg='dark violet')
d2629=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d2629), bg='dark violet')
d2730=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d2730), bg='dark violet')
d2831=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d2831), bg='dark violet')
d2932=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d2932), bg='dark violet')
d3033=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d3033), bg='dark violet')
d3134=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d3134), bg='dark violet')
d3235=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d3235), bg='dark violet')
d3336=tk.Button(frame_bets, width=2, height=2, command=lambda: bet(d3336), bg='dark violet')
# double numbers - vertical
d12=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d12), bg='dark violet')
d23=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d23), bg='dark violet')
d45=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d45), bg='dark violet')
d56=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d56), bg='dark violet')
d78=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d78), bg='dark violet')
d89=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d89), bg='dark violet')
d1011=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d1011), bg='dark violet')
d1112=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d1112), bg='dark violet')
d1314=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d1314), bg='dark violet')
d1415=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d1415), bg='dark violet')
d1617=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d1617), bg='dark violet')
d1718=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d1718), bg='dark violet')
d1920=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d1920), bg='dark violet')
d2021=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d2021), bg='dark violet')
d2223=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d2223), bg='dark violet')
d2324=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d2324), bg='dark violet')
d2526=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d2526), bg='dark violet')
d2627=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d2627), bg='dark violet')
d2829=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d2829), bg='dark violet')
d2930=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d2930), bg='dark violet')
d3132=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d3132), bg='dark violet')
d3233=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d3233), bg='dark violet')
d3435=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d3435), bg='dark violet')
d3536=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(d3536), bg='dark violet')
# thirds and quarters for 0
t012=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(t012), bg='darkorange4')
t023=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(t023), bg='darkorange4')
q0123=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q0123), bg='navy')
# thirds
t123=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t123), bg='darkorange4')
t456=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t456), bg='darkorange4')
t789=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t789), bg='darkorange4')
t101112=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t101112), bg='darkorange4')
t131415=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t131415), bg='darkorange4')
t161718=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t161718), bg='darkorange4')
t192021=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t192021), bg='darkorange4')
t222324=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t222324), bg='darkorange4')
t252627=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t252627), bg='darkorange4')
t282930=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t282930), bg='darkorange4')
t313233=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t313233), bg='darkorange4')
t343536=tk.Button(frame_bets, width=4, height=1, command=lambda: bet(t343536), bg='darkorange4')
# quarters
q1245=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q1245), bg='navy')
q2356=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q2356), bg='navy')
q4578=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q4578), bg='navy')
q5689=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q5689), bg='navy')
q781011=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q781011), bg='navy')
q891112=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q891112), bg='navy')
q10111314=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q10111314), bg='navy')
q11121415=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q11121415), bg='navy')
q13141617=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q13141617), bg='navy')
q14151718=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q14151718), bg='navy')
q16171920=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q16171920), bg='navy')
q17182021=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q17182021), bg='navy')
q19202223=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q19202223), bg='navy')
q20212324=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q20212324), bg='navy')
q22232526=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q22232526), bg='navy')
q23242627=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q23242627), bg='navy')
q25262829=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q25262829), bg='navy')
q26272930=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q26272930), bg='navy')
q28293132=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q28293132), bg='navy')
q29303233=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q29303233), bg='navy')
q31323435=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q31323435), bg='navy')
q32333536=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(q32333536), bg='navy')
# sixes
s123456=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(s123456), bg='deep pink')
s456789=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(s456789), bg='deep pink')
s789101112=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(s789101112), bg='deep pink')
s101112131415=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(s101112131415), bg='deep pink')
s131415161718=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(s131415161718), bg='deep pink')
s161718192021=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(s161718192021), bg='deep pink')
s192021222324=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(s192021222324), bg='deep pink')
s222324252627=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(s222324252627), bg='deep pink')
s252627282930=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(s252627282930), bg='deep pink')
s282930313233=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(s282930313233), bg='deep pink')
s313233343536=tk.Button(frame_bets, width=2, height=1, command=lambda: bet(s313233343536), bg='deep pink')
# dozens and columns
doz112=tk.Button(frame_bets, width=31, height=2, text='1 to 12', command=lambda: bet(doz112), bg='green', fg='white')
doz1324=tk.Button(frame_bets, width=31, height=2, text='13 to 24', command=lambda: bet(doz1324), bg='green', fg='white')
doz2536=tk.Button(frame_bets, width=31, height=2, text='25 to 36', command=lambda: bet(doz2536), bg='green', fg='white')
col134=tk.Button(frame_bets, width=8, height=2, text='1st 12', command=lambda: bet(col134), bg='green', fg='white')
col235=tk.Button(frame_bets, width=8, height=2, text='2nd 12', command=lambda: bet(col235), bg='green', fg='white')
col336=tk.Button(frame_bets, width=8, height=2, text='3rd 12', command=lambda: bet(col336), bg='green', fg='white')
# colours
red=tk.Button(frame_bets, width=7, height=2, background='red', command=lambda: bet(red))
black=tk.Button(frame_bets, width=7, height=2, background='black', command=lambda: bet(black))

o0.grid(row=0, column=0, rowspan=6, sticky='n')
o1.grid(row=4, column=2)
o2.grid(row=2, column=2)
o3.grid(row=0, column=2)
o4.grid(row=4, column=4)
o5.grid(row=2, column=4)
o6.grid(row=0, column=4)
o7.grid(row=4, column=6)
o8.grid(row=2, column=6)
o9.grid(row=0, column=6)
o10.grid(row=4, column=8)
o11.grid(row=2, column=8)
o12.grid(row=0, column=8)
o13.grid(row=4, column=10)
o14.grid(row=2, column=10)
o15.grid(row=0, column=10)
o16.grid(row=4, column=12)
o17.grid(row=2, column=12)
o18.grid(row=0, column=12)
o19.grid(row=4, column=14)
o20.grid(row=2, column=14)
o21.grid(row=0, column=14)
o22.grid(row=4, column=16)
o23.grid(row=2, column=16)
o24.grid(row=0, column=16)
o25.grid(row=4, column=18)
o26.grid(row=2, column=18)
o27.grid(row=0, column=18)
o28.grid(row=4, column=20)
o29.grid(row=2, column=20)
o30.grid(row=0, column=20)
o31.grid(row=4, column=22)
o32.grid(row=2, column=22)
o33.grid(row=0, column=22)
o34.grid(row=4, column=24)
o35.grid(row=2, column=24)
o36.grid(row=0, column=24)
# double numbers - vertical
d01.grid(row=4, column=1)
d02.grid(row=2, column=1)
d03.grid(row=0, column=1)
d14.grid(row=4, column=3)
d25.grid(row=2, column=3)
d36.grid(row=0, column=3)
d47.grid(row=4, column=5)
d58.grid(row=2, column=5)
d69.grid(row=0, column=5)
d710.grid(row=4, column=7)
d811.grid(row=2, column=7)
d912.grid(row=0, column=7)
d1013.grid(row=4, column=9)
d1114.grid(row=2, column=9)
d1215.grid(row=0, column=9)
d1316.grid(row=4, column=11)
d1417.grid(row=2, column=11)
d1518.grid(row=0, column=11)
d1619.grid(row=4, column=13)
d1720.grid(row=2, column=13)
d1821.grid(row=0, column=13)
d1922.grid(row=4, column=15)
d2023.grid(row=2, column=15)
d2124.grid(row=0, column=15)
d2225.grid(row=4, column=17)
d2326.grid(row=2, column=17)
d2427.grid(row=0, column=17)
d2528.grid(row=4, column=19)
d2629.grid(row=2, column=19)
d2730.grid(row=0, column=19)
d2831.grid(row=4, column=21)
d2932.grid(row=2, column=21)
d3033.grid(row=0, column=21)
d3134.grid(row=4, column=23)
d3235.grid(row=2, column=23)
d3336.grid(row=0, column=23)
# double numbers - horizontal
d12.grid(row=3, column=2)
d23.grid(row=1, column=2)
d45.grid(row=3, column=4)
d56.grid(row=1, column=4)
d78.grid(row=3, column=6)
d89.grid(row=1, column=6)
d1011.grid(row=3, column=8)
d1112.grid(row=1, column=8)
d1314.grid(row=3, column=10)
d1415.grid(row=1, column=10)
d1617.grid(row=3, column=12)
d1718.grid(row=1, column=12)
d1920.grid(row=3, column=14)
d2021.grid(row=1, column=14)
d2223.grid(row=3, column=16)
d2324.grid(row=1, column=16)
d2526.grid(row=3, column=18)
d2627.grid(row=1, column=18)
d2829.grid(row=3, column=20)
d2930.grid(row=1, column=20)
d3132.grid(row=3, column=22)
d3233.grid(row=1, column=22)
d3435.grid(row=3, column=24)
d3536.grid(row=1, column=24)
# thirds and quarters for 0
t012.grid(row=3, column=1)
t023.grid(row=1, column=1)
q0123.grid(row=5, column=1)
# thirds
t123.grid(row=5, column=2)
t456.grid(row=5, column=4)
t789.grid(row=5, column=6)
t101112.grid(row=5, column=8)
t131415.grid(row=5, column=10)
t161718.grid(row=5, column=12)
t192021.grid(row=5, column=14)
t222324.grid(row=5, column=16)
t252627.grid(row=5, column=18)
t282930.grid(row=5, column=20)
t313233.grid(row=5, column=22)
t343536.grid(row=5, column=24)
# quarters
q1245.grid(row=3, column=3)
q2356.grid(row=1, column=3)
q4578.grid(row=3, column=5)
q5689.grid(row=1, column=5)
q781011.grid(row=3, column=7)
q891112.grid(row=1, column=7)
q10111314.grid(row=3, column=9)
q11121415.grid(row=1, column=9)
q13141617.grid(row=3, column=11)
q14151718.grid(row=1, column=11)
q16171920.grid(row=3, column=13)
q17182021.grid(row=1, column=13)
q19202223.grid(row=3, column=15)
q20212324.grid(row=1, column=15)
q22232526.grid(row=3, column=17)
q23242627.grid(row=1, column=17)
q25262829.grid(row=3, column=19)
q26272930.grid(row=1, column=19)
q28293132.grid(row=3, column=21)
q29303233.grid(row=1, column=21)
q31323435.grid(row=3, column=23)
q32333536.grid(row=1, column=23)
# sixes
s123456.grid(row=5, column=3)
s456789.grid(row=5, column=5)
s789101112.grid(row=5, column=7)
s101112131415.grid(row=5, column=9)
s131415161718.grid(row=5, column=11)
s161718192021.grid(row=5, column=13)
s192021222324.grid(row=5, column=15)
s222324252627.grid(row=5, column=17)
s252627282930.grid(row=5, column=19)
s282930313233.grid(row=5, column=21)
s313233343536.grid(row=5, column=23)
# dozens and columns
doz112.grid(row=6, column=2, columnspan=7, sticky='w')
doz1324.grid(row=6, column=10, columnspan=7, sticky='w')
doz2536.grid(row=6, column=18, columnspan=7, sticky='w')
col134.grid(row=0, column=25)
col235.grid(row=2, column=25)
col336.grid(row=4, column=25)
# colours
red.grid(row=7, column=11, columnspan=2)
black.grid(row=7, column=14, columnspan=2)

# neighbours
n26=tk.Button(frame_neighbours, width=3, height=1, text='26', command=lambda: bet(n26), bg='black', fg='white')
n3=tk.Button(frame_neighbours, width=3, height=1, text='3', command=lambda: bet(n3), bg='red', fg='white')
n35=tk.Button(frame_neighbours, width=3, height=1, text='35', command=lambda: bet(n35), bg='black', fg='white')
n12=tk.Button(frame_neighbours, width=3, height=1, text='12', command=lambda: bet(n12), bg='red', fg='white')
n28=tk.Button(frame_neighbours, width=3, height=1, text='28', command=lambda: bet(n28), bg='black', fg='white')
n7=tk.Button(frame_neighbours, width=3, height=1, text='7', command=lambda: bet(n7), bg='red', fg='white')
n29=tk.Button(frame_neighbours, width=3, height=1, text='29', command=lambda: bet(n29), bg='black', fg='white')
n18=tk.Button(frame_neighbours, width=3, height=1, text='18', command=lambda: bet(n18), bg='red', fg='white')
n22=tk.Button(frame_neighbours, width=3, height=1, text='22', command=lambda: bet(n22), bg='black', fg='white')
n9=tk.Button(frame_neighbours, width=3, height=1, text='9', command=lambda: bet(n9), bg='red', fg='white')
n31=tk.Button(frame_neighbours, width=3, height=1, text='31', command=lambda: bet(n31), bg='black', fg='white')
n14=tk.Button(frame_neighbours, width=3, height=1, text='14', command=lambda: bet(n14), bg='red', fg='white')
n20=tk.Button(frame_neighbours, width=3, height=1, text='20', command=lambda: bet(n20), bg='black', fg='white')
n1=tk.Button(frame_neighbours, width=3, height=1, text='1', command=lambda: bet(n1), bg='red', fg='white')
n33=tk.Button(frame_neighbours, width=3, height=1, text='33', command=lambda: bet(n33), bg='black', fg='white')
n16=tk.Button(frame_neighbours, width=3, height=1, text='16', command=lambda: bet(n16), bg='red', fg='white')
n24=tk.Button(frame_neighbours, width=3, height=1, text='24', command=lambda: bet(n24), bg='black', fg='white')
n5=tk.Button(frame_neighbours, width=3, height=1, text='5', command=lambda: bet(n5), bg='red', fg='white')
n10=tk.Button(frame_neighbours, width=3, height=1, text='10', command=lambda: bet(n10), bg='black', fg='white')
n23=tk.Button(frame_neighbours, width=3, height=1, text='23', command=lambda: bet(n23), bg='red', fg='white')
n0=tk.Button(frame_neighbours, width=3, height=1, text='0', command=lambda: bet(n0), bg='green', fg='white')
n32=tk.Button(frame_neighbours, width=3, height=1, text='32', command=lambda: bet(n32), bg='red', fg='white')
n15=tk.Button(frame_neighbours, width=3, height=1, text='15', command=lambda: bet(n15), bg='black', fg='white')
n19=tk.Button(frame_neighbours, width=3, height=1, text='19', command=lambda: bet(n19), bg='red', fg='white')
n4=tk.Button(frame_neighbours, width=3, height=1, text='4', command=lambda: bet(n4), bg='black', fg='white')
n21=tk.Button(frame_neighbours, width=3, height=1, text='21', command=lambda: bet(n21), bg='red', fg='white')
n2=tk.Button(frame_neighbours, width=3, height=1, text='2', command=lambda: bet(n2), bg='black', fg='white')
n25=tk.Button(frame_neighbours, width=3, height=1, text='25', command=lambda: bet(n25), bg='red', fg='white')
n17=tk.Button(frame_neighbours, width=3, height=1, text='17', command=lambda: bet(n17), bg='black', fg='white')
n34=tk.Button(frame_neighbours, width=3, height=1, text='34', command=lambda: bet(n34), bg='red', fg='white')
n6=tk.Button(frame_neighbours, width=3, height=1, text='6', command=lambda: bet(n6), bg='black', fg='white')
n27=tk.Button(frame_neighbours, width=3, height=1, text='27', command=lambda: bet(n27), bg='red', fg='white')
n13=tk.Button(frame_neighbours, width=3, height=1, text='13', command=lambda: bet(n13), bg='black', fg='white')
n36=tk.Button(frame_neighbours, width=3, height=1, text='36', command=lambda: bet(n36), bg='red', fg='white')
n11=tk.Button(frame_neighbours, width=3, height=1, text='11', command=lambda: bet(n11), bg='black', fg='white')
n30=tk.Button(frame_neighbours, width=3, height=1, text='30', command=lambda: bet(n30), bg='red', fg='white')
n8=tk.Button(frame_neighbours, width=3, height=1, text='8', command=lambda: bet(n8), bg='black', fg='white')
spiel=tk.Button(frame_neighbours, text='0 SPIEL', width=12, command=lambda: bet(spiel), bg='green', fg='white')
serie023=tk.Button(frame_neighbours, text='SEIRE 0/2/3', width=21, command=lambda: bet(serie023), bg='green', fg='white')
orphelins=tk.Button(frame_neighbours, text='ORPHELINS', width=21, command=lambda: bet(orphelins), bg='green', fg='white')
serie58=tk.Button(frame_neighbours, text='SERIE 5/8', width=25, command=lambda: bet(serie58), bg='green', fg='white')

n26.grid(row=1, column=0)
n3.grid(row=0, column=1)
n35.grid(row=0, column=2)
n12.grid(row=0, column=3)
n28.grid(row=0, column=4)
n7.grid(row=0, column=5)
n29.grid(row=0, column=6)
n18.grid(row=0, column=7)
n22.grid(row=0, column=8)
n9.grid(row=0, column=9)
n31.grid(row=0, column=10)
n14.grid(row=0, column=11)
n20.grid(row=0, column=12)
n1.grid(row=0, column=13)
n33.grid(row=0, column=14)
n16.grid(row=0, column=15)
n24.grid(row=0, column=16)
n5.grid(row=0, column=17)
n10.grid(row=0, column=18)
n23.grid(row=0, column=19)
n0.grid(row=2, column=1)
n32.grid(row=2, column=2)
n15.grid(row=2, column=3)
n19.grid(row=2, column=4)
n4.grid(row=2, column=5)
n21.grid(row=2, column=6)
n2.grid(row=2, column=7)
n25.grid(row=2, column=8)
n17.grid(row=2, column=10)
n34.grid(row=2, column=11)
n6.grid(row=2, column=12)
n27.grid(row=2, column=14)
n13.grid(row=2, column=15)
n36.grid(row=2, column=16)
n11.grid(row=2, column=17)
n30.grid(row=2, column=18)
n8.grid(row=2, column=19)
spiel.grid(row=1, column=1, columnspan=3, sticky='w')
serie023.grid(row=1, column=4, columnspan=5, sticky='w')
orphelins.grid(row=1, column=9, columnspan=5, sticky='w')
serie58.grid(row=1, column=14, columnspan=6, sticky='w')


# money
balance=tk.Label(frame_money, text='Your balance', background='white', borderwidth=2, relief='solid', width=12, height=2)
balance_label=tk.Label(frame_money, text='Balance', bg='green', fg='white', font=('TkDefaultFont', 10, 'bold'))
cur_bet=tk.Label(frame_money, text='Bet', background='white', borderwidth=2, relief='solid', width=12, height=2)
cur_bet_label=tk.Label(frame_money, text='Bet', bg='green', fg='white', font=('TkDefaultFont', 10, 'bold'))
chances=tk.Label(frame_money, text='Chances', background='white', borderwidth=2, relief='solid', width=12, height=2)
chances_label=tk.Label(frame_money, text='Chances', bg='green', fg='white', font=('TkDefaultFont', 10, 'bold'))
check5=tk.Radiobutton(frame_money, variable=var, value=1, bg='green')
check10=tk.Radiobutton(frame_money, variable=var, value=2, bg='green')
check25=tk.Radiobutton(frame_money, variable=var, value=3, bg='green')
check50=tk.Radiobutton(frame_money, variable=var, value=4, bg='green')
check100=tk.Radiobutton(frame_money, variable=var, value=5, bg='green')
coin5=tk.Button(frame_money, image=coin5_img, width=60, height=60, command=coin_choose_5, bg='green')
coin10=tk.Button(frame_money, image=coin10_img, width=60, height=60, command=coin_choose_10, bg='green')
coin25=tk.Button(frame_money, image=coin25_img, width=60, height=60, command=coin_choose_25, bg='green')
coin50=tk.Button(frame_money, image=coin50_img, width=60, height=60, command=coin_choose_50, bg='green')
coin100=tk.Button(frame_money, image=coin100_img, width=60, height=60, command=coin_choose_100, bg='green')

balance_label.grid(row=0, column=0, pady=(10,0))
cur_bet_label.grid(row=0, column=1, pady=(10,0))
chances_label.grid(row=0, column=2, pady=(10,0))
balance.grid(row=1, column=0)
cur_bet.grid(row=1, column=1)
chances.grid(row=1, column=2)
check5.grid(row=0, column=3)
check10.grid(row=0, column=4)
check25.grid(row=0, column=5)
check50.grid(row=0, column=6)
check100.grid(row=0, column=7)
coin5.grid(row=1, column=3)
coin10.grid(row=1, column=4)
coin25.grid(row=1, column=5)
coin50.grid(row=1, column=6)
coin100.grid(row=1, column=7)


root_main.mainloop()