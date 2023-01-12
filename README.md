# Task-Manager
This program is designed to help small businesses to manage tasks assigned to each member of the team.
# Description
The program allows for the following functionality:

* Login Section:
When the program starts, users are prompted to enter their username and password. These credentials are then validated against a list of stored credentials in the user.txt file. If the provided username and password match those in the user.txt file, the user is granted access to the system. Otherwise, the user is prompted to try again.

* Register User:
Only users with the username "admin" are able to add new users to the system. When the "register user" option is selected from the main menu, the user is prompted to enter a new username and password. The program then verifies that the entered password matches a confirmation of the password before storing the new credentials in the user.txt file.

* Add a task:
Users are able to add a new task to the system by providing information such as the task assignee, title, description, due date, and date assigned. This information is then stored in the tasks.txt file. When the "add a task" option is selected from the main menu, the user is prompted to enter the task assignee, title, description and due date. The date the task was assigned is automatically recorded by the program using the datetime library.

* View all tasks:
Users are able to view all tasks stored in the system by reading from the tasks.txt file. When the "view all tasks" option is selected from the main menu, the program reads through the tasks.txt file, line by line, and prints the task details in a formatted manner.

* View my tasks:
Users are able to view only the tasks that are assigned to them. When the "view my task" option is selected from the main menu, the program reads through the tasks.txt file, line by line, and prints only the task details that are assigned to the currently logged-in user.

* Exit:
Users are able to exit the program at any time by selecting the "exit" option from the main menu.

The program is written in Python and makes use of the datetime library to store the date a task was assigned. The user interface is command-line based and utilizes the input() function for user input and the print() function for output.
