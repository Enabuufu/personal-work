from tkinter import *

main_screen = Tk()  # create a GUI window


def main_account_screen():
    global main_screen
    main_screen.geometry("1920x1080")  # set the configuration of GUI window
    main_screen.title("Account Login")  # set the title of GUI window
    Button(text="Register", height="2", width="30", command=register()).pack()


# create a Form label
Label(text="Choose Login Or Register", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()

# create Login Button
Button(text="Login", height="2", width="30").pack()
Label(text="").pack()

# create a register button
Button(text="Register", height="2", width="30").pack()

main_screen.mainloop()  # start the GUI

main_account_screen()  # call the main_account_screen() function


def register():
        # The Toplevel widget work pretty much like Frame,
        # but it is displayed in a separate, top-level window.
        # Such windows usually have title bars, borders, and other “window decorations”.
        # And in argument we have to pass global screen variable

        register_screen = Toplevel(main_screen)
        register_screen.title("Register")
        register_screen.geometry("300x250")
        global username
        global password
        global username_entry
        global password_entry

        # Set text variables
        username = StringVar()
        password = StringVar()

        # Set label for user's instruction
        Label(register_screen, text="Please fill in the details below", bg="blue").pack()
        Label(register_screen, text="").pack()

        # Set username label
        username_lable = Label(register_screen, text="Username * ")
        username_lable.pack()

        # Set username entry
        # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()

        # Set password label
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()

        # Set password entry
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()

        Label(register_screen, text="").pack()

        # Set register button
        Button(register_screen, text="Register", width=10, height=1, bg="blue").pack()
        Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


def register_user():
    # get username and password
    username_info = username.get()
    password_info = password.get()

    # Open file in write mode
    file = open(username_info, "w")

    # write username and password information into file
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)


# set a label for showing success information on screen

Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
