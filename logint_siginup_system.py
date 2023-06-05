print("Create your account now!")
username = input("Enter your user name: ")
password = input("Enter your password: ")
print("Your acount has been created successfully :)")
print("You can now login :)")
username2 = input("Enter your username: ")
password2 = input("Enter your password: ")

if username == username2 and password == password2:
    print("Welcome! " , username)
else :
    print("invalid username or password")