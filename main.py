import pyAesCrypt

password = input('Enter password: ')

# encrypt
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', passw=password)

# decrypt
# pyAesCrypt.decryptFile('data.txt.aes', 'data_output.txt', passw=password)
