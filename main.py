import threading
import time
import tkinter as tk
from tkinter import messagebox, Frame, font
import webbrowser
import logging
import os
import win32gui
import win32api
import win32con

log_path = os.path.join(os.getcwd(), 'app.log')  # Save log in the current directory
logging.basicConfig(filename=log_path, level=logging.DEBUG)

# Global flag to control the simulation
running = False

def find_window_by_title(title):
    hwnd = None

    def enum_windows_callback(handle, extra):
        nonlocal hwnd
        window_title = win32gui.GetWindowText(handle)
        if title in window_title:
            hwnd = handle

    win32gui.EnumWindows(enum_windows_callback, None)
    return hwnd

# Function to simulate pressing 'H' in the specified window
def send_h_to_application(application_name):
    hwnd = find_window_by_title(application_name)  # Look for a window with the given title
    if hwnd:
        logging.info(f"Found window with handle: {hwnd}")
        # win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, ord('H'), 0)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RIGHT, 0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RIGHT, 0)
        time.sleep(1)  # Short delay between keypress and key release
        # win32api.PostMessage(hwnd, win32con.WM_KEYUP, ord('H'), 0)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_LEFT, 0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_LEFT, 0)
        time.sleep(1)
        print(f"wave on {application_name}")
        logging.info(f"wave on {application_name}")
    else:
        print(f"{application_name} window not found!")
        logging.warning(f"{application_name} window not found!")

# Function to simulate key presses repeatedly
def simulate_keypresses(application_name, interval):
    hwnd = find_window_by_title(application_name)  # Look for a window with the given title
    if hwnd:
        try:
            win32gui.SetForegroundWindow(hwnd)
        except ValueError:
            logging.info(f"Window minimised")

    global running
    while running:
        send_h_to_application(application_name)
        

# Function to start the simulation in a separate thread
def toggle_simulation():
    global running
    application_name = app_entry.get()  # Get the application name from the input field
    if application_name or running:
        hwnd = find_window_by_title(application_name)
        if hwnd:
            if not running:
                running = True
                try:
                    interval = float(1)  # Set interval to 1 secondhhhhhh
                    threading.Thread(target=simulate_keypresses, args=(application_name, interval)).start()  # Run in a separate thread
                    status_label.config(text=f"🌊🌊🌊 wavingggg in {application_name}!")  # Update status label
                    toggle_button.config(text="Stop Waving ✋!")
                    messagebox.showinfo("CurserWave Info", f"Waving started in {application_name}!")
                except ValueError:
                    messagebox.showerror("CurserWave Error", "Waving not started!!")
            else:
                running = False
                toggle_button.config(text="Start Waving 🌊!")
                status_label.config(text="😎! yet to wave..")  # Update status label
                messagebox.showinfo("CurserWave Info", f"Waving stopped in {application_name}!")
        else:
            messagebox.showinfo("CurserWave Info", f"Application {application_name} not found!! 🤐")
    else:
        messagebox.showinfo("CurserWave Error", "Please enter an application name!")




# Function to open Google in a web browser
def open_google():
    webbrowser.open("https://github.com/sasibhumaraju")

# Create the GUI window
root = tk.Tk()
# root.overrideredirect(True)
root.resizable(False, False) 

# Define a bold font
bold_font = font.Font(size=8, weight="bold")

root.title("CursorWave by @sasibhumaraju")
root.configure(bg='white')  # Set background color

# Create a frame for better layout
frame = Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Create GUI elements
label = tk.Label(frame, text="CursorWave sends 'cursor Wave' to the application window you specify.\nEnter the application name below and start the simulation.", bg='#f0f0f0')
label.pack(pady=10)

info_label = tk.Label(frame, text="INFO: Place the cursor in the targeted application and if targeted\n application is in background then CursorWave does not work on it. \n😅!", fg="green", bg='#f0f0f0')
info_label.pack(pady=5)

# Entry for the user to input the application name
app_entry = tk.Entry(frame, width=30)
app_entry.pack(pady=10)

toggle_button = tk.Button(frame, padx=20, pady=10, borderwidth=10, font=bold_font, cursor="hand2", text="Start Waving 🌊!!", command=toggle_simulation)
toggle_button.pack(pady=20)

# Status label to display simulation status
status_label = tk.Label(frame, text="😎! yet to wave..", bg='#f0f0f0')
status_label.pack(pady=10)

# Link to Google
google_link = tk.Label(frame, font=bold_font, text="Say thanks 💖 to @sasibhumaraju", fg="#FF69B4", cursor="hand2", bg='#f0f0f0')
google_link.pack(pady=10)
google_link.bind("<Button-1>", lambda e: open_google())  # Bind the click event

def on_closing():
    global running
    running = False  # Stop simulation on closing
    root.destroy()  # Close the window

root.protocol("WM_DELETE_WINDOW", on_closing)  # Bind the close eventhhhhhhhhhhhhhhhh

# Run the GUI loop
root.mainloop()
