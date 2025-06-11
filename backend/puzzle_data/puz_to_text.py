import json

def read_filled_puz(puz_file):
    with open(puz_file, 'r', encoding="utf-8") as xword_file:
        data = json.load(xword_file)
    solution = data['solution']
    size = data['dimensions']
    height = size['height']
    width = size['width']

    #grab words across- concat letters and skip any '#' chars
    across = []
    curr_word = ''
    for row in range(height):
        for col in range(width):
            cell = solution[row][col]
            if isinstance(cell, str) and cell != '#':
                curr_word += cell 
            elif cell == '#':
                if len(curr_word) > 0:
                    across.append(curr_word)
                curr_word = ''
    down = []
    curr_word = ''
    for col in range(width):
        for row in range(height):
            cell = solution[row][col]
            if cell != '#':
                curr_word += cell
            else:
                if len(curr_word) > 0:
                    down.append(curr_word)
                curr_word = ''


    print(f"Words across are: {across}")
    print(f"Words down are: {down}")
    with open("answers.txt", 'w') as f:
        f.write(json.dumps(
            {
                'across': across,
                'down': down
            }
        ))

if __name__ == "__main__":
    read_filled_puz('swahili_1.ipuz')