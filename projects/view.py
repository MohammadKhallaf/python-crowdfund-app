def view_projects():
    projects = []
    print("Hello to view projects menu")
    with open("database/projects.txt") as fileObj:
        for line in fileObj:
            projects.append(line.split(';'))

    print("The existing projects:")
    counter = 0
    for project in projects:
        counter += 1
        print(f"{counter} - {project[2]} with target: {project[4]}")

    return projects
