# Importing the easygui module
import easygui

# This dictionary holds all of the tasks with their details, organized 
# by unique task IDs. Each task contains information like Title, 
# Description, Assignee, Priority, and Status.
task_dictionary = {
    "T1" : {
        "Title" : "Design Homepage",
        "Description" : "Create a mockup of the homepage",
        "Assignee" : "JSM",
        "Priority" : 3,
        "Status" : "In Progress"
    },
    "T2" : {
        "Title" : "Implement Login page",
        "Description" : "Create the Login page for the website",
        "Assignee" : "JSM",
        "Priority" : 3,
        "Status" : "Blocked"
    },
    "T3" : {
        "Title" : "Fix navigation menu",
        "Description" : "Fix the navigation menu to be more user-friendly",
        "Assignee" : "None",
        "Priority" : 1,
        "Status" : "Not Started"
    },
    "T4" : {
        "Title" : "Add payment processing",
        "Description" : "Implement payment processing for the website",
        "Assignee" : "JLO",
        "Priority" : 2,
        "Status" : "In Progress"
    },
    "T5" : {
        "Title" : "Create an About Us page",
        "Description" : "Create a page with information about the company",
        "Assignee" : "BDI",
        "Priority" : 1,
        "Status" : "Blocked"
    }
}

# This dictionary contains the details for each team member.
# It is structured so that each member is referenced by a unique code.
# The information includes their name, email, and tasks assigned.
team_member_dictionary = {
    "JSM" : {
        "Name" : "John Smith",
        "Email" : "John@techvision.com",
        "Tasks Assigned" : ["T1", "T2"]
    },
    "JLO" : {
        "Name" : "Jane Love",
        "Email" : "Jane@techvision.com",
        "Tasks Assigned" : ["T4"]
    },
    "BDI" : {
        "Name" : "Bob Dillon",
        "Email" : "Bob@techvision.com",
        "Tasks Assigned" : ["T5"]
    }
}

def query_cancel(input):
    """This function makes it so when the user presses the x in the top
    right corner of any easygui input box, it takes them back to the
    menu, unless they are already in the menu, where it would just 
    quit the program."""
    # This block checks if the input is None, meaning the user has 
    # canceled. If so, it returns the user to the menu.
    if input == None:
        menu()
    else:
        # If the input is not None, the function returns True and 
        # continues.
        return True

def title_to_task_id(task_titles, chosen_task):
    """A function that converts a chosen task title to its
    corresponding task id, and saves the task id under a variable
    called "task_id, which it returns."""

    # makes the task ID number to 1. This will be increase by 1 as 
    # we check task titles.
    task_id_num = 1

    # Set a check variable to control the loop for finding the correct 
    # task.
    check = True

    # This while loop iterates through the titles to match the chosen 
    # task. It increases the task_id_num by 1 until it finds the correct 
    # title.
    while check == True:
        for i in task_titles:
            if i != chosen_task:
                task_id_num += 1               
            else:
                check = False
                break

    # Constructs the task ID string using the final task_id_num.
    task_id = f"T{task_id_num}"

    # Returns the generated task ID for the chosen task.
    return task_id

def string_checker(prompt, title):
    """This function checks whether the user's input is a valid string 
    and not a blank string so that it can be properlly handled."""
    while True:
        user_input = easygui.enterbox(prompt, title)
        query_cancel(user_input)
        if user_input.strip() == "":
            easygui.msgbox("Invalid Input. Enter a valid string", title = 
            "Enter Valid Input")
        else:
            return user_input

def quit_program():
    """When the user presses the quit button in the main menu, the 
    program will display an easygui message box with the prompt
    "Goodbye!" then after the user presses OK or the X in the top right,
    the program will close."""
    # the program displays an easygui message box with the prompt 
    # "Goodbye!", then after the user clicks OK or the X in the top 
    # right, the program will close.
    easygui.msgbox("Goodbye!", title = "Quit")
    quit()

def menu():
    """A function which contains the main menu for the program. The 
    user can choose to add a new task, update an exsiting task, search
    for a team member or task, generate a summary report, ouput all of 
    the tasks, or quit the program."""
    # This dictionary maps the main menu's options to their 
    # corresponding functions.
    options = {
        "Add Task" : add_task,
        "Update Task" : update_task,
        "Search" : search_menu,
        "Generate Report" : generate_report,
        "Output Tasks" : output_tasks,
        "Quit" : quit_program
    }

    # Creates an empty list to store the menu choices for their display
    # to later be used through an easygui buttonbox.
    menu_choices = []

    # This for loop apppens to the menu choices list 
    # based on the available options in the main menu.
    for key in options:
        menu_choices.append(key)

    # Sets the title for the menu and presents the options to the user
    # through an easygui button box.
    title = "Task Managment System - Menu"
    user_choice = easygui.buttonbox("What would you like to do?", title, \
    choices = menu_choices)

    # Calls the function associated with the user's choice.
    if user_choice != None:
        function = options[user_choice]()
    # If the user cancels the menu by clicking the X in the top right, 
    # the program calls the quit_program function.
    else:
        quit_program()

def add_task():
    """This is a function that allows the user to add a task to the task
    dictionary. It asks the user for the tasks title, description,
    assignee, priority, status, and adds an automatic sequential task
    ID to the task."""
    # Initializes the task counter for assigning a new ID.
    task_count = 1
    for key in task_dictionary:
        task_count += 1
    
    # Generates the task ID using the task counter.
    task_id = (f"T{task_count}")

    # List of possible statuses that can be selected for a new task.
    status_list = ["In Progress", "Blocked", "Not Started"]

    # List of possible assignees including "None".
    assignee_list = ["JSM", "JLO", "BDI", "None"]

    # Prompts the user to enter the title for the new task through an 
    # easygui enterbox. If they enter nothing, they see a message box
    # asking them to enter a title, then it brings them back to the 
    # enter a title enter box.
    task_title = string_checker("Please enter the title of the task", \
    "Add Task - Title")

    # Prompts the user to enter a description for the new task
    # through an easygui enterbox. If they enter nothing, they see a 
    # message box asking them to enter a description, then it brings 
    #them back to the enter a description enter box.

    task_description = string_checker(f"Please enter the description for \
{task_title}", "Add Task - Description")

    # Asks the user to select an assignee for the new task 
    # from the list of assignees, through an easygui buttonbox.
    task_assignee = easygui.buttonbox(f"Please enter the assignee for \
{task_title}", title = "Add Task - Assignee", choices = assignee_list)
    query_cancel(task_assignee)

    # Prompts the user to enter the priority of the new task 
    # (boundaries between 1 and 3), through an easygui integerbox.
    task_priority = easygui.integerbox(f"Please enter the priority for \
{task_title} from 1-3", title = "Add Task - Priority", lowerbound=1, \
    upperbound=3)
    query_cancel(task_priority)

    # Asks the user to select the status of the new task.
    # through an easygui buttonbox.
    task_status = easygui.buttonbox(f"Please enter the status for \
{task_title}", title = "Add Task - Status", choices = status_list)
    query_cancel(task_status)
    
    # Adds the new task to the task_dictionary using the generated 
    # task ID.
    task_dictionary[task_id] = {
        "Title" : task_title,
        "Description" : task_description,
        "Assignee" : task_assignee,
        "Priority" : task_priority,
        "Status" : task_status
    }

    # Adds the new task to the assigned team member's task list.
    if task_assignee == "None":
        pass
    else:
        team_member_dictionary[task_assignee]["Tasks Assigned"].append(task_id)
    
    # Returns the user to the main menu after adding the task.
    menu()

def output_tasks():
    """This is a function which prints all of the tasks in a readable
    format in an easygui message box."""
    # This is the output string that will hold all task details.
    output = ""

    # This for loop iterates over all tasks and adds their details to 
    # the output string.
    for task_id, content in task_dictionary.items():
        output += f"\nTask ID: {task_id}\n"

        for key in content:
            output += f"    {key}: {content[key]}\n"

    # Displays the entire output in an easygui message box.
    easygui.msgbox(output, title = "Output All Tasks")

    # Returns the user to the main menu after outputting all tasks.
    menu()

def update_task():
    """This function will allow the user to update a task. They will
    be able to update the tasks status, assign a team member to a task,
    and when a tasks status is complete, it should automatically be
    removed from the team members task list."""
    # Creates a list to store all task titles for selection.
    task_titles = []

    # Populates the list with the titles from all tasks.
    for task_id, titles in task_dictionary.items():
        task_titles.append(titles["Title"])

    # Prompts the user to select which task to update through an
    # easygui buttonbox.
    task_choice = easygui.buttonbox("What task would you like to update \
a detail of?", "Update Task", task_titles)
    query_cancel(task_choice)

    # Converts the chosen task title back to its corresponding task ID.
    task_id = title_to_task_id(task_titles, task_choice)

    # Creates a list of all editable fields for the chosen task.
    task_info = []

    for task_information in task_dictionary[task_id]:
        task_info.append(task_information)

    # Asks the user which detail of the task they would like to edit
    # through an easygui buttonbox.
    edit_choice = easygui.buttonbox(f"What detail of {task_choice} \
would you like to edit?", "Edit Choice", task_info)
    query_cancel(edit_choice)

    # List of possible assignees and statuses to select from.
    assignee_list = ["JSM", "JLO", "BDI", "None"]
    status_list = ["Completed", "In Progress", "Blocked", "Not Started"]

    # If the user chooses to edit the assignee, prompts them to select 
    # a new assignee through an easygui buttonbox.
    if edit_choice == "Assignee":
        old_assignee = task_dictionary[task_id]["Assignee"]
        new_assignee = easygui.buttonbox(f"Please \
select the new assignee for {task_choice}", "Update Assignee", \
choices = assignee_list)
    # If they click the X in the top right and so their input is None,
    # nothing happens, if they do click a new assignee, it will append
    # the new assignee to the task dictionary.
        if new_assignee != None:
            task_dictionary[task_id][edit_choice] = new_assignee
        query_cancel(new_assignee)

        # Removes the task from the old assignee's tasks assigned list, 
        # unless there wasn't an old assignee ("None").
        if old_assignee == "None":
            pass
        else:
            team_member_dictionary[old_assignee]["Tasks Assigned"]\
            .remove(task_id)

        # Adds the task to the new assignee's tasks assigned list, 
        # unless the new assignee is "None"
        if task_dictionary[task_id][edit_choice] == "None":
            pass
        else:
            team_member_dictionary[task_dictionary[task_id][edit_choice]]\
            ["Tasks Assigned"].append(task_id)

    # If the user chooses to edit the priority, the program prompts 
    # for a new priority value through an easygui integerbox.
    elif edit_choice == "Priority":
        task_dictionary[task_id][edit_choice] = easygui.integerbox(f"Please \
enter the updated priority for {task_choice} from 1 - 3", title = \
"Update Priority", lowerbound = 1, upperbound = 3)
        query_cancel(task_dictionary[task_id][edit_choice])

    # If the user chooses to update the status, prompts them to select 
    # a new status through an easygui buttonbox.
    elif edit_choice == "Status":
        new_status = easygui.buttonbox(f"Please \
select the updated status for {task_choice}", title = "Update Status", \
choices = status_list)
    # If they click the X in the top right and so their input is None,
    # nothing happens, if they do click a new status, it will append
    # the new status to the task dictionary.
        if new_status != None:
            task_dictionary[task_id][edit_choice] = new_status
        query_cancel(new_status)

    # If the user chooses to update the title, prompts them for the 
    # new title through an easygui enterbox. If they enter nothing, they
    # see a message box asking them to enter a title, then it brings 
    #them back to the enter a title enter box.
    elif edit_choice == "Title":
        task_dictionary[task_id][edit_choice] = string_checker(f"Please \
enter the new title for {task_choice}", "Update Title")

    # For all other cases, in this program it can only be if the user 
    # chooses to update the description, the program prompts them to select 
    # a new status through an easygui buttonbox. If they enter nothing,
    # message box asking them to enter a description, then it brings 
    #them back to the enter a description enter box.
    else:
        task_dictionary[task_id][edit_choice] = string_checker(f"Please \
enter the new description for {task_choice}", "Update Description")

    # If the task status is changed to "Completed", it updates the task 
    # and team member accordingly.
    if task_dictionary[task_id][edit_choice] == "Completed":
        task_assignee = task_dictionary[task_id]["Assignee"]
        task_dictionary[task_id]["Assignee"] = "None"
        if task_assignee == "None": 
            # If the task was already unassigned, do nothing further.
            pass
        else:
            # Otherwise, remove the task from the previous assignee's 
            # list.
            team_member_dictionary[task_assignee]["Tasks Assigned"]\
                .remove(task_id)

    # Returns the user to the main menu after updating the task.
    menu()

def search_menu():
    """This is the menu for the search function, where the user is able
    to decide if they would like to search for a task or a team
    team member."""
    # Creates a list to store task titles for searching.
    task_titles = []

    # Creates a list to store team member codes.
    members = []

    # appens to the list of task titles from all tasks in the 
    # dictionary.
    for task_id, titles in task_dictionary.items():
        task_titles.append(titles["Title"])

    # Populates the members list with team member codes.
    for team_member in team_member_dictionary:
        members.append(team_member)

    # Asks the user whether to search by team member or task title
    # through an easygui buttonbox.
    memb_or_task = easygui.buttonbox("Would you like to search by a team \
member or a task title?", choices = ["Team Member", "Task Title"], \
title = "Search")
    query_cancel(memb_or_task)

    # Calls the appropriate search function based on user choice.
    if memb_or_task == "Task Title":
        search_task(task_titles)
    else:
        search_member()
        

def search_task(task_titles):
    """This function allows the user to search for a task by
    choosing the title of the task they want to search for, then
    they should see an easygui message box with all of the tasks
    information."""
    # Prompts the user to choose the task they want to search for
    # through an easygui buttonbox.
    chosen_task = easygui.buttonbox("What task would you like to search \
for?", choices = task_titles, title = "Search for Task")
    query_cancel(chosen_task)

    # Finds the task ID for the selected task title.
    task_id = title_to_task_id(task_titles, chosen_task)

    # Iterates over all tasks to find the selected one and append its 
    # details.
    for key, content in task_dictionary.items():
        if task_id == key:
            msg = f"Title: {content['Title']}\n"
            msg += f"Description: {content['Description']}\n"
            msg += f"Assignee: {content['Assignee']}\n"
            msg += f"Priority: {content['Priority']}\n"
            msg += f"Status: {content['Status']}\n"

    # Displays the details of the found task in an easygui message box.
    easygui.msgbox(msg, title = f"Task ID: {task_id}")

    # Returns the user to the main menu after displaying the search 
    # result.
    menu()

def search_member():
    """This function allows the user to search for a team member by
    choosing the name of the team member they want to search for, then
    they should see an easygui message box with all of the team members
    details."""
    # Prompts the user to select which team member to search for
    # through an easygui buttonbox.
    chosen_member = easygui.buttonbox("Which team member would you \
like to search for?",choices = ["John Smith", "Jane Love", "Bob Dillon"], \
title = "Search for Team Member")
    query_cancel(chosen_member)

    # Iterates through all team members and appends the selected 
    # member's details.
    for assignee_code, content in team_member_dictionary.items():
        if content["Name"] == chosen_member:
            msg = f"Member ID: {assignee_code}\n"
            msg += f"Name: {content['Name']}\n"
            msg += f"Email: {content['Email']}\n"
            msg += f"Tasks Assigned: {content['Tasks Assigned']}\n"

    # Displays the found member's details in an easygui message box.
    easygui.msgbox(msg, title = chosen_member)

    # Returns the user to the main menu after displaying the team 
    # member details.
    menu()

def generate_report():
    """This is a function which generates a report for the status' for
    all of the tasks, including the number of tasks completed, in 
    progress, blocked, and not started."""
    # Creates counters for each possible task status.
    completed_tasks = 0
    in_progress_tasks = 0
    blocked_tasks = 0
    not_started_tasks = 0

    # Iterates through all tasks and updates the status counters by 
    # adding 1 to each status counter for every corresponding 
    # task found.
    for key, details in task_dictionary.items():
        if  details['Status'] == "Completed":
            completed_tasks += 1
        elif details['Status'] == "In Progress":
            in_progress_tasks += 1
        elif details['Status'] == "Blocked":
            blocked_tasks += 1
        elif details['Status'] == "Not Started":
            not_started_tasks += 1

    # Prepares the report message string to summarize all status counts.
    msg = f"Tasks Completed: {completed_tasks}\n"
    msg += f"Tasks in Progress: {in_progress_tasks}\n"
    msg += f"Tasks Blocked: {blocked_tasks}\n"
    msg += f"Tasks Not Started: {not_started_tasks}"

    # Displays the status report in an easygui message box.
    easygui.msgbox(msg, title = "Project's Progress Report")

    # Returns the user to the main menu after showing the report.
    menu()

# Calls the menu function to start the program, presenting the user 
# with the main menu.
menu()