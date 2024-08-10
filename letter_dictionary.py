def main():
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    letters = []
    letters_num_value = []
    for letter in lower_letters:
        letters.append(letter)
    print(letters)
    print(type(letters))
    letters_num_value = letter_values(letters)
    print(letters_num_value)
    print(type(letters_num_value))

def letter_values(list_of_letters):
    numbers = []
    for letter in list_of_letters:
        numbers.append(ord(letter))
    return numbers

main()