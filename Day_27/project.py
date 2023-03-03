from tkinter import * 
FONT = ('Arial',24,'bold')

def button_clicked():
    miles_input = input.get() 
    km_output = 1.6 * float(miles_input)
    label_km.config(text = km_output)

#create window
window = Tk()
window.title('Mile to Km converter')
window.minsize(width = 500, height = 300)

#input
input = Entry(width = 10)
input.grid(column = 1, row = 0)

#Label 
label_1 = Label(text = 'is equal to', font = FONT)
label_1.grid(column = 0,row = 1)

#Label 
label_2 = Label(text = 'Miles', font = FONT)
label_2.grid(column = 2,row = 0)

#Label 
label_3 = Label(text = 'Km', font = FONT)
label_3.grid(column = 2,row = 1)

#label 
label_km = Label(text = '0', font = FONT)
label_km.grid(column = 1,row = 1)


#Button 
button = Button(text = 'Calculate',command = button_clicked)
button.grid(column = 1, row = 2)


window.mainloop()



