# --- MODULES USED ---
# 1. tkinter --> For GUI
# 2. json --> For storing timetable data temporarily
# 3. datetime --> For validating time format

import tkinter as tk
from tkinter import messagebox
import datetime                           # Used to check correct HH:MM format

# Function: validate_time
# Purpose: Checks whether the user enters time correctly

def validate_time(time_str):
    """Validate time in HH:MM format."""
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

# Function: save_timetable
# Purpose: Saves one timetable entry entered by the user

def save_timetable():
    day = day_var.get()                                       # Selected day from dropdown
    subject = subject_entry.get()                             # Subject typed by user
    start = start_entry.get()                                 # Start time typed by user
    end = end_entry.get()                                     # End time typed by user

# Check if any field is empty
    if not (subject and start and end):
        messagebox.showerror("Error", "All fields must be filled!")
        return

# Validate both start and end time
    if not (validate_time(start) and validate_time(end)):
        messagebox.showerror("Error", "Time must be in HH:MM format!")
        return

# Store each entry in a dictionary
    entry = {"day": day, "subject": subject, "start": start, "end": end}
    timetable.append(entry)

    messagebox.showinfo("Saved", f"Timetable entry added for {day}.")
    # Clear the entry fields after saving
    subject_entry.delete(0, tk.END)
    start_entry.delete(0, tk.END)
    end_entry.delete(0, tk.END)

# Function: show_timetable
# Purpose: Displays all saved timetable entries

def show_timetable():
    if not timetable:
        messagebox.showwarning("Empty", "No timetable entries found!")
        return

    output = "Your Timetable:\n\n"
# Loop through all saved entries and format output
    for t in timetable:
        output += f"{t['day']} - {t['subject']} | {t['start']} to {t['end']}\n"
# Show the final timetable using messagebox
    messagebox.showinfo("Timetable", output)

# GUI SECTION
# Creating the main window

root = tk.Tk()
root.title("Student Timetable Manager")
root.geometry("400x400")
root.config(bg="#e7f0fe")# Light background color

# Application heading
header = tk.Label(root, text="Enter Your Timetable", font=("Arial", 16, "bold"), bg="#e7f0fe")
header.pack(pady=10)

# This list will store all saved timetable entries
timetable = []

# Dropdown menu for selecting day
day_var = tk.StringVar(value="Monday")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_menu = tk.OptionMenu(root, day_var, *days)
day_menu.pack(pady=5)

# Input field for subject
subject_entry = tk.Entry(root, width=30)
subject_entry.insert(0, "Subject")
subject_entry.pack(pady=5)

# Input field for start time
start_entry = tk.Entry(root, width=30)
start_entry.insert(0, "Start Time (HH:MM)")
start_entry.pack(pady=5)

# Input field for end time
end_entry = tk.Entry(root, width=30)
end_entry.insert(0, "End Time (HH:MM)")
end_entry.pack(pady=5)

# Button: Save timetable entry
save_btn = tk.Button(root, text="Save Entry", command=save_timetable, bg="#4caf50", fg="white")
save_btn.pack(pady=10)

# Button: Show timetable
show_btn = tk.Button(root, text="Show Timetable", command=show_timetable, bg="#2196f3", fg="white")
show_btn.pack(pady=5)

root.mainloop()