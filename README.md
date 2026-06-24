# File Integrity Monitor

##  Intern Details
- Name: Pavan Kumar Varri  
- Intern ID: CITS5128  
- Domain: Cybersecurity & Ethical Hacking  
- Internship Duration: 4 Weeks  


##  Project Name
File Integrity Monitor


##  Project Description
This project monitors a file and detects any changes using SHA-256 hashing.  
It continuously checks the file integrity and alerts the user if any modification is detected.


##  Project Objective
To detect unauthorized file modifications and ensure file integrity using hashing techniques.


##  Technologies Used
- Python  
- hashlib (SHA-256)  
- OS module  
- Time module  


##  Concepts Used
- File Handling  
- Cryptographic Hashing (SHA-256)  
- Loops and Delay Execution  
- Cybersecurity Basics (Integrity Checking)


##  How to Run

1. Create a file named `test.txt`
2. Keep `monitor.py` and `test.txt` in the same folder
3. Open terminal in project folder
4. Run the program:

python monitor.py

5. Modify `test.txt` content and save it
6. Observe detection messages in terminal


##  Project Structure

File-Integrity-Monitor/
│
├── monitor.py
├── README.md
├── test.txt
└── screenshots/

##  Output Screenshots

### source code
* Screenshot 2026-06-24 150013 code.png

### No Change Detected
* Screenshot 2026-06-24 150436 output1.png

### File Modified Detected
* Screenshot 2026-06-24 150617 output2.png

##  Result
The system successfully detects changes in file content using hashing and ensures file integrity.
