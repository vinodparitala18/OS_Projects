# 📂 Smart File Organizer

A real-time file organization tool that automatically sorts files into structured folders based on file type and date.

This project demonstrates core **Operating System concepts** such as file system operations, event-driven programming, and process automation.

---

## 🚀 Features

* ✅ Organizes files by **type** (Images, Documents, Videos, etc.)
* 📅 Creates folders based on **date (YYYY-MM)**
* 🔄 Works in **real-time** (auto-detects new files)
* 🛡️ Handles **duplicate file names safely**
* 📝 Maintains **logs** of all operations
* ⚡ Lightweight and fast

---

## 🧠 OS Concepts Covered

This project is designed to build practical understanding of:

* File System Management (`os`, `shutil`)
* File Metadata Handling (timestamps)
* Event-driven programming
* Real-time file monitoring
* Logging systems
* Basic concurrency (observer thread)

---

## 🏗️ Project Structure

```
file-organizer/
│
├── organizer.py        # Main script
├── organizer.log       # Log file (auto-generated)
├── test_folder/        # Folder to organize
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
```

### 2. Install dependencies

```bash
pip install watchdog
```

---

## ▶️ Usage

### 1. Create a folder to organize

```bash
mkdir test_folder
```

### 2. Add some files

Example:

```
test_folder/
  photo.jpg
  notes.txt
  video.mp4
```

### 3. Run the script

```bash
python organizer.py
```

---

## 🔄 How It Works

1. Organizes all existing files in the folder
2. Starts real-time monitoring
3. Detects new files automatically
4. Moves them into structured folders:

```
test_folder/
  Images/2026-04/
  Documents/2026-04/
  Videos/2026-04/
```

---

## 🧪 Example Output

```
Moved: test_folder/photo.jpg → test_folder/Images/2026-04/photo.jpg
Moved: test_folder/notes.txt → test_folder/Documents/2026-04/notes.txt
```

---

## 📝 Logs

All operations are recorded in:

```
organizer.log
```

Example:

```
2026-04-21 - INFO - Moved: test_folder/photo.jpg → test_folder/Images/2026-04/photo.jpg
```

---

## ⚠️ Limitations

* Large files may require additional handling (write completion check)
* Only predefined file types are categorized
* Does not currently support GUI

---

## 🚀 Future Improvements

* CLI support (`argparse`)
* Config file (JSON/YAML)
* GUI interface
* Docker support
* AI-based file classification
* Undo functionality

---

## 💼 Real-World Use Cases

* Organizing Downloads folder
* Log file management (DevOps)
* Data pipeline preprocessing
* Automated backup systems

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a pull request

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Vinod**

---

## ⭐ If you found this useful

Give it a ⭐ on GitHub!
