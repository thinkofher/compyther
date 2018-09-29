from compythertools import replace_word, marker
import json


oldfile = 'sample\\sample.tex'
newfile = 'output.tex'

first = True
with open('data.json') as file:
    data = json.load(file)

for word in data['words']:
    old_word = word['old_word']
    new_word = word['new_word']
    if first:
        replace_word(oldfile, newfile, marker(old_word), new_word)
        first = False
        print(word['old_word'], '-->', word['new_word'])
    else:
        replace_word(newfile, newfile, marker(old_word), new_word)
        print(word['old_word'], '-->', word['new_word'])

print("Done!")
