# Lab2
'''
I excluded using the board as we can code first and then move over to board as long as we are using the same version of python

Part1:
In the code folder, open RSA.py
Complete the following functions using Python3 (not Python or Python2)
get_d(): this function calculates the d value using the Extended Euclidean algorithm
generate_keypair(): this function accepts the p and q values and returns the public and private keypairs, uses get_d() and gcd functions
encrypt(): this function accepts one character and the keypair and performs encryption
decrypt(): this function accepts one character and performs decryption

Part2:
In this part, you will implement the DES encryption algorithm. 
You can start by reviewing DES 
This link gives a practical step-by-step explanation of DES
http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
Remember that the board Linux does not have NumPy installed so you need to implement every function with basic data structures (e.g. list)
Sufficient explanation is given in the accompanied Python files to help you complete the implementation

Go to the des.py file in the code folder, it is implemented as a class. Implement the following functions in des.py
Implement compute_s_box() function which returns the binary value for the 4-bit output of the S-box based on the 6-bit input block. This function returns a string, for example the input is ‘101010’ and the output is ‘1100’ (you can use binvalue() function from des.py!)
Implement substitute() function which accepts d_e, a string of 48 bits and returns another list which is substituted using the S_BOX

Part3:
This is the main code that you will run during the demo. No need to write any function here
There are two variables p and q. Each group will need to find their corresponding p and q values from the Prime_numbes.xlsx project file
	group numbers can be found in the online spreadsheet (here)
Again! Use python3 and not python or python2
The main code will ask for an 8-character DES key from you, perform RSA encryption and decryption on the key, and will also perform DES encryption and decryption on the penguin.jpg image (project file)
Successful implementation of RSA will result in correct key in the command line.
Successful implementation of DES will result in a penguin_decrypted.jpg image that can be opened in your PC as a JPEG image similar to penguin.jpg


'''
