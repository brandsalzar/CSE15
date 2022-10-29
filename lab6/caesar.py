# Exercise 1: Convert a string of characters to a list of numbers by taking the ASCII value of the numbers
def chars_to_nums(c):#ord() for ascii return #chr() for chracter return
# Provide the correct implementation of this function
     char = list(c) #creates a list of iindividual character based on c and stores it on char
     num = []       #empty list to store the ascii values
     for i in char: #traversing char's individual character
         x = ord(i) # set x to the ascii value
         num.append(x)#append that value to the empty list
     return num     #return the list

print chars_to_nums("HELLO WORLD")

# Exercise 2: Convert a list of numbers to a string of characters by converting the ASCII values to characters
def nums_to_chars(n):#ord() for ascii return #chr() for chracter return
# Provide the correct implementation of this function
    num = n
    char = []
    for i in num:
        x = chr(i)
        char.append(x)
    return char
    #return "Not the correct result"

print nums_to_chars([40, 37, 44, 44, 47, 0, 55, 47, 50, 44, 36])

# Exercise 3: Implement an encode procedure for the Caesar cipher. It should take in the plaintext as a string, the key as an integer, and a modulus as an integer, which corresponds to the size of the alphabet, and produce the appropriate ciphertext. In most cases the modulus will be 95, since there are 95 printable ASCII characters that we can use. The pair (key, mod) makes up the encryption key.
def caesar_encode(plaintext, key, mod):#ord() for ascii return #chr() for chracter return
    # Provide the correct implementation of this function
    char = list(plaintext)  #how am I supposed to implement mod?
    cyphertext = []
    for i in char:
        daKey = ord(i) + key
        daMod = daKey % mod
        cyphertext.append(daMod)
    return cyphertext
    #return "Not the correct result"

print caesar_encode("HELLO", 3, 95)

# Exercise 4: Implement the decode procedure for the Caesar cipher. It should take in the ciphertext and the encryption key, and produce the plaintext.
def caesar_decode(ciphertext, key, mod): #ord() for ascii return #chr() for chracter return
    # Provide the correct implementation of this function
    #return "Not the correct result"
    char = list(ciphertext)
    daChar = []
    for i in char:
        daKey = ord(i) - key
        daMod = daKey % mod
        decrypt = chr(daMod)
        daChar.append(decrypt)
    plaintext = ''.join(daChar)
    return plaintext

print caesar_decode("KHOOR", 3, 95)

# Exercise 5: Assuming the following string was encoded with the Caesar cipher, using some unknown encryption key, recover the plaintext. Type your answer in the string 'ex_5_plaintext' below, do not include any characters in the string, other than the recovered plaintext:

ex_5_ciphertext = "-HIIJSYCMY=IIF"

char = list(ex_5_ciphertext)
daChar = []
mod = 95
key = 6
for j in 95:
    for i in char:
        daKey = ord(i) + key
        daMod = daKey % mod
        decrypt = chr(daMod)
        daChar.append(decrypt)
        plaintext = ''.join(daChar)
    print plintext
    #ex_5_plaintext = plaintext

#print "The message is:", ex_5_plaintext
