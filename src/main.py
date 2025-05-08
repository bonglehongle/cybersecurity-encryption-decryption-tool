import tkinter as tk
from PIL import Image, ImageTk
import os
from src import caesar_cipher, playfair_cipher, rail_fence_cipher, rot13_cipher, substitution_cipher, vigenere_cipher

def open_cipher_page(main_window, cipher_function):
    """
    Opens a cipher page as a Toplevel window and hides the main window.

    Args:
        main_window (tk.Tk): The main application window.
        cipher_function (function): The function to create the cipher page.
    """
    main_window.withdraw()  # Hide the main window
    cipher_window = tk.Toplevel(main_window)
    cipher_function(cipher_window, main_window)  # Pass both windows to the cipher function


def main_page():
    """Creates and runs the main application interface."""
    main_window = tk.Tk()
    main_window.title("Secure File Encryption and Decryption")
    main_window.configure(bg="#0D0D0D")

    # Welcome label
    welcome_label = tk.Label(main_window, text="Welcome, Hacker Man!", font=("Arial", 24, "bold"), fg="#FFFFFF",
                             bg="#0D0D0D")
    welcome_label.pack(pady=(50, 10))

    # Welcome details label
    welcome_details_label = tk.Label(main_window, text="Choose the name of the algorithm you want to use",
                                     font=("Arial", 12), fg="#FFFFFF", bg="#0D0D0D")
    welcome_details_label.pack()

    # Space
    space_label = tk.Label(main_window, text="", bg="#0D0D0D")
    space_label.pack(pady=20)

    # Icon
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(script_dir, "assets")
        image_path = os.path.join(assets_dir, "img_icon.jpeg")
        print(f"Image path: {image_path}")  # Debug print
        original_image = Image.open(image_path)
        resized_image = original_image.resize((60, 70))
        icon = ImageTk.PhotoImage(resized_image)
        icon_label = tk.Label(main_window, image=icon, bg="#0D0D0D")
        icon_label.image = icon
        icon_label.pack()
    except FileNotFoundError as e:
        print(f"Error loading image: {e}")

    # Buttons frame
    buttons_frame = tk.Frame(main_window, bg="#0D0D0D")
    buttons_frame.pack(pady=20)

    # Button styles
    button_style = {"bg": "#F2E7DC", "fg": "#0D0D0D", "font": ("Arial", 18, "bold"), "bd": 0, "relief": tk.RIDGE,
                    "width": 20}

    # Button commands
    def caesar_cipher_cmd():
        open_cipher_page(main_window, caesar_cipher.caesar_page)

    def playfair_cmd():
        open_cipher_page(main_window, playfair_cipher.playfair_page)

    def rot13_cmd():
        open_cipher_page(main_window, rot13_cipher.rot13_page)

    def substitution_cmd():
        open_cipher_page(main_window, substitution_cipher.substitution_page)

    def rail_fence_cmd():
        open_cipher_page(main_window, rail_fence_cipher.rail_fence_page)

    def vigenere_cmd():
        open_cipher_page(main_window, vigenere_cipher.vigenere_page)

    # Create buttons
    caesar_cipher_button = tk.Button(buttons_frame, text="Caesar Cipher", command=caesar_cipher_cmd, **button_style)
    caesar_cipher_button.grid(row=0, column=0, padx=10, pady=5)

    playfair_button = tk.Button(buttons_frame, text="Playfair", command=playfair_cmd, **button_style)
    playfair_button.grid(row=0, column=2, padx=10, pady=5)

    rot13_button = tk.Button(buttons_frame, text="ROT13", command=rot13_cmd, **button_style)
    rot13_button.grid(row=1, column=0, padx=10, pady=5)

    substitution_button = tk.Button(buttons_frame, text="Substitution", command=substitution_cmd, **button_style)
    substitution_button.grid(row=1, column=1, padx=10, pady=5)

    rail_fence_button = tk.Button(buttons_frame, text="Rail Fence", command=rail_fence_cmd, **button_style)
    rail_fence_button.grid(row=0, column=1, padx=10, pady=5)

    vigenere_button = tk.Button(buttons_frame, text="Vigenère", command=vigenere_cmd, **button_style)
    vigenere_button.grid(row=1, column=2, padx=10, pady=5)

    # Hover effect
    def on_enter(event):
        event.widget.config(bg="#FFFFFF")

    def on_leave(event):
        event.widget.config(bg="#F2E7DC")

    for button in (
    caesar_cipher_button, playfair_button, rot13_button, substitution_button, rail_fence_button, vigenere_button):
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    main_window.mainloop()


if __name__ == "__main__":
    main_page()