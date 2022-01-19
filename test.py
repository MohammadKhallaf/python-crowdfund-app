# import time
#
# from projects.create import get_project_data
# from projects.db_queries import get_user_projects, get_all_projects, update_db
# from projects.edit import edt_project
# from validations import validate_input_num, validate_input_string_nosb
#
#
# # ee@gmail.com => user_details[0]
# def del_usr_fn_tst():
#     user_project_list = get_user_projects('ee@gmail.com')
#     print("These are the projects you have:")
#     counter = 0
#     for project_line in user_project_list:
#         counter += 1
#         project_name = project_line[2]
#         print(f"{counter}) {project_name}")
#
#     choice = validate_input_num("Enter the number of the project you want to delete:\t")
#     if choice > counter or choice < 1:
#         print("Wrong choice number !")
#     else:
#         to_delete = user_project_list[choice - 1][2]
#         print(f"you will delete:\t{to_delete}")
#         answer = validate_input_string_nosb("Confirm? (Y / n)\t")
#         if answer in 'yY':
#             # total_projects = get_all_projects()
#             # for project in total_projects:
#             #     print(f"list before delete: {project}")
#             print("deleting")
#             for i in range(0, 3):
#                 # time.sleep(1)
#                 print(".")
#             new_list = []
#             total_projects = get_all_projects()
#             for project in total_projects:
#                 if project[2] == to_delete and project[0] == "ee@gmail.com":
#                     continue
#                 new_list.append(project)
#
#                 with open("database/projects.txt", "w") as fileObj:
#                     for line in new_list:
#                         fileObj.write(";".join(line))
#
#             print("deleted")
#             # for project in new_list:
#             #     print(f"list after delete: {project}")
#
#
# def updt_usr_fn_tst():
#     user_project_list = get_user_projects("ee@gmail.com")
#
#     # list the projects of the user
#     print("These are the projects you have:")
#     counter = 0
#     for project_line in user_project_list:
#         counter += 1
#         project_name = project_line[2]
#         print(f"{counter}) {project_name}")
#     # input choice
#     choice = validate_input_num("Enter the number of the project you want to edit:\t")
#     if choice > counter or choice < 1:
#         print("Wrong choice number !")
#     else:
#         to_update = user_project_list[choice - 1][1]
#         project_old_id = user_project_list[choice - 1][1]
#
#         # get the new information
#         project_data = get_project_data()
#
#         # get the 2nd col in the last line {project id}
#         project_id = project_old_id
#
#         print(f"you will update:\t{to_update}")
#         answer = validate_input_string_nosb("Confirm? (Y / n)\t")
#         if answer in 'yY':
#             print("updating")
#             new_list = edt_project("ee@gmail.com", project_id, project_data)
#             # some interactive simulation
#             for i in range(0, 3):
#                 time.sleep(1)
#                 print(".")
#             # update the whole database
#             update_db(new_list)
#
#             print("updated")
#
#
# updt_usr_fn_tst()
