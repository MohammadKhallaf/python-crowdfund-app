
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
