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
    file_name = "swahili-freq-10000.pdf"
    full_path = os.path.join(Path.home(), 'Downloads', file_name)

    # open pdf
    doc = pymupdf.open(full_path)
    # for page in doc:
    all_matches = []
    for i in range(10):
        page = doc[i]
        text = page.get_text()

        matches = re.findall(word_pattern, text)
        all_matches.extend(matches)
    # for match in all_matches:
    #     frequency, swahili_word, tags, english_translation = match
        # import pdb; pdb.set_trace()

    with open('swahili_top_1000.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(('frequency', 'swahili_word', 'tags', 'english_translation'))
        writer.writerows(all_matches)
        
    # print(data)

def add_crossword_words():
    with open("swahili_top_1000.csv", 'r') as f:
        reader = list(csv.reader(f))
        header = reader[0]
        data_rows = reader[1:]

        count = 0
        with open('wordlist2.txt', 'a') as wordlist:
            for row in data_rows:
                swahili_word = row[1]
                if len(swahili_word) > 2 and len(swahili_word) < 16:
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
                    wordlist.write(f"{swahili_word};50\n")
                    print(swahili_word)

                    count += 1
        print(count)



    # load text 

if __name__ == "__main__":
    # process_words()
    add_crossword_words()