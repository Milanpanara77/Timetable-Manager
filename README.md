# Student Timetable Manager (Python GUI Application)

A simple and user-friendly desktop application built using Python and Tkinter that helps students store and view their daily class timetable.
This project allows users to select a day, enter the subject name, and input start & end times.
All entries are displayed in a clean popup window when requested.

🚀 **Project Overview

The Student Timetable Manager is designed to make timetable management easier for students.
Instead of writing schedules manually, this application provides a Graphical User Interface (GUI) where users can enter their timetable quickly and accurately.

The program validates the time format using the datetime module and ensures that users do not leave any fields empty.
This makes the system reliable and error-free.

🧩 Features

Easy-to-use Tkinter-based GUI

Dropdown menu for selecting the day

Input fields for:

Subject

Start Time (HH:MM)

End Time (HH:MM)

Time input validation using datetime

Error messages for wrong formats or empty fields

Display full timetable in a popup message box

Clean and lightweight program

🛠️ Technologies Used
Technology / Module	Purpose
Python 3	Programming language
Tkinter	GUI development
Datetime	Time validation (HH:MM format)
📂 Project Structure
│── main.py           # Main application code
│── README.md         # Project description

▶️ How to Run the Project

Install Python 3 on your system.

Download or clone this repository.

Open the folder in your editor (VS Code / PyCharm / IDLE).

Run the program using:

python main.py


The GUI window will open automatically.

🧪 Testing

This application has been tested for:

Blank input fields

Invalid time formats (e.g., 99:99, 7PM, 12.30)

Continuous addition of multiple entries

Viewing complete timetable

GUI behavior and button clicks

All tests passed successfully.

💡 Future Enhancements

Add save/load feature using JSON or CSV

Ability to edit and delete entries

Weekly timetable view

Dark mode theme

Export timetable as PDF or Excel

Add calendar integration

👨‍🎓 submited by
Milan Panara

Registration Number: 25BAI10042
