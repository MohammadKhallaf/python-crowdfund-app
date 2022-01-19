from validations import validate_input_date


def search_projects():
    print("Hello to search projects menu")
    search_date = validate_input_date("Enter date in the format:\t"
                                      "YYYY-MM-DD\n\t\t\t")

    projects = []
    print("Hello to view projects menu")
    with open("database/projects.txt") as fileObj:
        for line in fileObj:
            project = line.split(';')
            if project[5] == str(search_date):
                projects.append(project)

    print("The existing projects:")
    counter = 0
    for project in projects:
        counter += 1
        print(f"{counter} - {project[2]} with target: {project[4]}")
