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

    def load_encoder_page(self):
        self.current_page = "encoder"
        
        for widget in self.root.winfo_children():
            widget.destroy()

        self.encoder_label = tk.Label(self.root, text="Encoder Page", font=("Arial", 16))
        self.encoder_label.pack(pady=20)

        # Drag and Drop Area for Encoder
        self.drop_label = tk.Label(self.root, text="Drag and drop a .png or .bmp image here", bg="#f0f0f0", relief="solid", bd=2, width=60, height=4)
        self.drop_label.pack(pady=20)

        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.drop_file_encoder)

        # Load Image Button
        self.load_btn = tk.Button(self.root, text="Load Image Manually", command=self.load_image_encoder)
        self.load_btn.pack()

        # Image Display
        self.img_label = tk.Label(self.root, text="Image will appear here", bd=2, relief="sunken")
        self.img_label.pack(pady=20)

        # Text Input
        tk.Label(self.root, text="Enter text to hide:").pack()
        self.text_entry = tk.Text(self.root, height=5, width=60)
        self.text_entry.pack(pady=5)

        # Starting Index for encoding
        tk.Label(self.root, text="Enter Start Index for Encoding:").pack()
        self.coord_entry = tk.Entry(self.root, width=40)
        self.coord_entry.pack(pady=5)

        # Encode Button
        tk.Button(self.root, text="Hide Text in Image", command=self.encode_text).pack(pady=10)

        # Back to Home Button
        tk.Button(self.root, text="Back to Home", command=self.load_home_page).pack(pady=5)


if __name__ == '__main__':
    root = TkinterDnD.Tk()
    app = SteganographyApp(root)
    root.mainloop()