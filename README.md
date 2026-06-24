# File Integrity Monitor

## 📌 Project Description
This project monitors a file for any changes using SHA-256 hashing.  
If the file is modified, the program detects it and alerts the user.

## ⚙ Features
- Generates SHA-256 hash of a file
- Continuously monitors file changes
- Detects modifications in real-time

## 🧠 Concept Used
- File handling in Python
- Hashing (SHA-256)
- Infinite loop with time delay

## 🚀 How to Run
1. Create a file named `test.txt`
2. Make sure `monitor.py` is in the same folder
3. Open terminal in that folder
4. Run the program:
5. The program will start monitoring the file
6. Open `test.txt` and change its content
7. Save the file
8. You will see output in terminal:
- "✔ No change detected"
- "⚠ File Modified Detected!"

## 📁 Project Structure
File-Integrity-Monitor/
│
├── monitor.py
├── README.md
└── test.txt

## 👨‍💻 Output Example
Monitoring file: test.txt
✔ No change detected
⚠ File Modified Detected!

## 🎯 Purpose
This project demonstrates how file integrity can be monitored using hashing techniques in cybersecurity.