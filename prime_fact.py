def get_prime_factors(number):
    
    if number == 1:
        return []

    for i in range(2, number):
        
        rd, qt = divmod(number, i)
        if not qt: 
            return [i] + get_prime_factors(rd)

    return [number]

inp=int(input(''))
out=get_prime_factors(inp)

out=[str(m) for m in out]
print(' '.join(out))
