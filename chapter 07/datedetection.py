import re
dateRegex = re.compile(r'\d{2}/\d{2}/\d{4}')
date = input("enter date: ")
aaa = dateRegex.search(date)
if aaa==None:
    print("you gave an non existent date")
else:
    day, month, year = date.split("/")
    day, month, year = int(day), int(month), int(year)
    
    feb = 28
    if year%4==0:
        feb = 29
    elif year%400==0:
        feb = 29
    elif year%100==0:
        feb=28
    
    days_of_months=[31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     
    if month>12:
        print("there cant be more than 12 months")
    elif day>days_of_months[-1]:
        print("this day does not exist")
    else:
        print("good")
