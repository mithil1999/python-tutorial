name=input("Enter name:   ")
if (len(name))<3:
    print("name must hv min 3 characters")
elif(len(name))>15:
    print("name can hv max of 15")
else:
    print("good name! ")