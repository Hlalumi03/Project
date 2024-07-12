

def sign_up():
    username = input("Enter a username which you will use to access you account: ")
    if not username.isalpha():
        print("invalid user name")
        while True:
            username = input("Enter a username: ")
            if not username.isalpha():
                print("invalid username")
            else:
                break

    password = input("enter a password: ")

    if not password.isalnum():
        print("invalid password")
        while True:
            password = input("enter a password: ")
            if not password.isalnum():
                print("invalid password")
            else:
                break

    name = input("enter your name: ")
    surname = input("enter your surname: ")

    user_info = {
        "Username": username, "Password": password, "Name": name, "Surname": surname}

    user_information(user_info)
    print("signed up successfully")

    login()


def user_information(user_info):
    user_details = f"Username: {user_info['Username']}, Password: {user_info['Password']}"
    save_to_file(user_details)


def save_to_file(text):
    with open("user.txt", "a") as file:
        file.write(text + "\n")


def login():
    print("Enter login details")
    username = input("Enter your username: ")
    password = input("Enter password: ")

    with open("user.txt", "r") as file:
        for line in file:
            user_details = line.strip().split(", ")
            saved_username = user_details[0].split(": ")[1]
            saved_password = user_details[1].split(": ")[1]
            if username == saved_username and password == saved_password:
                print("Login successful!")
                return True

        print("Login failed. Username or password incorrect.")
        return False


def menu():
    print("please select one of the following options:")

    menu_items = {"r: to register user, "
                  "a: add task, "
                  "va: view all tasks, "
                  "vm: view my task, "
                  "e: to exit"}
    
    print(menu_items)

    for _ in menu_items:
        x = input("enter your choice: ")

        if x == "r":
            return login()

        with open("tasks.txt", "r") as file:
            while True:
                if x == "vm":
                    for line in file:
                        print(file.readline())

if __name__ in '__main__':
    print("do you have an account ?")
    x = input("if yes enter(1) or if no enter(2): ")
    if x == "1":
        print(login())
    elif x == "2":
        print(sign_up())
