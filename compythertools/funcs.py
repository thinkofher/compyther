import os
import sys
import json


def replace_word(infile, newfile, old_word, new_word):
    '''
    Reading old file and replacing all old words
    with new word, then saving it in newfile.
    '''
    if not os.path.isfile(infile):
        print("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)

    # Check this too if utf-8 fails:
    # fileRead = open(infile, 'r', encoding='utf-8').read()
    fileRead = open(infile, 'r').read()

    # fileWrite = open(newfile, 'w', encoding='utf-8')
    fileWrite = open(newfile, 'w')
    temporaryFile = fileRead.replace(old_word, new_word)
    fileWrite.write(temporaryFile)


def marker(word):
    '''
    Function for adding variable works for word
    to be replaced.
    '''
    return '<:' + word + ':>'


def replace_with_json(oldfile, newfile, jsonfile):
    '''
    Replacing all words from oldfile and saving it in
    new file. Reading words from jsonfile.
    '''
    print("Starting procedure.\n")

    # if first is true, only replacing old file
    # then replacing new file to have every
    # change in one file
    first = True
    with open(jsonfile) as file:
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

    print('\nDone!')
