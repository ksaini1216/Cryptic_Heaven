import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import Crypto.Util.Padding



# Prompt the user to enter a password which includes Char, Num or Special Charac.

Password = str(input('Password:'))
Password= Password.encode()

# Hash the password using the SHA-256 algorithm. 

Hpwd= hashlib.sha256(Password)

# Store password in text file

file= open("Hashed_Passwords.txt", 'a')
file.write(Hpwd.hexdigest() + '\n')

# Displaying hashed password on the screen

print ("Hashed Password:" + Hpwd.hexdigest())

# Prompt the user to enter a message for encryption.

Message = str(input('Enter a Message:'))

# Encrypt the message using AES in CBC mode.

Message_bytes= Message.encode('utf-8')
key = get_random_bytes(16)
iv= b"0123456789012345"
padding_length = 16- (len(Message_bytes) % 16)
padding_data = Message_bytes + bytes ([padding_length] * padding_length)
cipher= AES.new(key, AES.MODE_CBC, iv)
encrypted_data= cipher.encrypt(padding_data)

print("Encrypted_Value", encrypted_data )

# Save the encrypted message to a file named encrypted_message.bin.
file1= open("encrypted_message.bin", 'wb')
file1.write(encrypted_data)



# Decryption
file1= open("encrypted_message.bin", 'rb')
a=file1.read()
iv_File= b"0123456789012345"
cipher_decrypt = AES.new(key, AES.MODE_CBC, iv_File)
decrypted_data=cipher_decrypt.decrypt(a)


plain_text= Crypto.Util.Padding.unpad(decrypted_data, AES.block_size)
print ("Plain text", plain_text.decode('utf-8'))