import easygui

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

# Nested dictionary that contains all of the information for the team
# members.
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
    if input == None:
        menu()
    else:
        return True

def title_to_task_id(task_titles, chosen_task):
    """A function that converts a chosen task title to its
    corresponding task id."""

    task_id_num = 1

    check = True

    while check == True:
        for i in task_titles:
            if i != chosen_task:
                task_id_num += 1               
            else:
                check = False
                break

    task_id = f"T{task_id_num}"

    return task_id

def menu():
    """A function which contains the menu for the program. The user can 
    choose to add a new task, update an exsiting task, search for a team
    member or task, generate a summary report, or ouput the task 
    collection."""
    options = {
        "Add Task" : add_task,
        "Update Task" : update_task,
        "Search" : search_menu,
        "Generate Report" : generate_report,
        "Output Tasks" : output_tasks,
        "Quit" : quit
    }

    menu_choices = []

    for key in options:
        menu_choices.append(key)

    title = "Task Managment System - Menu"
    user_choice = easygui.buttonbox("What would you like to do?", title, \
    choices = menu_choices)

    if user_choice == None:
        quit()

    function = options[user_choice]()

def add_task():
    """This is a function that allows the user to add a task to the task
    dictionary. It asks the user for the tasks title, description, 
    assignee, priority, status, and adds an automatic sequential task
    ID to the task."""
    task_count = 1
    for key in task_dictionary:
        task_count += 1
    
    task_id = (f"T{task_count}")

    title = "Task Managment System - Add Task"

    status_list = ["In Progress", "Blocked", "Not Started"]

    assignee_list = ["JSM", "JLO", "BDI", "None"]

    task_title = easygui.enterbox(f"Please enter the title of the task", title)
    query_cancel(task_title)

    task_description = easygui.enterbox(f"Please enter the description for \
{task_title}", title)
    query_cancel(task_description)

    task_assignee = easygui.buttonbox(f"Please enter the assignee for \
{task_title}", title, choices = assignee_list)
    query_cancel(task_assignee)

    task_priority = easygui.integerbox(f"Please enter the priority for \
{task_title} from 1-3", title, lowerbound=1, upperbound=3)
    query_cancel(task_priority)

    task_status = easygui.buttonbox(f"Please enter the status for \
{task_title}", title, choices = status_list)
    query_cancel(task_status)
    
    task_dictionary[task_id] = {
        "Title" : task_title,
        "Description" : task_description,
        "Assignee" : task_assignee,
        "Priority" : task_priority,
        "Status" : task_status
    }

    team_member_dictionary[task_assignee]["Tasks Assigned"].append(task_id)
    
    menu()

def output_tasks():
    """This is a function which prints all of the tasks in a readable
    format in an easygui message box."""

    output = ""

    for task_id, content in task_dictionary.items():
        output += f"\nTask ID: {task_id}\n"

        for key in content:
            output += f"    {key}: {content[key]}\n"

    easygui.msgbox(output, title = "Output all Tasks")

    menu()

def update_task():
    """This function will allow the user to update a task. They will
    be able to update the tasks status, assign a team member to a task,
    and when a tasks status is complete, it should automatically be
    removed from the team members task list."""

    task_titles = []

    for task_id, titles in task_dictionary.items():
        task_titles.append(titles["Title"])

    task_choice = easygui.buttonbox("What task would you like to update \
a detail of?", "Update Task", task_titles)
    query_cancel(task_choice)

    task_id = title_to_task_id(task_titles, task_choice)

    task_info = []

    for task_information in task_dictionary[task_id]:
        task_info.append(task_information)

    edit_choice = easygui.buttonbox(f"What detail of {task_choice} \
would you like to edit?", "Edit Choice", task_info)
    query_cancel(edit_choice)

    assignee_list = ["JSM", "JLO", "BDI", "None"]

    status_list = ["Completed", "In Progress", "Blocked", "Not Started"]

    if edit_choice == "Assignee":
        old_assignee = task_dictionary[task_id]["Assignee"]

        task_dictionary[task_id][edit_choice] = easygui.buttonbox(f"Please \
select the new assignee for {task_choice}", "Update Assignee", \
choices = assignee_list)
        query_cancel(task_dictionary[task_id][edit_choice])

        team_member_dictionary[old_assignee]["Tasks Assigned"].remove(task_id)

        team_member_dictionary[task_dictionary[task_id][edit_choice]]\
        ["Tasks Assigned"].append(task_id)
        print(team_member_dictionary)

    elif edit_choice == "Priority":
        task_dictionary[task_id][edit_choice] = easygui.integerbox(f"Please \
enter the updated priority for {task_choice} from 1 - 3", title = \
"Update Priority", lowerbound = 1, upperbound = 3)
        query_cancel(task_dictionary[task_id][edit_choice])

    elif edit_choice == "Status":
        task_dictionary[task_id][edit_choice] = easygui.buttonbox(f"Please \
select the updated status for {task_choice}", title = "Update Status", \
choices = status_list)
        query_cancel(task_dictionary[task_id][edit_choice])

    elif edit_choice == "Title":
        task_dictionary[task_id][edit_choice] = easygui.enterbox(f"Please \
enter the new title for {task_choice}", title = "Update Title")
        query_cancel(task_dictionary[task_id][edit_choice])

    else:
        task_dictionary[task_id][edit_choice] = easygui.enterbox(f"Please \
enter the new description for {task_choice}", title = "Update Description")
    query_cancel(task_dictionary[task_id][edit_choice])

    if task_dictionary[task_id][edit_choice] == "Completed":
        task_assignee = task_dictionary[task_id]["Assignee"]
        task_dictionary[task_id]["Assignee"] = "None"
        if task_assignee == "None": 
            pass
        else:
            team_member_dictionary[task_assignee]["Tasks Assigned"]\
                .remove(task_id)

        print(team_member_dictionary)

    menu()

def search_menu():
    """This is the menu for the search function, where the user is able
    to decide if they would like to search for a task or a team
    team member."""
    task_titles = []

    members = []

    for task_id, titles in task_dictionary.items():
        task_titles.append(titles["Title"])

    for team_member in team_member_dictionary:
        members.append(team_member)

    memb_or_task = easygui.buttonbox("Would you like to search by a team \
member or a task title?", choices = ["Team Member", "Task Title"], \
title = "Search")
    query_cancel(memb_or_task)

    if memb_or_task == "Task Title":
        search_task(task_titles)
    else:
        search_member()
        

def search_task(task_titles):
    """This function allows the user to search for a task by
    choosing the title of the task they want to search for, then
    they should see an easygui message box with all of the tasks
    information."""
    chosen_task = easygui.buttonbox("What task would you like to search \
for?", choices = task_titles, title = "Search for task")
    query_cancel(chosen_task)

    task_id = title_to_task_id(task_titles, chosen_task)
    print(task_id)

    for key, content in task_dictionary.items():
        if task_id == key:
            msg = f"Title: {content['Title']}\n"
            msg += f"Description: {content['Description']}\n"
            msg += f"Assignee: {content['Assignee']}\n"
            msg += f"Priority: {content['Priority']}\n"
            msg += f"Status: {content['Status']}\n"

    easygui.msgbox(msg, title = f"Task ID: {task_id}")

    menu()

def search_member():
    """This function allows the user to search for a team member by
    choosing the name of the team member they want to search for, then
    they should see an easygui message box with all of the team members
    details."""
    chosen_member = easygui.buttonbox("Which team member would you \
like to search for?",choices = ["John Smith", "Jane Love", "Bob Dillon"], \
title = "Search for Team Member")
    query_cancel(chosen_member)

    for assignee_code, content in team_member_dictionary.items():
        if content["Name"] == chosen_member:
            msg = f"Member ID: {assignee_code}\n"
            msg += f"Name: {content['Name']}\n"
            msg += f"Email: {content['Email']}\n"
            msg += f"Tasks Assigned: {content['Tasks Assigned']}\n"

    easygui.msgbox(msg, title = chosen_member)

    menu()

def generate_report():
    """This is a function which generates a report for the status' for
    all of the tasks, including the number of tasks completed, in 
    progress, blocked, and not started."""
    completed_tasks = 0
    in_progress_tasks = 0
    blocked_tasks = 0
    not_started_tasks = 0


    for key, details in task_dictionary.items():
        if  details['Status'] == "Completed":
            completed_tasks += 1
        elif details['Status'] == "In Progress":
            in_progress_tasks += 1
        elif details['Status'] == "Blocked":
            blocked_tasks += 1
        elif details['Status'] == "Not Started":
            not_started_tasks += 1

    msg = f"Tasks Completed: {completed_tasks}\n"
    msg += f"Tasks in Progress: {in_progress_tasks}\n"
    msg += f"Tasks Blocked: {blocked_tasks}\n"
    msg += f"Tasks Not Started: {not_started_tasks}"

    easygui.msgbox(msg, title = "Project's Progress Report")

    menu()

menu()