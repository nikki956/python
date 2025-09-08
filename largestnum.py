def largest_of_three(a,b,c):
    res=" "
    if a>=b and a>=c:
        res="Largest number is:"+str(a)
    elif b>=a and b>=c:
        res="largest number is :"+str(b)
    else:
        res="largest number is:"+str(c)
    return res
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
print(largest_of_three(a,b,c))
