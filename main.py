def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    print(f"This book contains {num_words} words.")

def get_book_text(path):    
    with open(path) as f:
        return f.read()
    
def number_of_words(text_file):
    words = text_file.split()
    return len(words)  
    
    


main()        