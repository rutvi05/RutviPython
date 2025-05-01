#Loops Q 3
a = 0
d = 0
x = input("Enter the String: ")
for i in x:
    if i.isalpha() == True:
        a = a + 1
    elif i.isdigit() == True:
        d = d + 1

print("The Number of Alphabets: ",a)
print("The Number of Digits: ",d)
