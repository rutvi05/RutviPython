#Loops 10 Generate N numbers of Fibonacci Series
n = int(input("Enter numbers of terms: "))
a,b = 0,1
for i in range(n):
    print(a)
    a,b = b, a+b
print()

