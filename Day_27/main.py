from tkinter import *

def button_clicked():
    print('I got clicked')
    new_text = input.get() 
    my_label.config(text = new_text)

window = Tk()
window.title('My first GUI program')
window.minsize(width = 500, height = 300)

#Label 
my_label = Label(text = 'I Am a Label', font = ('Arial',24,'bold'))
my_label.grid(column = 0,row = 0)

#button_1
button_1 = Button(text = 'Click me',command = button_clicked)
button_1.grid(column = 1, row = 1)

#button_2
button_2 = Button(text = 'Click me',command = button_clicked)
button_2.grid(column = 2, row = 0)

#input
input = Entry(width = 10)
input.grid(column = 3, row = 2)















window.mainloop()