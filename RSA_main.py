#Joakim Skoog
#9709191135
#joaskoog



import random
import math



'''
make_message_hex(message)

This funktion takes a message of type str. And outputs a sting containing the ascii index of each caracter.

Input: message of type STR
Output: A hexadecimal number with the same value as the input message (typ STR)
'''
def make_message_hex(message):
	outPutString = ""
	for letter in message:
		value = hex(ord(letter))
		if len(value) < 4:
			value = "0x0" + value[2]
		outPutString += value[2:]

	return outPutString




"""
make_hex_str(message)

Takes a hexadecimal number and outputs the characters that number reprisent.
Input: A hexadecimal number (without 0x in the start)
Output: A string with the coresponding characters
"""
def make_hex_str(message):
	hex_message = str(message)
	message = bytearray.fromhex(hex_message).decode()
	return message



'''
crypt_message(message, e, n)

Makes a hexadecimal number cryptaded. This funktion takes a hexadecimal number "message" and computes the following function.
(message^e) mod n

Input: hexadecimal number message, integer e, integer n
Output: hexadecimal number without 0x at start
'''
def crypt_message(message, e, n):
	crypted =hex(pow(int(message,16), e, n))
	return crypted[2:]




'''
decrypt_message(message, d, n)

Makes a hexadecimal number decryptaded. This funktion takes a hexadecimal number "message" and computes the following function.
(message^d) mod n

Input: hexadecimal number message, integer d, integer n
Output: hexadecimal number without 0x at start
'''
def decrypt_message(message, d, n):
	message = int(message, 16)
	decrypded = hex(pow(message, d, n))
	decrypded = decrypded[2:]
	if len(decrypded) % 2 == 1:
		decrypded = "0" + decrypded
	return decrypded




'''
calculate_semi_random(lower_bond = 256, higher_bond = 257)

This funktion computes two primes that are somewhat random. The funktion guesses a number between lower_bond and higher_bond.
Then it tests if this number is a prime with probebilety testing. If the number is not a prime the function guesses another number.

Input: lower_bond (INT) default 256, higher_bond default 257 (INT)
Output: A semirandom prime (INT). The size of wich is 2^lower_bond < p < 2^higher_bond
'''
def calculate_semi_random(lower_bond = 256, higher_bond = 257):
	found_prime = False
	while not found_prime:
		p = random.randint(2**lower_bond, 2**higher_bond)
		found_prime = is_prime(p)
	return p



'''
calculate_n(p, q)

Calculates n where n is p * q.

Input: p (INT) should be a big prime, q (INT) should be a big prime.
Output: n (INT) n = p*q
'''
def calculate_n(p, q):
	return p*q




'''
calculate_CTF(p, q)

Compuets the Carmichael's totient function of n. Since p, q is primes then n = (p-1) * (q-1)

Input: p (INT) that is a big prime, q (INT) that is a big prime
Output: CTF (INT) that is the Carmichael's totient function of n
'''
def calculate_CTF(p, q):
	return (p-1)*(q-1)




'''
is_prime(x)
checks if x is a prime. This function can give false posetives if x is big but those are rare. This funktion can't give false negatives.

Input: x that is a big int.
Output: True if x is likly a prime, and False if x is not a prime.
'''
def is_prime(x):
	return miller_rabin(x)





'''
calculate_e(CTF, lower_bond = 16)

Finds a "e" that is smaler then CTF and bigger than 2^lower_bond (default = 16).
E is a prime number.

Input: CTF (INT), lower_bond (INT) 2^lower_bond needs to be smaler then CTF.
Output: e (INT)
'''
def calculate_e(CTF, lower_bond = 16):
	e = 2
	have_found_e = False
	while not have_found_e:
		e = random.randint(2**lower_bond, CTF-1)
		if is_prime(e):
			have_found_e = True

	return e




'''
calculate_d(CTF, e)

Calculates a "d" that satisfies the folwing ecuation. (d*e) mod CTF = 1 mod CTF.

Input: CTF (INT), e (INT)
Output: d (INT)
'''
def calculate_d(CTF, e):
	return gcdExtended(CTF, e)




"""
miller_rabin(n)

Calculets if n is likley a prime number using miller-rabin's probebelistik test. If n is likly a prime this function will return True else False.
This test is not 100% accuret for large nonprimes. It can give false posetives. But the risk is small.

Input: n (INT)
Output: True if n is likly a prime, False if n is not a prime
"""
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
				if pow(a, nTmp, n) == 1:
					pass
				else:
					return False

		return True



'''
gcdExtended(CTF, e)

Calculets the solotion to the folowing ecuation using the Extended Euclidean algorithm: (d*e) mod CTF = 1 mod CTF.

Input: CTF (INT), e (INT)
Output: d (INT) where d is the solotion to (d*e) mod CTF = 1 mod CTF
'''
def gcdExtended(CTF, e):
	s = 0
	r = CTF

	old_s = 1
	old_r = e
	while r != 0:
		q = old_r // r
		tmp = r
		r = old_r - (q * r)
		old_r = tmp


		tmp = s
		s = old_s - (q * s)
		old_s = tmp

	if old_s < 0:
		old_s += CTF

	return old_s




'''
gen_priv_and_pub_key()

generates two keys for encrypting and decrypting files. Those keys are saved as two textfiles.
Input: Nothing
Output: A privet key file, A public key file.
'''
def gen_priv_and_pub_key():
	p = calculate_semi_random()
	q = calculate_semi_random()
	n = calculate_n(p,q)
	CTF = calculate_CTF(p, q)
	e = calculate_e(CTF)
	d = calculate_d(CTF, e)
	priv = open("priv.txt", "w+")
	priv.write("n:"+str(n) + "\nd:" + str(d))
	pub = open("pub.txt", "w+")
	pub.write("n:"+str(n) + "\ne:" + str(e))




'''
encrypt(filename, keyfile="pub.txt")

This function encrypts the content of a given file and puts the content in another text file of name "encrypted_(filename).txt"
Input: filename (STR) of the file you want to encrypt, filename of the key file you want to use to encrypt (STR) default "pub.txt"
Output: a file with name "encrypted_(filename).txt" that contanes the crypteded content of "filename"
'''
def encrypt(filename, keyfile="pub.txt"):
	keys = open(keyfile, "r")
	n, e = keys.readlines()
	e = int(e[2:])
	n = int(n[2:])
	message = open(filename, "r")
	encrypded_file_name = "encrypded_" + filename
	encrypded_file = open(encrypded_file_name, "w+")
	message_str = message.read()
	counter = 0
	while counter < len(message_str):
		part_of_message = message_str[counter: counter + 40]
		crypted = internal_encrypt(part_of_message, e, n) + "\n"
		encrypded_file.write(crypted)
		counter += 40

	keys.close()
	message.close()
	encrypded_file.close()





'''
internal_encrypt(message, e, n)

Takes a message and encryption keys and encrypts message.

Input: message (STR), e (INT), n (INT)
Output: A string that is the encrypted verson of message (STR)
'''
def internal_encrypt(message, e, n):
	massage_hex = make_message_hex(message)
	crypted = crypt_message(massage_hex, e, n)
	return crypted





'''
decrypt(filename, keyfile="priv.txt")

This function decrypts the content of a given file and puts the content in another text file of name "decrypted_(filename).txt"
Input: filename (STR) of the file you want to decrypt, filename of the key file you want to use to decrypt (STR) default "priv.txt"
Output: a file with name "decrypted_(filename).txt" that contanes the decrypteded content of "filename"
'''
def decrypt(filename, keyfile="priv.txt"):
	keys = open(keyfile, "r")
	n, d = keys.readlines()
	n = int(n[2:])
	d = int(d[2:])
	crypded_message = open(filename, "r")
	decrypded_file_name = "decrypded_" + filename
	decrypded_file = open(decrypded_file_name, "w+", encoding="utf-8")
	crypded = crypded_message.readlines()
	for line in crypded:
		line = line[:-1]
		clearText = internal_decrypt(line, d, n)
		#print(clearText)
		decrypded_file.write(clearText) #cleartext[-1]???

	keys.close()
	crypded_message.close()
	decrypded_file.close()





'''
internal_decrypt(code, d, n)

Takes a message and decryption keys and decrypts code.

Input: code (STR), d (INT), n (INT)
Output: A string that is the decrypted verson of code (STR)
'''
def internal_decrypt(code, d, n):
	decrypded = decrypt_message(code, d, n)
	clearText = make_hex_str(decrypded)
	return clearText





'''
main()

generates priv and pub keys.

encrypts the content of "test.txt"

decrypts the content of "encrypded_test.txt"
'''
def main():
	gen_priv_and_pub_key()
	encrypt("test.txt")
	decrypt("encrypded_test.txt")

if __name__ == '__main__':
	main()
