from Tkinter import *
from functools import partial


def validateLogin(username, password):
	print ("User has entered the username :", username.get())
	print ("User has entered the password :", password.get())
	return


# Creating the GUI window 
console = Tk () # Initialization of Tkinter
console.geometry('400x300')  # Size of the window
console.title('Login page for using python Tkinter code')



