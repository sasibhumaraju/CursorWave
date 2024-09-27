import pyautogui
import threading
import time
import tkinter as tk
from tkinter import messagebox, Label, Frame, Text, END
import webbrowser

# Global flag to control the simulation
running = False

# Function to simulate left and right arrow key presses repeatedly
def simulate_arrows(interval):
    global running
    while running:
        pyautogui.press('left')  # Press left arrow
        time.sleep(interval)      # Wait for the interval
        pyautogui.press('right')  # Press right arrow
        time.sleep(interval)      # Wait for the interval

# Function to start the simulation in a separate thread
def toggle_simulation():
    global running
    if not running:
        running = True
        try:
            interval = float(1)  # Get interval from user input
            threading.Thread(target=simulate_arrows, args=(interval,)).start()  # Run in a separate thread
            status_label.config(text="🌊🌊🌊 wavingggg!")  # Update status label
            toggle_button.config(text="Stop Waving ✋!")
            messagebox.showinfo("Info", "Waving started!")
        except ValueError:
            messagebox.showerror("Input Error", "Waving not started!!")
    else:
        running = False
        toggle_button.config(text="Start Waving 🌊!")
        status_label.config(text="😎! yet to wave..")  # Update status label
        messagebox.showinfo("Info", "Waving stopped!")


# Function to open Google in a web browser
def open_google():
    webbrowser.open("https://github.com/sasibhumaraju")

# Create the GUI window
root = tk.Tk()
root.title("CursorWave by @sasibhumaraju")
root.configure(bg='white')  # Set background color

# Create a frame for better layout
frame = Frame(root,  padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Create GUI elements
label = tk.Label(frame, text="CursorWave creates a movement 😉 to right and left  by the cursor like a 🌊.\n It is mainly useful when you want to make 🖥 console alive.\n --> Place the cursor in the cosole,  sit back and relax <--", bg='#f0f0f0')
label.pack(pady=10)


toggle_button = tk.Button(frame,cursor="hand2", text="Start Waving 🌊!!", command=toggle_simulation)
toggle_button.pack(pady=20)


# Status label to display simulation status
status_label = tk.Label(frame, text="😎! yet to wave..", bg='#f0f0f0')
status_label.pack(pady=10)

# Link to Google
google_link = tk.Label(frame, text="Say thanks 💖 to @sasibhumaraju", fg="blue", cursor="hand2", bg='#f0f0f0')
google_link.pack(pady=10)
google_link.bind("<Button-1>", lambda e: open_google())  # Bind the click event



def on_closing():
    # Perform any cleanup here
    root.destroy()  # Close the window

root.protocol("WM_DELETE_WINDOW", on_closing)  # Bind the close event




# Run the GUI loop
root.mainloop()
