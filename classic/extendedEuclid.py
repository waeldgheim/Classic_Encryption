def extendedEuclid(a, m): #basic extended euclid function, same as one used in class, directly implemented from slides
    A2 = 0
    A3 = m
    B2 = 1
    B3 = a
    
    while B3 != 1 and B3 != 0:
        Q = A3 // B3
        (A2, A3, B2, B3) = (B2, B3, A2 - Q * B2, A3 - Q * B3)
        
    if B3 == 1:
        return str(B2%m)
    else:
        return "No inverse"
        
        