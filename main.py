import customtkinter as ctk
from tkinter import Canvas

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Initialize app and set size and title
app = ctk.CTk()
app.geometry("400x400")
app.title("Modern Login UI using CustomTkinter")

# Create canvas for moving element
canvas = Canvas(app, width=400, height=400)
canvas.pack()

# Create moving element
x = 50
y = 50
element = canvas.create_oval(x, y, x+50, y+50, fill="red")

# Function to update position of element
def move_element():
    global x, y
    x += 5
    y += 5
    canvas.coords(element, x, y, x+50, y+50)
    app.after(100, move_element)

# Schedule move_element function to be called after 100ms
app.after(100, move_element)

# Run app
app.mainloop()
