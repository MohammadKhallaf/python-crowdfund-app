from projects.db_queries import get_user_projects, append_record
from projects.poj_operations import get_project_data


def create_project(user_details):
    print(f"Hello  {user_details[1]} {user_details[2]} to create projects menu")
    [project_title, project_details, project_target, project_start, project_end] = get_project_data()
    user_project_list = get_user_projects(user_details[0])
    # get the 2nd col in the last line {project id}
    if len(user_project_list):
        last_id = int(user_project_list[-1][1])
        project_id = last_id + 1
    else:
        project_id = 0
    # append the data to the db
    append_record(user_details[0],
                  project_id,
                  project_title,
                  project_details,
                  project_target,
                  project_start,
                  project_end)

    print("Done !")
    print(f"Added {project_title} with target = {project_target}LE"
          f"\nfrom: {project_start} to {project_end}")

