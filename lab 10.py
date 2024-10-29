def value_count(string):
    counter= {}
    for letter in string:
         counter[letter] = counter.get(letter, 0) + 1
    return counter

def has_duplicates(word):
    value_count(word)
    return len(value_count(word).keys()) !=len(word)

def find_repeats(counter):
    result = []
    for k,v in counter.items():
        if v > 1:
            result.append(k)
    return result

counter1 = value_count('brontosaurus')
counter2 = value_count('brontosaurus')
def add_counter(counter1, counter2):
    result = dict(counter1)
    for k , v in counter2.items():
        result[k] = result.get(k, 0) + v
        return result

def load_word_dict(file_path):
    word_dict = {}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            word = word.strip().lower()
            word_dict[word] = True
    return word_dict

def is_interlocking(word, word_dict):
    word = word.lower()
    first = word[0::2]
    second = word[1::2]
    return first in word_dict and second in word_dict

print(has_duplicates('brontosaurus'))

print(value_count("brontosaurus"))
print(find_repeats(value_count('brontosaurus')))
print(add_counter(counter1, counter2))
print(is_interlocking('schooled', load_word_dict('wordfile/words.txt')))