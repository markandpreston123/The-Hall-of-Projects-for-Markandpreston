import time
import os
import calendar
Q1 = input("""
What would you like to do?

1) Sign in
2) Sign up (will replace old account)
3) Shut Down
""")

if Q1 == '2':
    Password = input("Enter your password (Will generate if no password is provided: ")
    while True:
        def doesFileExist(filePathAndName):
            return os.path.exists(filePathAndName)

        if doesFileExist('./Password.txt'):
            with open('Password.txt') as f:
                contents = f.read()
            if contents == Password:
                UserNameS = input("Enter your username: ")
                PasswordS = input("Enter your new password: ")
                with open('Username.txt', 'w') as f:
                    f.write(UserNameS)
                with open('Password.txt', 'w') as f:
                    f.write(PasswordS)
                    break
        else:
            with open('Password.txt', 'w') as f:
                f.write(Password)
            print(""" 
            The password file was created. 
            Please start the OS again and choose "Sign Up" again with the existing password provided to continue setup.
            """)
            time.sleep(1)
            print("Shutting down...")
            time.sleep(1.16)
            exit()


if Q1 == '3':
    print("Shutting down...")
    time.sleep(1)
    exit()
                
if Q1 == '1':
    Username = input("Enter your username: ")        
    Password = input("Enter your password: ")



    with open('Username.txt') as f:
        contents = f.read()
    with open('Password.txt') as f:
        contents = f.read()
while True:
    if contents == Password:
        print("Signing in...")
        time.sleep(1)
        print("Signed in. Welcome!")
        MainMenu = input("""
        ============== MAIN MENU ============== 
        1) Calendar
        2) Shut Down
        """)        
        if MainMenu == '1':
            c = calendar.TextCalendar(calendar.SUNDAY)
            str = c.formatmonth(2022, 2)
            print(str)
            CalendarInput = input("""Press q to exit.
""")
            if CalendarInput == 'q':
                print("Exiting...")
                time.sleep(1.15)
                print("Shutting down...")
                time.sleep(1.16)
                exit()
            

        if MainMenu == '2':
            print("Shutting Down...")
            time.sleep(1.15)
            exit()
    else:
        print("The username or password is incorrect")
        print("Shutting down...")
        exit()
        
        
                