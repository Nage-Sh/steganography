import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text in Image - Steganography")
        self.root.geometry("700x700")
        self.root.resizable(True, True)

        self.original_image = None
        self.image_path = None
        self.text_file_path = None
        self.current_page = "home"

        # Load Home Page
        self.load_home_page()

if __name__ == '__main__':
    root = TkinterDnD.Tk()
    app = SteganographyApp(root)
    root.mainloop()