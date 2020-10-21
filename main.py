
import des
import sys
from RSA import generate_keypair,encrypt,decrypt
import struct

SIZE = 1024
des_key = 'secret_k'


# first generate the key pair, get these two numbers from the excel file
p = 1297273  # pretty sure these two values should be provided in excel spreadsheet
q = 1297651
public, private = generate_keypair(p, q)  # returns (e,n) and (d, n)

print("RSA Public Key pair = " + str(public))
print("RSA Private Key pair = " + str(private))

# read message from user
print("enter the DES key, 8 Characters")
des_key = input()

while len(des_key) != 8:  # ensure proper input length
    print("wrong! 8 characters. Try again:")
    des_key = input()

# encrypt the DES key
print("encrypting DES KEY with RSA")
des_encoded = [str(encrypt(public, chars)) for chars in des_key]
print("the encrypted key is " + str(des_encoded))

# encrypt the image with DES
print('encrypting image using DES')
file = open(r'penguin.jpg', "rb")
image_data = file.read()
file.close()
coder = des.des()  # des is a class defined in des.py
r = coder.encrypt(des_key, image_data, cbc=False)  # encrypted image

# write the encrypted image into file
r_byte = bytearray()
for x in r:
    r_byte += bytes([ord(x)])
file = open(r'penguin_encrypted.bin', "wb+")
file.write(r_byte)
file.close()

# recover DES Key
des_key_decoded = []
for data in des_encoded:
    cipher = int(data)
    des_key_decoded += decrypt(private, cipher)
print("DES key decoded = " + str(des_key_decoded))
print("decrypting the image with the recovered key")
decoder = des.des()
des_key_decoded_str = ''
for i in des_key_decoded:
    des_key_decoded_str = des_key_decoded_str + str(i)

rr = decoder.decrypt(des_key, r, cbc=False)  # this is in string  format, must convert to byte format
rr_byte = bytearray()
for x in rr:
    rr_byte += bytes([ord(x)])

# write to file to make sure it is okay
file2 = open(r'penguin_decrypted.jpg', "wb")
file2.write(bytes(rr_byte))
file2.close()
print('decypting image completed')

# Test to see if decryption worked correctly
if bytes(rr_byte) == image_data:
    print('image decoded successfully')
else:
    print('image not decoded correctly')


