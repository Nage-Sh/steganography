import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text in Image - Steganography")
        self.root.geometry("1000x1000")
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

    def load_decoder_page(self):
        self.current_page = "decoder"
        
        for widget in self.root.winfo_children():
            widget.destroy()

        self.decoder_label = tk.Label(self.root, text="Decoder Page", font=("Arial", 16))
        self.decoder_label.pack(pady=20)

        # Drag and Drop Area for Decoder
        self.drop_label = tk.Label(self.root, text="Drag and drop a .png or .bmp image here", bg="#f0f0f0", relief="solid", bd=2, width=60, height=4)
        self.drop_label.pack(pady=20)

        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.drop_file_decoder)

        # Load Image Button (Drag and Drop)
        self.load_btn = tk.Button(self.root, text="Load Stego Image Manually", command=self.load_image_decoder)
        self.load_btn.pack(pady=5)

        # Image Display
        self.img_label = tk.Label(self.root, text="Image will appear here", bd=2, relief="sunken")
        self.img_label.pack(pady=10)

        # Start Index for decoding
        tk.Label(self.root, text="Enter Start Index for Decoding:").pack()
        self.decode_coord_entry = tk.Entry(self.root, width=40)
        self.decode_coord_entry.pack(pady=5)

        # Decode Button
        tk.Button(self.root, text="Reveal Text from Image", command=self.decode_text).pack(pady=10)

        # Text box to display decoded text
        tk.Label(self.root, text="Decoded Text:").pack()
        self.decoded_text_box = tk.Text(self.root, height=5, width=60)
        self.decoded_text_box.pack(pady=5)

        # Copy to Clipboard Button
        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)

        # Back to Home Button
        tk.Button(self.root, text="Back to Home", command=self.load_home_page).pack(pady=5)
    
    def load_image_encoder(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.bmp")])
        if file_path:
            self.show_image(file_path)

    def load_image_decoder(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.bmp")])
        if file_path:
            self.show_image(file_path)

    def drop_file_encoder(self, event):
        # Get the dropped file path
        file_path = event.data.strip('{}')  # Remove braces if path contains spaces
        if file_path.lower().endswith((".png", ".bmp")):
            self.show_image(file_path)
        else:
            messagebox.showerror("Invalid Format", "Only PNG or BMP images are supported.")

    def drop_file_decoder(self, event):
        # Get the dropped file path
        file_path = event.data.strip('{}')  # Remove braces if path contains spaces
        if file_path.lower().endswith((".png", ".bmp")):
            self.show_image(file_path)
        else:
            messagebox.showerror("Invalid Format", "Only PNG or BMP images are supported.")

    def show_image(self, path):
        try:
            img = Image.open(path)
            self.original_image = img
            self.image_path = path

            preview = img.copy()
            preview.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(preview)

            self.img_label.configure(image=photo, text="")
            self.img_label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")

    def encode_text(self):
        if not self.original_image:
            messagebox.showerror("No Image", "Load an image first.")
            return

        text = self.text_entry.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("No Text", "Enter some text to hide.")
            return

        try:
            start_index = int(self.coord_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Index", "Please enter a valid integer index.")
            return

        # Convert text to binary and append delimiter 'Y'
        binary = ''.join(format(ord(c), '08b') for c in text) + '1111111111111111'  # delimiter
        pixels = list(self.original_image.getdata())  # 1D array of pixels

        # Encode the text into the pixels starting from the given index
        idx = start_index
        for bit in binary:
            r, g, b = pixels[idx]
            r = (r & ~1) | int(bit)  # Set the LSB to the binary bit
            pixels[idx] = (r, g, b)
            idx += 1

            if idx >= len(pixels):
                messagebox.showerror("Error", "Not enough space in image to encode the text.")
                return

        # Save the image with encoded text
        encoded_image = self.original_image.copy()
        encoded_image.putdata(pixels)

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            encoded_image.save(save_path)
            messagebox.showinfo("Success", f"Text encoded and saved to: {save_path}")

        
    def decode_text(self):
        if not self.original_image:
            messagebox.showerror("No Image", "Load an image first.")
            return

        try:
            start_index = int(self.decode_coord_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Index", "Please enter a valid integer index.")
            return

        pixels = list(self.original_image.getdata())  # 1D array of pixels
        binary_data = ""
        idx = start_index
        while idx < len(pixels):
            r, g, b = pixels[idx]
            binary_data += str(r & 1)  # Extract the LSB
            idx += 1

            if binary_data.endswith('1111111111111111'):  # Delimiter found
                break

        # Convert binary to text
        chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
        text = ''.join(chr(int(char, 2)) for char in chars if char != '11111111')  # Stop at delimiter

        self.decoded_text_box.delete(1.0, tk.END)
        self.decoded_text_box.insert(tk.END, text)

    def copy_to_clipboard(self):
        decoded_text = self.decoded_text_box.get(1.0, tk.END).strip()
        if decoded_text:
            self.root.clipboard_clear()
            self.root.clipboard_append(decoded_text)
            self.root.update()
            messagebox.showinfo("Success", "Text copied to clipboard!")
        else:
            messagebox.showerror("No Text", "No decoded text to copy.")


if __name__ == '__main__':
    root = TkinterDnD.Tk()
    app = SteganographyApp(root)
    root.mainloop()