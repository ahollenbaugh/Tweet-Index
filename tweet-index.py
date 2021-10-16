# ---------- TO DO ----------
# 1. Filter out URLs, @ mentions, numbers, emojis, escape characters, punctuation, Arabic letters, Japanese characters
# 2. Use bucket sort to generate index
# 3. Create a GUI?
# 4. Make all words lowercase

import csv
from enum import Enum, auto
import sys


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        start = 0
        return count


class Bucket(AutoName):
    BUCKET_A = auto()
    BUCKET_B = auto()
    BUCKET_C = auto()
    BUCKET_D = auto()
    BUCKET_E = auto()
    BUCKET_F = auto()
    BUCKET_G = auto()
    BUCKET_H = auto()
    BUCKET_I = auto()
    BUCKET_J = auto()
    BUCKET_K = auto()
    BUCKET_L = auto()
    BUCKET_M = auto()
    BUCKET_N = auto()
    BUCKET_O = auto()
    BUCKET_P = auto()
    BUCKET_Q = auto()
    BUCKET_R = auto()
    BUCKET_S = auto()
    BUCKET_T = auto()
    BUCKET_U = auto()
    BUCKET_V = auto()
    BUCKET_W = auto()
    BUCKET_X = auto()
    BUCKET_Y = auto()
    BUCKET_Z = auto()


DEBUG = True
FILENAME = "trump-tweets.csv"
CHARS_REMOVE_FROM_WORD = set('.,!?\"^&*()\n_+=[]{};:\'<>~`“”✔’🔥🏆‘-') # if found in a word, remove from word
CHARS_REMOVE_WORD_ITSELF = set('@#$%\\/0123456789') # if found in word, throw out that word (check this first)
ALLOWED_CHARACTERS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
# Example: @ mentions, URLs, numbers, prices, percents, hashtags (avoids having to separate words)
SIZE = 26
ALPHABET = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

# 1. Create dictionary to store words and their ID:
word_dict = dict()
word_dict_size = 0

print("Working...")

# 2. Read .csv into a dictionary:
with open(FILENAME, mode='r', encoding="utf8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # This is the column name row, don't do anything here
            line_count += 1
        else:
            # 3. Separate words of each tweet:
            tweet_text = row["text"] # grab tweet text
            tweet_id = row["id"] # grab tweet id
            tweet_word_list = tweet_text.split() # split tweet text string into list of words
            # 4. Filter out non-words and remove certain characters accordingly:
            for word in tweet_word_list:
                throw_away = False
                for letter in word:
                    if letter not in ALLOWED_CHARACTERS:
                        throw_away = True
                        break
                # 5. Add word to word_dict and append id:
                if not throw_away:
                    word = word.lower()
                    if word not in word_dict:
                        word_dict[word] = list() # create new list so id can be appended
                        word_dict_size = word_dict_size + 1
                    word_dict[word].append(tweet_id) # append tweet id to list corresponding to this word
            line_count += 1

# 6. Bucket sort!
alphabet_tuple_list = []

count = 0
while count < SIZE:
    alphabet_tuple_list.append(list())
    count = count + 1

for key in word_dict.keys():
    if key[0] == 'a':
        alphabet_tuple_list[0].append((key,word_dict[key]))
        continue
    elif key[0] == 'b':
        alphabet_tuple_list[1].append((key,word_dict[key]))
        continue
    elif key[0] == 'c':
        alphabet_tuple_list[2].append((key,word_dict[key]))
        continue
    elif key[0] == 'd':
        alphabet_tuple_list[3].append((key,word_dict[key]))
        continue
    elif key[0] == 'e':
        alphabet_tuple_list[4].append((key,word_dict[key]))
        continue
    elif key[0] == 'f':
        alphabet_tuple_list[5].append((key,word_dict[key]))
        continue
    elif key[0] == 'g':
        alphabet_tuple_list[6].append((key,word_dict[key]))
        continue
    elif key[0] == 'h':
        alphabet_tuple_list[7].append((key,word_dict[key]))
        continue
    elif key[0] == 'i':
        alphabet_tuple_list[8].append((key,word_dict[key]))
        continue
    elif key[0] == 'j':
        alphabet_tuple_list[9].append((key,word_dict[key]))
        continue
    elif key[0] == 'k':
        alphabet_tuple_list[10].append((key,word_dict[key]))
        continue
    elif key[0] == 'l':
        alphabet_tuple_list[11].append((key,word_dict[key]))
        continue
    elif key[0] == 'm':
        alphabet_tuple_list[12].append((key,word_dict[key]))
        continue
    elif key[0] == 'n':
        alphabet_tuple_list[13].append((key,word_dict[key]))
        continue
    elif key[0] == 'o':
        alphabet_tuple_list[14].append((key,word_dict[key]))
        continue
    elif key[0] == 'p':
        alphabet_tuple_list[15].append((key,word_dict[key]))
        continue
    elif key[0] == 'q':
        alphabet_tuple_list[16].append((key,word_dict[key]))
        continue
    elif key[0] == 'r':
        alphabet_tuple_list[17].append((key,word_dict[key]))
        continue
    elif key[0] == 's':
        alphabet_tuple_list[18].append((key,word_dict[key]))
        continue
    elif key[0] == 't':
        alphabet_tuple_list[19].append((key,word_dict[key]))
        continue
    elif key[0] == 'u':
        alphabet_tuple_list[20].append((key,word_dict[key]))
        continue
    elif key[0] == 'v':
        alphabet_tuple_list[21].append((key,word_dict[key]))
        continue
    elif key[0] == 'w':
        alphabet_tuple_list[22].append((key,word_dict[key]))
        continue
    elif key[0] == 'x':
        alphabet_tuple_list[23].append((key,word_dict[key]))
        continue
    elif key[0] == 'y':
        alphabet_tuple_list[24].append((key,word_dict[key]))
        continue
    elif key[0] == 'z':
        alphabet_tuple_list[25].append((key,word_dict[key]))
        continue

alphabet_index = 0
for list in alphabet_tuple_list:
    list.sort()
    # print(f"----------{ALPHABET[alphabet_index]} List----------\n")
    # for item in list:
    #     print(item, "\n")
    alphabet_index = alphabet_index + 1

if DEBUG:
    # for key, value in word_dict.items():
    #     print(key, ": ", value)
    # word_dict_sorted = sorted(word_dict.items())
    # for item in word_dict_sorted:
    #     print(item, "\n")
    # print(f"----------{ALPHABET[0]} List----------\n")
    # for multipair in alphabet_tuple_list[0]:
    #     print(multipair)
    print(f"Number of words: {word_dict_size}")



