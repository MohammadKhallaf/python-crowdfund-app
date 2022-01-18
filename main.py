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
    print("\t<======================>\n\t "
          "| welcome to our app |"
          "\n\t<======================>\n")
    response = validate_input_string_nosb("- To login choose ( L )\n"
                                          "- To Register choose (R)\n")
    if response in "lL":
        login_user()
    elif response in "rR":
        register_user()
    else:
        # other function
        print("Bye !")
        return #TODO: this should be changed

    # TODO: user should be able to see this if only logged in
    print("Hello dear, now you can enter the app")
    second_response = validate_input_string_nosb("What do you want now?\n"
                                                 "\t- create new project\t\t=> C\n"
                                                 "\t- view curretn projects\t\t=> V\n"
                                                 "\t- edit your projects\t\t=> E\n"
                                                 "\t- search for a specifi project\t=> S\n"
                                                 "\t- delete a project of yours\t=> D\n")
    if second_response in "cC":
        create_project()
    elif second_response in "vV":
        view_projects()
    elif second_response in "eE":
        edit_project()
    elif second_response in "sS":
        search_projects()
    elif second_response in "dD":
        delete_project()
    else:
        print("please choose a right value from the menu !")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_menu()

# def main_menu():
#     fun_names = ["Build Array", "Fiz-Buz", "Reverse String", "User Details", "Find the Longest sub string","Calculations","Guess the word"]
#     print("="*5, "> Hi User <", "="*5)
#     print("Choose function to execute:")
#     c = 0
#     for fn in fun_names:
#         c += 1
#         print(f"\t{c}- {fn}")
#
#     choice = input(">\t")
#     if choice.isdigit() and (int(choice) <= len(fun_names)):
#         choice = int(choice)
#     else:
#         print("Wrong Input")
#         return
#     apply_fn(choice)
#
#     answer = input("go to main menu again?\t")
#     if answer in "yY":
#         main_menu()
#
#
# def apply_fn(choice):
#     print("="*5)
#     if choice == 1:
#         # arr build
#         print("Build Array")
#         length = validate_input_num("Length of the array:")
#         start = validate_input_num("Starting of the array:")
#         arr = num_arr(length, start)
#         print("your array ==>\t", arr)
#     elif choice == 2:
#         print("Fiz-Buz")
#         fbn = validate_input_num("Input the number you want:\t")
#         print(fiz_buz(fbn))
#     elif choice == 3:
#         print("Reverse String")
#         # reversing no need to check
#         w = input("Input string to reverse:\t")
#         print(rev_str(w))
#     elif choice == 4:
#         print("User Details")
#         usr_data()
#     elif choice == 5:
#         print("Find the Longest sub string")
#         wl = validate_input_string("Input string to search:\t")
#         print("Longest sub string is:\t", longest_sub_word(wl))
#     elif choice == 6:
#         print("Calculate the inputs")
#         num_tot()
#     elif choice == 7:
#         print("Guess the word game")
#         guess_ham()
#     else:
#         print("Wrong Input")
#     print("-" * 5)
#     answer = input("apply same function again?\t")
#     if answer in "yY":
#         apply_fn(choice)
