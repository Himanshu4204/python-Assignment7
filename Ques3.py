# Q3. Write a menu driven program with the following options:
#       a. Check whether a given set of three numbers are lengths of an isosceles  triangle or not
#       b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
#       c. Check whether a given set of three numbers are equilateral triangle or not
#       d. Exit.
l=int(input("Enter Length of First Side :"))
b=int(input("Enter Length of second Side :"))
h=int(input("Enter Length of Third Side :"))
print("Enter'a' if You check Isosceles Triangle")
print("Enter'b' if You check Right Angled Triangle")
print("Enter'c' if You check Equilateral Triangle")
print("Enter 'd' for Exit")
x=str(input('Enter One Option for check:'))
match x:
    case 'a':
        if l is b or b is h or h is l:
            print("Isosceles Triangle")
        else:
            print("Not Isosceles Triangle")
    case 'c':
        if l==b==h:
            print("Equilateral Triangle")
        else:
            print("This is not Equilateral Triangle")
    case 'b':
        if l**2==b**2+h**2 or b**2==l**2+h**2 or h**2==l**2+b**2:
            print("Right Angled Triangle")
        else:
            print("This is not Right Angled Triangle")
    case 'd':
        exit()
    case _:
        print("Default Value")



