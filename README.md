# Introduction  
🔐 Step into the world of password security! This project is a **Password Manager** built with Python and Tkinter. It helps you generate strong random passwords, copy them instantly to your clipboard, and save them safely into a local text file.  
💡  
🖥️ Want to check out the source code? See it here: [main.py](/main.py)  

---

# Background  
Driven by the need to create secure and unique passwords quickly, this project was developed to simplify password management. Instead of reusing weak passwords or relying on external tools, the app generates strong, randomized passwords and stores them locally in a structured way.  

### The questions I wanted to answer through my project were:  

1- How can I quickly generate secure, random passwords?  
2- How can I safely store them for future use?  

---

# Tools I Used  

For building this Password Manager, I relied on several key tools:  

**Python 3** 🐍 — The programming language powering the entire project.  

**Tkinter** 🎨 — The GUI toolkit used to build a simple and intuitive interface.  

**Pyperclip** 📋 — Enables instant password copying to the clipboard.  

**Random Module** 🎲 — Ensures strong, unpredictable password generation with a mix of letters, numbers, and symbols.  

---

# The Application  

Each feature of this project was designed to tackle specific password management needs. Here’s how it works:  

### 1. Password Generation  
To create strong and secure passwords, I combined lowercase and uppercase letters, digits, and symbols, then randomized their order for maximum security. The generated password is also copied to the clipboard automatically.  

```python
password_letters = [choice(letters) for _ in range(randint(8, 10))]
password_symbol  = [choice(symbols) for _ in range(randint(2, 4))]
password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

password_list = password_letters + password_symbol + password_numbers
shuffle(password_list)

password = ''.join(password_list)
password_input.insert(0, password)
pyperclip.copy(password)

```

### 2. Save Passwords  
To securely store credentials, I implemented a save function that validates inputs, confirms with the user, and writes the data into a local text file (`data.txt`).  

```python
def save():
    if len(email_input.get()) == 0 or len(password_input.get()) == 0:
       messagebox.showwarning(title='Empty cell', message=f'Please don\'t leave any fields empty.' )     
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f'These are the details entered:\nEmail: {email_input.get()}'
                    f'\nPassword: {password_input.get()}\nIs it okay to save?')

        if is_ok:
            with open('data.txt','a') as new_pass:
                new_pass.write(f'{website_input.get()} | {email_input.get()} | {password_input.get()}\n')
                website_input.delete(0,END)
                password_input.delete(0,END)
                website_input.focus()
```

# What I Learned  

Throughout this project, I’ve upgraded my Python skills and learned valuable lessons in GUI development and security:  

🧩 **Complex GUI Crafting:** Mastered Tkinter layout management, combining labels, entries, and buttons into a structured and user-friendly interface.  

📋 **Input Validation & User Interaction:** Learned how to add field validation and confirmation dialogs (`askokcancel`) to ensure safer and smoother user experience.  

🔐 **Clipboard Integration:** Implemented seamless password copying with `pyperclip`, reducing friction for end-users.  

💾 **File Handling in Python:** Practiced writing structured data (`Website | Email | Password`) into a text file, while managing appending and resetting fields automatically.  

💡 **Project Organization:** Enhanced my ability to separate concerns (UI setup, password generation, saving functions) to keep the code clean and maintainable.  
