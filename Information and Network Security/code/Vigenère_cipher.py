key = "hello"
value = "kmole"
code = "rqzws"

#Printing table
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
matrix = []

for i in range(26):
    row = []
    for j in range(26):
        row.append(alphabet[(i + j) % 26])
    matrix.append(row)

for row in matrix:
    print(" ".join(row))

#Encryption
print("Encrypted value : ", end = "")
for i in range(len(key)):
    print( chr(   (   (ord(value[i]) - 97) + (ord(key[i]) - 96)   ) % 27 + 96 ), end = "" )
print()

#Decryption
print("Decrypted value : ", end = "")
for i in range(len(key)):
    print( chr(   (   (ord(code[i]) - 96) - (ord(key[i]) - 97)   )  % 26 + 96 ), end = "" )