from time import sleep
import webbrowser
import platform
import os
import sys

try:
    import tkinter
    from tkinter.constants import *

except ImportError:
    print("Uh-Oh... Seems like some of the librarys arent installed :( Please debug.")
    errorcode = "lib"

version = 2.5

yes = True
no = False

AdminUser = "Administrator"
AdminPassword = "Jaibreaking"

Wrong_info = 'Sorry its wrong. But the username is: "user" and the password is "user".'
pylock_Wrong_info = 'Sorry its wrong. Try again'

User = "user"
UserPassword = "user"

def debug():
    secret = input("Are you sure to enable debug mode? [Y/n]")
    if secret == "y":
        sys.stdout = open('debug.py', 'wt')
        print("import platform")
        print("import sys")
        print("print(' ____    _____   ____    _   _    ____     __  __    ___    ____    _____ ')")
        print("print('|  _ \  | ____| | __ )  | | | |  / ___|   |  \/  |  / _ \  |  _ \  | ____|')")
        print("print('| | | | |  _|   |  _ \  | | | | | |  _    | |\/| | | | | | | | | | |  _|  ')")
        print("print('| |_| | | |___  | |_) | | |_| | | |_| |   | |  | | | |_| | | |_| | | |___ ')")
        print("print('|____/  |_____| |____/   \___/   \____|   |_|  |_|  \___/  |____/  |_____|')")
        print("while True:")
        print("    debug_term = input('debug:')")
        print("    if debug_term == 'check lib':")
        print("            try:")
        print("                    import tkinter")
        print("                    from tkinter import *")
        print("                    print('No Problems at all.')")
        print("            except ImportError:")
        print("                    input('Oh No... The Check found some Problems')")
        print("                    choice = input('Should I write a reapirer file? [Y/n]: ')")
        print("                    if choice == 'y':")
        print("                            while True:")
        print("                                if platform == 'linux' or platform == 'linux2':")
        print("                                        sys.stdout = open('repair.sh', 'wt')")
        print("                                        print('#!/usr/bin/bash/')")
        print("                                        print('sudo apt install -y python3-pip')")
        print("                                        print('pip3 install tkinter')")
        print("                                        print('read -p Done.')")
        print("                                        break")
        print("                                elif platform == 'darwin':")
        print("                                        sys.stdout = open('reapir.sh', 'wt')")
        print("                                        print('pip3 install tkinter')")
        print("                                        print('echo Done.')")
        print("                                        break")
        print("                                elif platform == 'win32':")
        print("                                    sys.stdout = open('installer.bat', 'wt'")
        print("                                    pip3 install tkinter")
        print("                                    pause")
        print("                                    break")
        print("                                else:")
        print("                                    pass")
        print("                    if choice == 'Y':")
        print("                            while True:")
        print("                                if platform == 'linux' or platform == 'linux2':")
        print("                                        sys.stdout = open('repair.sh', 'wt')")
        print("                                        print('#!/usr/bin/bash/')")
        print("                                        print('sudo apt install -y python3-pip')")
        print("                                        print('pip3 install tkinter')")
        print("                                        print('read -p Done.')")
        print("                                        break")
        print("                                elif platform == 'darwin':")
        print("                                        sys.stdout = open('reapir.sh', 'wt')")
        print("                                        print('pip3 install tkinter')")
        print("                                        print('echo Done.')")
        print("                                        break")
        print("                                elif platform == 'win32':")
        print("                                    sys.stdout = open('installer.bat', 'wt'")
        print("                                    pip3 install tkinter")
        print("                                    pause")
        print("                                    break")
        print("                                else:")
        print("                                    pass")
        print("                    if choice == 'n':")
        print("                            print('Abort')")
        print("                    if choice == 'N':")
        print("                            print('Abort.')")

def python_help_me():
    print("Thanks for downloading python for kids.")
    input()
    print("Here are some commands:")
    input()
    print("python make a Window = if you give this command, python will create a window.")
    answer1 = input("Was That helpfull?")
    if answer1 == "yes":
        input("Ok click enter to exit.")

    else:
        print("Oh so click enter for more commands.")
        input()
        print("the 2nd command is: python exit = python will exit and says: want you quit?")
        answer2 = input("was that helpfull [Y/n]")
        if answer2 == "yes":
            input("Ok click enter to exit.")

        else:
            print("the 3rd is: python say something = if you type python will ask what schould i say? type what you want python will reply it")
            answer3 = input("was that helpfull [Y/n]")
            if answer3 == "yes":
                input("Ok click enter to exit.")
            else:
                print("the 4th one is python make a clear window = if you give his command, python will create a clear window")
                answer = input("Was that helpful? [Y/n]")
                if answer == "y":
                    input("Oh! Ok then press enter to quit")
                
                else:
                    input("Sorry but no more commands are anavible. Go to \(the path to the python for kids folder)\More Command")
            
def python_make_a_window():
    if errorcode == "lib":
        print("You can't run this command. You need to debug.")
        
    else:
        tk = tkinter.Tk()
        frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
        frame.pack(fill=BOTH,expand=1)
        label = tkinter.Label(frame, text="i'ma your new Windows 10 setup window")
        label.pack(fill=X, expand=1)
        button = tkinter.Button(frame,text=">>>Install<<<",command=tk.destroy)
        button.pack(side=BOTTOM)
        tk.mainloop()


def python_exit():
    answer_for_quit = input("do you want to quit?")
    if answer_for_quit == "yes":
        exit()
    else:
        input("Ok!")

def python_say_something():
    say = input("What schould i say? ")
    print(say)

def python_make_a_clear_window():
    
    tk = tkinter.Tk()

def python_news():
    print("Looking for news...")
    sleep(3)
    print("Opening the browser...")
    sleep(3)
    webbrowser.open('https://news.google.com/')

def pylock():
    AdminUser = "Administrator"
    AdminPassword = "Jaibreaking"

    while yes:
        logon_info_as_username = input("Username: ")
        logon_info_as_password = input("Password: ")

        if logon_info_as_username == "user":
            if logon_info_as_password == "user":
                input("Welcome to python for kids 2.6!")

                while True:
                    command_line = input("command line: ")

                if command_line == "python help me":
                    python_help_me()

                elif command_line == "python make a window":
                    python_make_a_window()

                elif command_line == "python make a clear window":
                    python_make_a_clear_window()

                elif command_line == "python go to link":
                    python_go_to_link()

                elif command_line == "python download":
                    python_download()

                elif command_line == "python exit":
                    exit()

                elif command_line == "python say something":
                    python_say_something()

                elif command_line == "python news":
                    python_news()

                else:
                    print("invaild command: ", command_line)

        elif logon_info_as_username == "Administrator":
             if logon_info_as_password == "Admi14":
                 while True:
                     input("Hello Admin. I'm so exited to see you")
                
                     command_line = input("command line: ")

                     if command_line == "python help me":
                         python_help_me()

                     elif command_line == "python make a window":
                           python_make_a_window()

                     elif command_line == "python make a clear window":
                           python_make_a_clear_window()

                     elif command_line == "python go to link":
                           python_go_to_link()

                     elif command_line == "python download":
                           python_download()

                     elif command_line == "python exit":
                           exit()

                     elif command_line == "python say something":
                           python_say_something()

                     elif command_line == "python news":
                           python_news()
                     
                     elif command_line == "python debug":
                        debug()

    else:
        print(pylock_Wrong_info)
        



def bug():
    print("")
    


def python_go_to_link():
    option = input("Wanna go to a search engine? [Y/n] ")
    
    if option == "y":
        option2 = input("type the name here (here names:' Bing, Yandex, CC Search, Swisscows, DuckDuckGo, Google'): ")

        if option2 == "Bing":
            print("Running Web script...")
            sleep(4)
            webbrowser.open('https://www.bing.com/')

        elif option2 == "Yandex":
            print("Running Web script...")
            sleep(4)
            webbrowser.open('https://www.yandex.com/')

        elif option2 == "CC Search":
            print("Running Web script...")
            sleep(4)
            webbrowser.open('https://search.creativecommons.org/')

        elif option2 == "Swisscows":
            print("Running Web script...")
            sleep(4)
            webbrowser.open('https://swisscows.com/')

        elif option2 == "DuckDuckGo":
             print("Running Web script...")
             sleep(4)
             webbrowser.open('https://duckduckgo.com/')

        elif option2 == "Google":
             print("Running Web script...")
             sleep(4)
             webbrowser.open('https://google.com/')
    
    else:
        The_link = input("Oh Ok type the url Exanple: https://www.google.com ")
        print("Running Web script...")
        sleep(3)
        webbrowser.open(The_link)

def python_disk():
    disk_answer = input("On what disk schould i go? like Z: or Z:\just a folder: ")
    sleep(5)
    webbrowser.open("file:///", disk_answer)

print("login")

while yes:
    logon_info_as_username = input("Username: ")
    logon_info_as_password = input("Password: ")

    if logon_info_as_username == "user":
        if logon_info_as_password == "user":
            input("Welcome to python for kids 2.6!")

            while True:
                command_line = input("command line: ")

                if command_line == "python help me":
                    python_help_me()

                elif command_line == "python make a window":
                    python_make_a_window()

                elif command_line == "python make a clear window":
                    python_make_a_clear_window()

                elif command_line == "python go to link":
                    python_go_to_link()

                elif command_line == "python download":
                    python_download()

                elif command_line == "python exit":
                    exit()

                elif command_line == "python say something":
                    python_say_something()

                elif command_line == "python news":
                    python_news()

                elif command_line == "debug mode":
                      debug()

                else:
                    print("invaild command: ", command_line)

    elif logon_info_as_username == "Administrator":
         if logon_info_as_password == "Admi14":
             while True:
                 input("Hello Admin. I'm so exited to see you")
                
                 command_line = input("command line: ")

                 if command_line == "python help me":
                     python_help_me()

                 elif command_line == "python make a window":
                       python_make_a_window()

                 elif command_line == "python make a clear window":
                       python_make_a_clear_window()

                 elif command_line == "python go to link":
                       python_go_to_link()

                 elif command_line == "python download":
                       python_download()

                 elif command_line == "python exit":
                       exit()

                 elif command_line == "python say something":
                       python_say_something()

                 elif command_line == "python news":
                       python_news()

    else:
        print(Wrong_info)
        


