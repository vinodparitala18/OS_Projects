"""
SMART FILE ORGANIZER

This script automatically organizes files in a directory based on:
- File type (Images, Documents, Videos, etc.)
- Date (year-month)
- Handles duplicate file names
- Logs all operations
- Can run continuously (real-time monitoring)

OS Concepts Covered:
- File system operations (os module)
- Metadata handling (timestamps)
- Process automation
- Directory management
"""

import os                # OS-level file and directory operations
import shutil            # High-level file operations (move, copy)
import logging           # Logging system (used in real-world systems)
import time              # Time handling for timestamps
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# -------------------------------
# CONFIGURATION SECTION
# -------------------------------

# Folder to organize
SOURCE_FOLDER = "test_folder"

# File type mapping (you can expand this)
FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}


# -------------------------------
# LOGGING SETUP
# -------------------------------

# This creates a log file to track all operations
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -------------------------------
# HELPER FUNCTIONS
# -------------------------------

def get_unique_filename(path):
    """
    Prevents file overwrite by renaming duplicates.

    Example:
    file.txt → file_1.txt → file_2.txt

    OS Concept:
    - Checks file existence using file system calls
    """
    base, ext = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = f"{base}_{counter}{ext}"
        counter += 1

    return path


def get_file_category(extension):
    """
    Determines the category of a file based on its extension.

    If extension is not found → 'Others'
    """
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return "Others"


def organize_file(file_path):
    """
    Core function that organizes a single file.

    Steps:
    1. Get file extension
    2. Determine category
    3. Get file timestamp (for date-based folders)
    4. Create target directory
    5. Move file safely
    """

    try:
        # Skip if not a file
        if not os.path.isfile(file_path):
            return

        # Extract file extension
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()

        # Get category (Images, Docs, etc.)
        category = get_file_category(ext)

        # Get last modified time
        timestamp = os.path.getmtime(file_path)

        # Convert timestamp → Year-Month format
        date_folder = time.strftime("%Y-%m", time.localtime(timestamp))

        # Create target directory path
        target_folder = os.path.join(SOURCE_FOLDER, category, date_folder)

        # Create folder if it doesn't exist
        os.makedirs(target_folder, exist_ok=True)

        # Destination path
        filename = os.path.basename(file_path)
        dest_path = os.path.join(target_folder, filename)

        # Avoid overwriting existing files
        dest_path = get_unique_filename(dest_path)

        # Move file
        shutil.move(file_path, dest_path)

        # Log success
        logging.info(f"Moved: {file_path} → {dest_path}")
        print(f"Moved: {file_path} → {dest_path}")

    except Exception as e:
        # Log error
        logging.error(f"Error processing {file_path}: {e}")
        print(f"Error: {e}")


# -------------------------------
# INITIAL ORGANIZATION (Batch Mode)
# -------------------------------

def organize_existing_files():
    """
    Organizes all existing files in the source folder.

    OS Concept:
    - Directory traversal
    """
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)
        organize_file(file_path)


# -------------------------------
# REAL-TIME MONITORING
# -------------------------------

class FileHandler(FileSystemEventHandler):
    """
    Watches for new files in the directory.

    OS Concept:
    - Event-driven file system monitoring
    """

    def on_created(self, event):
        """
        Triggered when a new file is created.
        """
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            time.sleep(1)  # Wait to ensure file is fully written
            organize_file(event.src_path)


def start_monitoring():
    """
    Starts real-time monitoring of folder.
    """
    observer = Observer()
    event_handler = FileHandler()

    observer.schedule(event_handler, path=SOURCE_FOLDER, recursive=False)
    observer.start()

    print("📂 Monitoring started... Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


# -------------------------------
# MAIN FUNCTION
# -------------------------------

if __name__ == "__main__":
    print("🚀 Starting File Organizer...")

    # Step 1: Organize existing files
    organize_existing_files()

    # Step 2: Start real-time monitoring
    start_monitoring()