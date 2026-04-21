'''
Simple File Organizer Version 0.4.0
Created by Hyusein Berk Kanberoglu
'''

# region 1. IMPORTED LIBRARIES
import os
import sys
import shutil
from tkinter import filedialog

# endregion

# region 2. CATEGORIZATION OF THE FILE EXTENSIONS

# A dictionary that maps file extensions
CATEGORY_MAP = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw",
        ".bmp", ".dib", ".heif", ".heic", ".indd", ".svg", ".ai", ".eps", ".ps",
        ".svgz", ".ico", ".icns", ".xcf", ".cr2", ".nef", ".orf", ".sr2", ".jfif"
    ],

    "Videos": [
        ".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".webm", ".3gp", ".m4v",
        ".ts", ".mts", ".rmvb", ".rm", ".vob", ".ogv", ".ogg", ".mng", ".mpeg",
        ".mpg", ".m2ts", ".mxf", ".f4v"
    ],

    "Audio": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".alac", ".aiff",
        ".amr", ".ape", ".au", ".opus", ".m4b", ".m4p"
    ],

    "Documents": [
        ".pdf", ".txt", ".docx", ".doc", ".md", ".xlsx", ".xls", ".pptx", ".ppt",
        ".csv", ".word", ".numbers", ".pages", ".rtf", ".odt", ".ods", ".odp",
        ".tex", ".epub", ".mobi", ".azw3"
    ],

    "Archives": [
        ".zip", ".tar", ".gz", ".rar", ".7z", ".iso", ".tar.gz", ".tar.bz2",
        ".tar.xz", ".pkg.tar.zst", ".deb", ".rpm", ".cab", ".z", ".bz2", ".xz",
        ".lzma", ".tgz"
    ],

    "Code": [
        ".py", ".c", ".cpp", ".h", ".hpp", ".java", ".cs", ".js", ".ts", ".rb",
        ".go", ".swift", ".sh", ".bash", ".zsh", ".fish", ".s", ".asm", ".ipynb",
        ".json", ".yaml", ".yml", ".xml", ".html", ".css", ".php", ".sql", ".r",
        ".kt", ".dart", ".rs", ".pl", ".lua"
    ],

    "Executables": [
        ".exe", ".msi", ".bat", ".cmd", ".sh", ".AppImage", ".run"
    ]
}


# Categorizing all the file extensions, the name is self explanatory
def categorize_extensions():
    # An empty dictionary for the program to use
    extension_map = {}

    # Iterate through the categories and their associated lists
    for folder_name, extensions_list in CATEGORY_MAP.items():
        # Iterate through each extension inside the list
        for extension in extensions_list:
            # Assign the folder name as a value for the key
            extension_map[extension] = folder_name

    # After this loop, extension_map contains a direct mapping of extensions to folder names

    return extension_map
# endregion

# region 3. TKINTER SOURCE & TARGET PATH SELECTION

# Calling the categorize_extensions function to get the extension map
def source_target_selection():
    # Ask the user to select the source directory using a native OS window
    print("Please select the Source directory...")
    source_directory = filedialog.askdirectory(title="Select Source Directory")

    # Exit the program if no directory is selected
    if not source_directory:
        print("No source directory selected. Exiting program.")
        sys.exit()

    # Ask the user to select the target directory using a native OS window
    print("Please select the Target directory...")
    target_directory = filedialog.askdirectory(title="Select Target Directory")

    # Exit the program if no directory is selected (yeah, again...)
    if not target_directory:
        print("No target directory selected. Exiting program.")
        sys.exit()

    # Print the source and target directories
    print(f"Source: {source_directory}")
    print(f"Target: {target_directory}")
    print("Starting organization process...")

    return source_directory, target_directory


# endregion

# region 4. FILE ORGANIZATION

# The main function that organizes the files
def organize_files(source, target, extension_map=None, dry_run=False):
    # If extension map doesn't have any values rebuild it
    if extension_map is None:
        extension_map = categorize_extensions()

    # Iterate through the items in the source directory
    for item_name in os.listdir(source):
        # Create the full path to the items
        item_path = os.path.join(source, item_name)

        # Check if the item is an actual file, not a directory
        if os.path.isfile(item_path):
            # Split the file name from the file extension
            file_name, file_extension = os.path.splitext(item_name)

            # Convert the extension to lowercase to avoid potential case sensitivity issues
            file_extension = file_extension.lower()

            # If the extension is in the map, it returns the folder name. If not, it returns "Others"
            destination_folder_name = extension_map.get(file_extension, "Others")

            # Merging the target directory with the destination folder
            destination_folder_path = os.path.join(target, destination_folder_name)

            # Create the folder if it doesn't exist, otherwise just skip it
            os.makedirs(destination_folder_path, exist_ok=True)

            # Constructing the path for the file to be moved
            destination_file_path = os.path.join(destination_folder_path, item_name)

            # A counter to help rename files with the same name
            counter = 1

            # Look Before You Leap approach for Collision Resolution
            while os.path.exists(destination_file_path):
                # Constructing the new file name with a counter, (so we can count!)
                new_file_name = f"{file_name}({counter}){file_extension}"
                destination_file_path = os.path.join(destination_folder_path, new_file_name)
                counter += 1

            # Perform the cross-drive compatible move
            if dry_run:
                print(f"[DRY-RUN] Would move: {item_name} --> {destination_folder_name}")
            else:
                # Move the file to the new location
                # Try-except block to handle potential errors
                try:
                    shutil.move(item_path, destination_file_path)
                    print(f"Moved: {item_name} --> {destination_folder_name}")
                # Assign the error to the variable e
                except OSError as e:
                    print(f"Skipped {item_name}: {e}")
# endregion
