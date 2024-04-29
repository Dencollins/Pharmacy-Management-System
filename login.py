from tkinter import *
import tkinter
import customtkinter as custom
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import PhotoImage

custom.set_appearance_mode("light")
custom.set_default_color_theme("blue")


# newpage
def button_function():
    root.destroy()
    new_page = custom.CTk()
    new_page.geometry("1280x720")
    new_page.title("BENORA PHARMACY")
    l1 = custom.CTkLabel(
        master=new_page, text="BENORA PHARMACY", font=("Century Gothic", 60)
    )
    l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    new_page.mainloop()


# Function to check login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()
    # Replace these with actual credentials validation
    if username == "benora" and password == "1234":
        # messagebox.showinfo("welcome! Login successful")
        button_function()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Create the main window
root = custom.CTk()
root.title("Benora Pharmacy Login")
root.geometry("600X440")
# back ground image
bg_image = ImageTk.PhotoImage(Image.open("LoginSystem\loginBg.jpg"))
bg_label = Label(master=root, image=bg_image)
bg_label.pack()

frame = custom.CTkFrame(master=bg_label, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# Create and place labels and entry widgets
username_label = custom.CTkLabel(
    master=frame, text="Enter Username:", font=("Century Gothic", 20)
)
username_label.place(x=50, y=45)
username_entry = custom.CTkEntry(master=frame, width=220, placeholder_text="username")
username_entry.place(x=50, y=110)

password_label = custom.CTkLabel(
    master=frame, text="Password:", font=("Century Gothic", 20)
)
password_label.place(x=50, y=165)
password_entry = custom.CTkEntry(
    master=frame, width=220, placeholder_text="password", show="*"
)  # Show '*' instead of the actual characters
password_entry.place(x=50, y=200)

# Create and place the login button
login_button = custom.CTkButton(
    master=frame, width=220, text="Login", corner_radius=6, command=button_function
)
login_button.place(x=50, y=240)


# Start the tkinter event loop
root.mainloop()
