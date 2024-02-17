
# Developing a Python-based GUI Application Patcher with Object-Oriented Programming (OOP)
This is a Python-based graphical user interface (GUI) tool designed to assist users in applying File patches to an application. The patcher allows users to automatically apply files to the local application's installed directory. Additionally, it provides options for choosing configurations like fonts, and 64-bit options.

## Important Note
This repository has been simplified and generalized from its original production code. It excludes specific application names and is intended solely for displaying Python OOP functionality and GUI features. Please note that it does not serve the actual patching purpose that was present in the production code.

## User Features
- Browse and select the target directory for patching.
- Option to upgrade the client to 64-bit for improved performance. (Default)
- Select different skin font styles, including Arial and GBK style fonts.
- Informative instructions for users.
- Progress bar indicating the status of the patching process.
- Error handling for common issues such as incorrect paths or open application processes.
- Threaded operation to prevent GUI freezing during patching.

## Backup Functionality
This Patcher includes a robust backup functionality to ensure the safety of your original files before applying any patches. 
The patcher creates a backup of the original files overwritten during the patching process in a separate folder labeled with the version number of the current application.
If the user encounters any issues simply revert to the original state using the files.
*It's recommended to review the backup files and understand their contents before making any manual changes.

## User Instructions
1. Ensure the application client is updated and working correctly.
2. Close all application clients before applying the patch.
3. Click the "Browse" button to select the correct "res" folder of your application.
4. Choose the skin font style.
5. Check the "Upgrade to 64-Bit Client" option for better performance.
6. Click "Start Patch" and wait for the patching process to complete.

## Important Notes
If the patch version is outdated, Only fallback files will be applied.


