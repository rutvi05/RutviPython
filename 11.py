#Q 11 Functions
def create_list():
    lst1 = ['Rutvi','Solanki','Sandhya','Giriraj']
    lst2 = ['Solanki','Aditya','Raj','Anshu','Sandhya','Giriraj']
    lst3 = []
    x = set(lst1)
    y = set(lst2)

    for i in x:
        for a in y:
            if i == a:
                lst3.append(i)
            else:
                pass

    print("The Intersection List is: ",lst3)


create_list()
