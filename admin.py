#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import sys

import tkinter as tk
import tkinter.ttk as ttk

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = New_Toplevel (root)
    #admin_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = New_Toplevel (w)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("480x320+1369+370")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.add = tk.Button(top)
        self.add.place(relx=0.08, rely=0.09, height=64, width=141)
        self.add.configure(activebackground="#d9d9d9")
        self.add.configure(activeforeground="#000000")
        self.add.configure(background="#d9d9d9")
        self.add.configure(disabledforeground="#a3a3a3")
        self.add.configure(foreground="#000000")
        self.add.configure(highlightbackground="#d9d9d9")
        self.add.configure(highlightcolor="black")
        self.add.configure(pady="0")
        self.add.configure(text='''person''')
        self.add.configure(width=141)

        self.aufladen = tk.Button(top)
        self.aufladen.place(relx=0.5, rely=0.09, height=64, width=157)
        self.aufladen.configure(activebackground="#d9d9d9")
        self.aufladen.configure(activeforeground="#000000")
        self.aufladen.configure(background="#d9d9d9")
        self.aufladen.configure(disabledforeground="#a3a3a3")
        self.aufladen.configure(foreground="#000000")
        self.aufladen.configure(highlightbackground="#d9d9d9")
        self.aufladen.configure(highlightcolor="black")
        self.aufladen.configure(pady="0")
        self.aufladen.configure(text='''aufladen''')
        self.aufladen.configure(width=157)

        self.abfragen = tk.Button(top)
        self.abfragen.place(relx=0.5, rely=0.41, height=64, width=147)
        self.abfragen.configure(activebackground="#d9d9d9")
        self.abfragen.configure(activeforeground="#000000")
        self.abfragen.configure(background="#d9d9d9")
        self.abfragen.configure(disabledforeground="#a3a3a3")
        self.abfragen.configure(foreground="#000000")
        self.abfragen.configure(highlightbackground="#d9d9d9")
        self.abfragen.configure(highlightcolor="black")
        self.abfragen.configure(pady="0")
        self.abfragen.configure(text='''abfragen''')
        self.abfragen.configure(width=147)

def start():
    print("admingui wird gestartet")
    vp_start_gui()
    


if __name__ == '__main__':
    vp_start_gui()



