#Joakim Skoog
#9709191135
#joaskoog



import random
import math


'''
gen_priv_and_pub_key()

generates two keys for encrypting and decrypting files. Those keys are saved as two textfiles.
Input: Nothing
Output: A privet key file, A public key file.
'''
def gen_priv_and_pub_key():
    pass

'''
encrypt(filename, keyfile="pub.txt")

This function encrypts the content of a given file and puts the content in another text file of name "encrypted_(filename).txt"
Input: filename (STR) of the file you want to encrypt, filename of the key file you want to use to encrypt (STR) default "pub.txt"
Output: a file with name "encrypted_(filename).txt" that contanes the crypteded content of "filename"
'''
def encrypt(filename, keyfile="pub.txt"):
    pass



'''
decrypt(filename, keyfile="priv.txt")

This function decrypts the content of a given file and puts the content in another text file of name "decrypted_(filename).txt"
Input: filename (STR) of the file you want to decrypt, filename of the key file you want to use to decrypt (STR) default "priv.txt"
Output: a file with name "decrypted_(filename).txt" that contanes the decrypteded content of "filename"
'''
def decrypt(filename, keyfile="priv.txt"):
    pass

'''
internal_encrypt(message, e, n)

Takes a message and encryption keys and encrypts message.

Input: message (STR), e (INT), n (INT)
Output: A string that is the encrypted verson of message (STR)
'''
def internal_encrypt(message, e, n):
    return crypted
'''
internal_decrypt(code, d, n)

Takes a message and decryption keys and decrypts code.

Input: code (STR), d (INT), n (INT)
Output: A string that is the decrypted verson of code (STR)
'''
def internal_decrypt(code, d, n):
    return clearText

'''
calculate_semi_random(lower_bond = 256, higher_bond = 257)

This funktion computes two primes that are somewhat random. The funktion guesses a number between lower_bond and higher_bond.
Then it tests if this number is a prime with probebilety testing. If the number is not a prime the function guesses another number.

Input: lower_bond (INT) default 256, higher_bond default 257 (INT)
Output: A semirandom prime (INT). The size of wich is 2^lower_bond < p < 2^higher_bond
'''
def calculate_semi_random(lower_bond = 256, higher_bond = 257):
    return p
