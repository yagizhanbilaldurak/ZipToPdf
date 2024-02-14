import tkinter as tk
from tkinter import ttk, filedialog

def browse_folder(entry):
    """
    Opens a dialog to browse and select a folder. Updates the specified Entry widget with the selected folder path.

    Parameters:
        - entry (tkinter.Entry): The tkinter Entry widget to display the selected folder path.
    """
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)

def interface(run_program):
    """
    Creates the graphical user interface (GUI) for the PDF Conversion Tool.

    Description:
        This function initializes a tkinter GUI with Entry widgets for user input (directory paths),
        Browse buttons to select directories, and a Progressbar to display the progress of the program.
    """
    root = tk.Tk()
    root.title("PDF Conversion Tool")

    tk.Label(root, text="Zip File Directory : ").grid(row=0, column=0, padx=10, pady=5)
    input_entry = tk.Entry(root, width=50)
    input_entry.grid(row=0, column=1, padx=10, pady=5)
    input_button = tk.Button(root, text="Browse", command=lambda: browse_folder(input_entry))
    input_button.grid(row=0, column=2, padx=10, pady=5)

    tk.Label(root, text="Output Directory:").grid(row=1, column=0, padx=10, pady=5)
    output_entry = tk.Entry(root, width=50)
    output_entry.grid(row=1, column=1, padx=10, pady=5)
    output_button = tk.Button(root, text="Browse", command=lambda: browse_folder(output_entry))
    output_button.grid(row=1, column=2, padx=10, pady=5)

    tk.Label(root, text="PDF Directory:").grid(row=2, column=0, padx=10, pady=5)
    pdf_entry = tk.Entry(root, width=50)
    pdf_entry.grid(row=2, column=1, padx=10, pady=5)
    pdf_button = tk.Button(root, text="Browse", command=lambda: browse_folder(pdf_entry))
    pdf_button.grid(row=2, column=2, padx=10, pady=5)

    progress_var = tk.IntVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progress_bar.grid(row=3, column=1, pady=10)

    # Text widget for displaying messages
    message_text = tk.Text(root, height=10, width=80)
    message_text.grid(row=4, column=1, padx=10, pady=5, columnspan=2)

    run_button = tk.Button(root, text="Run Program",
                           command=lambda: run_program(input_entry, output_entry, pdf_entry, message_text, progress_var))
    run_button.grid(row=5, column=1, pady=10)

    root.mainloop()

