for n in (6,10):

    A = n % 2 == 0 and n % 3 == 0

    B = n % 2 == 0 or n % 3 == 0

    print (A)
    print (B)