import os
import sys


def replace_word(infile, old_word, new_word):
    if not os.path.isfile(infile):
        print("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)

    fileRead = open(infile, 'r', encoding='utf-8').read()
    fileWrite = open('output.tex', 'w', encoding='utf-8')
    temporaryFile = fileRead.replace(old_word, new_word)
    fileWrite.write(temporaryFile)


replace_word('sample\\sample.tex', '<:Beniamin:>', 'Marek świętokrzyski')
replace_word('output.tex', '<:sierść:>', 'Ćma sobie lata')
replace_word('output.tex', '<:typ_rur:>', 'Rura-5000')
