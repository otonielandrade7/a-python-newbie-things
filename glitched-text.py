import random
text = input("Introduce your text or phrase\n")
responseText=""
for letter in text:
    if random.randint(0,1) == 0:
        responseText+=letter.lower()
    else:
        responseText+= letter.upper()
print(responseText)
