import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
# import pyinstaller (Unnecessary import)

# Function to format the text
def format_text(input_text):
    # Correct paragraph indentation
    formatted_text = re.sub(r'\n\s*', '\n    ', input_text.strip())

    # Correct spacing after periods
    formatted_text = re.sub(r'\.(\S)', r'. \1', formatted_text)

    # Capitalize the start of sentences (simplified)
    formatted_text = re.sub(r'(?<=[\.\?\!]\s)(\w)', lambda x: x.group(1).upper(), formatted_text)

    return formatted_text

# Function to process the text and display the formatted version
def process_text():
    try:
        input_text = text_input.get("1.0", tk.END).strip()

        if not input_text:
            messagebox.showerror("Error", "Please paste some text into the box.")
            return

        if len(input_text.split()) > 100000:  # Roughly 500 pages
            messagebox.showerror("Error", "The input text exceeds the maximum allowed length of 500 pages.")
            return

        formatted_text = format_text(input_text)

        text_output.delete("1.0", tk.END)
        text_output.insert("1.0", formatted_text)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# GUI setup
app = tk.Tk()
app.title("Fiction Novel Formatter")
app.geometry("800x600")

# Input text area
label_input = tk.Label(app, text="Paste your text below:")
label_input.pack(pady=5)

text_input = scrolledtext.ScrolledText(app, wrap=tk.WORD, height=15)
text_input.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Process button
process_button = tk.Button(app, text="Format Text", command=process_text)
process_button.pack(pady=10)

# Output text area
label_output = tk.Label(app, text="Formatted text:")
label_output.pack(pady=5)

text_output = scrolledtext.ScrolledText(app, wrap=tk.WORD, height=15)
text_output.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Run the app
app.mainloop()

# Steps to package the app:
# 1. Install PyInstaller: pip install pyinstaller
# 2. Create a one-file executable: pyinstaller --onefile --windowed your_script_name.py
# 3. Locate the executable in the `dist` folder created by PyInstaller.
# 4. Move the executable to the desired location and test it on your MacBook Air.import tkinter as tk
# from tkinter import scrolledtext, messagebox, ttk
# import re
#
# # Function to format the text
# def format_text(input_text, double_space=False):
#     # Correct paragraph indentation
#     formatted_text = re.sub(r'\n\s*', '\n    ', input_text.strip())
#
#     # Correct spacing after periods
#     formatted_text = re.sub(r'\.(\S)', r'. \1', formatted_text)
#
#     # Capitalize the start of sentences (simplified)
#     formatted_text = re.sub(r'(?<=[\.\?\!]\s)(\w)', lambda x: x.group(1).upper(), formatted_text)
#
#     # Add double spacing if requested
#     if double_space:
#         formatted_text = re.sub(r'\n', r'\n\n', formatted_text)
#
#     return formatted_text
#
# # Function to process the text and display the formatted version
# def process_text():
#     try:
#         input_text = text_input.get("1.0", tk.END).strip()
#
#         if not input_text:
#             messagebox.showerror("Error", "Please paste some text into the box.")
#             return
#
#         if len(input_text.split()) > 100000:  # Roughly 500 pages
#             messagebox.showerror("Error", "The input text exceeds the maximum allowed length of 500 pages.")
#             return
#
#         # Check if double space is checked
#         double_space_enabled = double_space_var.get()
#         formatted_text = format_text(input_text, double_space=double_space_enabled)
#
#         text_output.delete("1.0", tk.END)
#         text_output.insert("1.0", formatted_text)
#     except Exception as e:
#         messagebox.showerror("Error", f"An error occurred: {e}")
#
#
# # GUI setup
# app = tk.Tk()
# app.title("Fiction Novel Formatter")
# app.geometry("800x650")
#
# # Input text area
# label_input = tk.Label(app, text="Paste your text below:")
# label_input.pack(pady=5)
#
# text_input = scrolledtext.ScrolledText(app, wrap=tk.WORD, height=15)
# text_input.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
#
# # Double space checkbox
# double_space_var = tk.BooleanVar()  # Use BooleanVar for checkbox state
# double_space_check = ttk.Checkbutton(app, text="Double Space", variable=double_space_var)
# double_space_check.pack(pady=5)
#
#
# # Process button
# process_button = tk.Button(app, text="Format Text", command=process_text)
# process_button.pack(pady=10)
#
# # Output text area
# label_output = tk.Label(app, text="Formatted text:")
# label_output.pack(pady=5)
#
# text_output = scrolledtext.ScrolledText(app, wrap=tk.WORD, height=15)
# text_output.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
#
# # Run the app
# app.mainloop()
#
# # Steps to package the app:
# # 1. Install PyInstaller: pip install pyinstaller
# # 2. Create a one-file executable: pyinstaller --onefile --windowed your_script_name.py
# # 3. Locate the executable in the `dist` folder created by PyInstaller.
# # 4. Move the executable to the desired location and test it on your MacBook Air.