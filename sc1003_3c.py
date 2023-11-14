import re

users = {
    'Test': 'Test12345', 
    'Jack': 'Test12345', 
    'Tom': 'Password1'
}
def is_password_strong(password):
    return (
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        len(password) > 8
    )

def register_user(user):
    username = user
    while True:
        if username in users:
            print("The user exists. Please choose another username.")
            username = input("Input your user name: ")
        else:
            break

    while True:
        print("Input your password: ")
        print("1. The password has at least one uppercase letter")
        print("2. The password has at least one lowercase letter")
        print("3. The password has at least one digit")
        print("4. Its length is more than 8")
        password = input()
        if is_password_strong(password):
            users[username] = password
            print("Your password is strong enough. User registered.")
            break
        else:
            print("Your password is not strong enough. Please follow these rules:")

print("User registration:")
username = input("Input your user name: ")
register_user(username)


