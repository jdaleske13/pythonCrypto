def encrypt(text, s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)        
    return result
#check the above function
text = "CEASER CIPHER DEMO"
s = 4

print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text, s))

#If my understanding is correct, this is a lot like bit shifting except with unicode.
#It took me re-reading the page to understand this was a unicode shift
#For some reason the website does not like putting print statements in paranthesis
#Also when I tabbed everything over, the return for the function was shifted causing only one letter to be present
#Jacob Daleske