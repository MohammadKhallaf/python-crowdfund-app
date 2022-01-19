from projects.db_queries import get_user_projects
from validations import validate_input_string, validate_input_num, validate_input_date, validate_input_one_line


def create_project(user_details):
    print(f"Hello  {user_details[1]} {user_details[2]} to create projects menu")
    project_title = validate_input_string("Enter project title:\t")
    project_details = validate_input_one_line("Enter project short details in one line:\t")
    # eliminate the delimiter of the database (;)
    # expand to list => loop through => join to string again
    project_details = ''.join(filter(lambda x: x != ';', list(project_details)))
    project_target = validate_input_num("Enter project total target in EGP:\t")
    project_start = validate_input_date("Enter starting date in the format:\t"
                                        "YYYY-MM-DD\n\t\t\t")
    project_end = project_start
    while project_end <= project_start:
        project_end = validate_input_date("Enter ending date in the format:\t"
                                          "YYYY-MM-DD\n\t\t\t")
        if project_end <= project_start:
            print("You can't end the project before it starts")

    user_project_list = get_user_projects(user_details[0])
    # get the 2nd col in the last line {project id}
    if len(user_project_list):
        last_id = int(user_project_list[-1][1])
        project_id = last_id + 1
    else:
        project_id = 0

    with open("database/projects.txt", "a") as fileObj:
        fileObj.write(f"{user_details[0]};"
                      f"{project_id};"
                      f"{project_title};"
                      f"{project_details};"
                      f"{project_target};"
                      f"{project_start};"
                      f"{project_end}"
                      f"\n")
