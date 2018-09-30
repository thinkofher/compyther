from compythertools import replace_with_json
from pathlib import Path

oldfile = Path('sample/sample.tex')
newfile = Path('output.tex')

replace_with_json(oldfile, newfile, 'data.json')
