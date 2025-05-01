#Loops8 Print the factorial of the number
x = int(input("Enter the number: "))

def fact(x):
    fact = 1
    for i in range(1,x+1):
        fact *= i
    return fact

print("Factorial of the given number: ",fact(x))
