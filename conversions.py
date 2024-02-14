import os
import zipfile
import pdfkit
from bs4 import BeautifulSoup

def update_progress(progress_var, value, max_value):
    """
    Updates the progress bar variable based on the current progress.

    Parameters:
        - progress_var (tkinter.Variable): Tkinter variable linked to the progress bar.
        - value (int): Current progress value.
        - max_value (int): Total number representing the maximum progress value.
    """
    progress_percentage = int((value / max_value) * 100)
    progress_var.set(progress_percentage)

class ZipExtractor:
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory

    def extract_zipFiles(self):
        """
        Extracts ONLY .html files from .zip files from given input_directory and saves them to the output+directory.
        Removes successfully processed .zip files from the input_directory.

        Raises:
            - FileNotFoundError: If the specified .zip file is not found in the input_directory.
            - zipfile.BadZipFile: If the .zip file is not a valid zip file.
            - PermissionError: If the function lacks the necessary permissions to extract or delete a file.
            - OSError: If an unexpected error occurs during the extraction process.
        """
        files = os.listdir(self.input_directory)
        total_files = len(files)
        successfully_processed_zips = []

        for index, zip_file in enumerate(files):
            try:
                with zipfile.ZipFile(os.path.join(self.input_directory, zip_file), 'r') as zip_ref:
                    file_list = zip_ref.namelist()
                    html_files = [file for file in file_list if file.endswith('.html')]

                    for html_file in html_files:
                        zip_ref.extract(html_file, self.output_directory)

                    successfully_processed_zips.append(zip_file)
            except Exception as e:
                print(f"error processing {zip_file} : {e}")

        ZipExtractor.remove_zip_files(successfully_processed_zips, self.input_directory)

        print("Extraction Complete!")

    @staticmethod
    def remove_zip_files(processed_zips, input_directory):
        """
        Removes the successfully processed .zip files from the specified input_directory.

        Parameters:
            - processed_zips (list): List of .zip files that have been successfully processed
            - input_directory (str): The directory containing the processed .zip files.
        Raises:
            - FileNotFoundError: If the specified .zip file is not found in the input_directory.
            - PermissionError: If the function lacks the necessary permissions to delete a file.
            - OSError: If an unexpected error occurs during the deletion process.
        """
        for zip_file in processed_zips:
            try:
                os.remove(os.path.join(input_directory, zip_file))
            except Exception as e:
                print(f'error deleting {zip_file} : {e}')

class HtmlToPdfConverter:
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory

    def convert_to_pdf(self, progress_var):
        """
        Converts .html files to .pdf files from input_directory and saves them into output_directory.

        Parameters:
             - progress_var (tkinter.Variable): Tkinter variable linked to the progress bar.

        Raises:
            - FileNotFoundError: If the specified .html file is not found in the input_directory.
            - pdfkit.ConfigurationError: If there is an issue with the configuration of pdfkit.
            - pdfkit.BlockingIOError: If there is an issue with file I/O operations during conversion.
            - OSError: If an unexpected error occurs during the conversion process.

        Note:
            - The pdfkit module must be installed and properly configured.
            - This function uses the wkhtmltopdf.exe for conversion. Make sure it is installed and
            its location properly specified in config.
        """
        config = pdfkit.configuration(wkhtmltopdf=r'path/to/wkhtmltopdf')
        files = os.listdir(self.input_directory)
        total_files = len(files)

        for index, html_file in enumerate(files):
            input_path = os.path.join(self.input_directory, html_file)
            output_path = os.path.join(self.output_directory, os.path.splitext(html_file)[0] + '.pdf')

            try:
                pdfkit.from_file(input_path, output_path, configuration=config)
                print(f'converted {html_file} to PDF')
                update_progress(progress_var, index + 1, total_files)

            except Exception as e:
                print(f'error converting {html_file} to PDF: {e}')
                update_progress(progress_var, index + 1, total_files)


class PdfRenamer:
    def __init__(self, pdf_directory, output_directory):
        self.pdf_directory = pdf_directory
        self.output_directory = output_directory

    def rename_PDF(self):
        """
        Renames .pdf files with using real customer names extracted from the corresponding .html files.

        Raises:
            - FileNotFoundError: If the specified .html file is not found in the output_dir.
            - PermissionError: If the function lacks the necessary permissions to rename or delete a file.
            - OSError: If an unexpected error occurs during the renaming process.
        """
        pdf_files = [file for file in os.listdir(self.pdf_directory) if file.endswith('.pdf')]

        for pdf_file in pdf_files:
            html_path = os.path.join(self.output_directory, os.path.splitext(pdf_file)[0] + '.html')

            try:
                name_surname = self.get_name_surname_withID(html_path)
                new_file_name = self.get_name_surname(name_surname) + '.pdf'
                new_PDF_path = os.path.join(self.pdf_directory, new_file_name)

                if os.path.exists(new_PDF_path):
                    os.remove(new_PDF_path)

                os.rename(os.path.join(self.pdf_directory, pdf_file), new_PDF_path)
                print(f'Renamed {pdf_file} to {new_file_name}')

            except Exception as e:
                print(f'error renaming {pdf_file}: {e}')

    def get_name_surname_withID(self, html_file_path):
        """
        Extracts information (name, surname, address etc.) from the specified table of html files.

        Parameters:
            - html_file_path (str): The path to html files.

        Returns:
            str: The extracted information from customerPartyTable.

        Note:
            - The HTML file should contain a table with the id 'customerPartyTable'.
            - The function assumes that the name is located in the first column of the table.
        """
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        target_table = soup.find('table', {'id': 'customerPartyTable'})

        if target_table:
            rows = target_table.find_all('tr')

            for row in rows:
                cells = row.find_all('td')

                if len(cells) >= 2:
                    name = cells[0].text.strip()

        return name

    def get_name_surname(self, data):
        """
        Extracts name and surname information from the given data set.

        Parameters:
            - data (str): A data set which includes name and surname information.

        Returns:
            str: Concatenation of the first and second elements of the dataset.

        Note:
            - The function assumes that the name and surname are the first two elements in the dataset.
            - It is designed to work correctly if the customer has one name and one surname.
              For example, for a customer named Jack Sparrow, the return will be "Jack Sparrow".
              However, for a customer named Captain Jack Sparrow, the return will be "Captain Jack".
            - The function assumes the length of a customer name never exceeds 60 characters.
        """
        lst = data[5:60].split()
        return lst[0] + " " + lst[1]

class PDFConversionTool:
    def __init__(self, input_directory, output_directory, pdf_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory
        self.pdf_directory = pdf_directory

    def run_conversion(self, progress_var):
        """
        Starts the conversion operations.

        Parameters:
            - progress_var (tkinter.Variable): Tkinter variable linked to the progress bar.
        """
        extractor = ZipExtractor(self.input_directory, self.output_directory)
        extractor.extract_zipFiles()

        converter = HtmlToPdfConverter(self.output_directory, self.pdf_directory)
        converter.convert_to_pdf(progress_var)

        renamer = PdfRenamer(self.pdf_directory, self.output_directory)
        renamer.rename_PDF()

