# ---------- TO DO ----------
# 1. Filter out URLs, @ mentions, numbers, emojis, escape characters, punctuation
# 2. Use bucket sort to generate index
# 3. Create a GUI?

import csv

DEBUG = True
FILENAME = "trump-tweets.csv"

# 1. Create dictionary to store words and their ID:
word_dict = dict()

# 2. Read .csv into a dictionary:
with open(FILENAME, mode='r', encoding="utf8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # 3. Separate words of each tweet and store them in word_dict along with corresponding ID:
            # print(f'ID: {row["id"]} Text: {row["text"]}')
            tweet_text = row["text"] # grab tweet text
            tweet_id = row["id"] # grab tweet id
            tweet_word_list = tweet_text.split(" ") # split tweet text string into list of words
            for word in tweet_word_list:
                if word not in word_dict: word_dict[word] = list() # create new list so id can be appended
                word_dict[word].append(tweet_id) # append tweet id to list corresponding to this word
            line_count += 1
    # print(f'Processed {line_count} lines.')

for key, value in word_dict.items():
    print(key, ": ", value)



