import tkinter
from tkinter import ttk

# app = tkinter.Tk()
# app.minsize(300, 300)
#
# f1 = ttk.Frame(app)
# f1.pack(fill='x')
#
# btn = ttk.Button(f1, text='Button name')
# btn.pack(side='left')
# label = ttk.Label(f1, text='label')
# label.pack(side='right')

# input = tkinter.Entry(app)
# input.pack()
# txt = tkinter.Text(app)
# txt.pack()
# lb = tkinter.Listbox(app)
# lb.insert(tkinter.END, 'item 1')
# lb.insert(tkinter.END, 'item 2')
# lb.insert(tkinter.END, 'item 3')
# lb.pack()
# cb = tkinter.Checkbutton(app, text='Check')
# cb.pack()
# rbvar = tkinter.IntVar()
# rb1 = tkinter.Radiobutton(app, text='Choice 1', variable=rbvar, value=1)
# rb2 = tkinter.Radiobutton(app, text='Choice 2', variable=rbvar, value=2)
# rb1.pack()
# rb2.pack()
from frames.main import TopButtons, TextFrame


class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.build_elements()

    def build_elements(self):
        f1 = TopButtons(self)
        f1.pack(fill='x', side='top')
        txt = TextFrame(self)
        txt.pack()


app = App()
app.minsize(300, 300)
app.mainloop()

