from tkinter import *
from tkinter import messagebox
from random import choice, shuffle,randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    password_input.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbol = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbol + password_numbers

    shuffle(password_list)

    password = ''.join(password_list)

    password_input.insert(0,password)

    pyperclip.copy(password)

    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    if len(email_input.get()) == 0 or len(password_input.get()) == 0:
       messagebox.showwarning(title='Empty cell', message=f'Please dont leave any fields empty.' )     
    else:
        is_ok = messagebox.askokcancel(title=website,message=f'These are the details entered: \nEmail: {email_input.get()}'
                            f'\nPassword: {password_input.get()} \n Is it okey to save?')

        if is_ok:
            with open('data.txt','a') as new_pass:
                new_pass.write(f'{website_input.get()} | {email_input.get()} | {password_input.get()}\n')
                website_input.delete(0,END)
                password_input.delete(0,END)
                website_input.focus()
        




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)


canvas = Canvas(width=200, height=200,highlightthickness=False)
logo_png = PhotoImage(file='logo.png')
canvas.create_image(100,100,image = logo_png)
canvas.grid(row= 0,column=1)


# Labels 

website = Label(text='Website:')
website.grid(row=1,column=0)

email = Label(text='Email/Username:')
email.grid(row=2,column=0)

password = Label(text='Password:')
password.grid(row=3,column=0)


# Entries

website_input = Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2,sticky='w')
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2,sticky='w')
email_input.insert(0,'efilsahinercan1@gmail.com')


password_input = Entry(width=35)
password_input.grid(row=3,column=1,sticky='w')


# Buttons

generate_password = Button(text='Generate Password',padx=10,command = generate_password)
generate_password.grid(row=3,column=2)


add_password = Button(text='Add',width=36,command=save)
add_password.grid(row=4,column=1,columnspan=2,sticky='w')







window.mainloop()