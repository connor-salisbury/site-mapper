import os
import tkinter as tk
from tkinter import messagebox
import subprocess


def run_secondary_script(argument):
    # Define the path to the secondary script
    script_path = 'site-mapper.py'

    # Run the script with the argument
    try:
        result = subprocess.run(['python', script_path, argument], capture_output=True, text=True)
        if result.returncode != 0:
            messagebox.showerror('Error', result.stderr)
        else:
            messagebox.showinfo('Success!', result.stdout)
    except FileNotFoundError:
        messagebox.showerror('Error', f'Script not found: {script_path}')


def on_submit():
    argument = argument_entry.get()
    if not argument:
        messagebox.showerror('Error', 'Please enter an argument value')
        return
    run_secondary_script(argument)


# Create the GUI
root = tk.Tk()
root.title('Secondary Script Runner')
root.geometry('400x200')

# Create the argument entry field
argument_label = tk.Label(root, text='Argument:')
argument_label.pack(pady=10)
argument_entry = tk.Entry(root)
argument_entry.pack(pady=10)

# Create the submit button
submit_button = tk.Button(root, text='Go', command=on_submit)
submit_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()