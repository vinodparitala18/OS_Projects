1. # 📂 Smart File Organizer

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

## ⭐ If you found this useful

Give it a ⭐ on GitHub!


2.  # 🖥️ Simple Command Line Shell

A minimal command-line shell built in Python that replicates core behavior of system shells like Bash.
This project demonstrates fundamental **Operating System concepts** such as process execution, command parsing, and environment management.

---

## 🚀 Features

* 🧾 Execute system commands (`ls`, `pwd`, `echo`, etc.)
* 📁 Built-in `cd` (change directory)
* ❌ Built-in `exit` to terminate shell
* 📍 Displays current working directory in prompt
* ⚡ Continuous interactive shell loop
* 🛡️ Basic error handling

---

## 🧠 OS Concepts Covered

This project helps in understanding:

* Process creation & execution
* Shell architecture
* Built-in vs external commands
* System calls abstraction
* Working directory management
* Command parsing
* Parent vs child process behavior

---

## 🏗️ Project Structure

```id="o0m7z7"
simple-shell/
│
├── shell.py        # Main shell implementation
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash id="2zt3eq"
git clone https://github.com/your-username/simple-shell.git
cd simple-shell
```

### 2. Run the shell

```bash id="4ibqu4"
python shell.py
```

---

## ▶️ Usage

Once started, the shell will display a prompt:

```id="h2p0a9"
/home/user $
```

You can run commands like:

```bash id="qonhcf"
ls
pwd
echo Hello
```

---

## 📁 Built-in Commands

### 🔹 `cd <directory>`

Change current working directory.

```bash id="5uv1cs"
cd Documents
cd ..
cd ~
```

---

### 🔹 `exit`

Exit the shell.

```bash id="a2wq3y"
exit
```

---

## ⚙️ How It Works

1. Displays current directory using `os.getcwd()`
2. Accepts user input
3. Parses command
4. Executes:

   * Built-in commands internally (`cd`, `exit`)
   * Other commands using subprocess (new process)
5. Loops continuously

---

## 🔄 Example Session

```id="r9d6is"
/home/user $ pwd
/home/user

/home/user $ cd ..
/home

/home $ ls
Documents  Downloads

/home $ exit
Exiting shell...
```

---

## ⚠️ Limitations

* No support for pipes (`|`)
* No background processes (`&`)
* No command history
* Uses `subprocess` instead of low-level system calls
* Limited parsing (basic commands only)

---

## 🚀 Future Improvements

* Pipe support (`|`)
* Background execution (`&`)
* Command history (`readline`)
* Environment variables support (`$HOME`)
* Auto-completion (tab support)
* Low-level implementation using `os.fork()` and `os.exec()`
* Colored prompt UI

---

## 💼 Real-World Relevance

Shells are fundamental tools in:

* Linux/Unix systems
* DevOps workflows
* Cloud environments
* System administration
* Container systems (Docker, Kubernetes)

---

## 👨‍💻 Author

**Vinod**

---

## ⭐ If you found this useful

Consider giving this repo a ⭐!

3.  # CPU Scheduling Simulator

A Python-based simulator implementing FCFS, SJF, and Round Robin algorithms. It models process scheduling, calculates waiting and turnaround times, and demonstrates CPU execution behavior. This project helps understand core operating system concepts like scheduling strategies, process management, and performance evaluation in a simple, practical way.

