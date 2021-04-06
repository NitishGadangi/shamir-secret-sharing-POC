import random

def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1

#return --> prime number greater than given input
def getPrime(greaterThan):
	primes = []
	num = greaterThan + 1
	while True:
		if(isPrime(num)):
			break
		num = num + 1
	return num

#p: prime number for feild
#returns --> co-efficients randomly generated, required to form the polynomial equation
def getCoefficients(p, k, key):
	coefficients = []
	while True:
		if k == 1:
			break
		temp = random.randint(1,p)
		if temp not in coefficients:
			k = k-1
			coefficients.append(temp)
	coefficients.append(key)
	coefficients.reverse()
	return coefficients

#x: number of shares required (x>k)
#p: prime number for feild
#k: threshold for minimum number of shares required for reconstruction
#key: key which is to be shared
#returns --> x number of shares as array
def y_x(x, p, k, key):
	coefficients = getCoefficients(p, k, key)
	result = []
	for j in range(1,x+1):
		share = 0
		for i in range(0,k):
			share = share + coefficients[i]*(j**i)
		result.append(share)
	return result

#f_x_arr: list of f(x) values, here in this case list of share vales
#x_arr: list of x values, here in this case list of share numbers
#returns --> constructs polynomial using langranges interpolation and returns the constant value
def langrange_constant(f_x_arr, x_arr, k):
	result = 0
	for i in range(k):
		temp = f_x_arr[i]
		for j in range(k):
			if j != i:
				temp=temp*((0 - x_arr[j])/(x_arr[i]-x_arr[j]))
		result = result + temp
	return result

#n: number of shares required (n>k)
#k: threshold for minimum number of shares required for reconstruction
#key: key which is to be shared
#returns --> n number of shares as array
def generate_shares(key, k, n):
	p = getPrime(key)
	shares = y_x(n, p, k, key)
	return shares

#all_shares: list of all the n shares generated
#returns --> asks to specify k shares using which the key will be reconstructed and returned
def reconstruct_key(all_shares, k):
	print(f"Enter {k} share numbers between 1 and {len(all_shares)}:")
	share_nums = []
	for i in range(1,k+1):
		num = input(f"{i}th share number:")
		share_nums.append(int(num))
	shares = []
	for num in share_nums:
		shares.append(all_shares[num-1])
	return int(langrange_constant(shares, share_nums, len(shares)))

if __name__=="__main__":
	key = 120 #key which is to be shared
	k = 3 #minimun shares required to regenerate
	n = 5 #number of shares to be generated
	all_share = generate_shares(key, k, n)
	print(all_share)
	key = reconstruct_key(all_share, k)
	print(key)

