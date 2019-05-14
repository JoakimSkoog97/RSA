import random
import math

def make_message_hex(message):
	outPutString = ""
	for letter in message:
		value = hex(ord(letter))
		if len(value) < 4:
			value = "0x0" + value[2]
		outPutString += value[2:]

	return outPutString

def crypt_message(message, e, n):
	return (message**e)%n

def calculate_two_semi_random():
	return 10007, 997

def calculate_n(p, q):
	return p*n

def calculate_CTF(p, q):
	return (p-1)*(q-1)


def is_prime(x): #Bad Alg
	i = 2
	while i < x:
		if x%i == 0:
			return False
		i += 1

	return True


def calculate_e(CTF, p, q):
	e = 3
	have_found_e = False
	while not have_found_e:
		if is_prime(e):
			if CTF%e != 0 and p%e != 0and q%e != 0:
				have_found_e = True

		e += 1

	return e
				
def calculate_d(CTF, e):
	pass

def miller_rabin(n):
	nTmp = n
	aList = [2, 3, 5, 7, 11, 13, 
			17, 19, 23, 29, 31, 37, 
			41, 43, 47, 53, 59, 61, 
			67, 71, 73, 79, 83, 89, 
			97, 101, 103, 107, 109, 
			113, 127, 131, 137, 139, 
			149, 151, 157, 163, 167, 
			173, 179, 181, 191, 193, 
			197, 199]
	if nTmp % 2 ==0 or nTmp%3 ==0:
		return False

	else:
		nTmp -= 1
		s = 0
		while nTmp %2 != 0:
			s += 1
			nTmp = nTmp /2

		for a in aList:
			if a < nTmp:
				if (a**nTmp)%n == 1 and (a**nTmp)%n == 1 and (a**nTmp)%n == 1:
					pass
				else:
					return False

		return True

for a in range(4,100000):
	print(miller_rabin(a),":", is_prime(a), ":", a)
	assert(miller_rabin(a) == is_prime(a))




