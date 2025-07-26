n=input("Enter list elements:")
list=[int(x.strip()) for x in n.split(',')]
if(list[0] == list[-1]):
    print("True")
else:
    print("False")