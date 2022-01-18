import re


def validate_input_string(prompt):
    while True:
        word = input(prompt)
        if word.isalpha():
            return word


def validate_input_string_nosb(prompt):
    while True:
        word = input(prompt)
        if word.isalpha() and not word.isspace():
            return word


# TODO: change email validation
def validate_input_mail(prompt):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
        word = input(prompt)
        if re.fullmatch(regex, word):
            return word


def validate_input_num(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)