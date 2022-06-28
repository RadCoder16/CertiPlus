from tkinter import *


#============== GLOBAL VARIABLES =============#

window = Tk()
window.title("Certify")
window.resizable(False, False)
window.geometry('700x500')

#================== TITLE VARIABLES FOR THE NAME OF THE APP ==================#

Title = Label(window,text="CERTIPLUS",  font='bold,arial 17', fg='lightseagreen')
Title.grid(row=2, column=5)
Title.place(relx=0.5, rely=0.1, anchor=CENTER)

#================== LABEL, GRID TEMPLATES, PLACEMENTS AND ENTRY FOR FIRST NAME ===================#

username = Label(window,text='FirstName: ',  font='bold')
userEntry = Entry(window)

username.grid(row=3, column=1)
userEntry.grid(row=4, column=1)

username.place(relx=0.5, rely=0.2, anchor=CENTER)
userEntry.place(relx=0.7, rely=0.2, anchor=CENTER)

#================== LABEL, GRID TEMPLATES, PLACEMENTS AND ENTRY FOR LAST NAME ===================#


Lastname = Label(window,text='LastName: ',  font='bold')
lastEntry = Entry(window)

Lastname.grid(row=3, column=1)
lastEntry.grid(row=4, column=1)

Lastname.place(relx=0.5, rely=0.3, anchor=CENTER)
lastEntry.place(relx=0.7, rely=0.3, anchor=CENTER)

#================== LABEL, GRID TEMPLATES, PLACEMENTS AND ENTRY FOR USER NAME ===================#


Username = Label(window, text="Username", font='bold')
Username_entry = Entry(window)

Username.grid(row=3, column=1)
Username_entry.grid(row=4, column=1)

Username.place(relx=0.5, rely=0.4, anchor=CENTER)
Username_entry.place(relx=0.7, rely=0.4, anchor=CENTER)

#================== LABEL, GRID TEMPLATES, PLACEMENTS AND ENTRY FOR PASSWORD ===================#

passWord = Label(window, text='Password: ', font='bold')
passEntry = Entry(window)

passWord.grid(row=3, column=1)
passEntry.grid(row=4, column=1)

passWord.place(relx=0.5, rely=0.5, anchor=CENTER)
passEntry.place(relx=0.7, rely=0.5, anchor=CENTER)

#================== LABEL, GRID TEMPLATES, PLACEMENTS AND ENTRY FOR PASSWORD VERIFICATION ===================#


reEnter = Label(window, text='Re enter password: ', font='bold')
reEntry = Entry(window)

reEnter.grid(row=3, column=1)
reEntry.grid(row=4, column=1)

reEnter.place(relx=0.5, rely=0.6, anchor=CENTER)
reEntry.place(relx=0.7, rely=0.6, anchor=CENTER)

#================== LABEL, GRID TEMPLATES, PLACEMENTS AND ENTRY FOR EMAIL ===================#


Email = Label(window, text='Email: ', font='bold')
emailEntry = Entry(window)

Email.grid(row=3, column=1)
emailEntry.grid(row=4, column=1)

Email.place(relx=0.5, rely=0.7, anchor=CENTER)
emailEntry.place(relx=0.7, rely=0.7, anchor=CENTER)


#================ FUNCTIONS, BUTTONS, PLACEMENTS & GRID TEMPLATES ================#

def my_command():
   reg_button.config(text= "Registered succesful!")


reg_button = Button(window, text="Sign up", font='bold', command=my_command, borderwidth=0)


reg_button.grid(row=3, column=1)
reg_button.place(relx=0.5, rely=0.8)

#================== SCREEN LOOP =====================#

window.mainloop()