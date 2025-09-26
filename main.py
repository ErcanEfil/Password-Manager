from tkinter import *
from tkinter import messagebox
from random import choice, shuffle,randint
import pyperclip
import json



def find_password():

    try:
        with open('data.json','r') as new_pass:
            data = json.load(new_pass)
        if website_input.get() in data:
            messagebox.showinfo(title=f'{website_input.get()}', message=f'Email: {data[website_input.get()]['email']}\n'
                                f'Password: {data[website_input.get()]['password']}' )
        else:
            messagebox.showinfo(title='Website Name Error', message=f'No details for the website exists.' )
    except FileNotFoundError:
        messagebox.showinfo(title='Data File Error', message=f'No Data File Found.' )







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

    new_data = {
        website_input.get(): {
            'email':email_input.get(),
            'password':password_input.get(),
        }

    }

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
       messagebox.showwarning(title='Empty cell', message=f'Please dont leave any fields empty.' )     
    else:
        try:
            with open('data.json','r') as new_pass:
                
                data = json.load(new_pass)
        except FileNotFoundError:
                with open('data.json','w') as new_pass:
                    json.dump(new_data,new_pass,indent=4)
        else:
            data.update(new_data)

            with open('data.json','w') as new_pass:
                json.dump(data,new_pass,indent=4)
        
        finally:
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
website_input.grid(row=1,column=1,sticky='w')
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2,sticky='w')
email_input.insert(0,'efilsahinercan1@gmail.com')


password_input = Entry(width=35)
password_input.grid(row=3,column=1,sticky='w')



# Buttons

generate_password = Button(text='Generate Password',padx=10,command = generate_password)
generate_password.grid(row=3,column=2)


add_password = Button(text='Add',width=35,command=save)
add_password.grid(row=4,column=1,columnspan=2,sticky='w')

search = Button(text='Search',command=find_password)
search.grid(row=1,column=2,sticky='w')






window.mainloop()