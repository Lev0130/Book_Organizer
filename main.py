import file_manager
from tkinter import filedialog
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import webbrowser
import ai_client

from file_manager import get_all_books, get_names_books, move_books_to_all


class MyGUI:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("500x400")
        self.root.title("Book Organizer")

        self.folder_path = ""

        # ===== TITLE (top left) =====
        self.title = tk.Label(
            self.root,
            text="Book Organizer",
            font=("Segoe UI", 18, "bold")
        )
        self.title.pack(anchor="nw", padx=20, pady=10)

        # ===== DESCRIPTION =====
        self.description = tk.Label(
            self.root,
            text="Welcome! This app helps you automatically organize your books\nusing AI into clean and structured folders.",
            font=("Segoe UI", 11),
            justify="center"
        )
        self.description.pack(pady=10)

        # ===== FOLDER SELECTOR =====
        self.frame_folder = tk.Frame(self.root)
        self.frame_folder.pack(pady=20, padx=40, fill="x")

        self.entry = tk.Entry(self.frame_folder, font=("Segoe UI", 10))
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.button = tk.Button(
            self.frame_folder,
            text="Browse",
            command=self.select_folder
        )
        self.button.pack(side="right")

        # ===== API KEY TEXT =====
        self.api_text = tk.Label(
            self.root,
            text="You need an API key to use this app.\nDon't have one?",
            font=("Segoe UI", 10)
        )
        self.api_text.pack(pady=(10, 0))

        self.link = tk.Label(
            self.root,
            text="Get your API key here",
            fg="blue",
            cursor="hand2",
            font=("Segoe UI", 10, "underline")
        )
        self.link.pack()

        self.link.bind("<Button-1>", lambda e: webbrowser.open("https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key"))

        # ===== RUN BUTTON (bottom right) =====
        self.run_button = tk.Button(
            self.root,
            text="Run",
            font=("Segoe UI", 11, "bold"),
            width=15,
            height=2,
            command=self.run
        )
        self.run_button.pack(side="bottom", anchor="se", padx=20, pady=20)

        self.root.mainloop()

        
    def select_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.folder_path = folder
            self.entry.delete(0, tk.END)
            self.entry.insert(0, folder)

    def run(self):
        print(f"Running with: {self.folder_path}")
        path = Path(self.folder_path)
        files = get_all_books(path)
        files_names = get_names_books(path)

        move_books_to_all(path, files)
        organized = ai_client.classify_books(files_names)

        #organized = {'Programming': ['automate-the-boring-stuff-with-python-2nd-edition.epub', 'Grokking Algorithms by Aditya Y. Bhargava.pdf', 'Introducción a las redes.pdf', 'pythonlearn.pdf'], 'Artificial Intelligence': ['Apuntes-Curso-Desarrollo-IA-Clase-1.pdf', 'Apuntes-Curso-Desarrollo-IA-Clase-2.pdf', 'Apuntes-Curso-Desarrollo-IA-Clase-3.pdf'], 'Philosophy': ['Del inconveniente de haber nacido(E.M Cioran) .pdf'], 'Poetry': ['Cartas a un joven poeta - Rilke.epub', 'Diarios - Alejandra Pizarnik.epub', 'en-la-tierra-somos-fugazmente-grandiosos.epub_compress.epub']}
        print(organized)
        file_manager.organize_books(organized, path)
        
    
        
MyGUI()