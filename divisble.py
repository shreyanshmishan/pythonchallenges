numn=int(input("enter a number (numerator) "))
print(f"the numerator is {numn}")
numd=int(input("enter a number(denominator) "))
print(f"the denominator is {numd}")
if numn%numd==0:
    print(numn, "is divisible by", numd)
else:
    print(f"{numn} is not divisible by {numd}")