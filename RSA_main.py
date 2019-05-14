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

def make_hex_str(message):
	hex_message = str(message)
	message = bytearray.fromhex(hex_message).decode()
	return message

def crypt_message(message, e, n):
	crypted =hex(pow(int(message,16), e, n))
	return crypted[2:]

def decrypt_message(message, d, n):
	message = int(message, 16)
	decrypded = hex(pow(message, d, n))
	return decrypded[2:]

def calculate_semi_random():
	found_prime = False
	while not found_prime:
		p = random.randint(2**256, 2**257)
		found_prime = is_prime(p)
	return p

def calculate_n(p, q):
	return p*q

def calculate_CTF(p, q):
	return (p-1)*(q-1)


def is_prime(x):
	return miller_rabin(x)


def calculate_e(CTF):
	e = 2
	have_found_e = False
	while not have_found_e:
		e = random.randint(2**16, CTF-1)
		if is_prime(e):
			have_found_e = True

	return e

def calculate_d(CTF, e):
	return gcdExtended(CTF, e)

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



def gen_priv_and_pub_key(): #or GET_KEYS()
	p = calculate_semi_random()
	q = calculate_semi_random()
	n = calculate_n(p,q)
	CTF = calculate_CTF(p, q)
	e = calculate_e(CTF)
	d = calculate_d(CTF, e)
	priv = open("priv.txt", "w+")
	priv.write(str(n) + "\n" + str(d))
	pub = open("pub.txt", "w+")
	pub.write(str(n) + "\n" + str(e))

def encrypt(filename, keyfile="pub.txt"):
	keys = open(keyfile, "r")
	n, e = keys.readlines()
	e = int(e)
	n = int(n)
	message = open(filename, "r")
	encrypded_file_name = "encrypded_" + filename
	encrypded_file = open(encrypded_file_name, "w+")
	message_str = message.read()
	counter = 0
	while counter < len(message_str):
		part_of_message = message_str[counter: counter + 100]
		crypted = internal_encrypt(part_of_message, e, n) + "\n"
		encrypded_file.write(crypted)
		counter += 100

	keys.close()
	message.close()
	encrypded_file.close()


def internal_encrypt(message, e, n):
	massage_hex = make_message_hex(message)
	crypted = crypt_message(massage_hex, e, n)
	return crypted

def decrypt(filename, keyfile="priv.txt"):
	keys = open(keyfile, "r")
	n, d = keys.readlines()
	n = int(n)
	d = int(d)
	crypded_message = open(filename, "r")
	decrypded_file_name = "decrypded_" + filename
	decrypded_file = open(decrypded_file_name, "w+")
	crypded = crypded_message.readlines()
	for line in crypded:
		line = line[:-1]
		clearText = internal_decrypt(line, d, n)
		#print(clearText)
		decrypded_file.write(clearText) #cleartext[-1]???

	keys.close()
	crypded_message.close()
	decrypded_file.close()


def internal_decrypt(code, d, n):
	decrypded = decrypt_message(code, d, n)
	clearText = make_hex_str(decrypded)
	return clearText


def main():
	gen_priv_and_pub_key()
	'''
	p = calculate_semi_random()
	print("p  : ",p)
	q = calculate_semi_random()
	print("q  : ",q)
	n = calculate_n(p,q)
	print("n  : ",n)
	CTF = calculate_CTF(p, q)
	print("CTF : ",CTF)
	e = calculate_e(CTF)
	print("e  : ",e)
	d = calculate_d(CTF, e)
	print("d   : ",d, "\n")
	'''
	#massage = "Hej Mousse"
	#print("message: ", massage)
	#massage_hex = make_message_hex(massage)
	#print("massage_hex: ", massage_hex)
	#crypted = crypt_message(massage_hex, e, n)
	#print("Crypded: ", crypted)
	#decrypded = decrypt_message(crypted, d, n)
	#print("Decrypded: ", decrypded)
	#clearText = make_hex_str(decrypded)

	encrypt("test.txt")
	decrypt("encrypded_test.txt")


if __name__ == '__main__':
	main()
