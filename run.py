from compythertools import replace_with_json
from pathlib import Path
from gui import GuiApp
from tkinter import Tk

oldfile = Path('sample/sample.tex')
newfile = Path('output/output.tex')
jsonfile = Path('data/data.json')

replace_with_json(oldfile, newfile, jsonfile)

root = Tk()
app = GuiApp(master=root)
app.mainloop()
