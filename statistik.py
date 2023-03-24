#-*- coding:utf-8 -*-
"""
statistik.py
Dieses Modul kümmert sich um die Statistik.
"""
import settings

import json
import tkinter as tk
import os.path


SPENT = 'spent'
PEOPLE = 'people'
NAME = 'name'



def top10(frame):
    """
    Schreibt die 10 umsatzstärksten Kunden in ein Frame
    
    Args:
        frame: Das frame, in dem die Namen stehen sollen
    
    """
    frame.Listbox1.delete(0, tk.END)
    data = settings.getData('data.json')
    list = {}
    i = 0
    for key, value in sorted(list.items(), key=lambda item: (-item[1], item[0]), reverse=True):
        if(i >= 5):
            break
        frame.Listbox1.insert(tk.END, '%s %s' % (value, key))
        i = i+1
 
