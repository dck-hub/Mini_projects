
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("kay.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            # get the characters in the password file that between in the | and put it in to the list.
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account_Name: ")
    pwd = input("Password: ")

# use with keyword to automatically close the file open. we need to close the file manually using close.file()
# w- override the file everytime. r - read, a - add something in end to the file. create file if there are not file by that name.

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add new password or view previous passwords(view/add), Press Q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()

    else:
        print("Invalid mode")
        continue
