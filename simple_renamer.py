# -*- coding: utf-8 -*-
import os


# Default folder path (used if user leaves input empty)
DEFAULT_FOLDER_PATH = r"C:\Users\new\Desktop\rename_test"


def main():
    # Ask for folder (optional)
    print("Press Enter to use default folder:")
    print("  ", DEFAULT_FOLDER_PATH)
    folder_path = input("Enter folder path (or leave empty): ").strip()

    if not folder_path:
        folder_path = DEFAULT_FOLDER_PATH

    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist:", folder_path)
        return

    # Get details from user
    subject = input("Enter subject code (e.g., CN): ").strip()
    lab_no = input("Enter lab/assignment number (e.g., 1): ").strip()
    student_name = input("Enter student name/ID (e.g., Harine): ").strip()

    if not subject or not lab_no or not student_name:
        print("Subject, lab number, and name are required.")
        return

    # Get files in folder
    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    if not files:
        print("No files found in the folder.")
        return

    print("\nFiles found:")
    for f in files:
        print("  ", f)

    print("\nPreview of new names:")
    new_names = []
    for index, filename in enumerate(files, start=1):
        name, ext = os.path.splitext(filename)
        new_name = f"{subject}_LAB{lab_no}_{student_name}_{index:02d}{ext}"
        new_names.append((filename, new_name))
        print(f"  {filename} -> {new_name}")

    # Ask for confirmation
    answer = input("\nProceed with renaming? (y/n): ").strip().lower()
    if answer not in ("y", "yes"):
        print("Aborted. No files were renamed.")
        return

    print("\nRenaming files...")
    for (old_name, new_name) in new_names:
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        if os.path.exists(new_path):
            print(f"Skipping {old_name} -> {new_name} (target already exists)")
            continue

        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

    print("\nDone!")


if __name__ == "__main__":
    main()
