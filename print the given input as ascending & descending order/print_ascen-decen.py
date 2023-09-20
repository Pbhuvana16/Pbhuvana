numbers = []
words = []

# Input loop for numbers
while True:
    num = input("Enter a number (or 0 to stop): ")
    if num == '0':
        break
    try:
        numbers.append(int(num))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Input loop for words
while True:
    word = input("Enter a word (or END to stop): ")
    if word == 'END':
        break
    words.append(word)

# Sort and print numbers
numbers.sort()
print("Numbers in ascending order:", numbers)
numbers.sort(reverse=True)
print("Numbers in descending order:", numbers)

# Sort and print words
words.sort()
print("Words in ascending order:", words)
words.sort(reverse=True)
print("Words in descending order:", words)
