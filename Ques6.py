# Q6.Write a python program to check whether a given string is a multiword string or single
#    word string using match case statement?
x=str(input("Enter a Word :"))
match x:
    case x if ' ' in x:
        print("Multi Word ")
    case x if ' ' not in x:
        print("Single Word ")