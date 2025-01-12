def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    print(f"{num_words} words found in the document")
    print(f"The frequency of the use of characters in the document are:{num_characters}")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_characters(text):
    text_lower = text.lower()
    character_count = {"e": 1}
    for i in range(len(text_lower)):
        if text_lower[i].isalpha() == True:        
            if text_lower[i] not in character_count:
                character_count[text_lower[i]] = 1
            else:
                character_count[text_lower[i]] += 1
    return character_count
        



main()