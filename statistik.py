"""
statistik.py
Dieses Modul kuemmert sich um die Statistik.
"""
import settings

import json
import Tkinter as tk
import os.path


SPENT = 'spent'
PEOPLE = 'people'
NAME = 'name'
DATAPATH = '/home/pi/jt/data.json'



def top10(frame):
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
    for key, value in sorted(list.iteritems(), key=lambda(k,v): (v,k), reverse=True):
        if(i >= 5):
            break
        frame.Listbox1.insert(tk.END, '%s %s' % (value, key))
        i = i+1  
