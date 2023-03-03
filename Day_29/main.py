from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [choice(letters) for i in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for i in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for i in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,f'{password}')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    new_data = {
        website : {
            'email':email,
            'password':password
        }
    }
    
    if website == '' or password == '':
        messagebox.showerror(title = 'Error', message= "Please don't leave any field empty!")

    else:
        try:
            with open('data.json','r') as data_file:
                #Reading old data
                data = json.load(data_file)
        
        except FileNotFoundError:
            with open('data.json','w') as data_file:
                json.dump(new_data,data_file,indent= 4)
        
        else: 
            #Updating old data with new data
            data.update(new_data)

            with open('data.json','w') as data_file:
                json.dump(data, data_file, indent = 4)
        
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open('data.json','r') as data_file:
            data = json.load(data_file)
            email = data[website]['email']
            password = data[website]['password']

    except FileNotFoundError:
        messagebox.showinfo(text = 'No Data File Found')
    except KeyError:
        messagebox.showinfo(text = 'No details for the website exists')
    else:
        messagebox.showinfo(title = 'Result', message = f'Email: {email}\nPassword: {password}')


# ---------------------------- UI SETUP ------------------------------- #

#window
window = Tk()
window.title('Password Manager')
window.config(padx = 30, pady = 30)

#canvas
canvas = Canvas(width = 200, height = 200, highlightthickness=0)
logo_img = PhotoImage(file = 'logo.png')
image_logo = canvas.create_image(100,100,image = logo_img)
canvas.grid(row = 0, column = 1)

#LABELS ----------------------------------------------------------------------

#website_label 
website_label = Label(text = 'Website:', font= ('Arial',12))
website_label.grid(row = 1,column= 0)

#username_label
username_label = Label(text = 'Email/Username:', font= ('Arial',12))
username_label.grid(row = 2,column= 0)

#password_label
password_label = Label(text = 'Password:', font= ('Arial',12))
password_label.grid(row = 3,column= 0)


#BUTTONS ----------------------------------------------------------------------

#generate_pass_button
generate_pass_button = Button(text="Generate Password", command= generate_password,width = 16)
generate_pass_button.grid(row = 3, column = 2)

#add_button
add_button = Button(text="Add",width = 44,command= save)
add_button.grid(row = 4, column = 1, columnspan= 2)

#Search button
search_button = Button(text = 'Search',width = 16, command = find_password)
search_button.grid(row = 1,column = 2)


#ENTRIES ----------------------------------------------------------------------

#website_entry
website_entry = Entry(window,width = 32)
website_entry.grid(row = 1, column = 1)
website_entry.focus()

#username_entry
username_entry = Entry(window,width = 52)
username_entry.grid(row = 2, column = 1,columnspan=2)
username_entry.insert(0,'18gianlucab@gmail.com')

#password_entry
password_entry = Entry(window,width = 32)
password_entry.grid(row = 3, column = 1)





window.mainloop()