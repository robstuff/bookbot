def word_count(file_to_count):
    return len(file_to_count.split())

def char_count(file_to_count):
    char_counter ={}
    for char in file_to_count:
        char = char.lower()
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    return char_counter

def char_count_sorted(char_counts):
    data = []
    for char, num in char_counts.items():
        if char.isalpha():
            dict = {
                "char": char,
                "num": num
            }
            data.append(dict)
    data.sort(key=lambda x: x["num"], reverse=True)
    return data
