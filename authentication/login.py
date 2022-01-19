import getpass

from validations import validate_input_mail, validate_exist_mail


def login_user():
    # globalize the vars to affect all sections
    # there is a problem .. !

    print("Hello to login menu")
    mail = validate_input_mail("Enter your email :\t")
    if not validate_exist_mail(mail):
        print("This email is not exist !")
        return False

    with open("database/users.txt") as fileObj:
        for line in fileObj:
            if mail in line:
                user_details = line.split(";")
                break
    while True:
        passwd = getpass.getpass("Enter your password:\t")
        if passwd == user_details[1]:
            print(f"Hello {user_details[2]} {user_details[3]} !")
            break
        print("Not correct\n")

    return user_details[0], user_details[2], user_details[3]
