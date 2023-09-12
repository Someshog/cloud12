import tkinter as tk
import time

def update_datetime():
    current_time = time.strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
    current_date = time.strftime("%Y-%m-%d")  # Get the current date in YYYY-MM-DD format
    time_label.config(text=current_time)  # Update the time label text
    date_label.config(text=current_date)  # Update the date label text
    root.after(1000, update_datetime)  # Schedule the update_datetime function to run again after 1000 milliseconds (1 second)

root = tk.Tk()
root.title("Clock")

# Create labels for time and date
time_label = tk.Label(root, text="", font=("Helvetica", 24))
date_label = tk.Label(root, text="", font=("Helvetica", 24))

# Pack the labels
time_label.pack()
date_label.pack()

update_datetime()  # Start updating the time and date

root.mainloop()
