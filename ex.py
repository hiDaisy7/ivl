import tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import torch


class Application(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root, width=420, height=320, borderwidth=4, relief="groove")
        self.root = root
        self.pack()
        self.pack_propagate(0) 
        self.creat_widgets()

    def creat_widgets(self):
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig)
        self.canvas.get_tk_widget().pack()

        text = tkinter.Text()
    def plot(self):
        pass

if __name__ == '__main__':

    root = tkinter.Tk()
    root.title("練習")
    root.geometry("512x512")
    app = Application(root)
    app.mainloop()