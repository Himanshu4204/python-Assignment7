# Q5. Write a program which takes a number from user. Print Saurabh Shukla if the number
#         is even, print Prateek Jain if the number is negative odd number and print Aditya
#         Choudhary if number is positive odd number.
x=int(input("Enter a Number"))
match x:
    case x if x%2==0:
        print("Saurabh Shukla")
    case x if x%2==1 and x<0:
        print(" Prateek Jain")
    case x if x%2==1 and x>0:
        print("Aditya choudhary")