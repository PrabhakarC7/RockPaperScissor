from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Initialize window
window = Tk()
window.configure(bg='black')
window.title("Rock Paper Scissors")

# Load Images
image_rock1 = ImageTk.PhotoImage(Image.open("rock1.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("paper1.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor1.png"))
image_rock2 = ImageTk.PhotoImage(Image.open("rock2.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("paper2.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor2.png"))

# Labels
Label(window, text="COMPUTER", bg="black", fg="white", font="Arial 10 bold").grid(row=1, column=2, pady=10)
Label(window, text="PLAYER", bg="black", fg="white", font="Arial 10 bold").grid(row=1, column=4)

# Default Images
l_computer = Label(window, image=image_rock1)
l_computer.grid(row=0, column=1)
l_player = Label(window, image=image_rock2)
l_player.grid(row=0, column=9)

# Scores
l_computer_score = Label(window, text="0", bg="green", fg="black", font="Arial 20 bold")
l_computer_score.grid(row=0, column=2)
l_player_score = Label(window, text="0", bg="green", fg="black", font="Arial 20 bold")
l_player_score.grid(row=0, column=4)

# Result Message
result_msg = Label(window, text="Make your choice", bg="green", fg="white", font="Courier 20 bold")
result_msg.grid(column=3)

# Score Update Functions
def msg_update(a):
    result_msg.config(text=a)

def comp_update():
    score = int(l_computer_score["text"])
    l_computer_score.config(text=str(score + 1))

def playr_update():
    score = int(l_player_score["text"])
    l_player_score.config(text=str(score + 1))

# Winning Conditions
def win_conditions(p, c):
    if p == c:
        msg_update("Tie!!!")
    elif (p == "Rock" and c == "Scissor") or (p == "Paper" and c == "Rock") or (p == "Scissor" and c == "Paper"):
        msg_update("You Won!!!")
        playr_update()
    else:
        msg_update("Computer Wins!!!")
        comp_update()

# Choices
choices = ["Rock", "Paper", "Scissor"]

# Update Choices
def choice_update(a):
    comp_choice = choices[randint(0, 2)]

    if comp_choice == "Rock":
        l_computer.config(image=image_rock1)
    elif comp_choice == "Paper":
        l_computer.config(image=image_paper1)
    else:
        l_computer.config(image=image_scissor1)

    if a == "Rock":
        l_player.config(image=image_rock2)
    elif a == "Paper":
        l_player.config(image=image_paper2)
    else:
        l_player.config(image=image_scissor2)

    win_conditions(a, comp_choice)

# Buttons
Button(window, text="Rock", font="Andalus 20 bold", bg="blue", fg="white", width=7, height=3, command=lambda: choice_update("Rock")).grid(row=7, column=2)
Button(window, text="Paper", font="Andalus 20 bold", bg="yellow", fg="black", width=7, height=3, command=lambda: choice_update("Paper")).grid(row=7, column=3, padx=5)
Button(window, text="Scissor", font="Andalus 20 bold", bg="red", fg="white", width=7, height=3, command=lambda: choice_update("Scissor")).grid(row=7, column=4)

window.mainloop()
