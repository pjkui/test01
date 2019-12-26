
def quick_mod(a,p,n): 
	result = a % n
	remainders = []
	while p != 1:
		remainders.append(p & 1)
		p = p >> 1
	print(remainders)
	while remainders:
		rem = remainders.pop()
		result = ((a ** rem) * result ** 2) % n
	return result
def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result

# t = quick_mod(1234567,12345678901234567890,999999997)
t = fastExpMod(1234567,12345678901234567890,999999997)
print(t)