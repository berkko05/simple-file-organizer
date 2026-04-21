## Simple File Organizer (SFO)

SFO is a lightweight utility that automatically categorizes and moves files from a source directory into specific, sorted folders based on their extensions. 

As of version 0.4.0, the application utilizes native OS dialogs for dynamic path selection and features a modular backend, paving the way for a fully integrated graphical interface.

### How to Use

1. Run the `sfo_main.py` script.
2. Select your desired **Source** directory using the popup window.
3. Select your desired **Target** directory for the sorted folders.
4. Choose whether to execute a **Dry Run**. Selecting "Yes" will print the expected file movements to the console without modifying your disk. Selecting "No" will execute the file sorting.

### Development Roadmap

This project is actively being developed. Below are the milestones for transitioning this utility into a fully functional desktop application.

#### [v0.4] Dynamic Path Selection & Target Routing - (Completed)
* Eliminated the need to hardcode file paths inside the script.
* Integrated a native OS folder selection window.
* Allowed the user to define separate "Source" and "Target" directories.
* Restructured code into modular frontend and backend files.

#### [v0.5] Graphical User Interface - (Next)
* **Goal:** Make the tool fully accessible to non-technical users with a working interface.
* **Implementation:** * Build a clean, modern user interface.
  * Map the existing Python logic functions to UI buttons and progress indicators.

#### [v1.0] Standalone Binary Release
* **Goal:** Distribute the software as a zero-dependency application.
* **Implementation:** * Compile the complete Python project into a standalone executable.
  * Release native `.exe` executables for Windows and binaries for Linux environments.
