message = 'This is program to explain reverse cipher.'
translated = '' #cipher text is stored in this variable
i = len(message) - 1

while i >= 0:
   translated = translated + message[i]
   i = i - 1
print("The cipher text is : ", translated)

#So reverse cyphering is literally taking a message and mirroring the message. This seems pretty simple.
#Also for a side note, make sure you change the quotation marks ("") in any message that appears
#Jacob Daleske