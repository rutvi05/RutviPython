#Q4 Set
s = {'rutvi','Anshu','Aditya','aarambh','Aarushi','bavo','Bhavi','namrata','nikita'}
sA = set()
sB = set()

for i in list(s):
    k = i.upper()
    if k.startswith("A"):
        sA.add(k)
    elif k.startswith("B"):
        sB.add(k)



      
print(sA)
print(sB)
