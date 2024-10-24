def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
text = input("Enter the text to be encrypted : ")
s = int(input("Enter the number of keys to be shifted : "))
encryptedStr = encrypt(text,s)
def decrypt(encryptedStr,s):
    result = ""
    for i in range(len(encryptedStr)):
        char = encryptedStr[i]
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))
print("Decrypted String: "+decrypt(encryptedStr,s))
