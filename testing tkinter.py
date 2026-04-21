import tkinter as tk

root = tk.Tk()

# Input 1: row 0, column 0
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, padx=5, pady=5)

# Input 2: same row (0), but column 1
entry2 = tk.Entry(root)
entry2.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()
