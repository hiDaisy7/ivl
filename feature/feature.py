import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk


class Plot:
    def __init__(self):
        pass

def show_help():
    root = tk.Tk()
    root.geometry("400x400")
    root.title('usage')
    app = ttk.Label(root, text='''機能追加の方法:
                    1. plotするメソッドを書く．
                    1.1. メソッドはファイルの名前を引数にしている．
                    1.2. もしも，ファイルの名前以外を受け取りたいときは頑張って解読すること．
                    2. registerに登録を忘れないようにすること．
                    2.1. メソッドはregisterに登録されて，plotボタンでまとめて実行する．'''
    )
    app.pack(side=tk.LEFT, anchor='nw')
    app.mainloop()

def plot_ex(file_a, file_b):    
    fig = plt.figure()
    ax = fig.subplots()
    ax.plot([1, 2, 3], label=file_a)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    pass