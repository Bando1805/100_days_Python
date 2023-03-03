from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
# ---------------------------- TIMER RESET  ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_pomodoro, text = '00:00')
    title_label.config(text = 'Timer')
    checkmark_label.config(text = '')
    global reps
    reps = 0
# ---------------------------- TIMER  ------------------------------- # 
reps  =  0 
def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        min = WORK_MIN
        title_label.config(text= 'Work',fg= GREEN)
    elif reps % 8 == 0:
        min = LONG_BREAK_MIN
        title_label.config(text= 'Break',fg= RED)
    else:
        min = SHORT_BREAK_MIN
        title_label.config(text= 'Break',fg= PINK)
    
    count_down(min *60)
    
# ---------------------------- COUNTODOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if len(str(count_sec)) == 1:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(text_pomodoro, text = f'{count_min}:{count_sec}')
    if count >0:
        timer = window.after(1000, count_down,count -1)
    else:
        mark = ''
        for _ in range(reps//2):
            mark += '✔'
        checkmark_label.config(text = mark)
        start_timer()
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx = 100, pady = 50, bg = YELLOW)

#canvas
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = 'tomato.png')
image_pomodoro = canvas.create_image(100,112,image = tomato_img)
text_pomodoro = canvas.create_text(100,130,text = '00:00',fill = 'white', font = (FONT_NAME,35,'bold'))
canvas.grid(row = 1, column = 1)

#title 
title_label = Label(text = 'Timer', fg = GREEN,bg = YELLOW,font= (FONT_NAME,40,'bold'))
title_label.grid(row = 0,column= 1)

#button_start
button_start = Button(text="Start",command= start_timer)
button_start.grid(row = 2, column = 0)

#button reset 
button_reset = Button(text = 'reset',command = reset_timer)
button_reset.grid(row = 2, column = 2)

#label checkmark
checkmark_label = Label(fg = GREEN, bg = YELLOW)
checkmark_label.grid(row = 3, column=1)

window.mainloop()