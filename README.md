# Steganograph

**Steganograph** is a simple image-based steganography tool that allows you to **hide text inside an image** using the Least Significant Bit (LSB) technique.

---

## What is Steganography?

Steganography is the practice of concealing a message within another medium such as images, audio, or video. In this project, we embed **text messages inside images** by modifying the least significant bits of pixel data.

---

## How It Works

### Encoding (Hiding Text)

1. **Convert Text to Binary**  
   Each character in the text is converted to its 8-bit binary equivalent.  
   Example: `'A'` → ASCII `65` → Binary `01000001`

2. **Add End Delimiter**  
   Append a special delimiter `1111111111111111` to signal the end of the message.

3. **Embed into Image Pixels**  
   Modify the LSB of the **Red** channel of each pixel with the binary bits of the message.

---

## Example
Embedding Binary Data into Image:
The binary data (converted from the text) is then encoded into the least significant bit (LSB) of each pixel's color channel (Red, Green, or Blue).

Each pixel has 3 color channels: Red, Green, and Blue (RGB). The idea is to take the least significant bit of each channel and replace it with the binary data of the text.

We iterate over each pixel and replace the LSB of the Red channel first, then Green, and finally Blue if needed.


### Encoding Text into Image

        ```python
        binary = ''.join(format(ord(c), '08b') for c in text) + '1111111111111111'
        pixels = list(self.original_image.getdata())  # Get pixel array
        idx = start_index

        for bit in binary:
            r, g, b = pixels[idx]
            r = (r & ~1) | int(bit)  # Set LSB of Red channel
            pixels[idx] = (r, g, b)
            idx += 1
            if idx >= len(pixels):
                messagebox.showerror("Error", "Not enough space in image to encode the text.")
                return


----

### 🔍 Decoding (Retrieving Text)

1. **Extract LSBs**  
   Read the LSBs of the Red channel of each pixel starting from a given index.

2. **Stop at Delimiter**  
   Continue collecting bits until the end delimiter `1111111111111111` is detected.

3. **Convert Binary to Text**  
   Split binary into 8-bit chunks and convert each chunk back to its ASCII character.

----

### Example

01000001 (which represents the letter A) will be decoded back to its corresponding character.
Decoding Process (Steps)
Extract Binary Data:
Loop through the image pixels and extract the least significant bit from each color channel to rebuild the binary data:

        pixels = list(self.original_image.getdata())  # 1D array of pixels
        binary_data = ""
        idx = start_index
        while idx < len(pixels):
            r, g, b = pixels[idx]
            binary_data += str(r & 1)  # Extract the LSB of the red channel
            idx += 1
            if binary_data.endswith('1111111111111111'):  # Stop when the delimiter is found
                break

## How to run this project in your system

- Zeroth step clone the repository 


        git clone git@github.com:Nage-Sh/steganography.git
        cd project

- Steps for Windows user


        python -m venv env
        env/Scripts/activate
        pip install -r requirements.txt
        python steganograph.py

- Steps for Linux user


        python3 -m venv env
        source venv/bin/activate
        pip install -r requirements.txt
        python3 steganograph.py
