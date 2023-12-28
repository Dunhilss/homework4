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
numwords = list(map(int,input("\nPlease enter a number to search for: ").split()))
numdigits = int(input("Enter the number to search for: "))
num = 0
for i in numwords:
    if i == numdigits:
        num += 1
print(f"Number {numdigits} occurs {num} times")
string = input("Please enter your text:  ")
search_word = input("Type in the word you want to find:  ")
replace_word = input("Enter the word you want to replace the found word with:  ")
words = string.split()
modified_words = []
for word in words:
   if word == search_word:
       modified_words.append(replace_word)
   else:
       modified_words.append(word)
modified_string = " ".join(modified_words)
result = "Result: " + modified_string
print(result)

text = "Viking"
print(text[:])
print(text[2:3])
print(text[4:5])
print(text[:5])
print(text[:4])
print(text[::2])
print(text[1::2])
print(text[::-1])
print(text[::-2])
print(len(text))