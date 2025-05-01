#Q 4 Functions

"""
#METHOD 1
def sum_avg():
    total = 0
    for i in range(1,6):
        x = int(input(f"For {i}, Enter the Value: "))
        total = x + total
    print(f"The Total of all the subjects: {total}")
    avg = total / 5
    print(f"The average of all the Five Subjects: {avg}")


sum_avg()

"""

#METHOD 2

def sum_avg(s1,s2,s3,s4,s5):
    total = s1 + s2 + s3 + s4 + s5
    avg = total / 5
    print(f"The Total of all the five subjects: {total}")
    print(f"The average of all the five subjects: {avg}")


sum_avg(5,5,3,4,2)
