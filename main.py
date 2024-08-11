def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    letter_count = count_of_letters(text)
    letter_dict_list = letter_list(letter_count)
    sorted_letter_list = sorted(letter_dict_list, key=sort_on_num, reverse=True)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"Number of words: {num_words}")
    print()
    for letter in sorted_letter_list:
        print(f"The '{letter['letter']}' was found {letter['num']} times")
    print(f"---- End of report ----")    

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
    
    # Convert list to Dictionary

    for letter in letters:
        count_of_letters[letter] = 0
    # print(count_of_letters)
    
    # Count each letter in dictionary and increment

    for letter in book_lowercase:
        if letter in count_of_letters:
            count_of_letters[letter] = count_of_letters.get(letter) + 1
    
    return count_of_letters

def letter_list(dict):
    list_of_count_of_letters = []
    for k in dict:
        letter_dict = {"letter": k, "num": dict.get(k)}
        print(letter_dict)
        list_of_count_of_letters.append(letter_dict)
   
    return list_of_count_of_letters

def sort_on_num(d):
    return d["num"]



main()        