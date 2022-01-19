from validations import validate_input_string, validate_input_num, validate_input_date, validate_input_one_line


def get_project_data():
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
    return [project_title, project_details, str(project_target), str(project_start), str(project_end)]
