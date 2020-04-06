#Solution to Figure Out SSS Problem Code: CTS1
#By Nitish Gadangi
#Refer Readme of the repo for detailed explanation of the operation

import random #for generating random numbers
from gf256 import GF256 #for making operations over Galois Field(256)

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

#for generating the polynomial
def y_x(a0,a1,x):
	return int((GF256(a0)+GF256(a1)*GF256(x)))

#lagranges function used for reconstruction
def lagrange(x0,x1,y0,y1):
	#havent done the mod operation using a prime number,how ever can be done if required
	return int(((GF256(0)-(GF256(x1))/(GF256(x0)-GF256(x1)))*GF256(y0))+((GF256(0)-(GF256(x0))/(GF256(x1)-GF256(x0)))*GF256(y1)))

def re_construct(share1,share2):
	x0=share1[0]
	x1=share2[0]
	print(f"\nre-constructing using share{x0} and share{x1}")
	secret=[]
	for i in range(1,len(share1)):
		secret.append(lagrange(x0,x1,share1[i],share2[i]))
	print(f"Decryted Secret: {secret}")

def generate_shares(secret,random_a1):
	share1=[1]	#adding share number as the first element of the list
	share2=[2]
	share3=[3]
	share4=[4]
	for key in secret:
		a0=key
		a1=random_a1
		share1.append(y_x(a0,a1,1))
		share2.append(y_x(a0,a1,2))
		share3.append(y_x(a0,a1,3))
		share4.append(y_x(a0,a1,4))
	return share1,share2,share3,share4

if __name__=="__main__":
	#list of secret keys
	secret=[152,115,147,193,161,68,64,121,166,171,81,154,136,118,93,133,118,63,51,128,138,160,208,186,147,72,174,92,65,154]
	print(f"secret: {secret}\n")
	#generate shares
	#here 256 is chosen,you can change it with any number required based on finite field
	share1,share2,share3,share4=generate_shares(secret,random.randrange(253))
	print(f"share1: {share1}")
	print(f"share2: {share2}")
	print(f"share3: {share3}")
	print(f"share4: {share4}")
	#reconstructing using any of the two shares
	#you can change shares,for instance here I opted to go with share 3 and 4
	re_construct(share3,share4)