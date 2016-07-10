'''
By Eng. Abed Eid
'''


#prime number
i=2;j=2
while i<=100:
    while (j<=(i/j)):
        if not (i%j):
            break
        j=j+1
    if (j>i/j):
      print i," is prime"
    i=i+1