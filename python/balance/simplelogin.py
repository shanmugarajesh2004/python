def login():

    print("Create an account")

    username = input("Enter a user name :")
    userpassword = input("Enter a password :")

    print("Your account Createt successfully")
    print("Login Now")

    c_user = input("Enter user name :")
    c_password = input("Enter a password :")

    if (username == c_user and userpassword == c_password):
        print("Login successfully")
    else:
        print("invalid")

    