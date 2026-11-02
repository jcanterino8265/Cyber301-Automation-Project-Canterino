# Cyber301 Automation Project: File Organizer

 Project selection
- **Selected project:** File organizer
- **Book:** *Automate the Boring Stuff with Python* by Al Sweigart
- **Book section:** Chapter 11, "Organizing Files"
- **Project type:** An adapted project based on the chapter's file-organizing concepts

What the script does
This Python program organizes files in a folder according to their file extensions. It creates category folders when needed and moves files into the matching folder.

Categories:

- `Documents` — PDF, Word, text, PowerPoint, Excel, and CSV files
- `Images` — JPG, PNG, GIF, BMP, and SVG files
- `Logs_and_Data` — LOG, JSON, XML, SQL, and DB files
- `Archives` — ZIP, TAR, GZ, 7Z, and RAR files
- `Scripts_and_Code` — Python, shell, batch, PowerShell, HTML, and JavaScript files
- `Miscellaneous` — files with extensions that are not listed above

After organizing the files, the program creates a timestamped ZIP backup beside the folder being organized. If a destination folder already contains a file with the same name, the program skips that file rather than overwriting it.

Requirements
- Python 3
- No third-party Python packages are required. The script uses modules included with Python.

How to run it
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the program:

   ```bash
   python3 file_organizer.py
   ```

   On Windows, `python file_organizer.py` may be the appropriate command.
4. When prompted, enter the path to a test folder. Press ENTER to use the current folder.
5. Review the category folders and the ZIP backup created beside the folder you organized.

Example of Project
Imagine the test folder initially contains:

```text
demo_folder/
├── incident_report.pdf
├── network_scan.log
├── evidence_photo.png
└── notes.xyz
```

After running the program, it should look something similar to:

```text
demo_folder/
├── Documents/
│   └── incident_report.pdf
├── Images/
│   └── evidence_photo.png
├── Logs_and_Data/
│   └── network_scan.log
└── Miscellaneous/
    └── notes.xyz
```

A ZIP backup named similar to `Backup_demo_folder_YYYYMMDD_HHMMSS.zip` is created in the parent folder. The exact output depends on the files in the test folder and the time the program is run.

Challenges and solutions
- **Files with duplicate names:** Moving a file could overwrite a file already in the destination folder. The script checks whether the destination filename exists and skips the move if it does.

Improvements and modifications
- Added categories for logs, structured data, and scripts to make the organizer useful for a basic IT or cybersecurity workflow.
- Used `pathlib` to work with folder paths.
- Added a timestamped ZIP backup after file organization.
- Added a check to avoid overwriting files with duplicate names.
- Added messages showing how many files were moved or skipped.

Repository contents
```text
Cyber301-Automation-Project/
├── file_organizer.py
└── README.md
```# Cyber301-Automation-Project-Canterino
Python file organizer and automated backup utility for CYB301
