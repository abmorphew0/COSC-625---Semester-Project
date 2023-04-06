# Menu For JAFN Runner Game:

from tkinter import *

#Sets Up Menu Page
root = Tk()
root.geometry("300x300")
root.title("Endless Runner Game")
#root.bg = PhotoImage(file = "Picture1.png")

#Displays Easy Medium and Hard Mode
def GameMode(Play, Exit,sc,title,High_Score):
    Easy = Button(root, height = 2, width = 20, text = "Easy Mode", command = lambda:EasyMode(sc,Easy, Medium, Hard, Back,title,High_Score))
    Medium = Button(root, height = 2, width = 20, text = "Medium Mode", command = lambda:MidMode(sc,Easy, Medium, Hard, Back,title,High_Score))
    Hard = Button(root, height = 2, width = 20, text = "Hard Mode", command = lambda:HardMode(sc, Easy, Medium, Hard, Back,title,High_Score))
    Back = Button(root, height = 2, width = 20, text = "Back",command = lambda:GameMenu(Easy, Medium, Hard, Play, Exit, Back))
    
    Play.forget()
    Exit.forget()
    Easy.pack()
    Medium.pack()
    Hard.pack()
    Back.pack()
#Plays Easy Mode
def EasyMode(sc,Easy, Medium, Hard, Back,title,High_Score):
    title.forget()
    High_Score.forget()
    Easy.forget()
    Medium.forget()
    Hard.forget()
    Back.forget()
    import JAFN_Game
    JAFN_Game.runGame(40,sc)
#Plays Medium Mode
def MidMode(sc,Easy, Medium, Hard, Back,title,High_Score):
    title.forget()
    High_Score.forget()
    Easy.forget()
    Medium.forget()
    Hard.forget()
    Back.forget()
    import JAFN_Game
    JAFN_Game.runGame(60,sc)
#Plays hard Mode
def HardMode(sc,Easy, Medium, Hard, Back,title,High_Score):
    title.forget()
    High_Score.forget()
    Easy.forget()
    Medium.forget()
    Hard.forget()
    Back.forget()
    import JAFN_Game
    JAFN_Game.runGame(80,sc)

#Exit Function
def Exit_Program(name):
    title.configure(text = "Goodbye "+name)
    exit
#Game Game Menu Function
def GameMenu(Easy, Medium, Hard, Play, Exit, Back):
    Easy.forget()
    Medium.forget()
    Hard.forget()
    Back.forget()
    Play.pack()
    Exit.pack()
#Creates Menu 
def mainMenu(sc):
    score = "HIGH SCORE: "+str(sc)
    title = Label(text = "Snatch 'N Dash",fg ="Blue",bg ="Orange",font = "Verdana 12 bold")
    High_Score = Label(text = score,fg ="Black",bg ="Orange",font = "Verdana 14 bold")
    Play = Button(root, height = 2, width = 20, text = "Play Game", command = lambda:GameMode(Play,Exit,sc,title,High_Score))
    Exit = Button(root, height = 2, width = 20, text = "Exit Game",command = exit)

    title.pack()
    High_Score.pack()
    Play.pack()
    #Character.pack()
    Exit.pack()

    mainloop()
