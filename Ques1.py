# Q1. Write a python script to display number of days of a given Month?
a=int(input("Enter a Month"))
match a:
    case a if a in (1,3,5,7,8,10,12):
        print("31 Days in this Month")
    case a if a in (4,6,9,11):
        print("30 Days in this Month")
    case 2:
        print("28 or 29 Days in this Month")
    case _:
        print("Enter a Valid Month")
        