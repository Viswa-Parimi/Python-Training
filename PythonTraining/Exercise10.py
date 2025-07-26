a=[]
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
for i in range(len(list1)):
    if list1[i]%2 == 1:
        a.append(list1[i])
for j in range(len(list2)):
    if list2[j]%2 == 0:
        a.append(list2[j])
print(a)