def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    print(f"This book contains {num_words} words.")
    print(count_of_letters(text))

def get_book_text(path):    
    with open(path) as f:
        return f.read()
    
def number_of_words(text_file):
    words = text_file.split()
    return len(words)  
    
def count_of_letters(text_file):
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    letters = []
    count_of_letters = {}
    book_lowercase = text_file.lower()
    
    # Create list with all lowercase letters
    for letter in lower_letters:
        letters.append(letter)
    # print(letters)
    # print(type(letters))
    
    # Convert list to Dictionary

    for letter in letters:
        count_of_letters[letter] = 0
    # print(count_of_letters)
    
    # Count each letter in dictionary and increment

    for letter in book_lowercase:
        if letter in count_of_letters:
            count_of_letters[letter] = count_of_letters.get(letter) + 1
    
    return count_of_letters
    

main()        