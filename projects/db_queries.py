def get_user_projects(user_mail):
    user_project_list = []
    with open("database/projects.txt") as fileObj:
        for line in fileObj:
            if user_mail in line:
                user_project_list.append(line.split(';'))
    return user_project_list


# def get_users_list(user_mail):
#     users_list = []
#     with open("database/users.txt") as fileObj:
#         for line in fileObj:
#             if user_mail in line:
#                 user_project_list.append(line.split(';'))

def get_all_projects():
    projects = []
    with open("database/projects.txt") as fileObj:
        for line in fileObj:
            projects.append(line.split(';'))

    return projects


def update_db(new_db):
    with open("database/projects.txt", "w") as fileObj:
        for line in new_db:
            fileObj.write(";".join(line))
