import os
import sys


def replace_word(infile, newfile, old_word, new_word):
    if not os.path.isfile(infile):
        print("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)

    fileRead = open(infile, 'r', encoding='utf-8').read()
    fileWrite = open(newfile, 'w', encoding='utf-8')
    temporaryFile = fileRead.replace(old_word, new_word)
    fileWrite.write(temporaryFile)
