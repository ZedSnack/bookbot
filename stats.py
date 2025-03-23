def get_word_count(file_contents):
    words = file_contents.split()
    count = len(words)
    return count


def get_char_counts(file_contents):
    lowercase_file = file_contents.lower()
    char_count = {}
    for char in lowercase_file:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def print_count_report(char_count):
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
