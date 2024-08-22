# m. 5 4 3 2 1
#    4 3 2 1 
#    3 2 1 
#    2 1 
#    1

n=5
for i in range(5):
    a = ''
    b = n
    for j in range(n):
        a += str(b)
        b -= 1
    n -= 1
    c = ' '.join(a)
    print(c)