def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    characters_dict = dict_characters(num_characters)
    sorted_letters = sort_letters(characters_dict)
    print(f"{num_words} words found in the document")
    print(f"The frequency of the use of characters in the document are:{num_characters}")
    print(f"This is the dictonary of characters: {characters_dict}")
    print(f"This is the dictonary sorted: {sorted_letters}")
    generate_report(book_path, num_words, sorted_letters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_characters(text):
    text_lower = text.lower()
    character_count = {}
    for i in range(len(text_lower)):
        if text_lower[i].isalpha() == True:        
            if text_lower[i] not in character_count:
                character_count[text_lower[i]] = 1
            else:
                character_count[text_lower[i]] += 1
    return character_count

def dict_characters(dictionary):
    print(dictionary)
    character_list = []
    for k in dictionary:
        print(k, dictionary[k])
        new_dict = {"char": k, "num": dictionary[k]}
        character_list.append(new_dict)
    return character_list

def sort_on(dict):
    return dict["num"]

def sort_letters(dict):
    dict.sort(reverse=True, key=sort_on)
    return dict

def generate_report(book, words, list_of_letters):
    print(f"--- Begin report on {book} ---")
    print(f"{words} words found in this document.\n")

    for letter in list_of_letters:
        print(f"The {letter["char"]} character was found {letter["num"]} times.")
    


        



main()