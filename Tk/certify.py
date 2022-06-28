from msilib.schema import CheckBox
from tkinter import *
import tkinter
from tkinter import messagebox
from numpy import column_stack
import sqlite3

#============ GLOBAL VARIABLES ============#

window = Tk()
window.title("CERTIPLUS")
window.resizable(False, False)
window.geometry('500x500')

#============ VARIABLES =============#

user_input = tkinter.StringVar()
pass_input = tkinter.StringVar()

#============== FUNCTIONS ===================#

def next_page():
    window.destroy()
    import page2        

def prev_page():
    window.destroy()
    import certify

def login():
    data_base = sqlite3.connect('login.sqlite')
    data_base.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)')
    #data_base.execute("INSERT INTO login(username, password) VALUES('admin', 'admin')")
    data_base.execute("INSERT INTO login(username, password) VALUES('user', 'admin')")
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM login where username=? AND password=?", (user_input.get(), pass_input.get()))
    row = cursor.fetchone()
    
    if row:
        messagebox.showinfo('info', 'login success!')
    else:
        messagebox.showinfo('info', 'login failed!')
        
    cursor.connection.commit()
    data_base.close()
    
#================ BUTTONS ====================#
    
sign_button = Button(window, text='Sign up', font="bold", command=next_page)

register_button = Button(window, text='Login',font='bold',command=login)

#===================== LABELS & ENTRIES ====================#

main_label = Label(window,text="CERTIPLUS",  font='bold, 17', fg='lightseagreen')

semi_label = Label(window,text="Get your documents done and dusted")

account = Label(window,text="Already have an account?")

username = Label(window,text="Username", font='bold, 11')
user_entry = Entry(window, textvariable=username)

password = Label(window,text="Password", font="bold, 11")
pass_input = Entry(window, textvariable=pass_input, show='.')

sign_label = Label(window,text="Don't have an account?")

#===================== GRID TEMPLATES & PLACEMENTS ======================#

main_label.grid(row=0, column=1)
main_label.place(relx=0.5, rely=0.1, anchor=CENTER)

semi_label.grid(row=1, column=0)
semi_label.place(relx=0.5, rely=0.2, anchor=CENTER)

account.grid(row=2, column=0)
account.place(relx=0.5, rely=0.3, anchor=CENTER)

username.grid(row=3, column=0)
username.place(relx=0.1, rely=0.4, anchor=CENTER)

user_entry.grid(row=3, column=1)
user_entry.place(relx=0.3, rely=0.4, anchor=CENTER)

password.grid(row=4, column=0)
password.place(relx=0.6, rely=0.4, anchor=CENTER)

pass_input.grid(row=4, column=0)
pass_input.place(relx=0.8, rely=0.4, anchor=CENTER)

register_button.grid(row=5, column=0)
register_button.place(relx=0.82, rely=0.45)

sign_label.grid(row=6, column=0)
sign_label.place(relx=0.5, rely=0.6, anchor=CENTER)

sign_button.grid(row=7, column=0)
sign_button.place(relx=0.5, rely=0.7, anchor=CENTER)

#================ SCREEN LOOP ================#

window.mainloop()