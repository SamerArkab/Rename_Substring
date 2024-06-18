# File Renamer

A simple Python application with a GUI to rename files in a specified directory. It allows you to replace a specific substring in filenames with another substring and optionally remove leading numbering patterns from filenames.

## Features

- Select a directory to rename files.
- Replace specified substrings in filenames.
- Option to remove leading numbering patterns from filenames (supports the following formats: `1_`, `1-`, `1.`, `(1)`).
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
    - Select the directory containing the files you want to rename.
    - Enter the old substring you want to replace.
    - Enter the new substring to replace the old one.
    - Check the "Remove numbering" checkbox if you want to remove any leading numbering patterns from the filenames.
    - Click the "Rename Files" button to perform the renaming operation.

3. Notes:
    - If 'Remove numbering' is checked, 'Old Substring' can be left empty.
    - If you want to completely remove the 'Old Substring', leave the 'New Substring' field empty.
    - Numbering patterns that will be removed include: #-, #_, #., (#), where '#' represents any digit.

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
