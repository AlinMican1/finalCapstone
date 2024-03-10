# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from datetime import date, datetime

"""
Add a function to register user to user.txt file.
We do not need to return anything, we just want to save this user data onto the file.
We need to pass user_data from the read file so that we can check if the username exists in the file already.
"""


def reg_user(user_data):
    """Add a new user to the user.txt file"""

    # Initiate an array and story all the user names that exist in the file by using split function and splitting from ; as we know that
    # Our file gets saved in the format of username;password, then we only take the 0th index which is the username.
    username_exists = []
    for name in user_data:
        username_exists.append(name.split(";")[0])

    # - Request input of a new username
    new_username = input("New Username: ")

    # - Check if the username already exists in the database (file) by comparing the new_username written with the one from the file.
    # If user name already exists re-ask the user to input a new name.
    while new_username in username_exists:
        print("User name already exists.")
        new_username = input("Please provide a new username: ")
    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

    """
    Add a function to add_task into the task file.
    """


def add_task(username_task):
    """Allow a user to add a new task to task.txt file
    Prompt a user for the following:
    - A username of the person whom the task is assigned to,
    - A title of a task,
    - A description of the task and
    - the due date of the task.
    """

    task_username = input("Name of person assigned to task: ")

    # Add a functionality to check if the username is already in the database if not return and exit the function.
    # For this function im not sure if i should put it in a while loop to keep asking the user until the user
    # writes a valid input, it doesn't say anywhere so i just return.
    if task_username not in username_task:
        print("User does not exist. Please enter a valid username")
        return

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(
                task_due_date, DATETIME_STRING_FORMAT
            )
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    """ Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.
    """

    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False,
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t["username"],
                t["title"],
                t["description"],
                t["due_date"].strftime(DATETIME_STRING_FORMAT),
                t["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t["completed"] else "No",
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


"""
Generate task and user reports
"""


def generate_report():
    # Task overview report
    # Set all the variables we require for the report

    total_tasks = 0
    completed_task_count = 0
    uncompleted_task_count = 0
    overdue_task_count = 0
    percent_uncomplete_tasks = 0
    percent_tasks_overdue = 0
    task_data = []
    # Open the tasks file in read mode
    with open("tasks.txt", "r") as task_file:
        # For loop to read each line
        # Strip each line and split it
        # to turn it into an array
        # so that we can check each index
        # and match it to the array and increment
        # the respected counter, for example
        # if line_data[5] is yes then we increment
        # the completed task
        for line in task_file:
            line_data = line.strip().split(";")
            if line_data[5] == "Yes":
                completed_task_count += 1
            if line_data[5] == "No":
                uncompleted_task_count += 1
            if line_data[3] < line_data[4] and line_data[5] == "No":
                overdue_task_count += 1

            # Form this array so that we can use it in the
            # user report data.
            task_data.append(line_data)
            # keep adding the tasks until the end of for loop
            # this tells us how many tasks we have.
            total_tasks += 1

    # Calculate the percentage of uncomplted and overdue tasks
    percent_uncomplete_tasks = (uncompleted_task_count / total_tasks) * 100
    percent_tasks_overdue = (overdue_task_count / total_tasks) * 100

    # Open a file in w+ mode , this creates a file if it doesnt't exist
    # or writes to the file.
    # We are writing the required data for the report
    with open("task_overview.txt", "w+") as task_report:
        task_report.write(f"Completed Tasks: {completed_task_count}\n")
        task_report.write(f"Uncompleted Tasks: {uncompleted_task_count}\n")
        task_report.write(f"Overdue Tasks: {overdue_task_count}\n")
        task_report.write(
            "Total Uncompleted Tasks Percentage:"
            f" {percent_uncomplete_tasks}%\n"
        )
        task_report.write(
            f"Total Overdue Tasks Completed: {percent_tasks_overdue}%\n"
        )
        task_report.write(f"Total Tasks: {total_tasks}\n")

    # Generate user report

    total_user_task = 0
    completed_user_task = 0
    uncompleted_user_task = 0
    overdue_user_task = 0

    # The reason for removing the user_overview
    # file is because we use append, so to overcome
    # appending lines in the fle every time we run
    # "gr", we remove the file then add all new
    # data to the file but we need to check if the file exists first.
    # so we don't run into errors with file not existing.

    if os.path.isfile("user_overview.txt"):
        os.remove("user_overview.txt")

    # Read the user.txt file to check the users we have
    # and use a nested for loop to go through each user
    # and find how many tasks they have, completed tasks
    # etc.
    with open("user.txt", "r") as user_file:
        for line in user_file:
            for tasks in task_data:
                # We only need the username so we user split to form
                # an array containing the username and password,
                # however we only extract the username from the array
                # using line_data[0] and we check with our tasks
                # where their names is the first element in the task array
                line_data = line.strip().split(";")
                # Check if the current username in the first for loop,
                # is the same as the username in the tasks in the second
                # for loop, and increment the counters accordingly.
                if line_data[0] == tasks[0]:
                    total_user_task += 1
                    if tasks[5] == "Yes":
                        completed_user_task += 1
                    if tasks[5] == "No":
                        uncompleted_user_task += 1
                    if tasks[3] < tasks[4] and tasks[5] == "No":
                        overdue_user_task += 1
            # Start appending to the file in the first for loop as we
            # because we want to do user by user.
            with open("user_overview.txt", "a+") as user_report:
                percent_total_task_to_user = 0
                percent_completed_by_user = 0
                percent_uncompleted_by_user = 0
                percent_overdue_by_user = 0
                # Check if is zero or not so we don't get divide
                # by zero error
                if total_user_task != 0:
                    percent_total_task_to_user = (
                        total_user_task / total_tasks
                    ) * 100

                    percent_completed_by_user = (
                        completed_user_task / total_user_task
                    ) * 100

                    percent_uncompleted_by_user = (
                        uncompleted_user_task / total_user_task
                    ) * 100

                    percent_overdue_by_user = (
                        overdue_user_task / total_user_task
                    ) * 100
                # Use this to write/append to our file.
                user_line = (
                    f"Total Tasks for {line_data[0]} is {total_user_task}\n"
                    " Percent of total number of tasks that have been to"
                    f" {line_data[0]} is {percent_total_task_to_user}%\n"
                    f" Percent of tasks\n assigned to {line_data[0]} that have"
                    f" been completed is {percent_completed_by_user}%\n"
                    f" Percent of tasks assigned to {line_data[0]} that need"
                    f" to be completed is {percent_uncompleted_by_user}%\n"
                    " Percent of tasks that are overdue and not completed by"
                    f" {line_data[0]} is {percent_overdue_by_user}\n"
                    "------------------------------------------------\n"
                )

                user_report.write(user_line)

                # Set everything back to zero so that our
                # counter doesn't carry on for a new user.
                total_user_task = 0
                uncompleted_user_task = 0
                completed_user_task = 0
                overdue_user_task = 0


def helper(all_tasks, user_choice):
    pass


"""
Main idea of this function
is to help the user mark our task
as completed or not based on their 
input.
"""


def mark_completed(all_tasks, user_choice):
    # make an array of user data and so that we
    # can check against the specified task.
    # if all the details in specified task such as the name and title match, then
    # mark as complete.
    # This can be done with an ID for each task, but I'm not sure if im allowed
    # to add more attributes to the tasks.txt file.
    user_data = []
    for line in task_data:
        user_data.append(line.split(";"))

    # Go through the user_data and check if the specified task
    # matches the user_data
    for i in range(len(user_data)):
        if (
            all_tasks[user_choice - 1][1].replace("Assigned to: ", "")
            == user_data[i][0]
            and all_tasks[user_choice - 1][0].replace("Task:  ", "")
            == user_data[i][1]
        ):
            # If it does we add all user data into an updated line
            updated_line = f"{user_data[i][0]};{user_data[i][1]};{user_data[i][2]};{user_data[i][3]};{user_data[i][4]};Yes\n"

            # Open the tasks file and read all lines.
            # so that we are able to compare the lines
            # with the user data
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
            # Now we want to overwrite the tasks.txt file
            # if that certain line is met
            with open("tasks.txt", "w") as file:
                for line in lines:
                    line_parts = line.strip().split(";")
                    # Here we check if the line_parts are the same
                    # as the user data information, this is because
                    # we want to find which line of the file we need
                    # to update so that we don't update all the lines
                    # to completed = yes.

                    if (
                        len(line_parts) == 6
                        and line_parts[0] == user_data[i][0]
                        and line_parts[1] == user_data[i][1]
                        and line_parts[2] == user_data[i][2]
                        and line_parts[3] == user_data[i][3]
                        and line_parts[4] == user_data[i][4]
                        and line_parts[5] == "No"
                    ):
                        file.write(updated_line)
                    else:
                        file.write(line)


"""
This function does the exact same job as the above function
mark_complete(), however we have an extra parameter called new_date
which is passed into our function and changes the date.
"""


def change_date(new_date, all_tasks, user_choice):
    user_data = []
    for line in task_data:
        user_data.append(line.split(";"))

    for i in range(len(user_data)):
        if (
            all_tasks[user_choice - 1][1].replace("Assigned to: ", "")
            == user_data[i][0]
            and all_tasks[user_choice - 1][0].replace("Task:  ", "")
            == user_data[i][1]
        ):
            updated_line = f"{user_data[i][0]};{user_data[i][1]};{user_data[i][2]};{user_data[i][3]};{new_date};{user_data[i][5]}\n"
            print(updated_line)

            with open("tasks.txt", "r") as file:
                lines = file.readlines()

            with open("tasks.txt", "w") as file:
                for line in lines:
                    line_parts = line.strip().split(";")

                    if (
                        len(line_parts) == 6
                        and line_parts[0] == user_data[i][0]
                        and line_parts[1] == user_data[i][1]
                        and line_parts[2] == user_data[i][2]
                        and line_parts[3] == user_data[i][3]
                        and line_parts[4] == user_data[i][4]
                        and line_parts[5] == user_data[i][5]
                    ):
                        file.write(updated_line)
                    else:
                        file.write(line)


def view_mine():
    """Reads the task from task.txt file and prints to the console in the
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    """

    # Set a counter to count the tasks at available for that user and
    # display a nice UI to tell the user which task number it is.
    count = 0
    all_tasks = []

    for t in task_list:
        # Check if the curr_user has a task mapped onto "username"
        # if they don't exit the for loop so we save resources and set no_task to True
        # So that we can later exit the whole function with an if statement.
        # The reason we add 'and count == 0' because we want to check for the
        # first iteration, for example if we don't have the and condition,
        # it will return no_task as true as when we get to the end of the for loop
        # it will execute the if statment.

        # if t["username"] != curr_user and count == 0:
        #     print("\nNo tasks available")
        #     return

        if t["username"] == curr_user:
            # increment the task by one after each iteration.
            count += 1
            print(
                "----------------------------TASK"
                f" {count}-------------------------------\n"
            )
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += (
                "Date Assigned: \t"
                f" {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            )
            disp_str += (
                "Due Date: \t"
                f" {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            )
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            print(
                "--------------------------------------------------------------\n"
            )
            # Append all tasks to an array so we can access the specific task the user wants to access.
            all_tasks.append(
                [
                    f"Task:  {t['title']}",
                    f"Assigned to: {t['username']}",
                    (
                        "Date Assigned:"
                        f" {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}"
                    ),
                    (
                        "Due Date:"
                        f" {t['due_date'].strftime(DATETIME_STRING_FORMAT)}"
                    ),
                    f"Task Description: {t['description']}",
                    f"{t['completed']}",
                ]
            )

    # Ask user to input if they want to view a specific task or return to main menu
    print("ENTER '-1' if you want to return to the main menu: ")

    user_choice = int(
        input(
            f"You have {len(all_tasks)} tasks, enter a number between"
            f" up to {len(all_tasks)} to view a specific task:  "
        )
    )
    loop = True
    repeat = 0
    # If user enters -1 then return.
    if user_choice == -1:
        return

    # Check what task the user what to specifically see,
    # showing them how many they have available so they can make a choice.
    # The logic with 'repeat' variable, is that when the user puts the right
    # answer between 1-len(all_task) then we ask if the user wants to return
    # to the main menu and we set the repeated variable to 1 to re-ask the user
    # to input a number between 1-len(all_tasks), we do this so that when we intially
    # start the while loop we dont ask the user to input a number 1-len(all_task)
    # twice since we ask it in the previous print statement.
    # Then if we enter an invalid number we ask the user to enter
    # a number between 1-len(all_tasks) and set the repeat variable to 0 so we dont ask for two inputs.

    else:
        while loop:
            if repeat == 1:
                user_choice = int(
                    input(
                        f"You have {len(all_tasks)} tasks, enter a number"
                        f" up to {len(all_tasks)} to view a specific task: "
                    )
                )
            if user_choice > 0 and user_choice <= len(all_tasks):
                # Do -1 because array is zero indexed
                print(
                    " -------------------------------------TASK"
                    f" {user_choice}-----------------------------\n"
                    f"\n {all_tasks[user_choice - 1][0]}\n",
                    f"{all_tasks[user_choice - 1][1]}\n",
                    f"{all_tasks[user_choice - 1][2]}\n",
                    f"{all_tasks[user_choice - 1][3]}\n",
                    f"{all_tasks[user_choice - 1][4]}\n",
                    "\n--------------------------------------------------------------------------\n",
                )
                # Ask user if they want to enter a edit menu
                edit_menu = input(
                    "Want to enter edit menu to edit this task? (yes/no): "
                ).lower()

                while edit_menu != "yes" and edit_menu != "no":
                    edit_menu = input(
                        "Want to enter edit menu to edit this task? (yes/no): "
                    ).lower()

                while edit_menu == "yes":
                    print(
                        "-------------------EDIT MENU-------------------\n"
                        "\nEnter 1 To mark this task as complete."
                        "\nEnter 2 To edit the due date of this task."
                        "\nEnter 3 To exit edit menu.\n"
                        "\n------------------------------------------------"
                    )
                    edit_selection = int(input("Enter a number: "))

                    while (
                        edit_selection != 1
                        and edit_selection != 2
                        and edit_selection != 3
                        and edit_selection != 4
                    ):
                        edit_selection = int(
                            input("Please enter a number as stated above: ")
                        )

                    if edit_selection == 1:
                        want_to_mark_as_complete = input(
                            "Do you want to set this task to completed?"
                            " (yes/no) : "
                        ).lower()
                        # Keep asking the user the same question if their input is not
                        # no or yes.
                        while (
                            want_to_mark_as_complete != "yes"
                            and want_to_mark_as_complete != "no"
                        ):
                            want_to_mark_as_complete = input(
                                "Do you want to set this task to completed?"
                                " (yes/no) : "
                            ).lower()

                        # If the user selectes yes to edit then
                        # update the completed from no to yes.

                        if want_to_mark_as_complete == "yes":
                            # Run mark_completed function if we select yes
                            # Pass the parameters all_tasks and user_choice
                            # so we can know which task the user has selected
                            # based on the user choice
                            mark_completed(all_tasks, user_choice)

                    elif edit_selection == 2:
                        # Check if the task is completed
                        # if is not do not allow to change due date
                        if all_tasks[user_choice - 1][5] == "False":
                            # Check if we have the right format of our
                            # new date input
                            while True:
                                new_date = input(
                                    "Insert a new date in the format of"
                                    " (yyyy-mm-dd): "
                                )
                                try:
                                    # Attempt to convert the input to a datetime object
                                    datetime.strptime(new_date, "%Y-%m-%d")
                                    print("Date format is correct!")
                                    break  # Break out of the loop if the format is correct
                                except ValueError:
                                    print(
                                        "Please enter the date in the format"
                                        " (yyyy-mm-dd)"
                                    )
                            # Once we got a new date we pass it to
                            # our change_date function.
                            change_date(new_date, all_tasks, user_choice)
                        else:
                            print("Cannot edit task because is Completed")

                    elif edit_selection == 3:
                        break

                repeat = 1
                want_to_exit = input(
                    "Want to return to the main menu? (yes/no): "
                ).lower()

                # Keep asking the user the same question
                # if their input is not yes or no.
                while want_to_exit != "yes" and want_to_exit != "no":
                    want_to_exit = input(
                        "Want to return to the main menu? (yes/no): "
                    ).lower()

                if want_to_exit == "yes":
                    loop = False
            else:
                user_choice = int(
                    input(
                        f"Please enter a number up to {len(all_tasks)} to view"
                        " a specific task:"
                    )
                )
                repeat = 0

    return


DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", "r") as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []

for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t["username"] = task_components[0]
    curr_t["title"] = task_components[1]
    curr_t["description"] = task_components[2]
    curr_t["due_date"] = datetime.strptime(
        task_components[3], DATETIME_STRING_FORMAT
    )
    curr_t["assigned_date"] = datetime.strptime(
        task_components[4], DATETIME_STRING_FORMAT
    )
    curr_t["completed"] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


# ====Login Section====
"""This code reads usernames and password from the user.txt file to 
    allow a user to login.
"""
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", "r") as user_file:
    user_data = user_file.read().split("\n")
    # Read all usernames from database


# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(";")
    username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    menu = input(
        """Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: """
    ).lower()

    if menu == "r":
        reg_user(user_data)

    elif menu == "a":
        add_task(username_password.keys())

    elif menu == "va":
        """Reads the task from task.txt file and prints to the console in the
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
        """

        for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += (
                "Date Assigned: \t"
                f" {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            )
            disp_str += (
                "Due Date: \t"
                f" {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            )
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)

    elif menu == "vm":
        # First check our current user logged in
        # has a task, we do this by using an array
        # and storing the names of all the people
        # that has a task assigned to them, if our
        # current user does not have a current task assigned
        # to them then, they have no tasks, else view the tasks.
        users = []
        for t in task_data:
            users.append(t.split(";")[0])
        if curr_user not in users:
            print("No tasks available")
        else:
            view_mine()

    # Check if the current user is admin then generate reports.
    elif menu == "gr" and curr_user == "admin":
        generate_report()

    elif menu == "ds" and curr_user == "admin":
        """If the user is an admin they can display statistics about number of users
        and tasks."""
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")

        # Check if the file exists, otherwise generate a report,
        # To generate the files.
        if not os.path.isfile("user_overview.txt") or not os.path.isfile(
            "task_overview.txt"
        ):
            generate_report()

        # Otherwise print the task and user report
        else:
            print(
                "------------------------------------------------TASK"
                " OVERVIEW------------------------------------------------\n"
            )
            with open("task_overview.txt", "r") as task_overview_data:
                print(task_overview_data.read())
            print(
                "----------------------------------------------------"
                "---------------------------------------------------------\n"
            )

            print(
                "------------------------------------------------USER"
                " OVERVIEW-------------------------------------------------\n"
            )
            with open("user_overview.txt", "r") as user_overview_data:
                print(user_overview_data.read())

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
