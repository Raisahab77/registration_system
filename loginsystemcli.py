from os import system, name
import time
def login(user_name,password):
    """
    This function takes 2 argument a user name and a password 
    which is pre register in login.txt file
    """
    # If flag value is changed to true that means user loggedin but if flag value won't change that means user doesn't exist
    flag = False 
    with open("login.txt","r") as file:
        for line in file:
            line = line.replace(":", ' ')
            line =line.split()
            # In login.txt file their are 3 values saperated by :(semi colon) second value is user_name and the third value is password value
            if line[1] == user_name and line[2] == password :
                flag = True
                print("logged in sucessfully")
                time.sleep(5)
                break
    if flag == False:
        registerd()
def registerd():
    """
    This function register the user it take a name, user_name and a password
    """
    clear()
    print("------------------------- Registration page -------------------------------")
    name = input("Enter Your name :")
    #to remove space from name and user_name
    name = name.replace(" ", "")
    global user_name ,password
    user_name = input("Enter a user name :")
    user_name = user_name.replace(" ", "")
    password = input_password()
    print(password)
    #Here we create/open login.txt file which stores name:user_name:password
    with open("login.txt","a") as f:
        f.write(f"{name}:{user_name}:{password} \n")


def input_password():
    """ 
    It takes password which is a valid password
    password validator checks if the password is valid 
    if password is not valid than it will ask to enter 
    a valid password and returns a valid password
    """
    password = input("Enter a password :")
    password = password.replace(" ", "")
    valid = pass_validation(password)
    if not valid :
        input_password()

    return password

def mainWindow():
    """ 
    After running the program this function appers and ask for options
    this function runs in a loop and all the functions execute from this 
    function
    """
    clear()
    print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
    print("Welcome to the login system :")
    print("Press 1 for Login :\nPress 2 For Registration :\nPress 3 for Exit :")
    choice = int(input())
    if choice==1:
        clear()
        print("-----------------------------------Login page------------------------------")
        user_name = input("Enter your user_name :")
        password = input("Enter your Password :")
        login(user_name,password)
    elif choice==2:
        registerd()
    elif choice==3:
        exit()
    else:
        print("Wrong Input")
        mainWindow()


def clear():
    """
    This function is used to clear the screen
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def pass_validation(password):
    """
    this function takes a password as argument and checks for 
    the validity of the password and returns a password when 
    the password is valid
    """
    valid = True
    lower, upper, digit, special_character = False, False, False,False
    special_char = ['!','@','#','$','%','-','_','&','*']
    length = len(password)
    if (length>=8 and length<=16):
        for i in password:
            if i.isupper():
                upper = True
            if i.islower():
                lower = True
            if i.isdigit():
                digit = True
            if i in special_char:
                special_character = True
    
    if lower and upper and digit and special_character:
        print("password is valid")
    else :
        valid = False
        print("password is invalid")
        if not lower:
            print("Missing lower case")
        if not upper:
            print("Missing upper case")
        if not digit:
            print("Missing digit")
        if not special_char:
            print("Missing special_char case")
        if length<8 or length>16:
            print("password length must be 8-16 char long")

    return valid

if __name__ =="__main__":
    while True:
        mainWindow()