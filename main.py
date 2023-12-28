string = input("Greetings. \nEnter your text using letters and numbers: ")
letter_count = 0
digit_count = 0
for char in string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
print("Number of letters in the text:  ", letter_count)
print("The number of digits in the text: ", digit_count)