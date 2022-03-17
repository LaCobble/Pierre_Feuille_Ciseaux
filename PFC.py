#    ______      __    __    __
#   / ____/___  / /_  / /_  / /__
#  / /   / __ \/ __ \/ __ \/ / _ \
# / /___/ /_/ / /_/ / /_/ / /  __/
# \____/\____/_.___/_.___/_/\___/

from tkinter import * 
import tkinter as tk
import random

def fermer():
    global fenetre
    fenetre.destroy()

def GAME1():

    def Pierre():
        choix=1
        play(choix)

    def Feuille():
        choix=2
        play(choix)

    def Ciseau():
        choix=3
        play(choix)

    def play(choix):
        
        bot = (random.randint(1, 3))
        if(choix == bot):
            replay2()
        else:
            if(choix == 1 and bot == 2):
                replay1()
            elif(choix == 2 and bot == 1):
                replay3()
            elif(choix == 3 and bot == 1):
                replay3()
            elif(choix == 1 and bot == 3):
                replay1()
            elif(choix == 3 and bot == 2):
                replay1()
            elif(choix == 2 and bot == 3):
                replay3()

    def replay1():
        # be treated as a new window
        replay1 = Toplevel(fenetre)
        
        # set the title 
        replay1.title(" Replay ? ")
        
        # sets the dimensions
        replay1.geometry("150x150")
        
        # in the Window
        label = Label(replay1, text=" WIN !", font=("Courier", 25))
        label.pack()
        Label(replay1, 
            text ="\n" + "You want replay ?" + "\n",fg='#FFCBA2',font='bold').pack()
        btn_0 = Button(replay1, text="Yes", fg='white',bg='#619ED6', height = 5, width = 8, command=replay1.destroy)
        btn_0.pack(side=RIGHT, padx=5, pady=5)  
        btn_1 = Button(replay1, text="No", fg='white',bg='#E64345', height = 5, width = 8, command=fermer)
        btn_1.pack(side=RIGHT, padx=5, pady=5)  
        #newWindow.iconbitmap('Back Up\\icon\\info.ico')

    def replay2():
        # be treated as a new window
        replay2 = Toplevel(fenetre)
        
        # set the title 
        replay2.title(" Replay ? ")
        
        # sets the dimensions
        replay2.geometry("150x150")
        
        # in the Window
        label = Label(replay2, text="EQUAL !", font=("Courier", 25))
        label.pack()
        Label(replay2, 
            text ="\n" + "You want replay ?" + "\n",fg='#FFCBA2',font='bold').pack()
        btn_0 = Button(replay2, text="Yes", fg='white',bg='#619ED6', height = 5, width = 8, command=replay2.destroy)
        btn_0.pack(side=RIGHT, padx=5, pady=5)  
        btn_1 = Button(replay2, text="No", fg='white',bg='#E64345', height = 5, width = 8, command=fermer)
        btn_1.pack(side=RIGHT, padx=5, pady=5)  
        #newWindow.iconbitmap('Back Up\\icon\\info.ico')

    def replay3():
        # be treated as a new window
        replay3 = Toplevel(fenetre)
        
        # set the title 
        replay3.title(" Replay ? ")
        
        # sets the dimensions
        replay3.geometry("150x150")
        
        # in the Window
        label = Label(replay3, text="LOOSE !", font=("Courier", 25))
        label.pack()
        Label(replay3, 
            text ="\n" + "You want replay ?" + "\n",fg='#FFCBA2',font='bold').pack()
        btn_0 = Button(replay3, text="Yes", fg='white',bg='#619ED6', height = 5, width = 8, command=replay3.destroy)
        btn_0.pack(side=RIGHT, padx=5, pady=5)  
        btn_1 = Button(replay3, text="No", fg='white',bg='#E64345', height = 5, width = 8, command=fermer)
        btn_1.pack(side=RIGHT, padx=5, pady=5)  
        #newWindow.iconbitmap('Back Up\\icon\\info.ico')

    # be treated as a new window
    GAME1 = Toplevel(fenetre)
      
    # set the title 
    GAME1.title("P1 VS IA !")
      
    # sets the dimensions
    GAME1.geometry("525x150")
      
    # in the Window
    Label(GAME1, 
        text ="\n" + "What do you play ?" + "\n",fg='#FFCBA2',font='bold').pack()
    btn_0 = Button(GAME1, text="Pierre", fg='white',bg='#8FCACA', height = 20, width = 20, command=Pierre)
    btn_0.pack(side=RIGHT, padx=5, pady=5)  
    btn_1 = Button(GAME1, text="Feuille", fg='white',bg='#97C1A9', height = 20, width = 20, command=Feuille)
    btn_1.pack(side=RIGHT, padx=5, pady=5)  
    btn_2 = Button(GAME1, text="Ciseau", fg='white',bg='#FF968A', height = 20, width = 20, command=Ciseau)
    btn_2.pack(side=RIGHT, padx=5, pady=5) 
    btn_5 = Button(GAME1, text="Exit", fg ='white',bg='black', height = 5, width = 5,command=GAME1.destroy)
    btn_5.pack(side=LEFT, padx=5, pady=5)
    #newWindow.iconbitmap('Back Up\\icon\\info.ico')

def GAME2():

    def close(ChoixGAME2,wnd):
        ChoixGAME2.destroy()
        wnd.destroy()
        
    def ChoixP11():
        choix=1
        ChoixGAME2(choix)
    
    def ChoixP12():
        choix=2
        ChoixGAME2(choix)

    def ChoixP13():
        choix=3
        ChoixGAME2(choix)

    def ChoixGAME2(choix):

        ChoixP1=choix
        Pierre=1
        Feuille=2
        Ciseau=3

        # be treated as a new window
        ChoixGAME2 = Toplevel(fenetre)
        
        # set the title 
        ChoixGAME2.title("P1 VS P2 !")
        
        # sets the dimensions
        ChoixGAME2.geometry("525x150")
        
        # in the Window
        Label(ChoixGAME2, 
            text ="\n" + "What do you play player 2 ?" + "\n",fg='#FFCBA2',font='bold').pack()
        btn_0 = Button(ChoixGAME2, text="Pierre", fg='white',bg='#8FCACA', height = 20, width = 20, command=lambda: [play(choix,Pierre,ChoixGAME2)])
        btn_0.pack(side=RIGHT, padx=5, pady=5)  
        btn_1 = Button(ChoixGAME2, text="Feuille", fg='white',bg='#97C1A9', height = 20, width = 20, command=lambda: [play(choix,Feuille,ChoixGAME2)])
        btn_1.pack(side=RIGHT, padx=5, pady=5)  
        btn_2 = Button(ChoixGAME2, text="Ciseau", fg='white',bg='#FF968A', height = 20, width = 20, command=lambda: [play(choix,Ciseau,ChoixGAME2)])
        btn_2.pack(side=RIGHT, padx=5, pady=5) 
        btn_5 = Button(ChoixGAME2, text="Exit", fg ='white',bg='black', height = 5, width = 5,command=ChoixGAME2.destroy)
        btn_5.pack(side=LEFT, padx=5, pady=5)
        #newWindow.iconbitmap('Back Up\\icon\\info.ico')

    def play(choixp1,choixp2,ChoixGAME2):
        
        if(choixp1 == choixp2):
            replay21v1(ChoixGAME2)
        else:
            if(choixp1 == 1 and choixp2 == 2):
                replay31v1(ChoixGAME2)
            elif(choixp1 == 2 and choixp2 == 1):
                replay11v1(ChoixGAME2)
            elif(choixp1 == 3 and choixp2 == 1):
                replay31v1(ChoixGAME2)
            elif(choixp1 == 1 and choixp2 == 3):
                replay11v1(ChoixGAME2)
            elif(choixp1 == 3 and choixp2 == 2):
                replay11v1(ChoixGAME2)
            elif(choixp1 == 2 and choixp2 == 3):
                replay31v1(ChoixGAME2)

    def replay11v1(ChoixGAME2):
        # be treated as a new window
        replay11v1 = Toplevel(fenetre)
        # set the title 
        replay11v1.title(" Replay ? ")
        
        # sets the dimensions
        replay11v1.geometry("165x150")
        
        # in the Window
        label = Label(replay11v1, text="P1 WIN !", font=("Courier", 25))
        label.pack()
        Label(replay11v1, 
            text ="\n" + "You want replay ?" + "\n",fg='#FFCBA2',font='bold').pack()
        btn_0 = Button(replay11v1, text="Yes", fg='white',bg='#619ED6', height = 5, width = 8, command=lambda: [close(ChoixGAME2,replay11v1)])
        btn_0.pack(side=RIGHT, padx=5, pady=5)  
        btn_1 = Button(replay11v1, text="No", fg='white',bg='#E64345', height = 5, width = 8, command=fermer)
        btn_1.pack(side=RIGHT, padx=5, pady=5)  
        #newWindow.iconbitmap('Back Up\\icon\\info.ico')

    def replay21v1(ChoixGAME2):
        # be treated as a new window
        replay21v1 = Toplevel(fenetre)
        
        # set the title 
        replay21v1.title(" Replay ? ")
        
        # sets the dimensions
        replay21v1.geometry("150x150")
        
        # in the Window
        label = Label(replay21v1, text="EQUAL !", font=("Courier", 25))
        label.pack()
        Label(replay21v1, 
            text ="\n" + "You want replay ?" + "\n",fg='#FFCBA2',font='bold').pack()
        btn_0 = Button(replay21v1, text="Yes", fg='white',bg='#619ED6', height = 5, width = 8, command=lambda: [close(ChoixGAME2,replay21v1)])
        btn_0.pack(side=RIGHT, padx=5, pady=5)  
        btn_1 = Button(replay21v1, text="No", fg='white',bg='#E64345', height = 5, width = 8, command=fermer)
        btn_1.pack(side=RIGHT, padx=5, pady=5)  
        #newWindow.iconbitmap('Back Up\\icon\\info.ico')

    def replay31v1(ChoixGAME2):
        # be treated as a new window
        replay31v1 = Toplevel(fenetre)
        
        # set the title 
        replay31v1.title(" Replay ? ")
        
        # sets the dimensions
        replay31v1.geometry("175x150")
        
        # in the Window
        label = Label(replay31v1, text="P1 LOOSE!", font=("Courier", 25))
        label.pack()
        Label(replay31v1, 
            text ="\n" + "You want replay ?" + "\n",fg='#FFCBA2',font='bold').pack()
        btn_0 = Button(replay31v1, text="Yes", fg='white',bg='#619ED6', height = 5, width = 8, command=lambda: [close(ChoixGAME2,replay31v1)])
        btn_0.pack(side=RIGHT, padx=5, pady=5)  
        btn_1 = Button(replay31v1, text="No", fg='white',bg='#E64345', height = 5, width = 8, command=fermer)
        btn_1.pack(side=RIGHT, padx=5, pady=5)  
        #newWindow.iconbitmap('Back Up\\icon\\info.ico')

    # be treated as a new window
    GAME2 = Toplevel(fenetre)
      
    # set the title 
    GAME2.title("P1 VS P2 !")
      
    # sets the dimensions
    GAME2.geometry("525x150")
      
    # in the Window
    Label(GAME2, 
        text ="\n" + "What do you play player 1 ?" + "\n",fg='#FFCBA2',font='bold').pack()
    btn_0 = Button(GAME2, text="Pierre", fg='white',bg='#8FCACA', height = 20, width = 20, command=ChoixP11)
    btn_0.pack(side=RIGHT, padx=5, pady=5)  
    btn_1 = Button(GAME2, text="Feuille", fg='white',bg='#97C1A9', height = 20, width = 20, command=ChoixP12)
    btn_1.pack(side=RIGHT, padx=5, pady=5)  
    btn_2 = Button(GAME2, text="Ciseau", fg='white',bg='#FF968A', height = 20, width = 20, command=ChoixP13)
    btn_2.pack(side=RIGHT, padx=5, pady=5) 
    btn_5 = Button(GAME2, text="Exit", fg ='white',bg='black', height = 5, width = 5,command=GAME2.destroy)
    btn_5.pack(side=LEFT, padx=5, pady=5)
    #newWindow.iconbitmap('Back Up\\icon\\info.ico')

def GAME3():

    def playIA():
        bot1 = (random.randint(1, 3))
        bot2 = (random.randint(1, 3))
        if(bot1 == bot2):
            replay2()
        else:
            if(bot1 == 1 and bot2 == 2):
                replay1IA()
            elif(bot1 == 2 and bot2 == 1):
                replay3IA()
            elif(bot1 == 3 and bot2 == 1):
                replay3IA()
            elif(bot1 == 1 and bot2 == 3):
                replay1IA()
            elif(bot1 == 3 and bot2 == 2):
                replay1IA()
            elif(bot1 == 2 and bot2 == 3):
                replay3IA()

    def replay1IA():
        # be treated as a new window
        replay1IA = Toplevel(fenetre)
        
        # set the title 
        replay1IA.title(" Replay ? ")
        
        # sets the dimensions
        replay1IA.geometry("150x150")
        
        # in the Window
        label = Label(replay1IA, text="IA1 WIN!", font=("Courier", 25))
        label.pack()
        Label(replay1IA, 
            text ="\n" + "You want replay ?" + "\n",fg='#FFCBA2',font='bold').pack()
        btn_0 = Button(replay1IA, text="Yes", fg='white',bg='#619ED6', height = 5, width = 8, command=replay1IA.destroy)
        btn_0.pack(side=RIGHT, padx=5, pady=5)  
        btn_1 = Button(replay1IA, text="No", fg='white',bg='#E64345', height = 5, width = 8, command=fermer)
        btn_1.pack(side=RIGHT, padx=5, pady=5)  
        #newWindow.iconbitmap('Back Up\\icon\\info.ico')

    def replay2IA():
        # be treated as a new window
        replay2IA = Toplevel(fenetre)
        
        # set the title 
        replay2IA.title(" Replay ? ")
        
        # sets the dimensions
        replay2IA.geometry("150x150")
        
        # in the Window
        label = Label(replay2IA, text="EQUAL !", font=("Courier", 25))
        label.pack()
        Label(replay2IA, 
            text ="\n" + "You want replay ?" + "\n",fg='#FFCBA2',font='bold').pack()
        btn_0 = Button(replay2IA, text="Yes", fg='white',bg='#619ED6', height = 5, width = 8, command=replay2IA.destroy)
        btn_0.pack(side=RIGHT, padx=5, pady=5)  
        btn_1 = Button(replay2IA, text="No", fg='white',bg='#E64345', height = 5, width = 8, command=fermer)
        btn_1.pack(side=RIGHT, padx=5, pady=5)  
        #newWindow.iconbitmap('Back Up\\icon\\info.ico')

    def replay3IA():
        # be treated as a new window
        replay3IA = Toplevel(fenetre)
        
        # set the title 
        replay3IA.title(" Replay ? ")
        
        # sets the dimensions
        replay3IA.geometry("165x150")
        
        # in the Window
        label = Label(replay3IA, text="IA1 LOOSE!", font=("Courier", 25))
        label.pack()
        Label(replay3IA, 
            text ="\n" + "You want replay ?" + "\n",fg='#FFCBA2',font='bold').pack()
        btn_0 = Button(replay3IA, text="Yes", fg='white',bg='#619ED6', height = 5, width = 8, command=replay3IA.destroy)
        btn_0.pack(side=RIGHT, padx=5, pady=5)  
        btn_1 = Button(replay3IA, text="No", fg='white',bg='#E64345', height = 5, width = 8, command=fermer)
        btn_1.pack(side=RIGHT, padx=5, pady=5)  
        #newWindow.iconbitmap('Back Up\\icon\\info.ico')

    # be treated as a new window
    GAME3 = Toplevel(fenetre)
      
    # set the title 
    GAME3.title(" IA VS IA !")
      
    # sets the dimensions
    GAME3.geometry("300x150")
      
    # in the Window
    Label(GAME3, 
        text ="\n" + "It's a IA VS IA !" + "\n",fg='#FFCBA2',font='bold').pack()
    btn_5 = Button(GAME3, text="PLAY", fg ='white',bg='#6BA547', height = 15, width = 15,command=playIA)
    btn_5.pack(side=RIGHT, padx=5, pady=5)
    btn_5 = Button(GAME3, text="Exit", fg ='white',bg='black', height = 5, width = 5,command=GAME3.destroy)
    btn_5.pack(side=LEFT, padx=5, pady=5)
    #newWindow.iconbitmap('Back Up\\icon\\info.ico')

# Information page
def new_window():

    # be treated as a new window
    newWindow = Toplevel(fenetre)
      
    # set the title 
    newWindow.title("Informations !")
      
    # sets the dimensions
    newWindow.geometry("550x350")
      
    # in the Window
    Label(newWindow, 
        text ="\n" + "Welcome to the information page" + "\n",fg='#1E90FF',font='bold').pack()
    Label(newWindow, 
        text ="[P1 VS P2] :" + "\n",fg='dark blue').pack()
    Label(newWindow, 
        text ="[P1 VS IA] ",fg='dark blue').pack()
    Label(newWindow, 
        text ="[IA VS IA] :",fg='dark blue').pack()
    Label(newWindow, 
        text ="\n" + "Thanks !" + "\n",fg='#A965CA',font='bold').pack()
    btn_5 = Button(newWindow, text="Exit", fg ='white',bg='black', command=newWindow.destroy)
    btn_5.pack(padx=5, pady=5)
    #newWindow.iconbitmap('Back Up\\icon\\info.ico')

def main():
    fenetre = Tk()
    # set the title of the main window
    fenetre.title("PYCode")
    # set the dimension of the main window
    fenetre.geometry("350x125")
    Label(fenetre, text ="\n" + "Welcome !" + "\n" "Are you ready to play ?" + "\n",fg='Black',font='bold').pack()

    btn_0 = Button(fenetre, text="IA VS IA", fg='white',bg='#FDC453', height = 5, width = 8, command=GAME3)
    btn_0.pack(side=RIGHT, padx=5, pady=5)  
    btn_1 = Button(fenetre, text=" P1 VS P2", fg='white',bg='#9ADBC5', height = 5, width = 8, command=GAME2)
    btn_1.pack(side=RIGHT, padx=5, pady=5)  
    btn_2 = Button(fenetre, text=" P1 VS IA", fg='white',bg='#A0DDE0', height = 5, width = 8, command=GAME1)
    btn_2.pack(side=RIGHT, padx=5, pady=5)  
    btn_4 = Button(fenetre, text="Info", fg='white',bg='#3D4048', command=new_window)
    btn_4.pack(side=LEFT, padx=5, pady=5)  
    #fenetre.iconbitmap('Back Up\\icon\\icon.ico')
    fenetre.mainloop()

if __name__ == "__main__":
    main()
