from tkinter import *
import pandas as pd
from random import choice
import time

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient="records")

def next_card():
    my_word = choice(to_learn)

    canvas.itemconfig(word,text = my_word['French'])
    canvas.itemconfig(card,image  = card_front_img)

    time.sleep(3)

    canvas.itemconfig(word,text = my_word['English'],fill= 'white')
    canvas.itemconfig(card,image = card_back_img)


    

#window
window = Tk()
window.config(padx= 20,pady=20,bg= BACKGROUND_COLOR)


#canvas
canvas = Canvas(width = 800, height = 526, highlightthickness=0)
canvas.configure(bg=BACKGROUND_COLOR)
canvas.create_text(400,150,text = "Title",font=("Arial",40,"italic"))
card_front_img = PhotoImage(file = 'images/card_front.png')
card = canvas.create_image(400,263,image = card_front_img)
word = canvas.create_text(400,263,text = "Word",font=("Arial",60,"bold"))
card_back_img = PhotoImage(file = 'images/card_back.png')
canvas.grid(row=0,column=0,columnspan=2)

#Buttons
X_image = PhotoImage(file= 'images/wrong.png')
button_X = Button(image=X_image,command=next_card)
button_X.grid(row=1,column=0)

V_image = PhotoImage(file= 'images/right.png')
button_V = Button(image=V_image,command = next_card)
button_V.grid(row=1,column=1)

next_card()















window.mainloop()