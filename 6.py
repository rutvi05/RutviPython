#Loop Q 6


for i in range(1,25):
    if 1 <= i <= 11:
        print(i,"AM")
    elif i == 12:
        print(i,"Noon")
    elif 13 <= i <= 23:
        print(i,"PM")
    else:
        print(i,"Midnight")
