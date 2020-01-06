import nltk
from nltk.corpus import words
nltk.download('words')

def encrypt(string,key): 
    encrypt_text = " " 
  
    for i in range(len(string)): 
        char = string[i] 
   
        if (char.isupper()): 
            encrypt_text += chr((ord(char) + key-65) % 26 + 65) 
  
        else: 
            encrypt_text += chr((ord(char) + key - 97) % 26 + 97) 
  
    return encrypt_text 

def decrypt(string,key):  
    decrypt_text = " " 
  
    for i in range(len(string)): 
        char = string[i] 
   
        if (char.isupper()): 
            decrypt_text += chr((ord(char) - key-65) % 26 + 65) 
  
        else: 
            decrypt_text += chr((ord(char) - key - 97) % 26 + 97) 
  
    return decrypt_text 
  

""" Testing out inputs"""
string = input("enter string: ")
key = int(input("enter key number: "))
print("original string: ", string)
print("after encryption: ", encrypt(string, key))
string = input("enter encrpyted string: ")
print("decryption: ", decrypt(string, key))