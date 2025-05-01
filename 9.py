#Q9 List
lst1 =[1,12,13,14,15,23,24,25]
lst2 =[2,3,12,13,34,23,45,65,1]
lst3 =[]
for i in range(len(lst1)):
    if (i in lst1 and i in lst2) == True:
        lst3.append(i)

print(lst3)
