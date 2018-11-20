import tkinter as tk
from tkinter import ttk


class GuiApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.countryvar = tk.StringVar()
        self.country = ttk.Combobox(self, textvariable=self.countryvar)
        self.country['values'] = ['USA', 'Canada', 'Poland']
        self.country.pack(side="top")

        self.quit = tk.Button(
            self, text="QUIT", fg="red", command=self.master.destroy
            )
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        print(self.countryvar.get())


if __name__ == "__main__":
    root = tk.Tk()
    app = GuiApp(master=root)
    app.mainloop()
