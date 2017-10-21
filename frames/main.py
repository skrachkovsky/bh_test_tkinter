from tkinter import ttk
from frames import BaseFrame
import tkinter


class TopButtons(BaseFrame):
    btn1 = None
    btn2 = None

    def _build_elements(self):
        f1 = ttk.Frame(self)
        self.btn1 = ttk.Button(f1, text='Button 1')
        self.btn2 = ttk.Button(f1, text='Button 1')
        self.btn1.pack(side='left')
        self.btn2.pack(side='right')
        f1.pack(fill='x', side='left', expand=True)

    def _handle_events(self):
        pass


class TextFrame(BaseFrame):
    txt = None

    def _build_elements(self):
        f1 = ttk.Frame(self)
        sb = ttk.Scrollbar(f1)
        sb.pack(side='right', fill='y')
        txt = tkinter.Text(f1)
        txt.pack(side='left', fill='both', expand=True)
        sb['command'] = txt.yview
        txt['yscrollcommand'] = sb.set
        f1.pack()

    def _handle_events(self):
        pass