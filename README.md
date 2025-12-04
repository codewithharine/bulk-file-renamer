# Bulk File Renamer

**"I hate manually renaming files, so I built this."**

This is a simple Python automation tool created for **Kiro Heroes Week 2 – Lazy Automation**.  
It renames all files inside a folder using a clean and consistent format:

<subject>LAB<lab_no><student_name>_<index>.<ext>

Example output:
CN_LAB1_Harine_01.txt
CN_LAB1_Harine_02.jpg
CN_LAB1_Harine_03.docx


---

## 🚀 Features

- Rename all files in a folder in one go  
- Interactive inputs:
  - Folder path  
  - Subject code  
  - Lab number  
  - Student name  
- Auto-numbers files (`01`, `02`, `03`, …)
- Shows a preview *before* renaming  
- Safe renaming (skips if file already exists)

---

## 📂 Project Structure

bulk-file-renamer/
simple_renamer.py
README.md
.kiro/ # Added from Kiro workspace (required for challenge)


---

## 🧪 Usage

Run the script:
python simple_renamer.py

The tool will:

Ask for a folder path

Ask for:

Subject code (e.g., CN)

Lab number (e.g., 1)

Student name (e.g., Harine)

Show a preview of the new names

Ask permission

Rename the files

Enter folder path (or leave empty): C:\Users\new\Desktop\rename_test
Enter subject code (e.g., CN): CN
Enter lab/assignment number (e.g., 1): 1
Enter student name/ID (e.g., Harine): Harine

Preview:
abc.txt -> CN_LAB1_Harine_01.txt
xyz.jpg -> CN_LAB1_Harine_02.jpg

🤖 How I Used Kiro

This project was built using the Kiro Agent:

Kiro helped me design the idea for lazy automation

Generated the first version of the script

Helped improve:

Input handling

Preview logic

Cleaner renaming logic

Error handling

I used Kiro to refine the project structure and README

Screenshots of Kiro suggestions and iterations will be added in my AWS Builder blog post

License

MIT

If you want:
- A more fancy README version  
- Badges  
- Screenshots section  
- Or a longer version for GitHub  

Just tell me — I can generate that too!
