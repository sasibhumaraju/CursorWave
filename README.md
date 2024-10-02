# CursorWave

CursorWave is a Python application that simulates a wave movement (left and right arrow keys) in a specified application window. This tool is particularly useful for keeping the application active and engaged, such as during presentations or coding sessions.

## Features

- Simulate left and right arrow key presses in the specified application window.
- The application detects whether the specified window is currently focused before executing key presses.
- User-friendly GUI built with Tkinter for easy interaction.
- Log file generated to track actions and events.

## Requirements

To run CursorWave, you will need Python installed on your machine. The following packages are required:

- `pyautogui`
- `pygetwindow`
- `pywin32`
- `Pillow` (optional, only if you need image processing features)

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
