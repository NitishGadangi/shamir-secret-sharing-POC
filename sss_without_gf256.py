import random
# from gf256 import GF256 

def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1

def getPrime(greaterThan):
	primes = [i for i in range(greaterThan,greaterThan+100) if isPrime(i)]
	n = random.choice(primes)
	return n

def y_x(a0,a1,x,p):
	return ((a0+a1*x)%p)

def lagrange(x0,x1,y0,y1):
	return int(((-x1/(x0-x1))*y0)+((-x0/(x1-x0))*y1))

def re_construct(share1,share2):
	x0=share1[0]
	x1=share2[0]
	secret=[]
	for i in range(1,len(share1)):
		secret.append(lagrange(x0,x1,share1[i],share2[i]))
	print(f"\n\nDecryted Secret: {secret}")

def generate_shares(secret,random_a1):
	share1=[1]
	share2=[2]
	share3=[3]
	share4=[4]
	p=getPrime(random_a1)
	for key in secret:
		a0=key
		a1=random_a1
		share1.append(y_x(a0,a1,1,p))
		share2.append(y_x(a0,a1,2,p))
		share3.append(y_x(a0,a1,3,p))
		share4.append(y_x(a0,a1,4,p))
	print(f"share1: {share1}")
	print(f"share2: {share2}")
	print(f"share3: {share3}")
	print(f"share4: {share4}")
	re_construct(share3,share4)

#array of length 30
secret=[160,147,149,118,149,110,193,165,174,175,163,199,158,188,108,83,98,128,137,111,97,193,167,146,166,113,195,130,173,178]
print(f"secret: {secret}\n\n")
#253 is basically a random number chosen such that it is greator than all the the keys above
generate_shares(secret,253)