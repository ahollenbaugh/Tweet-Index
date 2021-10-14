# ---------- TO DO ----------
# 1. Make sure column names are exactly the same for each .csv processed
# 2. Filter out URLs, @ mentions, numbers, emojis
# 3. Use bucket sort to generate index
# 4. Create a GUI?

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
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # 3. Separate words of each tweet and store them in word_dict along with corresponding ID:
            # print(f'ID: {row["id"]} Text: {row["text"]}')
            tweet_text = row["text"]
            tweet_id = row["id"]
            tweet_word_list = tweet_text.split(" ")
            for word in tweet_word_list:
                if DEBUG: print(word)
                word_dict[word] = tweet_id
            line_count += 1
    # print(f'Processed {line_count} lines.')



