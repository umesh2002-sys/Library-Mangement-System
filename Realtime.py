
'''
Realtime module is create the parenthesis to call time and date
on specific bill where user have issue books from system and
return book from the system.
'''
#Call a function
def getDate():
    import datetime
    now = datetime.datetime.now
    #print("Date: ",now().date())
    return str(now().date())

def getTime():
    import datetime
    now = datetime.datetime.now
    #print("Time: ",now().time())
    return str(now().time())

#printing real time date and time
