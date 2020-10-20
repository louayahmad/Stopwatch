import tkinter as Tkinter

from datetime import datetime

import time


counter = 0

running = False


def mainStopwatch(label):

    def count():

        if running:

            global counter
            

            tt = datetime.utcfromtimestamp(counter)
            string = tt.strftime('%H:%M:%S')
            display = string
	
            label['text'] = display
	
			
            label.after(1000, count)
            counter += 1
	
    count()
	
 
def Start(label):
    global running
    running = True
    mainStopwatch(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'
	

def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False
	

def Reset(label):
	global counter
	counter = 0
	 
	if not running:
		reset['state'] = 'disabled'
		label['text'] = '00:00:00'
	 
	else:
		label['text'] = '00:00:00'

	


root = Tkinter.Tk()
root.title("Stopwatch")
root.configure(bg='black')

root.minsize(width=350, height=85)
label = Tkinter.Label(root, bg='black',text="Click Start to Begin!", fg='white', font='Arial 24 bold')
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, bg='grey', text='Start', width=6, command=lambda: Start(label))
stop = Tkinter.Button(f, bg='grey', text='Stop', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(f, bg='grey', text='Reset', width=6, state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
root.mainloop()
