def get_num_words(text):
    words = text.split()
    return len(words)

def char_breakdown(text):
    dict = {}
    for char in text:
        lower = char.lower()
        if lower in dict:
            dict[lower] += 1
        else:
            dict[lower] = 1
    return dict


def helper(dict):
    return dict["num"]


def list_of_dictionaries(dict):
    sorted = []
    for ch in dict:
        sorted.append({"char": ch, "num": dict[ch]})
    sorted.sort(reverse=True, key=helper)
    return sorted
