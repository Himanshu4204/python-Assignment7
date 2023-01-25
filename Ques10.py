# Q10. Write a program to display day name on the basis of user’s liking of a colour. Ask user for his favorite colour. 
#       User can answer in a sentence like “I like red colour”.Assuming all colour name entered by user is in lowercase.
#       Use match case to displayday name associated with the colour.
#                a. Yellow - Monday
#                b. Blue - Tuesday
#                c. Orange - Wednesday
#                d. White - Thursday
#                e. Black - Friday
#                f. Red - Saturday
#                g. All other colours - Sunday

a=input("Enter Your Favourit colour:").lower()
match a:
    case a if 'red' in a:
        print("saturday")
    case a if 'white' in a:
        print("Sunday")
    case a if 'yellow' in a:
        print("Monday")
    case a if 'blue' in a:
        print("Tuesday")
    case a if 'orange' in a:
        print("Wednesday")
    case a if 'black' in a:
        print('Friday')
    case _:
        print("Sunday")
        