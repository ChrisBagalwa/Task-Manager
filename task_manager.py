# This program helps a small business to manage tasks assigned to each member of the team.
# Author: Chris Bagalwa
# 24/05/2022

# Importing libraries
from datetime import datetime
# Login Section
# Read usernames and password from the user.txt file
# Validate credential, and if correct login
user_file = open("user.txt","r")
text = user_file.readlines()
login = False
# Use the while loop to validate the username and password
while login == False:
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    for line in text:
        correct_user, correct_password = map(str.strip,line.split(","))
        if correct_user == username and correct_password == password:
            login = True
            print("Your login details are correct.")
            break
    else:
        print("Your login details are incorrect.")
user_file.seek(0)
# Provide the user with a menu option and convert to lower case
menu = input('''Select one of the following Options below:
r - register user
a - add a task
va - view all tasks
vm - view my task
s - stats
e - Exit
choice: ''').lower()
# If the user enters 'r', do the following:
# Check if the user is admin
# If Yes, allow the user to add the new users's login details
if menu == 'r':
    if username == "admin":
        new_user = False
        users_name = input("Please enter new user's username: ")
        while new_user == False:
            users_password = input("Please enter new user's password: ")
            confirm_password = input("Please confirm new user's password: ")
            if users_password == confirm_password:
                new_user = True
            if users_password != confirm_password:
                print("Password do not match. Enter again")
            if users_password == confirm_password:
                print("Password matches. New user has been created")
                append_me = open("user.txt", "a")
                append_me.write("\n" + str(users_name) + ", " + str(confirm_password))
                append_me.close()
    if username != "admin":
        print("Sorry, only admin user can add a new user.")
# Else if the user enters 'a', do the following:
# Allow the user to add a new task to task.txt file
# Open tasks.txt file and prompt the user to enter the following:
# task_assignee, task_title, task_description, due_date, date_assigned, task_completed
# Then write data to the tasks.txt file
elif menu == 'a':
    tasks = open("tasks.txt","a")
    task_assignee = input("Enter the usersname of assignee: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter task description: ")
    due_date = input("Enter task due date in this format dd-MonthName-yyyy: ")
    date_assigned = datetime.now()
    task_completed = "No"
    tasks.write("\n" + str(task_assignee) + ", " + str(task_title) + ", " + str(task_description) + ", " + str(date_assigned.strftime("%d %b %Y")) + ", " + str(due_date) + ", " + str(task_completed))
    tasks.close()
# Else if the user enters 'va', do the following:
# Read a line from the task.txt file, split that line where there is comma and space
# Then print as per the specified format
elif menu == 'va':
    view_tasks = open("tasks.txt","r+")
    for line in view_tasks:
        task_assignee, task_title, task_description, date_assigned, due_date, task_completed = line.split(", ")
        print(f'''
Assigned to:        {task_assignee}
Task:               {task_title}
Task description:   {task_description}
Date assigned:      {date_assigned}
Due date:           {due_date}
Task complete?:     {task_completed}
''')
    view_tasks.close()
# Else if the user enters 'vm', do the following:
# Read a line from the task.txt file, split that line where there is comma and space
# Check if the username of the person logged in is the same as the username you have read from the file
# If Yes, print the task as per the specified format
elif menu == 'vm':
    view_atask = open("tasks.txt","r+")
    for line in view_atask:
        task_assignee, task_title, task_description, date_assigned, due_date, task_completed = line.split(", ")
        if username == task_assignee:
            print(f'''
Assigned to:        {task_assignee}
Task:               {task_title}
Task description:   {task_description}
Date assigned:      {date_assigned}
Due date:           {due_date}
Task complete?:     {task_completed}
''')
    view_atask.close()
# Else if the user enters 's', do the following:
# Display the total number of tasks and the total number of users as per the specified format
elif menu == "s":
    if username == "admin":
        num_tasks = 0
        num_users = 0
        with open("tasks.txt","r") as task_stats:
            for line in task_stats:
                num_tasks += 1
        print (f"\nTotal number of tasks: {num_tasks}")
        with open("user.txt", "r") as username:
            for line in username:
                num_users += 1
        print (f"Total number of users: {num_users}")
        task_stats.close()
# Else if the user enters 'e', do the following:
# Print 'Goodbye!!!' and exit
elif menu == 'e':
    print('Goodbye!!!')
    exit()
# Else if the user makes a wrong choice from the menu option
# Print 'You have made a wrong choice, Please Try again'
else:
    print("You have made a wrong choice, Please Try again")