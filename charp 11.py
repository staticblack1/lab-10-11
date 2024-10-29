from pprint import pprint
from unittest import removeResult

# exercise 2
list0 = [1, 2, 3]
list1 = [4,5]
t = list0, list1 + [6]
print(t)
#d = {t: 'thsi is bad'}
#print(d)

# exercise 3
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))

def shift_word(word, number):
    shifted_word=''
    for l in word:
        shifted_word += letters[(letter_map[l] + number) % len(letters)]
    return shifted_word

print(shift_word('cheer', 7))
print(shift_word('melon', 16))

# exericse 4
def count_valued(word):
    counter = {}
    for l in word:
        if l in counter:
            counter[l] += 1
        else:
            counter[l] = 1
    return counter


def most_frequent_letter(word):
    counter = count_valued(word)
    return sorted(counter, key=lambda k: counter[k], reverse=True)

print(most_frequent_letter('worlddog'))

#exercise 5

def print_anagramss(d):
    for k, v in d.items():
        if len(v) > 1:
            print(v)

def load_word_dict(file_path):
    result ={}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            word = word.strip()
            key = ''.join(sorted(word))
            result.setdefault(key, []).append(word)
    return result

# exercise 6
word0 = 'letters'
word1 = 'latters'
print(print_anagramss(load_word_dict('wordfile/words.txt')))

def word_distance(word0,word1):
    counter = 0
    for c1,c2 in zip(word0, word1):
        if c1 != c2:
            counter += 1
    return counter
print(word_distance(word0,word1))

# exercise 7

def metathesis_pair():
    word_dict = load_word_dict('wordfile/words.txt')
    for k, v in word_dict.items():
        if len(v) > 1:
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    if word_distance(v[i], v[j]) == 2:
                        print(f"metabthesis words: {v[i]} {v[j]}")

print(metathesis_pair())







