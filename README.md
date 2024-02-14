# ZipToPdf

## Overview
ZipToPdf is a Python program designed to convert HTML format invoice documents downloaded as zip files from the "E-Arşiv Portal" website into PDF files. Additionally, it matches the names of the converted files to the customer names in the invoice files.

## Purpose
The purpose of this application is to streamline the process of uploading invoices by quickly converting them into a more accessible format (PDF) and aligning their filenames with customer names for easier management.

## Target Users
This application is intended for individuals and businesses, particularly those involved in e-commerce sales on platforms such as Trendyol and Hepsiburada, who seek to expedite the process of invoice uploading. Additionally, it is suitable for anyone who requires efficient invoice conversion and file management.

## Use Cases
E-Invoice Conversion: Easily convert invoice documents downloaded from the E-Arşiv Portal in HTML format to PDF.
File Naming: Automatically synchronize filenames with customer names extracted from the invoice files for better organization.
File Merging: Merge multiple PDF files into a single document for convenience and efficient record-keeping.

## Installation
1. If you have not installed Python yet, install it from [here](https://python.org).

2. This application uses Wkhtmltopdf for conversions. You have to install it from [wkhtmltopdf](https://wkhtmltopdf.org/).

3. Clone this repository.

4. Specify to path for wkhtmltopdf.exe on conversions.py.
   ![image](https://github.com/yagizhanbilaldurak/ZipToPdf/assets/115084674/be57f7e0-9515-45cd-9b31-ffce9139fef1)

## Usage
1. Make sure you completed all installation steps.
2. Navigate into project directory.
```bash
cd ZipToPdf
```
3. Create a new virtual environment.
- Windows:
```bash
> python -m venv venv
> .\venv\Scripts\activate
```
- MacOS:
```bash
$ python -m venv venv
$ . venv/bin/activate
```
- Linux:
```bash
> python3 -m venv myenv
> source myenv/bin/activate
```

4. Install the requirements.
```bash
pip install -r requirements.txt
```
5. Run the program.
```bash
python app.py
```
6. Run the program.
```bash
python app.py
```

## License
This project is licensed under the [MIT License](https://github.com/yagizhanbilaldurak/ZipToPdf?tab=MIT-1-ov-file#readme).

## Contributions
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests through GitHub.

## Disclaimer
This program is provided as-is without any warranties. Users are responsible for ensuring the accuracy and legality of converted documents.

For detailed instructions and additional information, please refer to my [website](https://yagizhanbilaldurak.com).
