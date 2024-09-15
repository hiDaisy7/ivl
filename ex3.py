import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
from feature import feature as F
from tkinter import messagebox


class FileManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Manager")
        self.master.geometry("400x400")

        self.file_path_a = ""
        self.file_path_b = ""
        
        self.register_functions()
        self.setup_style()
        self.create_widgets()
        
    def setup_style(self):
        style = ttk.Style()
        style.theme_use('alt')  # モダンなテーマを使用
        print(style.theme_names())
    
    def create_widgets(self):
        self.create_file_selection_widgets()
        self.create_plot_selection_widgets()
        self.create_action_buttons()
    
    def create_file_selection_widgets(self):
        self.label_a = self.create_label("A: chose file")
        self.frame_a = self.create_frame()
        self.select_button_a = self.create_button(self.frame_a, "A: ファイル選択", self.select_file_a)
        self.selected_file_label_a = self.create_label("", self.frame_a)
        
        self.label_b = self.create_label("B: chose file")
        self.frame_b = self.create_frame()
        self.select_button_b = self.create_button(self.frame_b, "B: ファイル選択", self.select_file_b)
        self.selected_file_label_b = self.create_label("", self.frame_b)
    
    def create_plot_selection_widgets(self):
        self.label_plot = self.create_label("select plot functions")
        self.frame_plot = self.create_frame()
        
        self.plot_vars = []
        
        for plot_function in self.plot_functions:
            var = tk.BooleanVar(value=True)
            check = ttk.Checkbutton(self.frame_plot, text=plot_function.__name__, variable=var)
            check.pack(anchor="w")
            self.plot_vars.append(var)
    
    def create_action_buttons(self):
        self.frame_buttons = self.create_frame()
        self.plot_button = self.create_button(self.frame_buttons, "plot", self.plot)
        self.help_button = self.create_button(self.frame_buttons, "help", self.show_help)
    
    def create_label(self, text, master=None):
        if master is None:
            master = self.master
        label = ttk.Label(master, text=text, anchor="w")
        label.pack(fill=tk.X, padx=10, pady=5)
        return label
    
    def create_frame(self, master=None, **kwargs):
        if master is None:
            master = self.master
        frame = ttk.Frame(master, **kwargs)
        frame.pack(fill=tk.X, padx=10, pady=5)
        return frame
    
    def create_button(self, master, text, command):
        button = ttk.Button(master, text=text, command=command)
        button.pack(side=tk.LEFT, padx=5)
        return button
    
    def select_file_a(self):
        self.file_path_a = self.select_file("A: ファイルを選択")
        if self.file_path_a:
            self.selected_file_label_a.config(text=os.path.basename(self.file_path_a))
    
    def select_file_b(self):
        self.file_path_b = self.select_file("B: ファイルを選択")
        if self.file_path_b:
            self.selected_file_label_b.config(text=os.path.basename(self.file_path_b))
    
    def select_file(self, title):
        return filedialog.askopenfilename(initialdir="data", title=title, filetypes=(("すべてのファイル", "*.*"),))
    
    def plot(self):
        if self.file_path_a and self.file_path_b:
            for i, var in enumerate(self.plot_vars):
                if var.get():
                    self.plot_functions[i](self.file_path_a, self.file_path_b)
        else:
            print("両方のファイルを選択してください")
            messagebox.showerror(title='FileSelectError', message='Chose two files, please')
    
    def show_help(self):
        F.show_help()

    def register_functions(self):
        self.plot_functions = []
        self.plot_functions.append(self.PLOT1)
        self.plot_functions.append(self.PLOT2)

    def PLOT1(self, file_path_a, file_path_b):
        # PLOT1関数の実装はここに書かないでください
        F.plot_ex(file_path_a, file_path_b)
        print(f"PLOT1関数が呼び出されました: A={file_path_a}, B={file_path_b}")
    
    def PLOT2(self, file_path_a, file_path_b):
        # PLOT2関数の実装はここに書かないでください
        print(f"PLOT2関数が呼び出されました: A={file_path_a}, B={file_path_b}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManager(root)
    root.mainloop()
