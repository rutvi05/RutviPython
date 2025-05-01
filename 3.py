#Q3 Set
s = set()
lst = ['KLRahul','Hardik','Virat','Rohit','Krunal']
'''
for i in range(1,6):
    i = input(f'Enter {i} name: ')
    lst.append(i)
print(set(lst))
'''
s.update(lst)
print(s)


s.remove("Virat")
s.add("Sandhya")

s.remove("Hardik")
s.remove("Rohit")

print('The required set: ',s)

