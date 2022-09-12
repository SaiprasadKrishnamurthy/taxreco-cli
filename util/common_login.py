import getpass

from commands.login import login_command


def common_login():
    username = input("Enter your login username:  ")
    password = getpass.getpass("Enter your login password: ")
    login_command(username, password)
