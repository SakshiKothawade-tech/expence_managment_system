#Expence Tracker project
expences=[ ]#list of expences in form of dictionary
print("WELCOME TO EXPENCE TRACKER: ")
while True:
    print("===== Menu=====")
    print("1.Add Expences")
    print("2.View All Expences")
    print("3.View Total Expences")
    print("4.Exit")
    choice=input("Please Enter Your Choice:")
    #1.add expence
    if(choice==1):
        date=input("enter date of expence:")
        category=input("Enter type of expence you can do?:{Food,Travel,makeup,Books}")
        description=input("Tell me in detail:")
        amount=float(input("Enter amount:",))
        expence={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expences.append(expence)
        print("\n Expence Added Succesfully")
    #2. View all expences
    elif(choice==2):
        if (len(expences)==0):
            print("No Expences Added.")
        else:
            print("This is your total Expence:")
            count=1
            for eachexpence in expence:
                print(f"Expence number{count} -> {eachexpence['date']} , {eachexpence['category']}, {eachexpence['descrption']},{eachexpence['notes']}")
                count=count+1

    # 3.view total spending 
    elif(choice==3):
        total=0
        for eachexpence in expence:
            total=total+eachexpence["amount"]
        print("Total Expence:",total)
    #Exit
    elif(choice==4):
        print("thanku for using my system.")
        break
    else:
        print("Invalid choise ,please try again")