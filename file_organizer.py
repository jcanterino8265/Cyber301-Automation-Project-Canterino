#!/usr/bin/env python3
"""
Cyber301 Automation Project: Selective File Organizer and Backup Utility

Adapted from the file-organizing concepts in Chapter 11, "Organizing Files,"
of Automate the Boring Stuff with Python by Al Sweigart.

The program sorts files in one folder into subfolders based on file extension,
then creates a timestamped ZIP backup of the organized folder.

Tip: Test this program on a copy of sample files; nothing too important. Moving files changes the
contents of the selected folder.
"""

import os
import shutil
import zipfile
from datetime import datetime
from pathlib import Path


# Map file extensions to the folders where those files should be placed.
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Logs_and_Data": [".log", ".json", ".xml", ".sql", ".db"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"],
    "Scripts_and_Code": [".py", ".sh", ".bat", ".ps1", ".html", ".js"],
}


def organize_directory(target_path):
    """Move files in the target folder into extension-based subfolders."""
    target_dir = Path(target_path).expanduser().resolve()

    # Check that the supplied path exists and is a directory.
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"[!] Error: '{target_path}' is not an existing directory.")
        return None

    print(f"\n[*] Organizing files in: {target_dir}")
    moved_count = 0
    skipped_count = 0

    # Look at the items directly inside the selected folder.
    for item in target_dir.iterdir():

        # Do not try to move folders or this running Python script.
        if item.is_dir() or item.name == Path(__file__).name:
            continue

        # Use the file extension to choose a category.
        file_extension = item.suffix.lower()
        destination_category = "Miscellaneous"

        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                destination_category = category
                break

        # Create the destination folder if it does not already exist.
        destination_folder = target_dir / destination_category
        destination_folder.mkdir(exist_ok=True)

        # Keep the original file if a file with the same name already exists.
        destination_path = destination_folder / item.name
        if destination_path.exists():
            print(f"[-] Skipped (destination already contains this name): {item.name}")
            skipped_count += 1
            continue

        # Move the file into its category folder.
        try:
            shutil.move(str(item), str(destination_path))
            print(f"[+] Moved: {item.name} -> {destination_category}/")
            moved_count += 1
        except OSError as error:
            print(f"[!] Could not move {item.name}: {error}")
            skipped_count += 1

    print(f"[*] Organization complete. Files moved: {moved_count}")
    print(f"[*] Files skipped: {skipped_count}")
    return target_dir


def backup_to_zip(target_dir):
    """Create a timestamped ZIP backup beside the organized folder."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"Backup_{target_dir.name}_{timestamp}.zip"
    zip_path = target_dir.parent / zip_name

    print(f"\n[*] Creating backup: {zip_name}")

    try:
        # Store the organized folder's contents in a compressed ZIP file.
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for root, _, filenames in os.walk(target_dir):
                for filename in filenames:
                    file_path = Path(root) / filename

                    # Preserve the folder structure inside the ZIP archive.
                    archive_name = file_path.relative_to(target_dir)
                    zip_file.write(file_path, arcname=archive_name)

        print(f"[+] Backup created: {zip_path}")
        return True

    except (OSError, zipfile.BadZipFile) as error:
        print(f"[!] Backup failed: {error}")

        # Remove an incomplete ZIP file, if one was created.
        if zip_path.exists():
            zip_path.unlink()
        return False


def main():
    """Ask the user for a folder, organize it, and create its backup."""
    print("=" * 60)
    print("CYBER301: SELECTIVE FILE ORGANIZER AND BACKUP UTILITY")
    print("=" * 60)
    print("Use a test folder or a copy of your files before trying this program.")

    folder_input = input(
        "\nEnter the folder path to organize "
        "(press ENTER to use the current folder): "
    ).strip()

    target_path = folder_input if folder_input else "."

    organized_folder = organize_directory(target_path)

    if organized_folder is not None:
        backup_successful = backup_to_zip(organized_folder)
        if backup_successful:
            print("\n[+] Organization and backup finished.")
        else:
            print("\n[!] Files were organized, but the backup was not completed.")
    else:
        print("\n[!] The program stopped because the folder path was invalid.")


if __name__ == "__main__":
    main()
