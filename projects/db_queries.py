def get_user_projects(user_mail):
    user_project_list = []
    with open("database/projects.txt") as fileObj:
        for line in fileObj:
            if user_mail in line:
                user_project_list.append(line.split(';'))
    return user_project_list


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


def append_record(mail, pr_id, title, details, target, start, end):
    with open("database/projects.txt", "a") as fileObj:
        fileObj.write(f"{mail};"
                      f"{pr_id};"
                      f"{title};"
                      f"{details};"
                      f"{target};"
                      f"{start};"
                      f"{end};"
                      f"\n")
