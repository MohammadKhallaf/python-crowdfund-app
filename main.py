from authentication.login import login_user
from authentication.register import register_user
from projects.create import create_project
from projects.delete import delete_project
from projects.edit import edit_project
from projects.search import search_projects
from projects.view import view_projects
from validations import validate_input_string_nosb


# user should register or login
def main_menu():
    logged_user_data = []
    print("\t<======================>\n\t "
          "| welcome to our app |"
          "\n\t<======================>\n")
    response = validate_input_string_nosb("- To login choose ( L )\n"
                                          "- To Register choose (R)\n")
    if response in "lL":
        logged_user_data = login_user()
    elif response in "rR":
        register_user()
    else:
        # other function
        print("Bye !")
        return  # TODO: this should be changed

    # TODO: user should be able to see this if only logged in
    print("Hello dear, now you can enter the app")
    second_response = validate_input_string_nosb("What do you want now?\n"
                                                 "\t- create new project\t\t=> C\n"
                                                 "\t- view curretn projects\t\t=> V\n"
                                                 "\t- edit your projects\t\t=> E\n"
                                                 "\t- search for a specifi project\t=> S\n"
                                                 "\t- delete a project of yours\t=> D\n")
    if second_response in "cC":
        create_project(logged_user_data)
    elif second_response in "vV":
        view_projects()
    elif second_response in "eE":
        edit_project()
    elif second_response in "sS":
        search_projects()
    elif second_response in "dD":
        delete_project(logged_user_data)
    else:
        print("please choose a right value from the menu !")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_menu()
