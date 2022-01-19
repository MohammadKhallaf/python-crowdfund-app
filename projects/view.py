from projects.db_queries import get_all_projects


def view_projects():
    projects = []
    print("Hello to view projects menu")
    print("The existing projects:")
    projects = get_all_projects()

    counter = 0
    for project in projects:
        counter += 1
        print(f"{counter} - {project[2]} with target: {project[4]}")
