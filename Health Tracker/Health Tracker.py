try:
    clientno = int(input("Press \n 1 For Swaraj \n 2 For Martin \n 3 for Bala \n"))
except:
    print("Please enter appropriate input")

def getdate():
    import datetime
    return datetime.datetime.now()

def Swaraj():
    choice1 = input("Press 1 if you want to log data \n 2 if you want to read data \n")
    if choice1 == "1":
        choice11 = input("What you want to log data into? \n Press 1 for Diet \n Press 2 for Excercise \n")
        if choice11 == "1":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Swarajdiet.txt" , "a")
            time= str(getdate())
            f.write(time)
            f.write("  ")
            f.write(  input("Enter the food items: \n ") )
            f.write("\n")
            f.close()
        elif choice11 == "2":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Swarajex.txt" , "a")
            time= str(getdate())
            f.write(time)
            f.write("  ")
            f.write(  input("Enter the excercises performed: \n"))
            f.write("\n")
            f.close()
        else:
            print("Please enter the correct keyword")
    elif choice1 == "2":
        choice11 = input("What data you want to read? \n Press 1 for Diet \n Press 2 for Excercise \n")
        if choice11 == "1":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Swarajdiet.txt" , "r")
            print(f.read())
            f.close()
        elif choice11 == "2":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Swarajex.txt" , "r")
            print(f.read())
            f.close()
        else:
            print("Please enter the correct keyword")
        print()
    else:
        print("Please enter the correct keyword")

def Martin():
    choice1 = input("Press 1 if you want to log data \n 2 if you want to read data \n")
    if choice1 == "1":
        choice11 = input("What you want to log data into? \n Press 1 for Diet \n Press 2 for Excercise \n")
        if choice11 == "1":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Martindiet.txt" , "a")
            food = input("Enter the food items: \n ") 
            f.write(str([str(getdate())]) + ": " + food + "\n")
            f.close()
        elif choice11 == "2":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Martinex.txt" , "a")
            time= str(getdate())
            f.write(time)
            f.write("  ")
            f.write(  input("Enter the excercises performed: \n"))
            f.write("\n")
            f.close()
        else:
            print("Please enter the correct keyword")
    elif choice1 == "2":
        choice11 = input("What data you want to read? \n Press 1 for Diet \n Press 2 for Excercise \n")
        if choice11 == "1":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Martindiet.txt" , "r")
            print(f.read())
            f.close()
        elif choice11 == "2":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Martinex.txt" , "r")
            print(f.read())
            f.close()
        else:
            print("Please enter the correct keyword")
        print()
    else:
        print("Please enter the correct keyword")

def Bala():
    choice1 = input("Press 1 if you want to log data \n 2 if you want to read data \n")
    if choice1 == "1":
        choice11 = input("What you want to log data into? \n Press 1 for Diet \n Press 2 for Excercise \n")
        if choice11 == "1":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Baladiet.txt" , "a")
            time= str(getdate())
            f.write(time)
            f.write("  ")
            f.write(  input("Enter the food items: \n ") )
            f.write("\n")
            f.close()
        elif choice11 == "2":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Balaex.txt" , "a")
            time= str(getdate())
            f.write(time)
            f.write("  ")
            f.write(  input("Enter the excercises performed: \n"))
            f.write("\n")
            f.close()
        else:
            print("Please enter the correct keyword")
    elif choice1 == "2":
        choice11 = input("What data you want to read? \n Press 1 for Diet \n Press 2 for Excercise \n")
        if choice11 == "1":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Baladiet.txt" , "r")
            print(f.read())
            f.close()
        elif choice11 == "2":
            f = open("E:\Python Prctise Programs\Python code with Harry\Excercise 5 (Heath Programme)\Excercise 5 text files\Balaex.txt" , "r")
            print(f.read())
            f.close()
        else:
            print("Please enter the correct keyword")
        print()
    else:
        print("Please enter the correct keyword")
        
if clientno == 1:
    Swaraj()
elif clientno == 2:
    Martin()
elif clientno == 3:
    Bala()
else:
    print("Please enter the right client no.")



    
