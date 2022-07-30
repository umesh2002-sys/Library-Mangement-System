'''
listSplit module is most important module. Split function is applied
on the listofbook.txt on the basic of (,) it convert text format into an array.
It convert specific text into name book list, author name list, quantity list
and price of book list.
'''

def listSplit():
    global bookname
    global authorname
    global quantity
    global cost
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]
    with open("listofbook.txt","r") as q:
        
        lines=q.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    bookname.append(a)
                elif(ind==1):
                    authorname.append(a)
                elif(ind==2):
                    quantity.append(a)
                elif(ind==3):
                    cost.append(a.strip("$"))
                ind=ind + 1
