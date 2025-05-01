def get_num_words(words):
    count = words.split()
    return len(count)

def count_chars(text):
    counts = {}
    for c in text:
        c = c.lower()
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

def sort_words(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

