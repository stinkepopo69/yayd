import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
import time as tm

root = tk.Tk()
root.geometry('600x200')
root.resizable(False,False)
root.title('<3')
root['background'] = 'black'

label = tk.Label(
    text="Hello my love,",
    font = "Consolas 15",
    fg = '#ff69b4',
    bg = 'black'
).pack()
label = tk.Label(
    text="Would you like to be my valentine this year?",
    font = "Consolas 15",
    fg = '#ff69b4',
    bg = 'black'
).pack()


agreement = tk.BooleanVar()

def submit():
    if agreement.get() == True:
        new= tk.Tk()
        root.destroy()
        new.geometry("500x100")
        new['background'] = 'black'
        new.title("WOOHOO")
        label = tk.Label(
            new,
            text="Woohoo! What an honor this is! :)",
            font = "Consolas 15",
            fg = '#ff69b4',
            bg = 'black'
        ).grid(column = 5, row = 0)
        new.after(3000,lambda:new.destroy())

    else:
        new= tk.Tk()
        root.destroy()
        new.geometry("200x100")
        new['background'] = 'black'
        new.title("oh.")
        label = tk.Label(
            new,
            text="Oh. Ok. :(",
            font = "Consolas 15",
            fg = '#ff69b4',
            bg = 'black'
        ).grid(column = 5, row = 0)
        new.after(3000,lambda:new.destroy())

    

yes = tk.Checkbutton(
    root,
    text='Yes',
    variable=agreement,
    onvalue= True,
    offvalue= False,
    fg = '#ff69b4',
    bg = 'black',
    font = 'Consolas',
)

no = tk.Checkbutton(
    root,
    text='No ',
    variable = agreement,
    onvalue= False,
    offvalue= True,
    fg = '#ff69b4',
    bg = 'black',
    font = 'Consolas',
)

submit = tk.Button(
    root,
    text = 'Submit',
    command= submit,
    fg = '#ff69b4',
    bg = 'black',
    font = 'Consolas 8',
)

yes.pack()
no.pack()
submit.pack()


root.mainloop()
exit()