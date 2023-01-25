# Q7. Write a python script to whether a given number is positive ,negative or Zero using match case statement ?
x=int(input("Enter a Number :"))
match x:
    case x if x>0:
        print("Positive Number")
    case x if x<0:
        print("Negative Number")
    case x if x==0:
        print("Zero")