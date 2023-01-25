# Q2. Write a menu driven program to perform following operations - Addition, Subtraction,
#   Multiplication, Division ?
print("For Addition Enter'1':","For Subtraction Enter'2':","For Multiplication Enter'3':","For Division Enter'4':", sep='\n')
a=int(input('Enter Operation Number :'))
b=int(input("Enter First Number :"))
c=int(input("Enter Second Number :"))
match a:
    case 1:
        print("Addition is:",b*c)
    case 2:
        print("Subtraction is :",b-c)
    case 3:
        print("Multiplication is :",b*c)
    case 4:
        print("Division is :",b/c)
    case _:
        print("Default number")
        