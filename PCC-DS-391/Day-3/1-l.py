# l. 1
#    2 1 
#    3 2 1 
#    4 3 2 1 
#    5 4 3 2 1

for i in range(5):
    a = ''
    b = i + 1
    for j in range(i+1):
        a += str(b) + ' '
        b -= 1
    print(a)