
# Distinctiveness and Complexity
An application like this was not covered in the course as such I decided to go with this idea as I myself currently work in a manpower office. This is not a social media or e commerce website. I also have multiple models inside: users (Inherited), leaves, projects and to do items. This fulfills the at least one model of the requirement. All data is stored using django and javascript is utilised heavily on the front-end especially for the calendar section, searching through employees and projects, apply leave and approving leave as well. Hence, I believe it fulfills this critera.Lastly, as demonstrated in the video the entier webpage is mobile responsive by using developer tools and switching to an iphoneXR display.

This is a HR application built entirely by me from the ground up. I would first like to elaborate on the aims of this application; namely I wanted to create an application that 1. Had an address book that allowed users to find others in their organisation and send them and email. 2. Had a project manager and team calendar that allowed users to see any upcoming deadlines or submissions and clear the projects that were done. 3. Create a leave system that allowed users to apply for and track not only their own leaves but their colleagues leaves as well, I also wanted to create an approval system for the leaves.

The use of javascript to dynamicallly render a calendar, fetch projects and display them in html was something that was not covered in the course, I would say this is the highlight of my application and what makes it the most unique as I did not see many calendar or date based applications in other projects. Morevover, certain CSS effects such as the hover effect on images and the use of SCSS were also things I am doing for the first time, displaying that there was an active attempt to go beyond the foundations laid by the course instead of simply copying previous projects. It is for these reasons that I belive this project satisfies the distinctiveness and complexity requirements.

# In each file
I will be skipping over the inherited files from django that I did not change. 
1. In models.py you can see the additional models that I have created. These being: leaves, employeestatus ,todoitems and tasks. All models reference django's in built user model. Each leave has a leavdate, leave status and the user that is applying for the leave. Employeestatus contains addidtional user data such as their profile picture, leavenumber and their role in the company. todolist is a more simple model which just stores a task that a user wants to do, this is for more informal individual productivity. Lastly, the tasks model contains information on projects such as the title, duedate, the status of the project and which users are stakeholders in the task.
2. In views.py there are several functions. login, logout and register are standard functions that redirect users to their respective templates and checks throguh the form data, creating / logging in a user if valid. home redirects the user to the homepage where the user is able to navigate between the 3 main HR functions of the application. It also displays the projects due in the coming week as well as any to do list items that the user has inputed for their own reference. employees allows users to view other employee data like an address book. project,get project, addprojcect and markasdone allow the users to view, add and mark projects as completed. similarly, viewleaves, approve, applyleave give users the ability to see their leaves, have leaves approved by their boss and apply leaves. viewleaves also helps to manage between leaves that were taken and never taken, if a leavdate was passed but never approved, the application will delete the leave entry and restore the user's leavecount. Applyleave similarly will adjust the leaves number under the employeestatus model when a leave object is created for that user; it also accepts the case where leaves are unapproved. 
3. HR.js provides the frontend functions such as calendar, which helps to dynamically generate a calendar with dates in the correct weekday slots (this took quite long to learn so I am satisfied I did it) as well as other functions which fetch data from the database. The function of changemonth, chnages the dates in the JS file and re renders the calendar, allowign us to see the correct date data for other months beyond just the current one. There are also in built JS for files like leave.HTML that ensures users cannot input a date beyond the cureent year AND before the current date (today).
4. URLS.py contain all the relevant paths needed for the application. Most are for display purposes buy for markasdone, addtodo, removetodo, approve and remvoe these include an id so that the function they are linked to will take the id as input so they know which object to ammend
5. HR.css / HR.scss contain the css that makes the website look less basic. 
6. Meida and meida/images store the profile pictures of users
7. HTML files:
⋅⋅*layout.html - standard html layout inherited by other html files. Contains navbar and javascript files
⋅⋅*employees.html - View of all other employees
⋅⋅*home.html - Homepage view with link to other applications
⋅⋅*leave.html - leave view with drop down form for people to apply leave.
⋅⋅*projects.html - projects view with dynamically generated calendar. Table of all unfinished tasks and a drop down form to add more.



# How to run your application.
Ideally this application would be used by a team of people. To use it simply use manage.py runserver to run the application. Create a few users and use the admin page to update any of their statuses to boss (at least one boss is neccessary) and go ahead and start planning, putting tasks in the calendar and applying leaves!

# Any other additional information the staff should know about your project.
NIL
