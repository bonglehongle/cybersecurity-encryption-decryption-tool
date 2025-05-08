import tkinter as tk
from tkinter import filedialog, messagebox
from src.utils import center_window, upload_file, download_file, setup_button_hover


def encrypt_rot13(text):
    """
    Encrypts text using the ROT13 Cipher.

    Args:
        text (str): The text to encrypt.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + 13) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt_rot13(text):
    """
    Decrypts text using the ROT13 Cipher (same as encryption).

    Args:
        text (str): The text to decrypt.

    Returns:
        str: The decrypted text.
    """
    return encrypt_rot13(text)  # ROT13 is its own inverse


def rot13_page(window, main_window):
    """Creates and runs the ROT13 Cipher GUI."""

    window.title("ROT13 Cipher")
    window.configure(bg="#0D0D0D")
    center_window(window, 600, 500)

    def back_to_main():
        window.destroy()
        main_window.deiconify()

    back_button = tk.Button(window, text="Back", font=("Arial", 12, "bold"), bg="#0D0D0D", fg="#FFFFFF",
                            command=back_to_main)
    back_button.place(x=10, y=10)

    algorithm_label = tk.Label(window, text="ROT13 Cipher", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#0D0D0D")
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

    buttons_frame = tk.Frame(window, bg="#0D0D0D")
    buttons_frame.pack(pady=(40, 0))

    def encrypt():
        text = entry_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "Please enter some text.")
            return
        encrypted_text = encrypt_rot13(text)
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, encrypted_text)
        result_text.config(state=tk.DISABLED)

    def decrypt():
        text = entry_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "Please enter some text.")
            return
        decrypted_text = decrypt_rot13(text)
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


