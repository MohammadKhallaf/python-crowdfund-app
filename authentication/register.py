import getpass

from validations import validate_input_string_nosb, validate_input_mail, validate_phone_num


def register_user():
    print("Hello to register menu")
    f_name = validate_input_string_nosb("Enter your first name :\t")
    l_name = validate_input_string_nosb("Enter your last name :\t")
    mail = validate_input_mail("Enter your email :\t")
    passwd = getpass.getpass("Enter your password:\t")
    conf_passwd = ''
    while conf_passwd != passwd:
        conf_passwd = getpass.getpass("Please re-enter your password to confirm:\t")
        if conf_passwd != passwd:
            print("Wrong password")
    phone_num = validate_phone_num("Enter your mobile phone :\t")

    print(f"Hi {f_name} {l_name}"
          f"\nThe entered email is {mail}"
          f"\nThe password is {passwd}"
          f"\nThw entered phone number is {phone_num}")

    if check_exist(mail):
        print("this email is already registered...")
        return

    # TODO: add id to the user

    with open("database/users.txt", "a") as fileObj:
        fileObj.write(F"{mail};{passwd};{f_name};{l_name};{phone_num}\n")


def check_exist(email):
    exist = False
    with open("database/users.txt") as fileObj:
        for line in fileObj:
            if email in line:
                exist = True
                break
    return exist
