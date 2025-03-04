import os
import shutil
import logging
import argparse
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define file categories
FILE_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"},
    "Videos": {".mp4", ".mov", ".avi", ".mkv", ".flv"},
    "Music": {".mp3", ".wav", ".aac", ".flac"},
    "Archives": {".zip", ".rar", ".tar", ".gz", ".7z"},
    "Code": {".py", ".java", ".cpp", ".js", ".html", ".css", ".sh"},
    "Executables": {".exe", ".bat", ".sh", ".dmg", ".app"},
    "Others": set(),  # Catch-all for unknown file types
}

def categorize_file(file: Path) -> str:
    """Categorizes a file based on its extension."""
    ext = file.suffix.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def create_folders(directory: Path):
    """Creates category folders in the given directory if they do not exist."""
    for category in FILE_CATEGORIES.keys():
        category_path = directory / category
        category_path.mkdir(exist_ok=True)

def move_file(file: Path, target_directory: Path):
    """Moves a file to its categorized folder, handling errors gracefully."""
    category = categorize_file(file)
    destination = target_directory / category / file.name
    try:
        shutil.move(str(file), str(destination))
        logging.info(f"Moved: {file.name} -> {category}/")
    except Exception as e:
        logging.error(f"Error moving {file.name}: {e}")

def organize_files(directory: Path):
    """Organizes files in the given directory into categorized folders."""
    if not directory.exists() or not directory.is_dir():
        logging.error(f"The folder '{directory}' was not found or is not a directory.")
        return
    
    create_folders(directory)
    
    for file in directory.iterdir():
        if file.is_file():
            move_file(file, directory)
    
    logging.info("The files have been successfully sorted! 🎉")

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory by type.")
    parser.add_argument("directory", type=str, help="Path to the directory to organize")
    args = parser.parse_args()
    organize_files(Path(args.directory))

if __name__ == "__main__":
    main()
