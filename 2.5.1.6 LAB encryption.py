message = input("Please input your message in one line: ")
encrypted = " "
while True:
    try: 
        shift_value = int(input("What shift value should be used? Enter a number between 1 and 25: "))
        if 1 <= shift_value <= 25:
            break
    except ValueError:
        print("Choose a number between 1 and 25, please!")
	
	
for char in message:
    if not char.isalpha():
        encrypted+=char
        continue
		
    converted_ASCII = ord(char) + shift_value
    
    if 65 <= ord(char) <= 90:
        if converted_ASCII > 90:
            converted_ASCII-=26
    
    if 97 <= ord(char) <= 122:
        if converted_ASCII > 122:
            converted_ASCII-=26

    encrypted += chr(converted_ASCII)
print(encrypted)