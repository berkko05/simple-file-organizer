'''
Simple File Organizer Version 0.4.0
Created by Hyusein Berk Kanberoglu
'''

# region 1. IMPORTED LIBRARIES
import tkinter as tk
import sfo_core   # Importing the SFO's own module
from tkinter import messagebox
# endregion

# region 2. RUN APPLICATION
# The function that runs (featherless biped?)
def run_application():
    # Setup GUI
    root = tk.Tk()
    root.withdraw()

    # Prompt the user for source and target directories
    source, target = sfo_core.source_target_selection()

    # Ask the user whether to do a dry-run first
    dry_run = messagebox.askyesno(
        title="Dry run?",
        message="Preview without moving?",
        icon="question",
        default="yes"
    )

    # Build the extension map
    extension_map = sfo_core.categorize_extensions()

    # Call the backend logic
    sfo_core.organize_files(source, target, extension_map, dry_run=dry_run)
    print("Sorting complete!" if not dry_run else "Dry-run complete!")
# endregion

# region 3. RUN IF MAIN
# Only run the run_application function if run method is main
if __name__ == "__main__":
    run_application()
# endregion