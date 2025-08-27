def count_words(text):
    return len(text.split())

def char_counts(text):
    result = {}
    
    for char in text:
        lower_char = char.lower()

        if lower_char in result:
            result[lower_char] += 1
        else:
            result[lower_char] = 1
    
    return result


def to_list(dict):
    char_list = []

    for char in dict:
        char_list.append(
            {"char": char, "num": dict[char]}
        )

    return char_list

