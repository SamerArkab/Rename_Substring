# File Renamer

A simple Python application with a GUI to rename files in a specified directory. It allows you to replace a specific substring in filenames with another substring and optionally remove numbering from filenames.

## Features

- Select a directory to rename files.
- Replace specified substrings in filenames.
- Option to remove numbering from filenames (supports various formats like `1_`, `1-`, `1.`, `(1)`, etc.).
- Simple and user-friendly GUI built with Tkinter.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SamerArkab/Rename_Substring.git
    ```

## Usage

1. Run the application:

    ```bash
    python rename_substring_GUI.py
    ```

2. Use the GUI to:
    - Browse and select the directory containing the files you want to rename.
    - Enter the old substring you want to replace.
    - Enter the new substring to replace the old one.
    - Check the "Remove numbering" checkbox if you want to remove numbers from filenames.
    - Click the "Rename Files" button to perform the renaming operation.

## Building an Executable

To create an executable file for easier distribution, use PyInstaller:

1. Install PyInstaller:

    ```bash
    pip install pyinstaller
    ```

2. Create the executable:

    ```bash
    pyinstaller --onefile --windowed --icon=rename.ico rename_substring_GUI.py
    ```

The executable will be found in the `dist` directory.
