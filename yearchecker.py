def leap_year_checker(year):
    if((year%4==0 and year %100!=0)or (year%400==0)):
        res=str(year)+"is a leap year"
    else:
        res=str(year)+"is not a leap year"
    return res
year=int(input("Enter year:"))
print(leap_year_checker(year))
