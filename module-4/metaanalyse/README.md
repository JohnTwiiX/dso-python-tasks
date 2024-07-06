# PDF Metadata Extractor

## Overview

The **PDF Metadata Extractor** is a Python program designed to automate the extraction of metadata from PDF files. This program can process individual PDF files or entire directories containing multiple PDFs. The extracted metadata is saved to a CSV file, with fields clearly marked and empty fields denoted by `undefined`.

## Features

- **Extract Metadata**: Automatically extract metadata such as Title, Author, Creator, Created, Modified, Subject, Keywords, Description, Producer, and PDF Version from PDF files.
- **Flexible Input**: Process a single PDF file or multiple files in a directory.
- **CSV Output**: Save metadata to a CSV file with customizable filename and path.
- **Clear Metadata Handling**: Metadata fields that are not present or empty in the PDF file are marked as undefined.

## Requirements

- Python 3.x
- PyPDF2
- argparse
- csv
- os

## Installation

Install the required dependencies using pip:

```bash
pip install PyPDF2
```

## Usage

You can run the program by specifying either a single PDF file or a directory containing multiple PDF files. Use the following commands:

## For a Single PDF File

```bash
python3 pdf_metadata_extractor.py -f /path/to/file.pdf -n output.csv
```

## For a Directory of PDFs

```bash
python3 pdf_metadata_extractor.py -d /path/to/directory -n output.csv
```

## Arguments

- `-f` or `--file`: Path to a single PDF file.
- `-d` or `--directory`: Path to a directory containing multiple PDF files.
- `-n` or `--name`: Name and path of the output CSV file (required).

## Example

To extract metadata from a single PDF file:

```bash
python3 pdf_metadata_extractor.py -f /path/to/file.pdf -n metadata.csv
```

To extract metadata from all PDF files in a directory:

```bash
python3 pdf_metadata_extractor.py -d /path/to/directory -n metadata.csv
```

## Code Explanation

`extract_pdf_metadata(file_path)`

This function extracts metadata from a given PDF file and returns a dictionary with the metadata. If a metadata field is missing, it sets the value to `undefined`.

- `Parameters`:
  - `file_path` (str): Path to the PDF file.
- Returns:
  - `metadata` (dict): Dictionary containing the extracted metadata.

`process_single_file(file_path, csv_path)
`
This function processes a single PDF file, extracts its metadata, and writes it to a CSV file.

- `Parameters`:
  - `file_path` (str): Path to the PDF file.
  - `csv_path` (str): Path to the output CSV file.

`process_directory(directory_path, csv_path)`

This function processes multiple PDF files in a given directory, extracts their metadata, and writes it to a CSV file.

- `Parameters`:
  - `directory_path` (str): Path to the directory containing PDF files.
  - `csv_path` (str): Path to the output CSV file.

## Notes

- Ensure you have the necessary permissions to read the PDF files and write to the specified output directory.
- This script assumes that all PDF files have a `.pdf` extension and are properly formatted.
- If you encounter any issues, ensure you have installed all dependencies and check the error messages for further details.
