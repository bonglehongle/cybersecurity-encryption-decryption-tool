import tkinter as tk
from tkinter import filedialog, messagebox


def center_window(window, width, height):
    """
    Centers the window on the screen.

    Args:
        window (tk.Tk): The Tkinter window.
        width (int): Window width.
        height (int): Window height.
    """
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def upload_file(entry_text):
    """
    Uploads a text file and displays its content in the text area.

    Args:
        entry_text (tk.Text): The text area to display the file content.
    """
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                entry_text.delete("1.0", tk.END)
                entry_text.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")


def download_file(result_text):
    """
    Saves the content of the result text area to a file.

    Args:
        result_text (tk.Text): The text area containing the content to save.
    """
    content = result_text.get("1.0", tk.END).strip()
    if not content:
        messagebox.showerror("Error", "No content to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")


def setup_button_hover(buttons):
    """
    Sets up hover effects for buttons.

    Args:
        buttons (list): List of Tkinter buttons.
    """

    def on_enter(event):
        event.widget.config(bg="#FFFFFF")

    def on_leave(event):
        event.widget.config(bg="#F2E7DC")

    for button in buttons:
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)