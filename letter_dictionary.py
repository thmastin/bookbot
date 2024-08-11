def main():
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    letters = []
    count_of_letters = {}
    for letter in lower_letters:
        letters.append(letter)
    print(letters)
    print(type(letters))
    for letter in letters:
        count_of_letters[letter] = 0
    print(count_of_letters)
    for letter in lower_letters:
        count_of_letters[letter] = count_of_letters.get(letter) + 1
    print(count_of_letters)
main()