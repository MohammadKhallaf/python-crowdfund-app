from authentication.login import login_user
from authentication.register import register_user
from projects.create import create_project
from projects.delete import delete_project
from projects.edit import edit_project
from projects.search import search_projects
from projects.view import view_projects
from validations import validate_input_string_nosb

logged_user_data = []
logged_in = False


# user should register or login
def main_menu():
    global logged_user_data
    global logged_in
    while not logged_in:
        print("\t<======================>\n\t "
              "| welcome to our app |"
              "\n\t<======================>\n")
        response = validate_input_string_nosb("- To login choose ( L )\n"
                                              "- To Register choose (R)\n")
        if response in "lL":
            logged_user_data = login_user()
            print("<======Logged in======>")
            if logged_user_data:
                logged_in = True
        elif response in "rR":
            register_user()
        else:
            # other function
            print("Bye !")
            return

    # Choose from list {if logged in}
    print("Hello dear, now you can enter the app")
    second_response = validate_input_string_nosb("What do you want now?\n"
                                                 "\t- create new project\t\t=> C\n"
                                                 "\t- view current projects\t\t=> V\n"
                                                 "\t- edit your projects\t\t=> E\n"
                                                 "\t- search for a specific project\t=> S\n"
                                                 "\t- delete a project of yours\t=> D\n"
                                                 "\t- quit the app => q\n\t")
    apply_fn(second_response)

    answer = input("go to main menu again?\t")
    if answer in "yY":
        main_menu()


def apply_fn(choice):
    if choice in "cC":
        print("")
        create_project(logged_user_data)
    elif choice in "vV":
        print("")
        view_projects(logged_user_data)
    elif choice in "eE":
        print("")
        edit_project(logged_user_data)
    elif choice in "sS":
        print("")
        search_projects()
    elif choice in "dD":
        print("")
        delete_project(logged_user_data)
    elif choice in "qQ":
        quit()
    else:
        print("please choose a right value from the menu !")
        main_menu()
    print("-" * 5)
    answer = input("apply same function again?\t")
    if answer in "yY":
        apply_fn(choice)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_menu()
