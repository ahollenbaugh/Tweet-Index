# ---------- TO DO ----------
# 1. Filter out URLs, @ mentions, numbers, emojis, escape characters, punctuation, Arabic letters, Japanese characters
# 2. Use bucket sort to generate index
# 3. Create a GUI?
# 4. Make all words lowercase

import csv

DEBUG = True
FILENAME = "trump-tweets.csv"
CHARS_REMOVE_FROM_WORD = set('.,!?\"^&*()\n_+=[]{};:\'<>~`“”✔’🔥🏆‘-') # if found in a word, remove from word
CHARS_REMOVE_WORD_ITSELF = set('@#$%\\/0123456789') # if found in word, throw out that word (check this first)
# Example: @ mentions, URLs, numbers, prices, percents, hashtags (avoids having to separate words)

# 1. Create dictionary to store words and their ID:
word_dict = dict()

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
                    for char in CHARS_REMOVE_WORD_ITSELF:
                        if letter == char:
                            throw_away = True
                            break
                    if not throw_away:
                        for char in CHARS_REMOVE_FROM_WORD:
                            if letter == char: # check whether or not to throw out a char
                                word = word.replace(char,"") # remove char from word
                    else:
                        break
                # 5. Add word to word_dict and append id:
                if not throw_away:
                    if word not in word_dict: word_dict[word] = list() # create new list so id can be appended
                    word_dict[word].append(tweet_id) # append tweet id to list corresponding to this word
            line_count += 1

if DEBUG:
    for key, value in word_dict.items():
        print(key, ": ", value)



