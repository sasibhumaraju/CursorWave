# CursorWave

CursorWave is a simple Python application that simulates left and right arrow key presses in a specified application window. It is particularly useful for keeping a console window active or for other automation tasks.

## Features

- **Simulates key presses**: Automatically sends left and right arrow key presses to a specified application.
- **User-friendly GUI**: Built with Tkinter for a simple and intuitive interface.
- **Customizable application target**: Allows you to specify which application window to send key presses to.

## Requirements

To run the CursorWave application, you need to have Python installed on your system. The application uses the following libraries:

- `tkinter` (included with standard Python installations)
- `pywin32` (to interact with Windows GUI)

You can install the required external library by running:

```bash
pip install pywin32
