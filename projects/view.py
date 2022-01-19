from projects.create import create_project
from projects.db_queries import get_all_projects
from validations import validate_input_string_nosb


def view_projects(logged_user_data):
    print("Hello to view projects menu")
    projects = get_all_projects()
    if not len(projects):
        print("There is no projects yet")
        answer = validate_input_string_nosb("Do you want to add some now? (Y / n)\t")
        if answer in 'yY':
            create_project(logged_user_data)
    else:
        print("The existing projects:")
        counter = 0
        for project in projects:
            counter += 1
            print(f"{counter} - {project[2]} with target: {project[4]}")
