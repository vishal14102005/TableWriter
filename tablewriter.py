print("Simple Table Writer")
print("Programmer Vishal Tyagi")

while True:
    x = input("Enter A Number or Press e to exit: ") #takes number input
    if x !='e':
        try:
            x= int(x)
            for i in range(1,11):
                print(x,"X",i,"=",x*i)
        except ValueError:
            print("Error: Invalid Input")
    else:
        print("Have a Good Day... :)")
        break

    