import tkinter as tk
import tkinter.ttk as ttk # for progress bar
from tkinter import filedialog

from organizer import organize_folders
from organizer import undo_organize

last_organized_path = None

# --- Functions ---
def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder_path)

def organize_command():
    global last_organized_path
    # get the filled dir path from the entry widget
    folder_path = folder_path_entry.get()

    if not folder_path:
        return
    
    # delete any old actions from the results list box
    results_list.delete(0, tk.END)

    results = organize_folders(folder_path)

    # add new actions to the list
    for i in results:
        results_list.insert(tk.END, i)

    # progress label & bar logic
    progress_label.config(text = f"Done - {len(results)} files processed")
    progress_bar["value"] = 100

    # store the last organized path for undo
    last_organized_path = folder_path

    # show the undo button only if the listbox is populated
    if results_list.size() > 0:
        undo_frame.grid()

def undo_command():
    if not last_organized_path:
        return

    results_list.delete(0, tk.END)

    results = undo_organize(last_organized_path)

    for i in results:
        results_list.insert(tk.END, i)

    progress_label.config(text = f"Done - {len(results)} files unorganized")
    progress_bar["value"] = 0

    undo_frame.grid_remove()  # hide after undo

# Initialize the TK window
root = tk.Tk()
root.title("File Organizer")
root.columnconfigure(0, weight = 1)
root.rowconfigure(3, weight = 1)

# --- Folder Selection Section (Lable, Entry, and Selection Button)---
folder_frame = tk.Frame(root, background = "#C0D6DF")
folder_frame.grid(row = 0, column = 0, sticky="ew")
folder_frame.columnconfigure(0, weight=1)

instruction_label = tk.Label(
    master = folder_frame,
    font = ("Helvetica", 12),
    text = "Folder",
    foreground = "black",
    background = "#C0D6DF"
)
instruction_label.grid(row = 0, column = 0, sticky = "w")

folder_path_entry = tk.Entry(
    master = folder_frame, 
    background = "white",
    foreground = "black",
    highlightbackground = "#4A6FA5",
    insertbackground = "black"
)
folder_path_entry.grid(row = 1, column = 0, sticky="ew")

folder_selection_btn = tk.Button(
    master = folder_frame, 
    text = "Browse", 
    highlightbackground = "#C0D6DF",
    command = browse_folder
)
folder_selection_btn.grid(row = 1, column = 1)

# --- Action Frame (Organize Button, Progress) ---
action_frame = tk.Frame(root, background = "#4F6D7A")
action_frame.grid(row = 1, column = 0, sticky = "ew")
action_frame.columnconfigure(0, weight = 1)

organize_button = tk.Button(
    master = action_frame,
    command = organize_command,
    text = "Organize",
    highlightbackground = "#4F6D7A",
    pady = 5
)
organize_button.grid(row = 0, column = 0, sticky = "ew")

# --- Progress Frame (Progress Bar, Progress Label) ---
progress_frame = tk.Frame(root, background = "#4F6D7A")
progress_frame.grid(row = 2, column = 0, sticky = "ew")
progress_frame.columnconfigure(0, weight = 1)

progress_bar = ttk.Progressbar(
    master = progress_frame,
    mode = "determinate",
    length = 300
)
progress_bar.grid(row = 0, column = 0, sticky = "ew")

progress_label = tk.Label(
    master = progress_frame,
    text = "Progress will display here",
    font = ("Helvetica", 10),
    foreground = "black",
    background = "#4F6D7A"
)
progress_label.grid(row = 1, column = 0, sticky = "w")

# --- Results Frame (Label, Listbox) -- 
results_frame = tk.Frame(root, background = "#4A6FA5")
results_frame.grid(row = 3, column = 0, sticky = "nsew")
results_frame.columnconfigure(0, weight = 1)
results_frame.rowconfigure(1, weight = 1)

results_label = tk.Label(
    master = results_frame,
    text = "Results:",
    font = ("Helvetica", 12),
    foreground = "black",
    background = "#4A6FA5"
)
results_label.grid(row = 0, column = 0, sticky = "w")

results_list = tk.Listbox(
    master = results_frame,
    foreground = "black",
    background = "#DBE9EE",
    font=("Menlo", 11),
    height = 10
)
results_list.grid(row = 1, column = 0, sticky = "nsew")

# --- Undo Frame (Undo Button) ---
undo_frame = tk.Frame(root, background = "#4A6FA5")
undo_frame.grid(row = 4, column = 0, sticky = "ew")
undo_frame.grid_remove() #hide the frame unless the listbox is filled
undo_frame.columnconfigure(0, weight = 1)

undo_button = tk.Button(
    master = undo_frame,
    command = undo_command,
    text = "Undo Organization",
    highlightbackground = "#4A6FA5"
)
undo_button.grid(row = 0, column = 0, sticky = "ew")

root.mainloop()