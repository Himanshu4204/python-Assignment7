# Q9. 9. Write a python script to check whether a given year is
#                a. Non century leap year
#                b. Century leap year
#                c. Non century non leap year
#                d. Century non leap year

print(" 'a'Non Century Leap year","'b' Century leap year","'c'Non Century non Leap year","'d'Century non leap year",sep='\n')
x=input("Enter One Option :")
year=int(input("Enter Year :"))
match x:
    case 'a' if year%400!=0:
        print(year,"Non century leap year")
    case 'b' if year%400==0:
        print(year,"Century leap year")
    case 'c' if year%100!=0 and year%4!=0:
        print(year,"Non Century non Leap year")
    case 'd' if year%100==0 and year%4!=0:
        print(year,"century non leap year")

