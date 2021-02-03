def gcd(m,n):
    
    # Factors of m
    m_factor = [x for x in range(1,m+1) if m % x == 0]

    # Factors of n
    n_factor = [x for x in range(1,n+1) if n % x == 0]

    # return the largest number that appears on both lists
    factor_list = []
    for i in m_factor:
        if i in n_factor:
            factor_list.append(i)
    return max(factor_list)

print(gcd(14,63))