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
    
    def load_home_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.home_label = tk.Label(self.root, text="Welcome to Text-in-Image Steganography", font=("Arial", 16))
        self.home_label.pack(pady=20)

        # Go to Encoder page button
        self.encoder_btn = tk.Button(self.root, text="Go to Encoder", command=self.load_encoder_page)
        self.encoder_btn.pack(pady=10)

        # Go to Decoder page button
        self.decoder_btn = tk.Button(self.root, text="Go to Decoder", command=self.load_decoder_page)
        self.decoder_btn.pack(pady=10)

if __name__ == '__main__':
    root = TkinterDnD.Tk()
    app = SteganographyApp(root)
    root.mainloop()