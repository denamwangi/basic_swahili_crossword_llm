import pymupdf
import csv
import os
from pathlib import Path
import re
import json



# word_pattern = r'(\d+)\s+"([^"]+)"\s+[^{]*\{\s*([^}]+)\s*\}'
# word_pattern = r'(\d+)\s+"([^"]+)"\s+([^{]*?)\s*\{\s*([^}]+)\s*\}'
word_pattern = r'(\d+)\s+"([^"]+)"\s+([^{]*?)\s*\{\s*([^}]+)\s*\}'

def process_words():
    file_name = "kamusi.csv"
    full_path = os.path.join(Path.home(), 'Downloads', file_name)
    words = []
    definitions = ''
    with open(full_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            words.append(row[1])
            definition = row[2]
            definition_array = definition.split('|')
            for item in definition_array:
                individual_words = item.split(' ')
                for word in individual_words:
                    if len(word) > 2 and len(word) < 16:
                        words.append(word)

    words_deduped = list(set(words))
    with open('wordlist2.txt', 'a') as wordlist_csv:
        for swahili_word in words_deduped:
            if len(swahili_word) > 3 and len(swahili_word) < 16:
                swahili_word = swahili_word.replace('_', '')
                swahili_word = swahili_word.replace('-', '')
                swahili_word = swahili_word.replace('*', '')
                swahili_word = swahili_word.replace('!', '')
                swahili_word = swahili_word.replace(',', '')
                swahili_word = swahili_word.replace('.', '')
                swahili_word = swahili_word.replace("'", '')
                swahili_word = swahili_word.replace("(", '')
                swahili_word = swahili_word.replace(")", '')
                swahili_word = swahili_word.replace('"', '')
                swahili_word = swahili_word.replace('?', '')
                swahili_word.strip(' ')

                wordlist_csv.write(f"{swahili_word};50\n")
    print(f'Kamusi added: {len(words_deduped)}')

    # open pdf
            # import pdb; pdb.set_trace()
    # for page in doc:
    # all_matches = []
    # for i in range(10):
    #     page = doc[i]k
    #     text = page.get_text()

    #     matches = re.findall(word_pattern, text)
    #     all_matches.extend(matches)
    # # for match in all_matches:
    # #     frequency, swahili_word, tags, english_translation = match
    #     # import pdb; pdb.set_trace()

    # with open('kamusi.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(('frequency', 'swahili_word', 'tags', 'english_translation'))
    #     writer.writerows(all_matches)
        
    # print(data)

def add_crossword_words():
    with open("swahili_top_1000.csv", 'r') as f:
        reader = list(csv.reader(f))
        header = reader[0]
        data_rows = reader[1:]

    
        with open('wordlist.txt', 'w') as wordlist:
            for row in data_rows:
                swahili_word = row[1]
                if len(swahili_word) > 3 and len(swahili_word) < 16:
                    swahili_word.replace('_', ' ')
                    wordlist.write(f"{swahili_word};50\n")
                    print(swahili_word)



    # load text 

if __name__ == "__main__":
    process_words()
    # add_crossword_words()