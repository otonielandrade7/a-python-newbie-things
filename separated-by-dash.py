text = input("Introduce your text here\n")
responseText=""
for letter in text:
    if letter == " ":
        responseText+="-"
    else:
        responseText+=letter
print(responseText)
