from compythertools import replace_word, marker

oldfile = 'sample\\sample.tex'
newfile = 'output.tex'

replace_word(
    'sample\\sample.tex', newfile,
    marker('Beniamin'), 'Marek świętokrzyski'
    )
replace_word('output.tex', 'output.tex', marker('sierść'), 'Ćma sobie lata')
replace_word('output.tex', 'output.tex', marker('typ_rur'), 'Rura-5000')
