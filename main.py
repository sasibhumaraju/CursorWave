import threading
import time
import tkinter as tk
from tkinter import messagebox, Frame, font
import webbrowser
import win32gui
import win32api
import win32con

# Global flag to control the simulation
running = False

def find_windows_by_title(title):
    hwnds = []

    def enum_windows_callback(handle, extra):
        window_title = win32gui.GetWindowText(handle)
        if title in window_title:
            hwnds.append(handle)

    win32gui.EnumWindows(enum_windows_callback, None)
    return hwnds

def ensure_num_lock_off():
    num_lock_state = win32api.GetKeyState(0x90)  # 0x90 is the virtual key code for Num Lock
    if num_lock_state:  # If Num Lock is on
        win32api.keybd_event(0x90, 0, 0, 0)  # Press down Num Lock
        win32api.keybd_event(0x90, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release Num Lock
        time.sleep(0.5)  # Optional: sleep to ensure the state change is processed

# Function to simulate key presses in the specified application
def send_keys_to_application(hwnd):
    if hwnd:
        ensure_num_lock_off()
        print("pressed")
        # Simulate left arrow key press
        win32api.keybd_event(win32con.VK_LEFT, 0, 0, 0)  # Press down left arrow
        win32api.keybd_event(win32con.VK_LEFT, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release left arrow
        time.sleep(0.1)
        win32api.keybd_event(win32con.VK_LEFT, 0, 0, 0)  # Press down left arrow
        win32api.keybd_event(win32con.VK_LEFT, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release left arrow
        time.sleep(0.5)
        
        # Simulate right arrow key press
        win32api.keybd_event(win32con.VK_RIGHT, 0, 0, 0)  # Press down right arrow
        win32api.keybd_event(win32con.VK_RIGHT, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release right arrow
        time.sleep(0.1)
        win32api.keybd_event(win32con.VK_RIGHT, 0, 0, 0)  # Press down right arrow
        win32api.keybd_event(win32con.VK_RIGHT, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release right arrow
        time.sleep(0.5)
    else:
        messagebox.showinfo("CursorWave Error", f"{win32gui.GetWindowText(hwnd)} window not found!")

def get_current_focused_application():
    hwnd = win32gui.GetForegroundWindow()  # Get the handle of the currently focused window
    window_title = win32gui.GetWindowText(hwnd)  # Get the title of the window
    return window_title

# Function to repeatedly simulate key presses
def simulate_keypresses(hwnd, interval):
    global running
    if hwnd:
        try:
            time.sleep(0.1)  # Short delay to ensure the window is in focus
            win32gui.SetForegroundWindow(hwnd)  # Bring the window to the foreground
        finally:
            print("window minimised")
        
    while running:
        if win32gui.GetWindowText(hwnd) != "":
            if hwnd == win32gui.GetForegroundWindow():
                send_keys_to_application(hwnd)
                time.sleep(interval)
        else: 
            running = False
            app_entry.config(state="normal")
            toggle_button.config(text="Start Waving 🌊!")
            status_label.config(text="😎! yet to wave..")  # Update status label
            messagebox.showinfo("CursorWave Error", f" window not found!")
            

# Function to start the simulation in a separate thread
def toggle_simulation():
    global running
    application_name = app_entry.get()  # Get the application name from the input field
    if application_name:
        hwnds = find_windows_by_title(application_name)  # Get all matching window handles
        if hwnds:
            if not running:
                running = True
                app_entry.config(state="disabled")
                try:
                    interval = float(0.0)  # Set interval to 0.5 seconds
                    threading.Thread(target=simulate_keypresses, args=(hwnds[0], interval)).start()  # Run in a separate thread
                    status_label.config(text=f"🌊🌊🌊 wavingggg in {application_name}!")  # Update status label
                    toggle_button.config(text="Stop Waving ✋!")
                except ValueError:
                    app_entry.config(state="normal")
                    messagebox.showerror("CursorWave Error", f"Waving not started on {win32gui.GetWindowText(hwnds[0])}!!")
            else:
                running = False
                app_entry.config(state="normal")
                toggle_button.config(text="Start Waving 🌊!")
                status_label.config(text="😎! yet to wave..")  # Update status label
                messagebox.showinfo("CursorWave Info", f"{win32gui.GetWindowText(hwnds[0])} Waving stopped!")
        else:
            app_entry.config(state="normal")
            messagebox.showinfo("CursorWave Info", f"No instances of '{application_name}' found!")
    else:
        app_entry.config(state="normal")
        messagebox.showinfo("CursorWave Error", "Please enter an application name!")

# Function to open GitHub in a web browser
def open_github():
    webbrowser.open("https://github.com/sasibhumaraju")

# Create the GUI window
root = tk.Tk()
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

# Link to GitHub
github_link = tk.Label(frame, font=bold_font, text="Say thanks 💖 to @sasibhumaraju", fg="#FF69B4", cursor="hand2", bg='#f0f0f0')
github_link.pack(pady=10)
github_link.bind("<Button-1>", lambda e: open_github())  # Bind the click event

def on_closing():
    global running
    running = False  # Stop simulation on closing
    root.destroy()  # Close the window

root.protocol("WM_DELETE_WINDOW", on_closing)  # Bind the close event

# Run the GUI loop
root.mainloop()
