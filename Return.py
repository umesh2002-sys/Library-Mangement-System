import ListSplit
import Realtime

"""
Return module executed when user press 3 on the main module. System asked user to 
First name of borrower if first name is valid then the bill of book will generate
on display but if name is invalid then the system will ask user for valid borrower
name. Again, system will ask user whether the return date of book is expired or not
(expire date of book is 10 days) if yes then specific penalty will applied on user.
Per day user should pay $1.5. 
"""

def returnBook():
    name=input("Enter name of borrower: ")
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r") as q:
            lines=q.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as q:
            data=q.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        returnBook()

    b="Return-"+name+".txt"
    with open(b,"w+")as q:
        q.write("Date: " + Realtime.getDate()+"    Time:"+ Realtime.getTime()+"\n\n")
        q.write("                Library Management System \n")
        q.write("                   Returned By: "+ name+"\n")
        q.write("                Bill of Book              \n\n ")
        q.write("S.N.\t\tBookname\t\tCost\n")


    total=0.0
    for i in range(10):
        if ListSplit.bookname[i] in data:
            with open(b,"a") as q:
                q.write(str(i+1)+"\t\t"+ListSplit.bookname[i]+"\t\t$"+ListSplit.cost[i]+"\n")
                ListSplit.quantity[i]=int(ListSplit.quantity[i])+1
            total+=float(ListSplit.cost[i])
            
    print("\t\t\t\t\t\t"+"Price of books"+"$"+str(total))
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        day=int(input())
        fine=1.5*day
        with open(b,"a")as q:
            q.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine
    


    print("Final Total: "+ "$"+str(total))
    with open(b,"a")as q:
        q.write("Total: $"+ str(total))
    
        
    with open("listofbook.txt","w+") as q:
            for i in range(10):
                q.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")
