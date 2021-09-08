weight=float(input("Enter weight= "))
units=input("(L)bs or (K)g= ")
if units.upper() == "L":
    output = 0.45  *  weight
    print(f"Your weight is:{output} kilos ")
elif units.upper() == "K":
    out = 2.20 * weight
    print(f"Your weight is {out} pounds")
else:
    print("invalid unit")