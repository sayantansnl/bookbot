import sys
from stats import count_words as get_num_words, char_counts, to_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    final_list = []
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    char_dict = char_counts(text)
    char_list = to_list(char_dict)
    char_list.sort(reverse=True, key=sort_on)

    for char in char_list:
        if char["char"].isalpha():
            final_list.append(char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at ./{sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for every_item in final_list:
        print(f"{every_item["char"]}: {every_item["num"]}")
    
    print("============= END ===============")
    

def sort_on(items):
    return items["num"]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

main()