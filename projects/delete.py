import time

from projects.db_queries import get_user_projects, get_all_projects, update_db
from validations import validate_input_num, validate_input_string_nosb


def delete_project(user_details):
    print(f"Hello  {user_details[1]} {user_details[2]} to delete projects menu")
    user_project_list = get_user_projects(user_details[0])
    # projects list
    print("These are the projects you have:")
    counter = 0
    for project_line in user_project_list:
        counter += 1
        project_name = project_line[2]
        print(f"{counter}) {project_name}")
    # input choice
    choice = validate_input_num("Enter the number of the project you want to delete:\t")
    if choice > counter or choice < 1:
        print("Wrong choice number !")
    else:
        to_delete = user_project_list[choice - 1][1]
        print(f"you will delete:\t{to_delete}")
        answer = validate_input_string_nosb("Confirm? (Y / n)\t")
        if answer in 'yY':
            print("deleting")
            new_list = del_project(user_details[0], to_delete)
            # some interactive simulation
            for i in range(0, 3):
                time.sleep(1)
                print(".")
            # update the whole database
            update_db(new_list)

            print("deleted")


# delete project with the composite PK ( mail & id )
def del_project(mail, project_id):
    new_list = []
    total_projects = get_all_projects()
    for project in total_projects:
        if project[1] == project_id and project[0] == mail:
            continue
        new_list.append(project)
    return new_list
