import tkinter as tk
from tkinter import filedialog, messagebox
from src.utils import center_window, upload_file, download_file, setup_button_hover


def encrypt_caesar(text, key):
    """
    Encrypts text using the Caesar Cipher with the given key.

    Args:
        text (str): The plaintext to encrypt.
        key (str): The shift key (letter or number).

    Returns:
        str: The encrypted ciphertext, or empty string if key is invalid.
    """
    if not key:
        messagebox.showerror("Error", "Please enter a key.")
        return ""

    if key.isalpha():
        key = key.upper()
        key_as_num = ord(key) - ord('A')
    elif key.isnumeric():
        key_as_num = int(key)
    elif key[0] == '-' and key[1:].isnumeric():
        key_as_num = -int(key[1:])
    else:
        messagebox.showerror("Error", "Invalid key format. Please enter a letter or a number.")
        return ""

    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + key_as_num - shift) % 26 + shift)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt_caesar(cipher, key):
    """
    Decrypts text using the Caesar Cipher with the given key.

    Args:
        cipher (str): The ciphertext to decrypt.
        key (str): The shift key (letter or number).

    Returns:
        str: The decrypted plaintext, or empty string if key is invalid.
    """
    if not key:
        messagebox.showerror("Error", "Please enter a key.")
        return ""

    if key.isalpha():
        key = key.upper()
        key_as_num = ord(key) - ord('A')
    elif key.isnumeric():
        key_as_num = int(key)
    elif key[0] == '-' and key[1:].isnumeric():
        key_as_num = -int(key[1:])
    else:
        messagebox.showerror("Error", "Invalid key format. Please enter a letter or a number.")
        return ""

    decrypted_text = ""
    for char in cipher:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - key_as_num - shift) % 26 + shift)
        else:
            decrypted_text += char
    return decrypted_text


def caesar_page(window, main_window):
    """Creates and runs the Caesar Cipher GUI.

    Args:
        window (tk.Toplevel): The cipher window.
        main_window (tk.Tk): The main application window.
    """
    window.title("Caesar Cipher")
    window.configure(bg="#0D0D0D")
    center_window(window, 600, 500)

    def back_to_main():
        window.destroy()
        main_window.deiconify()  # Restore the main window

    back_button = tk.Button(window, text="Back", font=("Arial", 12, "bold"), bg="#0D0D0D", fg="#FFFFFF",
                            command=back_to_main)
    back_button.place(x=10, y=10)

    algorithm_label = tk.Label(window, text="Caesar Cipher", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#0D0D0D")
    algorithm_label.pack(pady=20)

    text_frame = tk.Frame(window, bg="#0D0D0D")
    text_frame.pack()

    entry_label = tk.Label(text_frame, text="Enter text", font=("Arial", 16, "bold"), fg="#FFFFFF", bg="#0D0D0D")
    entry_label.grid(row=0, column=0, padx=(20, 10), pady=(10, 2))

    entry_text = tk.Text(text_frame, height=5, width=20, font=("Courier New", 12, "bold"), bg="#F2E7DC")
    entry_text.grid(row=1, column=0, padx=(20, 10), pady=(0, 10))

    result_label = tk.Label(text_frame, text="Result", font=("Arial", 16, "bold"), fg="#FFFFFF", bg="#0D0D0D")
    result_label.grid(row=0, column=1, padx=(20, 10), pady=(10, 2))

    result_text = tk.Text(text_frame, height=5, width=20, font=("Courier New", 12, "bold"), state=tk.DISABLED,
                          bg="#F2E7DC")
    result_text.grid(row=1, column=1, padx=(20, 10), pady=(0, 10))

    key_frame = tk.Frame(window, bg="#0D0D0D")
    key_frame.pack(pady=(10, 2))

    key_label = tk.Label(key_frame, text="Key:", font=("Arial", 16, "bold"), fg="#FFFFFF", bg="#0D0D0D")
    key_label.grid(row=0, column=0, padx=(12, 8), pady=(0, 2))

    key_entry = tk.Text(key_frame, height=1, width=42, font=("Arial", 12), bg="#F2E7DC")
    key_entry.grid(row=0, column=1, padx=(0, 9), pady=(0, 2))

    buttons_frame = tk.Frame(window, bg="#0D0D0D")
    buttons_frame.pack(pady=(40, 0))

    def encrypt():
        plaintext = entry_text.get("1.0", tk.END).strip()
        key = key_entry.get("1.0", tk.END).strip()
        if not plaintext:
            messagebox.showerror("Error", "Please enter some text.")
            return
        ciphertext = encrypt_caesar(plaintext, key)
        if ciphertext:
            result_text.config(state=tk.NORMAL)
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, ciphertext)
            result_text.config(state=tk.DISABLED)

    def decrypt():
        ciphertext = entry_text.get("1.0", tk.END).strip()
        key = key_entry.get("1.0", tk.END).strip()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter some text.")
            return
        plaintext = decrypt_caesar(ciphertext, key)
        if plaintext:
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