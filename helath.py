my={1:'Kautubh',2:'Swapnil',3:'Atul'}
you={1:'Exercise',2:'Diet'}
def getdate():
    import datetime
    return datetime.datetime.now()
def function1():
    print("Do you want to add details or check the data?")
    c = int(input("Press 1 for add details,2 for check the data\n"))
    if c==1:
        print("Which client do you want to log for?")
        a=int(input("Press 1 for Kaustubh,2 for Swapnil,3 for Atul\n"))
        print("What do you want to log for  or details?")
        b=int(input("Press 1 for Exercise,2 for Diet\n"))
        if b==1:
            with open(my[a]+you[b]+".txt","a") as e:
             k=input("Which Exercise did you do?\n")
             e.write(str([str(getdate())])+"-"+k+"\n")
             print("Successful")
        elif b==2:
            with open(my[a]+you[b]+".txt","a") as f:
             m=input("What did you eat?\n")
             f.write(str([str(getdate())])+"-"+m+"\n")
             print("Successful")
    elif c==2:
        print("Which client do you want to retrieve for?")
        r=int(input("Press 1 for kaustubh,2 for Swapnil,3 for Atul\n"))
        print("What do you want to retrieve?")
        s=int(input("Press 1 for Exercise,2 for Diet\n"))
        if s==1:
            with open(my[r] + you[s] + ".txt") as g:
                content=g.read()
                print(content)
        elif s==2:
            with open(my[r] + you[s] + ".txt") as h:
                body=h.read()
                print(body)
function1()
print('working successfully')