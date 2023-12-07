import openpyxl
from tkinter import *
from tkinter import messagebox
from openpyxl import Workbook
# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=20)

canvas = Canvas(window, width = 200, height = 200)
logo_img = PhotoImage(file="logo.png")

def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get the user input from the form
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    

    with open('data.txt', 'a') as data_file:
        data_file.write(f'{website} | {email} | {password}\n')
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        
    messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

       
            
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0,column=1)

#Create labels and entry fields for each input
#Website
website_label = Label(text="Website:", )
website_label.grid(row=1, column=0)
website_entry = Entry(width=38)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
#Email
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=38)
email_entry.insert(0, "akhmad@email.com")
email_entry.grid(row=2, column=1, columnspan=2)
#Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
#Buttons
generateP_button = Button(text="Generate Password", command=generate_password)
generateP_button.grid(row=3, column=2)

register_button = Button(text="Add", command=save, width=36)
register_button.grid(row=4, column=1, columnspan=2)


window.mainloop()