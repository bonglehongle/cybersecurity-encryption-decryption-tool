import tkinter as tk
from tkinter import filedialog, messagebox
from src.utils import center_window, upload_file, download_file, setup_button_hover


def generate_key(string, key):
    """
    Generates a key of the same length as the input string.

    Args:
        string (str): The input text.
        key (str): The initial key.

    Returns:
        str: The generated key.
    """
    key = key.upper()
    if len(string) == len(key):
        return key
    return key * (len(string) // len(key)) + key[:len(string) % len(key)]


def encrypt_vigenere(string, key):
    """
    Encrypts text using the Vigenère Cipher.

    Args:
        string (str): The plaintext to encrypt.
        key (str): The encryption key.

    Returns:
        str: The encrypted ciphertext.
    """
    key = generate_key(string, key)
    encrypt_text = []
    for i in range(len(string)):
        if string[i].isalpha():
            base = ord('A') if string[i].isupper() else ord('a')
            x = (ord(string[i]) + ord(key[i]) - 2 * base) % 26 + base
            encrypt_text.append(chr(x))
        else:
            encrypt_text.append(string[i])
    return ''.join(encrypt_text)


def decrypt_vigenere(cipher, key):
    """
    Decrypts text using the Vigenère Cipher.

    Args:
        cipher (str): The ciphertext to decrypt.
        key (str): The decryption key.

    Returns:
        str: The decrypted plaintext.
    """
    key = generate_key(cipher, key)
    decrypt_text = []
    for i in range(len(cipher)):
        if cipher[i].isalpha():
            base = ord('A') if cipher[i].isupper() else ord('a')
            x = (ord(cipher[i]) - ord(key[i]) + 26) % 26 + base
            decrypt_text.append(chr(x))
        else:
            decrypt_text.append(cipher[i])
    return ''.join(decrypt_text)


def vigenere_page(window, main_window):
    """Creates and runs the Vigenère Cipher GUI."""

    window.title("Vigenère Cipher")
    window.configure(bg="#0D0D0D")
    center_window(window, 600, 500)

    def back_to_main():
        window.destroy()
        main_window.deiconify()

    back_button = tk.Button(window, text="Back", font=("Arial", 12, "bold"), bg="#0D0D0D", fg="#FFFFFF",
                            command=back_to_main)
    back_button.place(x=10, y=10)

    algorithm_label = tk.Label(window, text="Vigenère Cipher", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#0D0D0D")
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
        plaintext = entry_text.get("1.0", tk.END).strip()
        key = key_entry.get().strip()
        if not plaintext or not key:
            messagebox.showerror("Error", "Please enter text and key.")
            return
        if not key.isalpha():
            messagebox.showerror("Error", "Key must contain only alphabetic characters.")
            return
        ciphertext = encrypt_vigenere(plaintext, key)
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, ciphertext)
        result_text.config(state=tk.DISABLED)

    def decrypt():
        ciphertext = entry_text.get("1.0", tk.END).strip()
        key = key_entry.get().strip()
        if not ciphertext or not key:
            messagebox.showerror("Error", "Please enter text and key.")
            return
        if not key.isalpha():
            messagebox.showerror("Error", "Key must contain only alphabetic characters.")
            return
        plaintext = decrypt_vigenere(ciphertext, key)
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, plaintext)
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



