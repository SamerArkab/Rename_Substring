import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files_in_directory(directory, old_substring, new_substring, remove_numbering):
    try:
        file_count = 0
        for filename in os.listdir(directory):
            old_file_path = os.path.join(directory, filename)
            if os.path.isfile(old_file_path):
                new_filename = filename.replace(old_substring, new_substring)
                if remove_numbering:
                    # Remove numbers in various formats
                    new_filename = re.sub(r'^\d+[\-_.\s]', '', new_filename)  # e.g., 1-, 1_, 1., 1 (space)
                    new_filename = re.sub(r'\(\d+\)', '', new_filename)        # e.g., (1)
                    new_filename = re.sub(r'^\d+', '', new_filename)          # e.g., 123filename
                    # new_filename = re.sub(r'\d+$', '', new_filename)          # e.g., filename123
                if new_filename != filename:  # Check if the filename is actually changing
                    new_file_path = os.path.join(directory, new_filename)
                    os.rename(old_file_path, new_file_path)
                    file_count += 1
        messagebox.showinfo("Success", f"A total of {file_count} files were renamed successfully.")
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

def on_submit():
    directory = directory_entry.get().strip()
    old_substring = old_substring_entry.get().strip()
    new_substring = new_substring_entry.get().strip()
    remove_numbering = remove_numbering_var.get()
    if not directory or (not old_substring and not remove_numbering) or not new_substring:
        messagebox.showwarning("Input Error", "All fields must be filled out.")
        return
    rename_files_in_directory(directory, old_substring, new_substring, remove_numbering)

def clear_fields():
    directory_entry.delete(0, tk.END)
    old_substring_entry.delete(0, tk.END)
    new_substring_entry.delete(0, tk.END)
    remove_numbering_var.set(False)

root = tk.Tk()
root.title("File Renamer")
# root.iconbitmap('rename.ico')

directory_label = tk.Label(root, text="Directory:")
directory_label.grid(row=0, column=0, padx=10, pady=10)
directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=0, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=10, pady=10)

old_substring_label = tk.Label(root, text="Old Substring:")
old_substring_label.grid(row=1, column=0, padx=10, pady=10)
old_substring_entry = tk.Entry(root, width=50)
old_substring_entry.grid(row=1, column=1, padx=10, pady=10)

new_substring_label = tk.Label(root, text="New Substring:")
new_substring_label.grid(row=2, column=0, padx=10, pady=10)
new_substring_entry = tk.Entry(root, width=50)
new_substring_entry.grid(row=2, column=1, padx=10, pady=10)

remove_numbering_var = tk.BooleanVar()
remove_numbering_checkbox = tk.Checkbutton(root, text="Remove numbering", variable=remove_numbering_var)
remove_numbering_checkbox.grid(row=3, column=0, columnspan=3, pady=10)

submit_button = tk.Button(root, text="Rename Files", command=on_submit)
submit_button.grid(row=4, column=0, columnspan=3, pady=20)

root.mainloop()
