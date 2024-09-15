import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt



class KeySelectorApp:
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.selected_keys = []
        self.root.title("Key Selector")

        self.frame = ttk.Frame(root, padding=10)
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.listbox = tk.Listbox(self.frame, height=10, selectmode=tk.MULTIPLE)
        self.listbox.grid(row=0, column=0, sticky=(tk.W, tk.E))

        for key in self.data.keys():
            self.listbox.insert(tk.END, key)

        self.plot_button = ttk.Button(self.frame, text="Plot", command=self.plot_data)
        self.plot_button.grid(row=1, column=0, pady=10)

    def plot_data(self):
        selected_indices = self.listbox.curselection()
        self.selected_keys = [self.listbox.get(i) for i in selected_indices]

        if self.selected_keys:
            num_plots = len(self.selected_keys)
            fig, axs = plt.subplots(num_plots, 1, figsize=(6, 4 * num_plots))

            if num_plots == 1:
                axs = [axs]

            for ax, key in zip(axs, self.selected_keys):
                ax.plot(self.data[key])
                ax.set_title(f"Plot for key: {key}")

            plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    # 辞書型配列の例
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [2, 3, 4, 5, 6],
        'C': [3, 4, 5, 6, 7]
    }
    app = KeySelectorApp(root, data)
    root.mainloop()
