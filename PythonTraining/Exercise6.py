n=input("enter list numbers:")
a=[int(x.strip()) for x in n.split(',')]
for i in a:
    if i%5 == 0:
        print(i)
    