import tkinter as tk
from tkinter import filedialog, messagebox
from src.utils import center_window, upload_file, download_file, setup_button_hover


def generate_key_table(key):
    """
    Generates a 5x5 key table for the Playfair Cipher.

    Args:
        key (str): The key string.

    Returns:
        list: A list of 25 characters forming the key table.
    """
    key = key.replace(" ", "").upper().replace("J", "I")
    key_table = []
    for char in key:
        if char not in key_table and char.isalpha():
            key_table.append(char)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key_table:
            key_table.append(char)
    return key_table


def split_text(text):
    """
    Splits text into pairs of characters, adding 'X' as needed.

    Args:
        text (str): The input text.

    Returns:
        list: List of character pairs.
    """
    text = text.replace(" ", "").upper()
    text_pairs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i + 1]:
            text_pairs.append(text[i] + "X")
            i += 1
        else:
            text_pairs.append(text[i] + text[i + 1])
            i += 2
    return text_pairs


def encrypt_playfair(text, key):
    """
    Encrypts text using the Playfair Cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (str): The encryption key.

    Returns:
        str: The encrypted ciphertext.
    """
    key_table = generate_key_table(key)
    text_pairs = split_text(text)
    encrypted_text = ""
    for pair in text_pairs:
        row1, col1 = divmod(key_table.index(pair[0]), 5)
        row2, col2 = divmod(key_table.index(pair[1]), 5)
        if row1 == row2:
            encrypted_text += key_table[row1 * 5 + (col1 + 1) % 5]
            encrypted_text += key_table[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += key_table[((row1 + 1) % 5) * 5 + col1]
            encrypted_text += key_table[((row2 + 1) % 5) * 5 + col2]
        else:
            encrypted_text += key_table[row1 * 5 + col2]
            encrypted_text += key_table[row2 * 5 + col1]
    return encrypted_text


def decrypt_playfair(cipher, key):
    """
    Decrypts text using the Playfair Cipher.

    Args:
        cipher (str): The ciphertext to decrypt.
        key (str): The decryption key.

    Returns:
        str: The decrypted plaintext.
    """
    key_table = generate_key_table(key)
    text_pairs = split_text(cipher)
    decrypted_text = ""
    for pair in text_pairs:
        row1, col1 = divmod(key_table.index(pair[0]), 5)
        row2, col2 = divmod(key_table.index(pair[1]), 5)
        if row1 == row2:
            decrypted_text += key_table[row1 * 5 + (col1 - 1) % 5]
            decrypted_text += key_table[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += key_table[((row1 - 1) % 5) * 5 + col1]
            decrypted_text += key_table[((row2 - 1) % 5) * 5 + col2]
        else:
            decrypted_text += key_table[row1 * 5 + col2]
            decrypted_text += key_table[row2 * 5 + col1]
    return decrypted_text


def playfair_page(window, main_window):
    """Creates and runs the Playfair Cipher GUI."""

    window.title("Playfair Cipher")
    window.configure(bg="#0D0D0D")
    center_window(window, 600, 500)

    def back_to_main():
        window.destroy()
        main_window.deiconify()

    back_button = tk.Button(window, text="Back", font=("Arial", 12, "bold"), bg="#0D0D0D", fg="#FFFFFF",
                            command=back_to_main)
    back_button.place(x=10, y=10)

    algorithm_label = tk.Label(window, text="Playfair Cipher", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#0D0D0D")
    algorithm_label.pack(pady=20)

    text_frame = tk.Frame(window, bg="#0D0D0D")
    text_frame.pack()

    entry_label = tk.Label(text_frame, text="Enter text", font=("Arial", 16, "bold"), fg="#FFFFFF", bg="#0D0D0D")
    entry_label.grid(row=0, column=0, padx=(20, 10), pady=(10, 2))

    global entry_text
    entry_text = tk.Text(text_frame, height=5, width=20, font=("Courier New", 12, "bold"), bg="#F2E7DC")
    entry_text.grid(row=1, column=0, padx=(20, 10), pady=(0, 10))

    result_label = tk.Label(text_frame, text="Result", font=("Arial", 16, "bold"), fg="#FFFFFF", bg="#0D0D0D")
    result_label.grid(row=0, column=1, padx=(20, 10), pady=(10, 2))

    global result_text
    result_text = tk.Text(text_frame, height=5, width=20, font=("Courier New", 12, "bold"), state=tk.DISABLED,
                          bg="#F2E7DC")
    result_text.grid(row=1, column=1, padx=(20, 10), pady=(0, 10))

    key_frame = tk.Frame(window, bg="#0D0D0D")
    key_frame.pack(pady=(10, 2))

    key_label = tk.Label(key_frame, text="Key:", font=("Arial", 16, "bold"), fg="#FFFFFF", bg="#0D0D0D")
    key_label.grid(row=0, column=0, padx=(12, 8), pady=(0, 2))

    global key_entry
    key_entry = tk.Entry(key_frame, font=("Arial", 12, "bold"), bg="#F2E7DC", width=42)
    key_entry.grid(row=0, column=1, padx=(0, 9), pady=(0, 2))

    buttons_frame = tk.Frame(window, bg="#0D0D0D")
    buttons_frame.pack(pady=(40, 0))

    def encrypt():
        text = entry_text.get("1.0", tk.END).strip()
        key = key_entry.get().strip()
        if not text or not key:
            messagebox.showerror("Error", "Please enter text and key.")
            return
        if not key.isalpha():
            messagebox.showerror("Error", "Key must contain only alphabetic characters.")
            return
        encrypted_text = encrypt_playfair(text, key)
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, encrypted_text)
        result_text.config(state=tk.DISABLED)

    def decrypt():
        cipher = entry_text.get("1.0", tk.END).strip()
        key = key_entry.get().strip()
        if not cipher or not key:
            messagebox.showerror("Error", "Please enter text and key.")
            return
        if not key.isalpha():
            messagebox.showerror("Error", "Key must contain only alphabetic characters.")
            return
        decrypted_text = decrypt_playfair(cipher, key)
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, decrypted_text)
        result_text.config(state=tk.DISABLED)

    encrypt_button = tk.Button(buttons_frame, text="Encrypt", font=("Arial", 12, "bold"), bg="#F2E7DC", command=encrypt,
                               width=42)
    encrypt_button.grid(row=0, column=0, padx=10, pady=8, columnspan=2)

    decrypt_button = tk.Button(buttons_frame, text="Decrypt", font=("Arial", 12, "bold"), bg="#F2E7DC", command=decrypt,
                               width=42)
    decrypt_button.grid(row=1, column=0, padx=10, pady=8, columnspan=2)

    file_buttons_frame = tk.Frame(window, bg="#0D0D0D")
    file_buttons_frame.pack(pady=10)

    upload_button = tk.Button(file_buttons_frame, text="Upload File", font=("Arial", 12, "bold"), bg="#F2E7DC",
                              command=lambda: upload_file(entry_text), width=20)
    upload_button.grid(row=0, column=0, padx=10)

    download_button = tk.Button(file_buttons_frame, text="Download File", font=("Arial", 12, "bold"), bg="#F2E7DC",
                                command=lambda: download_file(result_text), width=19)
    download_button.grid(row=0, column=1, padx=10)

    setup_button_hover([encrypt_button, decrypt_button, upload_button, download_button])



