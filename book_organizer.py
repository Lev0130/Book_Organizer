from operator import ne
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import os



class MyGUI:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("800x500")
        
        self.title = tk.Label(self.root, text= "Book_Organizer", font=("Times New Roman", 26))
        self.title.pack(pady=20)
        
        self.button = tk.Button(self.root, text="Seleccionar carpeta", command=self.select_folder)
        self.button.pack(pady=20)
        
        self.label = tk.Label(self.root, text="No folder selected")
        self.label.pack(pady=10)

        self.run_button = tk.Button(self.root, text="Run", command=self.run)
        self.run_button.pack(pady=20)
        
        self.root.mainloop()
        
        #text askinf if they have an api key and link to info
        #two button at bottom, cancel and run
        
    def select_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.folder_path = folder
            self.label.config(text=folder)

    def run(self):
        print(f"Running with: {self.folder_path}")
        
        
        
MyGUI()