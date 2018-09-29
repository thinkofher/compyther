import os
import sys


def replace_word(infile, newfile, old_word, new_word):
    if not os.path.isfile(infile):
        print("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)
    
    # Check this too: fileRead = open(infile, 'r', encoding='utf-8').read()
    fileRead = open(infile, 'r').read()

    # Check this too: fileWrite = open(newfile, 'w', encoding='utf-8')
    fileWrite = open(newfile, 'w')
    temporaryFile = fileRead.replace(old_word, new_word)
    fileWrite.write(temporaryFile)


def marker(word):
    return '<:' + word + ':>'
