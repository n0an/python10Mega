from tkinter import *

window = Tk()

def km_to_miles():
    print(e1_value.get())
    try:
        miles = float(e1_value.get()) * 1.6
    except ValueError:
        miles = 'Error'
    t1.insert(END, miles)

b1 = Button(window, text='Execute', command=km_to_miles)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column = 1)


t1 = Text(window, height=1,width=20)
t1.grid(row=0, column=2)


window.mainloop()
