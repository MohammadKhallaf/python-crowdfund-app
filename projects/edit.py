import time

from projects.create import get_project_data
from projects.db_queries import get_user_projects, get_all_projects, update_db
from validations import validate_input_string_nosb, validate_input_num


def edit_project(user_details):
    print(f"Hello  {user_details[1]} {user_details[2]} to edit projects menu")
    user_project_list = get_user_projects(user_details[0])

    # list the projects of the user
    print("These are the projects you have:")
    counter = 0
    for project_line in user_project_list:
        counter += 1
        project_name = project_line[2]
        print(f"{counter}) {project_name}")
    # input choice
    choice = validate_input_num("Enter the number of the project you want to edit:\t")
    if choice > counter or choice < 1:
        print("Wrong choice number !")
    else:
        to_update = user_project_list[choice - 1][1]
        project_old_id = user_project_list[choice - 1][1]

        # get the new information
        project_data = get_project_data()

        # get the 2nd col in the last line {project id}
        project_id = project_old_id

        print(f"you will update project:\t{user_project_list[choice - 1][2]}")
        answer = validate_input_string_nosb("Confirm? (Y / n)\t")
        if answer in 'yY':
            print("updating")
            new_list = edt_project("ee@gmail.com", project_id, project_data)
            # some interactive simulation
            for i in range(0, 3):
                time.sleep(1)
                print(".")
            # update the whole database
            update_db(new_list)

            print("updated")


# delete then create
# but with the same old id


# edit project with the composite PK ( mail & id )

def edt_project(mail, project_id, data):
    data = list(data)
    new_list = []
    total_projects = get_all_projects()
    for project in total_projects:
        if project[1] == project_id and project[0] == mail:
            new_prj = [mail, project_id]
            new_prj.extend(data)
            new_prj.append("\n")
            project = new_prj

        new_list.append(project)
    return new_list
