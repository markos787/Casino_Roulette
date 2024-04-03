import functions as ff
import tkinter as tk
import time

# main window
root_main=tk.Tk()
root_main.title('Casino Roulette')
root_main.geometry('1500x600')

# main frame
frame_main=tk.Frame(root_main, width=(root_main.winfo_width())/2, height=(root_main.winfo_height())/2)
frame_main.grid(row=0, column=0)

# sub frames
frame_prev=tk.Frame(frame_main, width=50)
frame_circle=tk.Frame(frame_main)
frame_bets=tk.Frame(frame_main)
frame_neighbours=tk.Frame(frame_main)
frame_money=tk.Frame(frame_main)

frame_prev.grid(row=0, column=0, rowspan=3)
frame_circle.grid(row=0, column=1, rowspan=3)
frame_bets.grid(row=0, column=2)
frame_neighbours.grid(row=1, column=2)
frame_money.grid(row=2, column=2)

# list of last numbers
label1=tk.Label(frame_prev, text='--')
label2=tk.Label(frame_prev, text='--')
label3=tk.Label(frame_prev, text='--')
label4=tk.Label(frame_prev, text='--')
label5=tk.Label(frame_prev, text='--')
label6=tk.Label(frame_prev, text='--')
label7=tk.Label(frame_prev, text='--')
label8=tk.Label(frame_prev, text='--')
label9=tk.Label(frame_prev, text='--')
label10=tk.Label(frame_prev, text='--')

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

# circle of roulette and play button


root_main.mainloop()