# Function to input numbers
def input_numbers():
    numbers = []
    while True:
        num = input("Enter a number (or 0 to stop): ")
        if num == '0':
            break
        try:
            numbers.append(int(num))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers

# Function to input words
def input_words():
    words = []
    while True:
        word = input("Enter a word (or END to stop): ")
        if word == 'END':
            break
        words.append(word)
    return words

# Function to print numbers in ascending and descending order
def print_sorted_numbers(numbers):
    numbers.sort()
    print("Numbers in ascending order:", numbers)
    numbers.sort(reverse=True)
    print("Numbers in descending order:", numbers)

# Function to print words in ascending and descending order
def print_sorted_words(words):
    words.sort()
    print("Words in ascending order:", words)
    words.sort(reverse=True)
    print("Words in descending order:", words)

if __name__ == "__main__":
    # Call input functions to get numbers and words
    numbers = input_numbers()
    words = input_words()

    # Call print functions to display sorted numbers and words
    print_sorted_numbers(numbers)
    print_sorted_words(words)
