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
    for i in data[PEOPLE]:
        try:
            list[str(i[NAME]).translate(None, '\n')] = i[SPENT]
        except KeyError:
            # Key is not present
            print("KeyError "+i[NAME])
            i[SPENT] = float(0)
            list[i[NAME]] = i[SPENT]
            settings.saveData(data, 'data.json')
            pass
    i = 0
    for key, value in sorted(list.iteritems(), key=lambda k,v: (v,k), reverse=True):
        if(i >= 5):
            break
        frame.Listbox1.insert(tk.END, '%s %s' % (value, key))
        i = i+1  
