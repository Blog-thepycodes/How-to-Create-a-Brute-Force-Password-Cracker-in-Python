import itertools
import string
import tkinter as tk
from tkinter import messagebox
 
 
def generate_passwords(length):
   characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
   for password in itertools.product(characters, repeat=length):
       yield ''.join(password)
 
 
def brute_force(target_password, max_length=8):
   for length in range(1, max_length + 1):
       for password in generate_passwords(length):
           if password == target_password:
               return password
           #update_attempted_password(password)  # Show the process of hacking the password
   return None
 
 
def crack_password():
   target_password = entry_target_password.get()
   cracked_password = brute_force(target_password)
   if cracked_password:
       label_cracked_password.config(text=f"Password cracked: {cracked_password}")
       messagebox.showinfo("Password Cracked", f"The password is: {cracked_password}")
   else:
       messagebox.showinfo("Failed", "Failed to crack the password.")
 
 
#def update_attempted_password(password):
#   label_attempted_password.config(text=f"Trying password: {password}")
 #  label_attempted_password.update()  # Force update the GUI
 
 
# GUI setup
root = tk.Tk()
root.title("Password Cracker - The Pycodes")
root.geometry('400x300')
root.resizable(False,False)
 
 
label_target_password = tk.Label(root, text="Enter the target password:")
label_target_password.pack()
 
 
entry_target_password = tk.Entry(root, width=30)
entry_target_password.pack()
 
 
button_crack = tk.Button(root, text="Crack Password", command=crack_password)
button_crack.pack()
 
 
label_attempted_password = tk.Label(root, text="")
label_attempted_password.pack()
 
 
label_cracked_password = tk.Label(root, text="")
label_cracked_password.pack()
 
root.mainloop()
