# ---------- TO DO ----------
# 1. Change main menu so that user cannot search unless they select [1]
# 2. Bonus feature: most commonly used words
# 3. Output to text file
# 4. GUI

# ---------- LIBRARIES/PACKAGES ----------
import csv

# ---------- FUNCTIONS ----------
def print_everything(bucket_list):
    # bucket_list: list of lists of tuples(key: word, value: list of ids)
    # Print everything:
    i = 0
    for bucket in bucket_list: # bucket: list
        print(f"---------- {ALPHABET[i].upper()} ----------")
        for item in bucket: # item: tuple
            print(f"{item[0]}")
        i = i + 1

def index_menu():
    # Print main menu
    print("---------- T R U M P  T W E E T  I N D E X ----------")
    print("[1] SELECT SECTION")
    print("[2] SEARCH          (MUST SELECT [1] FIRST)")
    print("[3] SHOW ALL")
    print("[4] HELP")
    print("[5] GET TWEET")
    print("[6] EXIT")
    print("-----------------------------------------------------")
    answer = input(">>> ")
    return answer

def index_help():
    # Print help menu
    print("---------- H E L P ------------------------------------------------------------")
    print("SELECT SECTION   View words starting with the letter A, B, etc.")
    print("SEARCH           Search for a word in the index and view associated tweets")
    print("SHOW ALL         Display the entire index")
    print("HELP             Helps you")
    print("GET TWEET        Find tweet given an id")
    print("EXIT             End program")
    print("-------------------------------------------------------------------------------")
    print("[1] OK")
    input(">>> ")

def get_section(letter, index):
    # Returns all the words beginning with letter
    i = ord(letter.lower()) - ord('a')
    if DEBUG: print(i)
    return index[i]

def print_section(section):
    # Print all the words in this section (they all start with the same letter)
    for tuple in section:
        print(f"{tuple[0]}, {tuple[1]}")

def search(word, section):
    # Search for word in section (it will only search section, not the whole index!)
    for tuple in section:
        if tuple[0] == word:
            return tuple[1]
    return ()

def print_tweets(id_list, id_dict, word):
    # Print all tweets containing a particular word
    line_num = 0
    for id in id_list:
        print(id)
        print(id_dict[id])
        print("-----------------------------------")
        line_num = line_num + 1
    print(f"Number of tweets containing \"{word}\": {line_num}")

# ---------- CONSTANTS ----------
DEBUG = False
FILENAME = "trump-tweets.csv"
ALLOWED_CHARACTERS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
SIZE = 26 # number of buckets
ALPHABET = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')


# 1. Create dictionary to store words and their ID:
word_dict = dict()
word_dict_size = 0

tweet_dict = dict() # contains tweet id as key and text as value

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
            # Insert tweet id and associated text into tweet_dict:
            tweet_dict[row["id"]] = row["text"]
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
    alphabet_tuple_list.append(list()) # Create all the buckets A - Z
    count = count + 1

# Words starting with "a" go into the "a" bucket, etc.
for key in word_dict.keys():
    i = ord(key[0]) - ord('a')
    alphabet_tuple_list[i].append((key,word_dict[key]))

# Sort within each bucket:
alphabet_index = 0
for bucket in alphabet_tuple_list:
    bucket.sort()
    alphabet_index = alphabet_index + 1

# Main program:
while True:
    option = int(index_menu())
    if option == 1:
        while True:
            print("Enter a letter between A and Z")
            print("[1] BACK")
            letter = input(">>> ")
            if letter == "1": break
            if letter not in ALLOWED_CHARACTERS:
                print("Not a letter")
            else: break
        if not letter == "1":
            section = get_section(letter, alphabet_tuple_list)
            print_section(section)
    elif option == 2:
        while True:
            print("Enter a word to see tweets")
            print("[1] BACK")
            word = input(">>> ")
            if "1" in word:
                break
            tweet_id_list = search(word, section)
            if not tweet_id_list:
                print(f"{word} not found.")
            else: break
        if "1" not in word:
            print_tweets(tweet_id_list, tweet_dict, word)
    elif option == 3:
        print_everything(alphabet_tuple_list)
    elif option == 4:
        index_help()
    elif option == 5:
        print("Enter tweet id")
        print("[1] BACK")
        while True:
            tweet_id = input(">>> ")
            if tweet_id == "1": break
            if tweet_id not in tweet_dict:
                print("id not found")
            else:
                print(f"{tweet_id}: {tweet_dict[tweet_id]}")
                break
    elif option == 6:
        break

    if DEBUG: print(option)
