import Realtime
import ListSplit

"""
ToBorrrow module executed when user press 2 on main module. System ask user for his first name and check whether name
which user have assigned is valid or not if user first name is valid then system asked for last name and if user first
name is invalid the system display massage invalid input and again asked user for first name. Again system check
whether last name which user have assigned is valid or not if last name is valid then user are asked to choose
the book according to the choice and if last name is invalid the system display massage invalid input and
again asked for last name. After that when user enter valid choice then condition occur that asked user whether
yes to borrow book and no for doesn’t want to borrow. Borrow name is registered in text file and quantity of
book borrowed will be decrease by one. But when user enter invalid choice then system will asked user for valid choice.
"""
def borrowBook():
    correct=False
    while(True):
        firstName=input("first name of the borrower: ")
        if firstName.isalpha():
            break
        print("please input alphabet from A to Z")
    while(True):
        lastName=input("last name of the borrower: ")
        if lastName.isalpha():
            break
        print("please input alphabet from A to Z only")
            
    t="Borrow-"+firstName+".txt"
    with open(t,"w+") as q:
        q.write("    Date: " +Realtime.getDate()+"    Time:"+Realtime.getTime()+"\n\n")
        q.write("               Library Management System  \n")
        q.write("")
        q.write("                    Bill of books                            \n  ")
        q.write("     Borrowed By: "+ firstName+" "+lastName+"\n")
        q.write("S.N. \t\t Bookname \t\t      Authorname \n" )
    
    while correct==False:
        print("Please select a option below:")
        for i in range(len(ListSplit.bookname)):
            print("Enter", i, "to borrow book", ListSplit.bookname[i])
    
        try:   
            a=int(input())
            try:
                if(int(ListSplit.quantity[a])>0):
                    print("Book which you have choose is avilabele. Good chooice!! humm")
                    with open(t,"a") as q:
                        q.write("1. \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                    ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                    with open("listofbook.txt","w+") as q:
                        for i in range(10):
                            q.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")


                    #multi borrowing books code
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Are you sure that you want to borrow this book? press Y for yes and N for no: "))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(ListSplit.bookname)):
                                print("Enter", i, "to borrow book", ListSplit.bookname[i])
                            a=int(input())
                            if(int(ListSplit.quantity[a])>0):
                                print("Book is available")
                                with open(t,"a") as q:
                                    q.write(str(count) +". \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                                ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                                with open("listofbook.txt","w+") as q:
                                    for i in range(10):
                                        q.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")
                                        correct=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing.")
                            print("please check out again for borrowing books :)") 
                            print("")
                            loop=False
                            correct=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Book is not available")
                    borrowBook()
                    correct=False
            except IndexError:
                print("")
                print("Please choose book acording to their number.")
        except ValueError:
            print("")
            print("Please choose as suggested.")
