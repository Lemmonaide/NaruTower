from tkinter import *
import tkinter as tk

def roleplay():
    #Create the window
    rpWin = Toplevel()
    rpWin.title("Naru Tower Roleplay")
    rpWin.geometry("1220x500")

    #Roleplay Title
    roleplayTitle = Label(rpWin, text="Naru Tower Roleplay", font="bold 24").grid(row=0, column=0, columnspan=100)

    #------------------------------------------------Spacer------------------------------------------------------

    spacerRP = Label(rpWin, text=" ").grid(row=1, column=1, rowspan=100)

    #----------------------------------------------Storytelling---------------------------------------------------

    storytellingTitle = Label(rpWin, text="Storytelling", font="bold 16").grid(row=1, column=0)

    #Character Background
    backgroundTitle = Label(rpWin, text="Character Backstory").grid(row=2, column=0)
    backgroundEntry = Text(rpWin, width=75, height=5).grid(row=3, column=0)

    #Goals
    shortGoalTitle = Label(rpWin, text="Short Term Goals").grid(row=4, column=0)
    shortGoal = Text(rpWin, width=75, height=5).grid(row=5, column=0)

    longGoalTitle = Label(rpWin, text="Long Term Goals").grid(row=6, column=0)
    longGoal = Text(rpWin, width=75, height=5).grid(row=7, column=0)

    #-----------------------------------------------Character Profile------------------------------------------
    charProfile = Label(rpWin, text="Character Profile", font="bold 16").grid(row=1, column=2)

    #Personality Trait
    personTrait = Label(rpWin, text="Personality Traits").grid(row=2, column=2)
    personTraitEnter = Text(rpWin, width=75, height=5).grid(row=3, column=2)

    #Strengths
    strengthTrait = Label(rpWin, text="Strengths").grid(row=4, column=2)
    strengthTraitEnter = Text(rpWin, width=75, height=5).grid(row=5, column=2)

    #Flaws
    flawTrait = Label(rpWin, text="Flaws").grid(row=6, column=2)
    flawTraitEnter = Text(rpWin, width=75, height=5).grid(row=7, column=2)

    # ----------------------------------------------------Exit----------------------------------------
    quitSpacer = Label(rpWin, text=" ").grid(row=100, column=0, columnspan=100)
    button_quit = Button(rpWin, text="Exit Roleplay", command=rpWin.destroy, bg="black", fg="white", width=35, height=2)
    button_quit.grid(row=101, column=0, columnspan=100, sticky="NESW")

    rpWin.mainloop()