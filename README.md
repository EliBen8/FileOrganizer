# File Organizer

A desktop app built with Python and tkinter that automatically sorts files in a selected folder into categorized subdirectories based on file extension.

## Features

- Browse and select any folder on your machine
- Automatically organizes files into categories: Media, Videos, Audio, Documents, Spreadsheets, Presentations, Code, Compressed, and Executables
- Displays a results log of every file moved
- Progress bar and status label that update on completion
- Undo functionality to reverse the organization and restore the original folder structure

## Project Structure

```
FileOrganizer/
├── app.py          # UI and button logic
├── organizer.py    # File organizing and undo logic
└── categories.py   # Dictionary of file categories and extensions
```

## Requirements

- Python 3.x
- tkinter (built into Python)
- tkinter.ttk (built into Python)

No third-party dependencies required.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/eliben8/FileOrganizer.git
cd FileOrganizer
```

2. Run the app:
```bash
python3 app.py
```

## Usage

1. Click **Browse** to select the folder you want to organize
2. Click **Organize** to sort the files
3. View the results log to see what was moved and where
4. Click **Undo Organization** to reverse the changes if needed

## Supported File Types

| Category      | Extensions                                              |
|---------------|---------------------------------------------------------|
| Media         | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp, .tiff     |
| Videos        | .mp4, .mov, .avi, .mkv, .wmv, .flv                    |
| Audio         | .mp3, .wav, .flac, .aac, .ogg, .m4a                   |
| Documents     | .pdf, .docx, .doc, .txt, .rtf, .odt, .pages           |
| Spreadsheets  | .xlsx, .xls, .csv, .ods                                |
| Presentations | .pptx, .ppt, .key                                      |
| Code          | .py, .js, .ts, .html, .css, .java, .cpp, .c, .go, .rs, .sh |
| Compressed    | .zip, .tar, .gz, .rar, .7z                             |
| Executables   | .exe, .msi, .dmg, .pkg, .deb, .appimage               |