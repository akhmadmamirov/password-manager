import openpyxl
from tkinter import *
from tkinter import messagebox
from openpyxl import Workbook
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=20)

canvas = Canvas(window, width = 200, height = 200)
logo_img = PhotoImage(file="logo.png")

def generatePassword():
    pass

def register():
    # Get the user input from the form
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    # Create a new row with the user input
    new_row = [website, email, email]

    # Append the new row to the Excel sheet
    file_path = "registration_data.xlsx"

    try:
        # Try to load the existing workbook
        workbook = openpyxl.load_workbook(file_path)
    except FileNotFoundError:
        # If the file does not exist, create a new workbook
        workbook = Workbook()
        workbook.save(file_path)
    # Now, you can load the newly created workbook
    
    sheet = workbook.active
    sheet.append(new_row)
    workbook.save("registration_data.xlsx")
    messagebox.showinfo("Success", "Registration successful!")


canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0,column=1)

#Create labels and entry fields for each input
#Website
website_label = Label(text="Website:", )
website_label.grid(row=1, column=0)
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
#Email
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
#Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
#Buttons
generateP_button = Button(text="Generate Password", command=generatePassword)
generateP_button.grid(row=3, column=2)

register_button = Button(text="Add", command=register, width=36)
register_button.grid(row=4, column=1, columnspan=2)


window.mainloop()