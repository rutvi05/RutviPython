#Q6 Functions
def q6(n):
    lst = []
    for i in range(1,n+1):
        tup = (i ,i**2 ,i**3)
        a = print(tuple(tup))
        lst.append(tup)# aa khatarnak hatu
    print(lst)


q6(int(input(f"Enter the Number: ")))
        
