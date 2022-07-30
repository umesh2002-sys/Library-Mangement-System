import Return
import ListSplit
import Realtime
import ToBorrow
'''
This is the main module where all the functionality carryout. When this module is run a display is displayed and user are
asked to enter specific integer value for specific task.
If user press 1 then a listofbook.txt file would display and again main module is run. And again ask user for choice.
When user press 2 then ToBorrow module file open. Process will be shown on ToBorrow module.
When user press 3 then return module open. And the process is explained below on return module.
Main module file hands over all the execution of program which including write file, read file, split and read user input and many more.
'''

def main():
    while(True):
        print("--------------------------------------------------------")
        print("|                                                      |")
        print("|            Library Management System                 |")
        print("|                                                      |")
        print("|        Press 1: To Display books available LMS       |")
        print("|             Press 2: To Borrow a book                |")
        print("|             Press 3: To Return a book                |")
        print("|             Press 4: To exit                         |")
        print("|                                                      |")
        print("--------------------------------------------------------")
        try:
            x=int(input("Press or choice from 1 or 2 or 3 or 4: "))
            print()
            if(x==1):
                with open("listofbook.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print()
   
            elif x==2:
                ListSplit.listSplit()
                ToBorrow.borrowBook()
            elif x==3:
                ListSplit.listSplit()
                Return.returnBook()
            elif x==4:
                print("library management system")
                print("         is              ")
                print("      shutdowning        ")
                print("  Thank u for using LMS  ")
                print("     Hope you like it    ")
                break
            else:
                print("Please insert/press valid input as shown in display")
        except ValueError:
            print("Please press the number as suggested.")
main()
