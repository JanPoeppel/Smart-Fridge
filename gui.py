# -*- coding: UTF-8 -*-
import tkinter as tk
import time
import person
import money
import shop
from tkinter.constants import SINGLE, WORD
import rfid
from subprocess import call



LARGE_FONT= ('Verdana', 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, Page0, Page1, Page2, Page3, PageAdminLogin, PageBuyLogin, Page5, PageAdmin, PageNewMoney, PageDeposit, Page9, Page10, Page11, Page12, Page13,Page14, PageError, PageOverview, PageAddPerson):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPage)
      
    def show_frame(self, cont, name = None, rfids = None, amount = 0, controller = None, error = None, page = None):
        if(cont == None):
            cont = StartPage
        frame = self.frames[cont]
        frame.tkraise()
        frame.update()
        
        
        
        if(cont == PageAdminLogin):
            rfids = rfid.readUID()
            status = person.auth(rfids)
            if(status == True):
                self.show_frame(PageAdmin)
            else:
                self.show_frame(StartPage)
        elif(cont == Page1):
            frame.show_ele(frame)
        elif(cont == Page2):
            frame.show_ele(frame)
        elif(cont == PageBuyLogin):
            rfids = rfid.readUID()
            status = shop.buy(rfids, float(amount))
            if(status == -1):
                self.show_frame(PageError, error = 'Nicht genug Geld', controller = controller, page = Page5)
            else:                
                reseteinkauf()
                self.show_frame(PageNewMoney, rfids = rfids, controller = controller)
        elif(cont == Page5):
            frame.init(frame)
        elif(cont == PageNewMoney):
            if(amount != 0 and amount != None):
                money.addMoney(rfids, amount)
            frame.setRFIDLabel(frame, rfids, controller)
            time.sleep(5)
            self.show_frame(StartPage)
        elif(cont == Page9):
            frame.reset(frame)
            frame.setRFIDLabel(frame, rfids)
        elif(cont == Page11):
            frame.reset(frame)
        elif(cont == Page12):
            rfids = rfid.readUID()
            self.show_frame(PageOverview, rfids = rfids)
        elif(cont == PageAddPerson):
            status = person.addPerson(name, rfids)
            if(status == 1):
                frame.setRFIDLabel(frame, name, rfids)
                time.sleep(2)
                self.show_frame(StartPage)
            elif(status == -1):
                self.show_frame(PageError, controller= controller, error = 'Name bereits vorhanden', page =Page9)
                return #showFrame 9(?)
            elif(status == -2):
                self.show_frame(PageError, controller= controller, error = 'RFID bereits vorhanden, Vorgang wird abgebrochen')
                return #showFrame StartPage
        elif(cont == Page13):
            rfids = rfid.readUID()
            self.show_frame(PageNewMoney, rfids = rfids, amount = amount, controller = controller)
        elif(cont == Page14):
            rfids = rfid.readUID()
            self.show_frame(Page9, rfids = rfids, controller = controller)
        elif(cont == PageError):
            frame.setError(frame, error, controller, page = page)
        elif(cont == PageOverview):
            if(name == None):
                cont.setRFIDLabel(frame, rfids = rfids)
            else:
                cont.setRFIDLabel(frame, name = name)
    
        
"""
Startpage:
---------------------------
Trinken     Essen
Admin       Abfrage
"""

def __setButtonAttributes(self, button, relx, rely, height, width, activebackground, activeforeground, background, disabledforeground, foreground, highlightbackground, highlightcolor, pady, text, width2):
        button.place(relx= relx, rely=rely, height= height, width = width)
        button.configure(activebackground=activebackground)
        button.configure(activeforeground=activeforeground)
        button.configure(background=background)
        button.configure(disabledforeground=disabledforeground)
        button.configure(foreground=foreground)
        button.configure(highlightbackground=highlightbackground)
        button.configure(highlightcolor=highlightcolor)
        button.configure(pady=pady)
        button.configure(text=text)
        button.configure(width=width2)

class StartPage(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, height = 320, width = 480)

        self.drinkButton = tk.Button(self)
        #__setButtonAttributes(self, self.drinkButton, 0.0, 0.0, 160, 240, '#d9d9d9', '#000000', '#d9d9d9', '#a3a3a3', '#000000', '#d9d9d9', 'black', '0', 'Trinken', 162)
        self.drinkButton.bind('<Button-1>',lambda e:controller.show_frame(Page0))
        self.drinkButton.place(relx=0.0, rely=0.0, height=160, width=240)
        self.drinkButton.configure(activebackground='#d9d9d9')
        self.drinkButton.configure(activeforeground='#000000')
        self.drinkButton.configure(background='#d9d9d9')
        self.drinkButton.configure(disabledforeground='#a3a3a3')
        self.drinkButton.configure(foreground='#000000')
        self.drinkButton.configure(highlightbackground='#d9d9d9')
        self.drinkButton.configure(highlightcolor='black')
        self.drinkButton.configure(pady='0')
        self.drinkButton.configure(text='Trinken')
        self.drinkButton.configure(width=162)
        

        self.foodButton = tk.Button(self)
        self.foodButton.place(relx=0.5, rely=0.0, height=160, width=240)
        self.foodButton.configure(activebackground='#d9d9d9')
        self.foodButton.configure(activeforeground='#000000')
        self.foodButton.configure(background='#d9d9d9')
        self.foodButton.configure(disabledforeground='#a3a3a3')
        self.foodButton.configure(foreground='#000000')
        self.foodButton.configure(highlightbackground='#d9d9d9')
        self.foodButton.configure(highlightcolor='black')
        self.foodButton.configure(pady='0')
        self.foodButton.configure(text='Essen')
        self.foodButton.configure(width=142)
        self.foodButton.bind('<Button-1>',lambda e:controller.show_frame(Page3))

        self.adminButton = tk.Button(self)
        self.adminButton.place(relx=0.0, rely=0.5, height=160, width=240)
        self.adminButton.configure(activebackground='#d9d9d9')
        self.adminButton.configure(activeforeground='#000000')
        self.adminButton.configure(background='#d9d9d9')
        self.adminButton.configure(disabledforeground='#a3a3a3')
        self.adminButton.configure(foreground='#000000')
        self.adminButton.configure(highlightbackground='#d9d9d9')
        self.adminButton.configure(highlightcolor='black')
        self.adminButton.configure(pady='0')
        self.adminButton.configure(text='Admin')
        self.adminButton.configure(width=102)
        self.adminButton.bind('<Button-1>',lambda e:controller.show_frame(PageAdminLogin))

    
"""
Page zur Auswahl:
-----------------------
Alk         NonAlk
Zurück
"""
class Page0(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.back = tk.Button(self)
        self.back.place(relx=0.0, rely=0.5, relheight=0.5, relwidth=0.5)
        self.back.configure(activebackground='#d9d9d9')
        self.back.configure(activeforeground='#000000')
        self.back.configure(background='#d9d9d9')
        self.back.configure(disabledforeground='#a3a3a3')
        self.back.configure(foreground='#000000')
        self.back.configure(highlightbackground='#d9d9d9')
        self.back.configure(highlightcolor='black')
        self.back.configure(pady='0')
        self.back.configure(text='zurueck')
        self.back.configure(width=147)
        self.back.bind('<Button-1>',lambda e:controller.show_frame(StartPage))

        self.noalk = tk.Button(self)
        self.noalk.place(relx=0.5, rely=0.0, relheight=0.5, relwidth=0.5)
        self.noalk.configure(activebackground='#d9d9d9')
        self.noalk.configure(activeforeground='#000000')
        self.noalk.configure(background='#d9d9d9')
        self.noalk.configure(disabledforeground='#a3a3a3')
        self.noalk.configure(foreground='#000000')
        self.noalk.configure(highlightbackground='#d9d9d9')
        self.noalk.configure(highlightcolor='black')
        self.noalk.configure(pady='0')
        self.noalk.configure(text='noalk')
        self.noalk.configure(width=107)
        self.noalk.bind('<Button-1>',lambda e:controller.show_frame(Page2))

        self.alk = tk.Button(self)
        self.alk.place(relx=0.0, rely=0.0, relheight=0.5, relwidth=0.5)
        self.alk.configure(activebackground='#d9d9d9')
        self.alk.configure(activeforeground='#000000')
        self.alk.configure(background='#d9d9d9')
        self.alk.configure(disabledforeground='#a3a3a3')
        self.alk.configure(foreground='#000000')
        self.alk.configure(highlightbackground='#d9d9d9')
        self.alk.configure(highlightcolor='black')
        self.alk.configure(pady='0')
        self.alk.configure(text='alk')
        self.alk.configure(width=117)
        self.alk.bind('<Button-1>',lambda e:controller.show_frame(Page1))


einkauf = {'Greif' : 0, 'Gaas-Seidla':0, 'Zwickel':0, 'Weisses_Limo':0, 'Gelbes_Limo': 0, 'Spezi' : 0 ,'Pfirsich-Eistee' : 0 ,'Zitronen-Eistee':0,'Monster-Energy':0 , 'Redbull':0, 'Brezel':0, 'Pizza':0, 'Pizza-Schwank':0}

def reseteinkauf():
    for ele in einkauf:
        einkauf[ele]= 0
                
"""
Getränkeauswahl
-----------------------
Liste mit Getränken auswählen
Liste mit Warenkorb wird angezeigt
"""

class Page1(tk.Frame):
    
    def init(self, cont):
        cont.show_ele(cont)
    
    def show_ele(self, cont):
            cont.Listbox2.delete(0, tk.END)
            for ele in einkauf:
                if (einkauf[ele] != 0):
                    cont.Listbox2.insert(tk.END, '{}x {}'.format(einkauf[ele], ele))

    def __init__(self, parent, controller):
        font9 = '-family {Courier New} -size 15 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'

        

        def add(evt):
            # Note here that Tkinter passes an event object to onselect()
            w = evt.widget
            indices = w.curselection()
            if (indices.__len__() > 0):
                index = int(indices[0])
                value = w.get(index)
                einkauf[value]+= 1

                self.show_ele(self)


        def dell(evt):
            # Note here that Tkinter passes an event object to onselect()
            w = evt.widget
            indices = w.curselection()
            if(indices.__len__() >0):
                index = int(indices[0])
                value = w.get(index).split(' ',2)[1]
                if(einkauf[value] >= 1):
                    einkauf[value] -= 1

                self.show_ele(self)
        
        tk.Frame.__init__(self, parent)

        self.Listbox1 = tk.Listbox(self)
        self.Listbox1.place(relx=0.0, rely=0.0, relheight=0.7, relwidth=0.48)
        self.Listbox1.configure(background='white')
        self.Listbox1.configure(disabledforeground='#a3a3a3')
        self.Listbox1.configure(font=font9)
        self.Listbox1.configure(foreground='#000000')
        self.Listbox1.configure(selectmode=SINGLE)
        self.Listbox1.insert(tk.END, 'Greif')
        self.Listbox1.insert(tk.END, 'Gaas-Seidla')
        self.Listbox1.insert(tk.END, 'Zwickel')
        self.Listbox1.bind('<<ListboxSelect>>', add)


        self.Listbox2 = einkauf = tk.Listbox(self)
        self.Listbox2.place(relx=0.52, rely=0.0, relheight=0.7, relwidth=0.48)
        self.Listbox2.configure(background='white')
        self.Listbox2.configure(disabledforeground='#a3a3a3')
        self.Listbox2.configure(font=font9)
        self.Listbox2.configure(foreground='#000000')
        self.Listbox2.configure(selectmode=SINGLE)
        self.Listbox2.bind('<<ListboxSelect>>', dell)


        self.back = tk.Button(self)
        self.back.place(relx=0.03, rely=0.75, relheight=0.1, relwidth=0.3)
        self.back.configure(activebackground='#d9d9d9')
        self.back.configure(activeforeground='#000000')
        self.back.configure(background='#d9d9d9')
        self.back.configure(disabledforeground='#a3a3a3')
        self.back.configure(foreground='#000000')
        self.back.configure(highlightbackground='#d9d9d9')
        self.back.configure(highlightcolor='black')
        self.back.configure(pady='0')
        self.back.configure(text='zurueck')
        self.back.configure(width=117)
        self.back.bind('<Button-1>',lambda e:controller.show_frame(Page0))

        self.nonalk = tk.Button(self)
        self.nonalk.place(relx=0.35, rely=0.75, relheight=0.1, relwidth=0.3)
        self.nonalk.configure(activebackground='#d9d9d9')
        self.nonalk.configure(activeforeground='#000000')
        self.nonalk.configure(background='#d9d9d9')
        self.nonalk.configure(disabledforeground='#a3a3a3')
        self.nonalk.configure(foreground='#000000')
        self.nonalk.configure(highlightbackground='#d9d9d9')
        self.nonalk.configure(highlightcolor='black')
        self.nonalk.configure(pady='0')
        self.nonalk.configure(text='Essen')
        self.nonalk.configure(width=87)
        self.nonalk.bind('<Button-1>', lambda e: controller.show_frame(Page3))

        self.buy = tk.Button(self)
        self.buy.place(relx=0.67, rely=0.75, relheight=0.1, relwidth=0.3)
        self.buy.configure(activebackground='#d9d9d9')
        self.buy.configure(activeforeground='#000000')
        self.buy.configure(background='#d9d9d9')
        self.buy.configure(disabledforeground='#a3a3a3')
        self.buy.configure(foreground='#000000')
        self.buy.configure(highlightbackground='#d9d9d9')
        self.buy.configure(highlightcolor='black')
        self.buy.configure(pady='0')
        self.buy.configure(text='kaufen')
        self.buy.configure(width=87)
        self.buy.bind('<Button-1>',lambda e:controller.show_frame(Page5, controller))






class Page2(tk.Frame):
    
    def show_ele(self, cont):
            cont.Listbox2.delete(0, tk.END)
            for ele in einkauf:
                if (einkauf[ele] != 0):
                    cont.Listbox2.insert(tk.END, '{}x {}'.format(einkauf[ele], ele))

    def __init__(self, parent, controller):
        
        font9 = '-family {Courier New} -size 15 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'

        def add(evt):
            # Note here that Tkinter passes an event object to onselect()
            w = evt.widget
            indices = w.curselection()
            if (indices.__len__() > 0):
                index = int(indices[0])
                value = w.get(index)
                einkauf[value] += 1
                self.Listbox2.delete(0, tk.END)
                self.show_ele(self)

        def dell(evt):
            # Note here that Tkinter passes an event object to onselect()
            w = evt.widget
            indices = w.curselection()
            if (indices.__len__() > 0):
                index = int(indices[0])
                value = w.get(index).split(' ', 2)[1]
                if (einkauf[value] >= 1):
                    einkauf[value] -= 1
                self.Listbox2.delete(0, tk.END)
                self.show_ele(self)

        tk.Frame.__init__(self, parent)
        self.Listbox1 = tk.Listbox(self)
        self.Listbox1.place(relx=0.0, rely=0.0, relheight=0.7, relwidth=0.48)
        self.Listbox1.configure(background='white')
        self.Listbox1.configure(disabledforeground='#a3a3a3')
        self.Listbox1.configure(font=font9)
        self.Listbox1.configure(foreground='#000000')
        self.Listbox1.configure(selectmode=SINGLE)
        self.Listbox1.insert(tk.END, 'Weisses_Limo')
        self.Listbox1.insert(tk.END, 'Gelbes_Limo')
        self.Listbox1.insert(tk.END, 'Spezi')
        self.Listbox1.insert(tk.END, 'Pfirsich-Eistee')
        self.Listbox1.insert(tk.END, 'Zitronen-Eistee')
        self.Listbox1.insert(tk.END, 'Monster-Energy')
        self.Listbox1.insert(tk.END, 'Redbull')
        self.Listbox1.bind('<<ListboxSelect>>', add)

        self.Listbox2 = einkauf = tk.Listbox(self)
        self.Listbox2.place(relx=0.52, rely=0.0, relheight=0.7, relwidth=0.48)
        self.Listbox2.configure(background='white')
        self.Listbox2.configure(disabledforeground='#a3a3a3')
        self.Listbox2.configure(font=font9)
        self.Listbox2.configure(foreground='#000000')
        self.Listbox2.configure(selectmode=SINGLE)
        self.Listbox2.bind('<<ListboxSelect>>', dell)

        self.back = tk.Button(self)
        self.back.place(relx=0.03, rely=0.75, relheight=0.1, relwidth=0.3)
        self.back.configure(activebackground='#d9d9d9')
        self.back.configure(activeforeground='#000000')
        self.back.configure(background='#d9d9d9')
        self.back.configure(disabledforeground='#a3a3a3')
        self.back.configure(foreground='#000000')
        self.back.configure(highlightbackground='#d9d9d9')
        self.back.configure(highlightcolor='black')
        self.back.configure(pady='0')
        self.back.configure(text='zurueck')
        self.back.configure(width=117)
        self.back.bind('<Button-1>', lambda e: controller.show_frame(Page0))

        self.nonalk = tk.Button(self)
        self.nonalk.place(relx=0.35, rely=0.75, relheight=0.1, relwidth=0.3)
        self.nonalk.configure(activebackground='#d9d9d9')
        self.nonalk.configure(activeforeground='#000000')
        self.nonalk.configure(background='#d9d9d9')
        self.nonalk.configure(disabledforeground='#a3a3a3')
        self.nonalk.configure(foreground='#000000')
        self.nonalk.configure(highlightbackground='#d9d9d9')
        self.nonalk.configure(highlightcolor='black')
        self.nonalk.configure(pady='0')
        self.nonalk.configure(text='alk')
        self.nonalk.configure(width=87)
        self.nonalk.bind('<Button-1>', lambda e: controller.show_frame(Page1))

        self.buy = tk.Button(self)
        self.buy.place(relx=0.67, rely=0.75, relheight=0.1, relwidth=0.3)
        self.buy.configure(activebackground='#d9d9d9')
        self.buy.configure(activeforeground='#000000')
        self.buy.configure(background='#d9d9d9')
        self.buy.configure(disabledforeground='#a3a3a3')
        self.buy.configure(foreground='#000000')
        self.buy.configure(highlightbackground='#d9d9d9')
        self.buy.configure(highlightcolor='black')
        self.buy.configure(pady='0')
        self.buy.configure(text='kaufen')
        self.buy.configure(width=87)
        self.buy.bind('<Button-1>',lambda e:controller.show_frame(Page5, controller))
 
class Page3(tk.Frame):
    
    def init(self, cont):
        cont.show_ele(cont)
    
    def show_ele(self, cont):
            cont.Listbox2.delete(0, tk.END)
            for ele in einkauf:
                if (einkauf[ele] != 0):
                    cont.Listbox2.insert(tk.END, '{}x {}'.format(einkauf[ele], ele))

    def __init__(self, parent, controller):
        font9 = '-family {Courier New} -size 15 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'

        

        def add(evt):
            # Note here that Tkinter passes an event object to onselect()
            w = evt.widget
            indices = w.curselection()
            if (indices.__len__() > 0):
                index = int(indices[0])
                value = w.get(index)
                einkauf[value]+= 1

                self.show_ele(self)


        def dell(evt):
            # Note here that Tkinter passes an event object to onselect()
            w = evt.widget
            indices = w.curselection()
            if(indices.__len__() >0):
                index = int(indices[0])
                value = w.get(index).split(' ',2)[1]
                if(einkauf[value] >= 1):
                    einkauf[value] -= 1

                self.show_ele(self)
        
        tk.Frame.__init__(self, parent)

        self.Listbox1 = tk.Listbox(self)
        self.Listbox1.place(relx=0.0, rely=0.0, relheight=0.7, relwidth=0.48)
        self.Listbox1.configure(background='white')
        self.Listbox1.configure(disabledforeground='#a3a3a3')
        self.Listbox1.configure(font=font9)
        self.Listbox1.configure(foreground='#000000')
        self.Listbox1.configure(selectmode=SINGLE)
        self.Listbox1.insert(tk.END, 'Brezel')
        self.Listbox1.insert(tk.END, 'Pizza')
        self.Listbox1.insert(tk.END, 'Pizza-Schwank')
        self.Listbox1.bind('<<ListboxSelect>>', add)


        self.Listbox2 = tk.Listbox(self)
        self.Listbox2.place(relx=0.52, rely=0.0, relheight=0.7, relwidth=0.48)
        self.Listbox2.configure(background='white')
        self.Listbox2.configure(disabledforeground='#a3a3a3')
        self.Listbox2.configure(font=font9)
        self.Listbox2.configure(foreground='#000000')
        self.Listbox2.configure(selectmode=SINGLE)
        self.Listbox2.bind('<<ListboxSelect>>', dell)


        self.back = tk.Button(self)
        self.back.place(relx=0.03, rely=0.75, relheight=0.1, relwidth=0.3)
        self.back.configure(activebackground='#d9d9d9')
        self.back.configure(activeforeground='#000000')
        self.back.configure(background='#d9d9d9')
        self.back.configure(disabledforeground='#a3a3a3')
        self.back.configure(foreground='#000000')
        self.back.configure(highlightbackground='#d9d9d9')
        self.back.configure(highlightcolor='black')
        self.back.configure(pady='0')
        self.back.configure(text='zurueck')
        self.back.configure(width=117)
        self.back.bind('<Button-1>',lambda e:controller.show_frame(Page0))

        self.nonalk = tk.Button(self)
        self.nonalk.place(relx=0.35, rely=0.75, relheight=0.1, relwidth=0.3)
        self.nonalk.configure(activebackground='#d9d9d9')
        self.nonalk.configure(activeforeground='#000000')
        self.nonalk.configure(background='#d9d9d9')
        self.nonalk.configure(disabledforeground='#a3a3a3')
        self.nonalk.configure(foreground='#000000')
        self.nonalk.configure(highlightbackground='#d9d9d9')
        self.nonalk.configure(highlightcolor='black')
        self.nonalk.configure(pady='0')
        self.nonalk.configure(text='nonalk')
        self.nonalk.configure(width=87)
        self.nonalk.bind('<Button-1>', lambda e: controller.show_frame(Page2))

        self.buy = tk.Button(self)
        self.buy.place(relx=0.67, rely=0.75, relheight=0.1, relwidth=0.3)
        self.buy.configure(activebackground='#d9d9d9')
        self.buy.configure(activeforeground='#000000')
        self.buy.configure(background='#d9d9d9')
        self.buy.configure(disabledforeground='#a3a3a3')
        self.buy.configure(foreground='#000000')
        self.buy.configure(highlightbackground='#d9d9d9')
        self.buy.configure(highlightcolor='black')
        self.buy.configure(pady='0')
        self.buy.configure(text='kaufen')
        self.buy.configure(width=87)
        self.buy.bind('<Button-1>',lambda e:controller.show_frame(Page5, controller))
        
class PageAdminLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font10 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'
        font9 = '-family {Segoe UI} -size 28 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'


        self.loginLabel = tk.Label(self)
        self.loginLabel.place(relx=0.33, rely=0.11, height=51, width=164)
        self.loginLabel.configure(background='#d9d9d9')
        self.loginLabel.configure(disabledforeground='#a3a3a3')
        self.loginLabel.configure(font=font9)
        self.loginLabel.configure(foreground='#000000')
        self.loginLabel.configure(text='Login')
        self.loginLabel.configure(width=164)

        self.infoLabel = tk.Label(self)
        self.infoLabel.place(relx=0.27, rely=0.33, height=71, width=274)
        self.infoLabel.configure(background='#d9d9d9')
        self.infoLabel.configure(disabledforeground='#a3a3a3')
        self.infoLabel.configure(font=font10)
        self.infoLabel.configure(foreground='#000000')
        self.infoLabel.configure(text='Chip an RFID Sensor halten')
        self.infoLabel.configure(width=274)
        
class PageBuyLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font10 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'
        font9 = '-family {Segoe UI} -size 28 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'


        self.loginLabel = tk.Label(self)
        self.loginLabel.place(relx=0.33, rely=0.11, height=51, width=164)
        self.loginLabel.configure(background='#d9d9d9')
        self.loginLabel.configure(disabledforeground='#a3a3a3')
        self.loginLabel.configure(font=font9)
        self.loginLabel.configure(foreground='#000000')
        self.loginLabel.configure(text='Kaufen')
        self.loginLabel.configure(width=164)

        self.infoLabel = tk.Label(self)
        self.infoLabel.place(relx=0.27, rely=0.33, height=71, width=274)
        self.infoLabel.configure(background='#d9d9d9')
        self.infoLabel.configure(disabledforeground='#a3a3a3')
        self.infoLabel.configure(font=font10)
        self.infoLabel.configure(foreground='#000000')
        self.infoLabel.configure(text='Chip an RFID Sensor halten')
        self.infoLabel.configure(width=274)

        
class Page5(tk.Frame):
    
    def init(self, cont):
        cont.show_ele(cont)
        cont.sum(cont)
        
    def show_ele(self, cont):
        cont.Listbox2.delete(0,'end')
        for ele in einkauf:
            if (einkauf[ele] != 0):
                cont.Listbox2.insert(tk.END, '{}x {}'.format(einkauf[ele], ele))
    def sum(self, cont):
        summe = 0.0
        for ele in einkauf:
            if(einkauf[ele] != 0):
                summe += int(einkauf[ele]) * shop.getPrice(str(ele))
        cont.sumLabel.configure(text=str(summe) + ' EUR')

    def __init__(self, parent, controller):
        
        font11 = '-family {Segoe UI} -size 12 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'
        font9 = '-family {Courier New} -size 15 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'

       


        tk.Frame.__init__(self, parent)
       
        self.Listbox2 = tk.Listbox(self) # = einkauf
        self.Listbox2.place(relx=0.0, rely=0.0, relheight=0.7, relwidth=0.48)
        self.Listbox2.configure(background='white')
        self.Listbox2.configure(disabledforeground='#a3a3a3')
        self.Listbox2.configure(font=font9)
        self.Listbox2.configure(foreground='#000000')
        self.Listbox2.configure(selectmode=SINGLE)

        self.back = tk.Button(self)
        self.back.place(relx=0.03, rely=0.75, relheight=0.1, relwidth=0.3)
        self.back.configure(activebackground='#d9d9d9')
        self.back.configure(activeforeground='#000000')
        self.back.configure(background='#d9d9d9')
        self.back.configure(disabledforeground='#a3a3a3')
        self.back.configure(foreground='#000000')
        self.back.configure(highlightbackground='#d9d9d9')
        self.back.configure(highlightcolor='black')
        self.back.configure(pady='0')
        self.back.configure(text='Abbruch')
        self.back.configure(width=117)
        self.back.bind('<Button-1>', lambda e: controller.show_frame(Page0))
        
        self.sumLabel = tk.Label(self)
        self.sumLabel.place(relx=0.6, rely=0.22, height=41, width=164)
        self.sumLabel.configure(background='#d9d9d9')
        self.sumLabel.configure(disabledforeground='#a3a3a3')
        self.sumLabel.configure(font=font11)
        self.sumLabel.configure(foreground='#000000')
        self.sumLabel.configure(text='Kosten')
        self.sumLabel.configure(width=164)
        
        self.buyButton = tk.Button(self)
        self.buyButton.place(relx=0.35, rely=0.75, relheight=0.1, relwidth=0.6)
        self.buyButton.configure(activebackground='#d9d9d9')
        self.buyButton.configure(activeforeground='#000000')
        self.buyButton.configure(background='#d9d9d9')
        self.buyButton.configure(disabledforeground='#a3a3a3')
        self.buyButton.configure(foreground='#000000')
        self.buyButton.configure(highlightbackground='#d9d9d9')
        self.buyButton.configure(highlightcolor='black')
        self.buyButton.configure(pady='0')
        self.buyButton.configure(font=font11)
        self.buyButton.configure(text='Kostenpflichtig kaufen')
        self.buyButton.configure(width=117)
        self.buyButton.bind('<Button-1>', lambda e: controller.show_frame(PageBuyLogin, amount =str(self.sumLabel.cget('text')).split()[0], controller = controller))


class PageAdmin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.personButton = tk.Button(self)
        self.personButton.place(relx=0.08, rely=0.09, height=64, width=141)
        self.personButton.configure(activebackground='#d9d9d9')
        self.personButton.configure(activeforeground='#000000')
        self.personButton.configure(background='#d9d9d9')
        self.personButton.configure(disabledforeground='#a3a3a3')
        self.personButton.configure(foreground='#000000')
        self.personButton.configure(highlightbackground='#d9d9d9')
        self.personButton.configure(highlightcolor='black')
        self.personButton.configure(pady='0')
        self.personButton.configure(text='person')
        self.personButton.configure(width=141)
        self.personButton.bind('<Button-1>',lambda e:controller.show_frame(Page14, controller = controller))

        self.aufladen = tk.Button(self)
        self.aufladen.place(relx=0.5, rely=0.09, height=64, width=157)
        self.aufladen.configure(activebackground='#d9d9d9')
        self.aufladen.configure(activeforeground='#000000')
        self.aufladen.configure(background='#d9d9d9')
        self.aufladen.configure(disabledforeground='#a3a3a3')
        self.aufladen.configure(foreground='#000000')
        self.aufladen.configure(highlightbackground='#d9d9d9')
        self.aufladen.configure(highlightcolor='black')
        self.aufladen.configure(pady='0')
        self.aufladen.configure(text='aufladen')
        self.aufladen.configure(width=157)
        self.aufladen.bind('<Button-1>',lambda e:controller.show_frame(PageDeposit))

        self.abfragen = tk.Button(self)
        self.abfragen.place(relx=0.5, rely=0.41, height=64, width=147)
        self.abfragen.configure(activebackground='#d9d9d9')
        self.abfragen.configure(activeforeground='#000000')
        self.abfragen.configure(background='#d9d9d9')
        self.abfragen.configure(disabledforeground='#a3a3a3')
        self.abfragen.configure(foreground='#000000')
        self.abfragen.configure(highlightbackground='#d9d9d9')
        self.abfragen.configure(highlightcolor='black')
        self.abfragen.configure(pady='0')
        self.abfragen.configure(text='abfragen')
        self.abfragen.configure(width=147)
        self.abfragen.bind('<Button-1>',lambda e:controller.show_frame(Page10))
        
        self.zuruck = tk.Button(self)
        self.zuruck.place(relx=0.08, rely=0.41, height=64, width=147)
        self.zuruck.configure(activebackground='#d9d9d9')
        self.zuruck.configure(activeforeground='#000000')
        self.zuruck.configure(background='#d9d9d9')
        self.zuruck.configure(disabledforeground='#a3a3a3')
        self.zuruck.configure(foreground='#000000')
        self.zuruck.configure(highlightbackground='#d9d9d9')
        self.zuruck.configure(highlightcolor='black')
        self.zuruck.configure(pady='0')
        self.zuruck.configure(text=u'zurück')
        self.zuruck.configure(width=147)
        self.zuruck.bind('<Button-1>',lambda e:controller.show_frame(StartPage))
        
        self.shutdown = tk.Button(self)
        self.shutdown.place(relx=0.25, rely=0.70, height=64, width=147)
        self.shutdown.configure(activebackground='#d9d9d9')
        self.shutdown.configure(activeforeground='#000000')
        self.shutdown.configure(background='#d9d9d9')
        self.shutdown.configure(disabledforeground='#a3a3a3')
        self.shutdown.configure(foreground='#000000')
        self.shutdown.configure(highlightbackground='#d9d9d9')
        self.shutdown.configure(highlightcolor='black')
        self.shutdown.configure(pady='0')
        self.shutdown.configure(text='Herunterfahren')
        self.shutdown.configure(width=147)
        self.shutdown.bind('<Button-1>',lambda e:call("sudo reboot now", shell=True))
        
        
class PageNewMoney(tk.Frame):
    def setRFIDLabel(self,cont, rfids, controller):
        newMoneyLabel = person.getName(rfids)
        cont.pageNameLabel.configure(text='Neues Guthaben von ' +newMoneyLabel)
        newmoney = money.getMoney(rfids)
        cont.newMoneyLabel.configure(text= str(newmoney))
        controller.update()
        time.sleep(5)
        controller.show_frame(StartPage)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font10 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'
        font11 = '-family {Segoe UI} -size 12 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'

        self.pageNameLabel = tk.Label(self)
        self.pageNameLabel.place(relx=0.35, rely=0.22, height=41, width=264)
        self.pageNameLabel.configure(background='#d9d9d9')
        self.pageNameLabel.configure(disabledforeground='#a3a3a3')
        self.pageNameLabel.configure(font=font10)
        self.pageNameLabel.configure(foreground='#000000')
        self.pageNameLabel.configure(text='Neues Guthaben')

        self.newMoneyLabel = tk.Label(self)
        self.newMoneyLabel.place(relx=0.2, rely=0.4, height=41, width=324)
        self.newMoneyLabel.configure(background='#d9d9d9')
        self.newMoneyLabel.configure(disabledforeground='#a3a3a3')
        self.newMoneyLabel.configure(font=font11)
        self.newMoneyLabel.configure(foreground='#000000')
        self.newMoneyLabel.configure(text='neues Guthaben')
        
class PageDeposit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font9 = '-family {Segoe UI} -size 18 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'




        self.pageNameLabel = tk.Label(self)
        self.pageNameLabel.place(relx=0.29, rely=0.06, height=51, width=224)
        self.pageNameLabel.configure(background='#d9d9d9')
        self.pageNameLabel.configure(disabledforeground='#a3a3a3')
        self.pageNameLabel.configure(font=font9)
        self.pageNameLabel.configure(foreground='#000000')
        self.pageNameLabel.configure(text='Guthaben aufladen')
        self.pageNameLabel.configure(width=224)

        self.amountLabel = tk.Label(self)
        self.amountLabel.place(relx=0.19, rely=0.34, height=31, width=64)
        self.amountLabel.configure(background='#d9d9d9')
        self.amountLabel.configure(disabledforeground='#a3a3a3')
        self.amountLabel.configure(foreground='#000000')
        self.amountLabel.configure(text='Summe')
        self.amountLabel.configure(width=64)

        self.amount = tk.Text(self)
        self.amount.place(relx=0.38, rely=0.38, relheight=0.08, relwidth=0.24)
        self.amount.configure(background='white')
        self.amount.configure(font='TkTextFont')
        self.amount.configure(foreground='black')
        self.amount.configure(highlightbackground='#d9d9d9')
        self.amount.configure(highlightcolor='black')
        self.amount.configure(insertbackground='black')
        self.amount.configure(selectbackground='#c4c4c4')
        self.amount.configure(selectforeground='black')
        self.amount.configure(width=114)
        self.amount.configure(wrap=WORD)

        self.back = tk.Button(self)
        self.back.place(relx=0.1, rely=0.66, height=64, width=107)
        self.back.configure(activebackground='#d9d9d9')
        self.back.configure(activeforeground='#000000')
        self.back.configure(background='#d9d9d9')
        self.back.configure(disabledforeground='#a3a3a3')
        self.back.configure(foreground='#000000')
        self.back.configure(highlightbackground='#d9d9d9')
        self.back.configure(highlightcolor='black')
        self.back.configure(pady='0')
        self.back.configure(text='Abbruch')
        self.back.configure(width=107)
        self.back.bind('<Button-1>',lambda e:controller.show_frame(PageAdmin))

        self.buy = tk.Button(self)
        self.buy.place(relx=0.52, rely=0.66, height=54, width=87)
        self.buy.configure(activebackground='#d9d9d9')
        self.buy.configure(activeforeground='#000000')
        self.buy.configure(background='#d9d9d9')
        self.buy.configure(disabledforeground='#a3a3a3')
        self.buy.configure(foreground='#000000')
        self.buy.configure(highlightbackground='#d9d9d9')
        self.buy.configure(highlightcolor='black')
        self.buy.configure(pady='0')
        self.buy.configure(text='aufladen')
        self.buy.configure(width=87)
        self.buy.bind('<Button-1>',lambda e:controller.show_frame(Page13, amount = int(str(self.amount.get('1.0','end')).translate(None, '\n')), controller = controller))
        
class Page9(tk.Frame):
    
    def reset(self, cont):
        cont.Label4.configure(text='Waiting...')
        
    
    def setRFIDLabel(self,cont, rfids):
        cont.Label4.configure(text= str(rfids))

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font9 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'


        self.addbutton = tk.Button(self)
        self.addbutton.place(relx=0.58, rely=0.69, height=54, width=117)
        self.addbutton.configure(activebackground='#d9d9d9')
        self.addbutton.configure(activeforeground='#000000')
        self.addbutton.configure(background='#d9d9d9')
        self.addbutton.configure(disabledforeground='#a3a3a3')
        self.addbutton.configure(foreground='#000000')
        self.addbutton.configure(highlightbackground='#d9d9d9')
        self.addbutton.configure(highlightcolor='black')
        self.addbutton.configure(pady='0')
        self.addbutton.configure(text='hinzufuegen')
        self.addbutton.configure(width=117)
        self.addbutton.bind('<Button-1>',lambda e:controller.show_frame(PageAddPerson, name = self.name.get('1.0','end'),rfids =self.Label4.cget('text'), controller = controller))

        self.back = tk.Button(self)
        self.back.place(relx=0.15, rely=0.66, height=74, width=97)
        self.back.configure(activebackground='#d9d9d9')
        self.back.configure(activeforeground='#000000')
        self.back.configure(background='#d9d9d9')
        self.back.configure(disabledforeground='#a3a3a3')
        self.back.configure(foreground='#000000')
        self.back.configure(highlightbackground='#d9d9d9')
        self.back.configure(highlightcolor='black')
        self.back.configure(pady='0')
        self.back.configure(text='Abbruch')
        self.back.configure(width=97)
        self.back.bind('<Button-1>',lambda e:controller.show_frame(PageAdmin))

        self.add = tk.Label(self)
        self.add.place(relx=0.23, rely=0.03, height=41, width=284)
        self.add.configure(background='#d9d9d9')
        self.add.configure(disabledforeground='#a3a3a3')
        self.add.configure(font=font9)
        self.add.configure(foreground='#000000')
        self.add.configure(text='Neuen Nutzer hinzufuegen')
        self.add.configure(width=284)

        self.amountLabel = tk.Label(self)
        self.amountLabel.place(relx=0.19, rely=0.22, height=41, width=54)
        self.amountLabel.configure(background='#d9d9d9')
        self.amountLabel.configure(disabledforeground='#a3a3a3')
        self.amountLabel.configure(foreground='#000000')
        self.amountLabel.configure(text='Name')
        self.amountLabel.configure(width=54)

        self.rfidLabel = tk.Label(self)
        self.rfidLabel.place(relx=0.19, rely=0.41, height=41, width=64)
        self.rfidLabel.configure(background='#d9d9d9')
        self.rfidLabel.configure(disabledforeground='#a3a3a3')
        self.rfidLabel.configure(foreground='#000000')
        self.rfidLabel.configure(text='RFID')
        self.rfidLabel.configure(width=64)

        self.name = tk.Text(self)
        self.name.place(relx=0.46, rely=0.25, relheight=0.08, relwidth=0.15)
        self.name.configure(background='white')
        self.name.configure(font='TkTextFont')
        self.name.configure(foreground='black')
        self.name.configure(highlightbackground='#d9d9d9')
        self.name.configure(highlightcolor='black')
        self.name.configure(insertbackground='black')
        self.name.configure(selectbackground='#c4c4c4')
        self.name.configure(selectforeground='black')
        self.name.configure(width=74)
        self.name.configure(wrap=WORD)


        self.Label4 = tk.Label(self)
        self.Label4.place(relx=0.4, rely=0.44, relheight=0.08, relwidth=0.26)
        self.Label4.configure(background='#d9d9d9')
        self.Label4.configure(disabledforeground='#a3a3a3')
        self.Label4.configure(foreground='#000000')
        self.Label4.configure(text='Waiting...')
        self.Label4.configure(width=64)
        
class Page10(tk.Frame):

    def __init__(self, parent, controller):
        
        

        tk.Frame.__init__(self,parent, height = 320, width = 480)

        self.drink = tk.Button(self)
        self.drink.place(relx=0.1, rely=0.16, height=104, width=162)
        self.drink.configure(activebackground='#d9d9d9')
        self.drink.configure(activeforeground='#000000')
        self.drink.configure(background='#d9d9d9')
        self.drink.configure(disabledforeground='#a3a3a3')
        self.drink.configure(foreground='#000000')
        self.drink.configure(highlightbackground='#d9d9d9')
        self.drink.configure(highlightcolor='black')
        self.drink.configure(pady='0')
        self.drink.configure(text='name')
        self.drink.configure(width=162)
        self.drink.bind('<Button-1>',lambda e:controller.show_frame(Page11))
        

        self.food = tk.Button(self)
        self.food.place(relx=0.6, rely=0.16, height=104, width=142)
        self.food.configure(activebackground='#d9d9d9')
        self.food.configure(activeforeground='#000000')
        self.food.configure(background='#d9d9d9')
        self.food.configure(disabledforeground='#a3a3a3')
        self.food.configure(foreground='#000000')
        self.food.configure(highlightbackground='#d9d9d9')
        self.food.configure(highlightcolor='black')
        self.food.configure(pady='0')
        self.food.configure(text='rfid')
        self.food.configure(width=142)
        self.food.bind('<Button-1>',lambda e:controller.show_frame(Page12))

        self.back = tk.Button(self)
        self.back.place(relx=0.06, rely=0.72, height=54, width=102)
        self.back.configure(activebackground='#d9d9d9')
        self.back.configure(activeforeground='#000000')
        self.back.configure(background='#d9d9d9')
        self.back.configure(disabledforeground='#a3a3a3')
        self.back.configure(foreground='#000000')
        self.back.configure(highlightbackground='#d9d9d9')
        self.back.configure(highlightcolor='black')
        self.back.configure(pady='0')
        self.back.configure(text='back')
        self.back.configure(width=102)
        self.back.bind('<Button-1>',lambda e:controller.show_frame(StartPage))

class Page11(tk.Frame):

    def reset(self, cont):
        cont.name.delete('1.0', 'end')
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font9 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'


        self.ok = tk.Button(self)
        self.ok.place(relx=0.4, rely=0.66, height=54, width=117)
        self.ok.configure(activebackground='#d9d9d9')
        self.ok.configure(activeforeground='#000000')
        self.ok.configure(background='#d9d9d9')
        self.ok.configure(disabledforeground='#a3a3a3')
        self.ok.configure(foreground='#000000')
        self.ok.configure(highlightbackground='#d9d9d9')
        self.ok.configure(highlightcolor='black')
        self.ok.configure(pady='0')
        self.ok.configure(text='OK')
        self.ok.configure(width=117)
        self.ok.bind('<Button-1>',lambda e:controller.show_frame(PageOverview, name = str(self.name.get('1.0','end'))))

        self.add = tk.Label(self)
        self.add.place(relx=0.21, rely=0.03, height=41, width=284)
        self.add.configure(background='#d9d9d9')
        self.add.configure(disabledforeground='#a3a3a3')
        self.add.configure(font=font9)
        self.add.configure(foreground='#000000')
        self.add.configure(text='Uebersicht')
        self.add.configure(width=284)

        self.amountLabel = tk.Label(self)
        self.amountLabel.place(relx=0.19, rely=0.22, height=41, width=54)
        self.amountLabel.configure(background='#d9d9d9')
        self.amountLabel.configure(disabledforeground='#a3a3a3')
        self.amountLabel.configure(foreground='#000000')
        self.amountLabel.configure(text='Name')
        self.amountLabel.configure(width=54)

        self.name = tk.Text(self)
        self.name.place(relx=0.46, rely=0.25, relheight=0.08, relwidth=0.15)
        self.name.configure(background='white')
        self.name.configure(font='TkTextFont')
        self.name.configure(foreground='black')
        self.name.configure(highlightbackground='#d9d9d9')
        self.name.configure(highlightcolor='black')
        self.name.configure(insertbackground='black')
        self.name.configure(selectbackground='#c4c4c4')
        self.name.configure(selectforeground='black')
        self.name.configure(width=74)
        self.name.configure(wrap=WORD)

        
class Page12(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font10 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'
        font9 = '-family {Segoe UI} -size 28 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'


        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.33, rely=0.11, height=51, width=164)
        self.Label1.configure(background='#d9d9d9')
        self.Label1.configure(disabledforeground='#a3a3a3')
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground='#000000')
        self.Label1.configure(text='Uebersicht')
        self.Label1.configure(width=164)

        self.amountLabel = tk.Label(self)
        self.amountLabel.place(relx=0.27, rely=0.33, height=71, width=274)
        self.amountLabel.configure(background='#d9d9d9')
        self.amountLabel.configure(disabledforeground='#a3a3a3')
        self.amountLabel.configure(font=font10)
        self.amountLabel.configure(foreground='#000000')
        self.amountLabel.configure(text='Chip an RFID Sensor halten')
        self.amountLabel.configure(width=274)
        
class Page13(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font10 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'
        font9 = '-family {Segoe UI} -size 28 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'


        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.33, rely=0.11, height=51, width=164)
        self.Label1.configure(background='#d9d9d9')
        self.Label1.configure(disabledforeground='#a3a3a3')
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground='#000000')
        self.Label1.configure(text='Aufladen')
        self.Label1.configure(width=164)

        self.amountLabel = tk.Label(self)
        self.amountLabel.place(relx=0.27, rely=0.33, height=71, width=274)
        self.amountLabel.configure(background='#d9d9d9')
        self.amountLabel.configure(disabledforeground='#a3a3a3')
        self.amountLabel.configure(font=font10)
        self.amountLabel.configure(foreground='#000000')
        self.amountLabel.configure(text='Chip an RFID Sensor halten')
        self.amountLabel.configure(width=274)
        
class Page14(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font10 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'
        font9 = '-family {Segoe UI} -size 28 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'


        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.33, rely=0.11, height=51, width=164)
        self.Label1.configure(background='#d9d9d9')
        self.Label1.configure(disabledforeground='#a3a3a3')
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground='#000000')
        self.Label1.configure(text='Person hinzufuegen')
        self.Label1.configure(width=164)

        self.amountLabel = tk.Label(self)
        self.amountLabel.place(relx=0.27, rely=0.33, height=71, width=274)
        self.amountLabel.configure(background='#d9d9d9')
        self.amountLabel.configure(disabledforeground='#a3a3a3')
        self.amountLabel.configure(font=font10)
        self.amountLabel.configure(foreground='#000000')
        self.amountLabel.configure(text='Chip an RFID Sensor halten')
        self.amountLabel.configure(width=274)
        

class PageError(tk.Frame):
    
    def setError(self, cont, error = None, controller = None, page = StartPage):
        cont.amountLabel.configure(text = error)
        controller.update()
        time.sleep(5)
        controller.show_frame(page)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font10 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'
        font9 = '-family {Segoe UI} -size 28 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'


        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.33, rely=0.11, height=51, width=164)
        self.Label1.configure(background='#d9d9d9')
        self.Label1.configure(disabledforeground='#a3a3a3')
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground='#000000')
        self.Label1.configure(text='Error')
        self.Label1.configure(width=164)

        self.amountLabel = tk.Label(self)
        self.amountLabel.place(relx=0.27, rely=0.33, height=71, width=274)
        self.amountLabel.configure(background='#d9d9d9')
        self.amountLabel.configure(disabledforeground='#a3a3a3')
        self.amountLabel.configure(font=font10)
        self.amountLabel.configure(foreground='#000000')
        self.amountLabel.configure(text='Waiting for Error')
        self.amountLabel.configure(width=274)
        
        
class PageOverview(tk.Frame):
    def setRFIDLabel(self,cont, rfids = None, name = None):
        if(rfids == None):
            rfids = person.getRFID(name)            
        cont.name.configure(text= str(person.getName(rfids)))
        cont.rfid.configure(text= str(rfids))
        cont.seen.configure(text= str(person.lastSeen(rfids)))
        cont.money.configure(text = str(money.getMoney(rfids)))

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font9 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'


        self.ok = tk.Button(self)
        self.ok.place(relx=0.4, rely=0.66, height=54, width=117)
        self.ok.configure(activebackground='#d9d9d9')
        self.ok.configure(activeforeground='#000000')
        self.ok.configure(background='#d9d9d9')
        self.ok.configure(disabledforeground='#a3a3a3')
        self.ok.configure(foreground='#000000')
        self.ok.configure(highlightbackground='#d9d9d9')
        self.ok.configure(highlightcolor='black')
        self.ok.configure(pady='0')
        self.ok.configure(text='OK')
        self.ok.configure(width=117)
        self.ok.bind('<Button-1>',lambda e:controller.show_frame(PageAdmin))

        self.add = tk.Label(self)
        self.add.place(relx=0.21, rely=0.03, height=41, width=284)
        self.add.configure(background='#d9d9d9')
        self.add.configure(disabledforeground='#a3a3a3')
        self.add.configure(font=font9)
        self.add.configure(foreground='#000000')
        self.add.configure(text='Uebersicht')
        self.add.configure(width=284)

        self.amountLabel = tk.Label(self)
        self.amountLabel.place(relx=0.19, rely=0.22, height=41, width=54)
        self.amountLabel.configure(background='#d9d9d9')
        self.amountLabel.configure(disabledforeground='#a3a3a3')
        self.amountLabel.configure(foreground='#000000')
        self.amountLabel.configure(text='Name')
        self.amountLabel.configure(width=54)

        self.rfidLabel = tk.Label(self)
        self.rfidLabel.place(relx=0.19, rely=0.31, height=41, width=64)
        self.rfidLabel.configure(background='#d9d9d9')
        self.rfidLabel.configure(disabledforeground='#a3a3a3')
        self.rfidLabel.configure(foreground='#000000')
        self.rfidLabel.configure(text='RFID')
        self.rfidLabel.configure(width=64)
        
        self.seenLabel = tk.Label(self)
        self.seenLabel.place(relx=0.21, rely=0.44, height=21, width=30)
        self.seenLabel.configure(background='#d9d9d9')
        self.seenLabel.configure(disabledforeground='#a3a3a3')
        self.seenLabel.configure(foreground='#000000')
        self.seenLabel.configure(text='seen')
        
        self.moneyLabel = tk.Label(self)
        self.moneyLabel.place(relx=0.21, rely=0.54, height=21, width=30)
        self.moneyLabel.configure(background='#d9d9d9')
        self.moneyLabel.configure(disabledforeground='#a3a3a3')
        self.moneyLabel.configure(foreground='#000000')
        self.moneyLabel.configure(text='money')
        
        self.name = tk.Label(self)
        self.name.place(relx=0.46, rely=0.25, relheight=0.08, relwidth=0.15)
        self.name.configure(background='#d9d9d9')
        self.name.configure(disabledforeground='#a3a3a3')
        self.name.configure(foreground='#000000')
        self.name.configure(text='RFID')
        self.name.configure(width=64)
        
        self.rfid = tk.Label(self)
        self.rfid.place(relx=0.4, rely=0.34, relheight=0.08, relwidth=0.26)
        self.rfid.configure(background='#d9d9d9')
        self.rfid.configure(disabledforeground='#a3a3a3')
        self.rfid.configure(foreground='#000000')
        self.rfid.configure(text='RFID')
        self.rfid.configure(width=64)
        
        self.seen = tk.Label(self)
        self.seen.place(relx=0.42, rely=0.44, relheight=0.08, relwidth=0.22)
        self.seen.configure(background='#d9d9d9')
        self.seen.configure(disabledforeground='#a3a3a3')
        self.seen.configure(foreground='#000000')
        self.seen.configure(text='seen')
        self.seen.configure(width=64)
        
        self.money = tk.Label(self)
        self.money.place(relx=0.41, rely=0.54, height=21, width=30)
        self.money.configure(background='#d9d9d9')
        self.money.configure(disabledforeground='#a3a3a3')
        self.money.configure(foreground='#000000')
        self.money.configure(text='money')
        self.money.configure(width=64)
        

class PageAddPerson(tk.Frame):
    
    def setRFIDLabel(self,cont, name, rfids):
        cont.name.configure(text= name+'('+str(name)+')')
        cont.rfid.configure(text= name+'('+str(rfids)+')')


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font10 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'
        font11 = '-family {Segoe UI} -size 12 -weight normal -slant '  \
            'roman -underline 0 -overstrike 0'

        self.pageNameLabel = tk.Label(self)
        self.pageNameLabel.place(relx=0.35, rely=0.22, height=41, width=164)
        self.pageNameLabel.configure(background='#d9d9d9')
        self.pageNameLabel.configure(disabledforeground='#a3a3a3')
        self.pageNameLabel.configure(font=font10)
        self.pageNameLabel.configure(foreground='#000000')
        self.pageNameLabel.configure(text='Neuer Nutzer')
        self.pageNameLabel.configure(width=164)

        self.name = tk.Label(self)
        self.name.place(relx=0.2, rely=0.4, height=41, width=324)
        self.name.configure(background='#d9d9d9')
        self.name.configure(disabledforeground='#a3a3a3')
        self.name.configure(font=font11)
        self.name.configure(foreground='#000000')
        self.name.configure(text='name')
        self.name.configure(width=324)
        
        self.rfid = tk.Label(self)
        self.rfid.place(relx=0.2, rely=0.6, height=41, width=324)
        self.rfid.configure(background='#d9d9d9')
        self.rfid.configure(disabledforeground='#a3a3a3')
        self.rfid.configure(font=font11)
        self.rfid.configure(foreground='#000000')
        self.rfid.configure(text='rfid')
        self.rfid.configure(width=324)
        
def start():
    app = SeaofBTCapp()
    app.mainloop()
