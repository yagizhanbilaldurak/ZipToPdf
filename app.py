import tkinter as tk
from conversions import PDFConversionTool
from gui import interface
import sys
import io

def run_program(input_dir, output_dir, pdf_dir, message_text, progress_var):
    """
    Runs the program to extract, convert, and rename files based on user input.

    Parameters:
       - input_dir (str): The input directory path.
       - output_dir (str): The output directory path.
       - pdf_dir (str): The PDF directory path.
       - message_text (CustomText): Text widget to display messages.
       - progress_var (tkinter.Variable): Tkinter variable linked to the progress bar.
    """
    input_directory = input_dir.get()
    output_directory = output_dir.get()
    pdf_directory = pdf_dir.get()

    message_text.delete('1.0', tk.END)

    captured_output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output

    try:
        conversion_tool = PDFConversionTool(input_directory, output_directory, pdf_directory)

        conversion_tool.run_conversion(progress_var)

        print("PDF Conversion Completed!")
    except Exception as e:
        print(f"Error: {str(e)}")

    sys.stdout = original_stdout  # Restore original stdout

    message_text.insert(tk.END, captured_output.getvalue())

def main():
    interface(run_program)

if __name__ == "__main__":
    main()
