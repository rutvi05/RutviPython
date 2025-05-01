#Q2 Set
import random
s = set()
lst = []
for i in range(10):
    x = random.randint(15,45)
    lst.append(x)
print(lst)

a = 0
for i in lst:
    if i < 30:
        a = a + 1
print("Digits less than 30: ",a)

for h in lst:
    if h > 35:
        lst.remove(h)

print("The Required Set is: ",set(lst))
    
