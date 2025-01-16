# How to run this application.
The following needs to be done before running the application:
pip install pillow
pip install schedule
pip install python-dateutil
pip install django

After which simply run the server locally using python mangage.py


# Introduction
The problem statement we have selected is by the Singapore book council: Develop a cost-effective digital PA system for administrators to efficiently arrange and schedule meetings and automate tasks such as sending follow-up tasks to themselves or others, sending reminders, generating summaries of email threads, and arranging meetings.

# In each file
File Overview
**1. Models (models.py)**
This file contains the additional models for the application:

leaves: Tracks leave dates, statuses, and the user applying for the leave.
employeestatus: Stores additional user data, such as profile pictures, leave count, and their role in the organization.
todoitems: A simple model to store personal to-do list items for individual productivity.
tasks: Tracks project details, including title, due date, status, and stakeholders.
All models reference Django's built-in User model to link data to specific users.

**2. Views (views.py)**
Key functions in the views.py file:

Authentication:
login, logout, register handle user authentication and redirection.
Homepage:
home directs users to the main interface. This page allows navigation between the app's features and displays:
Upcoming project deadlines.
Personal to-do list items.
Employee Management:
employees displays user profiles and allows viewing employee details like an address book.
Task Management:
project, get_project, add_project, mark_as_done manage projects by allowing users to view, create, and complete tasks.
Leave Management:
view_leaves, approve, apply_leave enable users to:
Track leaves.
Apply for new leaves (adjusting the leave count automatically).
Approve or reject leave requests.
Remove outdated or unapproved leave requests.
**3. Frontend Scripts (HR.js)**
This JavaScript file powers the dynamic aspects of the app:

Calendar Functionality:
Generates a calendar dynamically with correct dates and weekday alignments.
Includes the changeMonth function to update calendar views when switching between months.
Form Validations:
Scripts like leave.HTML ensure date inputs are valid, preventing past or out-of-year selections.
4. URL Configurations (urls.py)
Contains all the necessary paths for routing, including:

Display routes for pages like home and employees.
Action routes like mark_as_done, add_todo, remove_todo, approve, and remove. These routes utilize object IDs to modify specific entries in the database.

**5. Stylesheets (HR.css / HR.scss)**
These files contain custom CSS that enhances the visual design of the app and makes the interface user-friendly.
**6. Media Storage**
media/ and media/images/ directories store user-uploaded profile pictures.
**7. Templates (HTML Files)**
layout.html:
A base template with navigation bars and linked JavaScript files.
employees.html:
Displays all employee profiles in a structured format.
home.html:
The homepage that serves as the app's dashboard, linking other functionalities.
leave.html:
A leave application page with dropdown forms.
projects.html:
Features a dynamically generated calendar, a table of unfinished tasks, and a dropdown to add new projects.

# Additional Information
Profile pictures and media files are securely stored under the media directory.
The app ensures dynamic and responsive behavior through the integration of custom JavaScript.
Leave management includes logic for auto-restoring leave counts for unapproved or outdated leave requests.
