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
	i = 0
	while i < x/2:
		if x%i == 0:
			return False
		i += 1

	return True


def calculate_e(CTF, p, q):
	e = 3:
	have_found_e = False
	while not have_found_e:
		if is_prime(e):
			if CTF%e != 0 and p%e != 0and q%e != 0:
				have_found_e = True

		e += 1

	return e
				






