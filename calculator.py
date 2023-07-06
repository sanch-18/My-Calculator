from tkinter import *


def click(event):
    txt = event.widget.cget('text')
    if txt =='=':
        string = tval.get()
        if tval.get().isdigit():
            value = int(tval.get())
        else:
            if 'x' in string:
                string = string.replace('x', '*')
            if '^' in string:
                string = string.replace('^', '**')
            try:
                value = eval(string)
            except:
                value = 'ERROR'
        tval.set(value)
        screen.update()
    elif txt == 'C':
        tval.set('')
        screen.update()
    elif txt == 'B':
        tval.set(tval.get()[0:-1])
    else:
        tval.set(tval.get()+txt)
        screen.update()

def frames():
    global f
    f = Frame(root, bg='black')
    f.pack()

def buttons(txt):
    ft = 21
    x = 2
    if (txt=='-'):
        ft = 22
        x = 4
    if (txt=='/'):
        x = 6
    if (txt=='.'):
        x = 5
        
    if (txt=='B' or txt=='C'):
        x = 1
    if (txt=='('):
        x = 5
    if (txt==')'):
        x = 5
    global b
    b = Button(f, text=txt, font=('lucida', ft, 'bold'), padx=x)
    b.pack(side=LEFT, padx=30, pady=9)
    b.bind('<Button-1>', click)

def textbar():
    global tval, screen
    tval = StringVar()
    tval.set('')
    screen = Entry(root, textvar = tval, font = ('lucida', 32, 'bold'))
    screen.pack(fill=X, padx=10, pady=10)

def line(a, b, c):
    frames()
    buttons(a)
    buttons(b)
    buttons(c)


if __name__=='__main__':
    root = Tk()
    root.title('Calculator By Sancho')
    root.wm_iconbitmap("games.ico")
    root.configure(background='grey')
    root.geometry('444x640')
    textbar()
    line('9', '8', '7')
    line('6', '5', '4')
    line('3', '2', '1')
    line('0', '-', '+')
    line('/', 'x', '^')
    line('(', ')', 'B')
    line('.', '=', 'C')
    root.mainloop()