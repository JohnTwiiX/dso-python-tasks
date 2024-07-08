# PDF Metadata Removal Tool

This Python script allows you to remove metadata from PDF documents using either ExifTool or QPDF. It's a command-line tool that can process a single PDF file and save the result with all metadata stripped out.

## Requirements

Ensure you have the following tools installed on your system:

- **ExifTool**: A command-line application for reading, writing, and editing metadata. You can install it using:

  ```bash
  sudo apt-get install exiftool
  ```

- `QPDF`: A command-line tool for PDF transformation and inspection. Install it with:

  ```bash
  sudo apt-get install qpdf
  ```

## How to Use

### Basic Usage

1. Save the script in a file, for example, `remove_metadata.py`.
2. Run the script via the command line with the appropriate arguments:

- **Using ExifTool**:

```bash
python3 remove_metadata.py -i test.pdf -o output.pdf -t exiftool
```

- **Using QPDF**:

```bash
python3 remove_metadata.py -i test.pdf -o output.pdf -t qpdf
```

Replace `test.pdf` with the path to your input PDF file and `output.pdf` with the desired path for the output PDF file.

### Command-line Options

- `-i` or `--input`: Specifies the path to the test PDF file.
- `-o` or `--output`: Specifies the path to the output PDF file.
- `-t` or `--tool`: Specifies the tool to remove metadata, either `exiftool` or `qpdf`. The default is `exiftool`.

## Functions Explained

### `remove_metadata_exiftool(input_file, output_file)`

This function removes metadata from a PDF file using ExifTool.

- `Parameters`:

  - `input_file`: The path to the input PDF file.
  - `output_file`: The path to the output PDF file where the cleaned file will be saved.

- **How it Works**:

  - Constructs a command to run ExifTool with options to remove all metadata and save the result to the specified output file.
  - Executes the command using `subprocess.run`.
  - Handles errors if the command fails.

### `remove_metadata_qpdf(input_file, output_file)`

This function removes metadata from a PDF file using QPDF.

- `Parameters`:
  - `input_file`: The path to the input PDF file.
  - `output_file`: The path to the output PDF file where the cleaned file will be saved.

- **How it Works**:
  - Constructs a command to run QPDF with options to remove metadata and save the result to the specified output file.
  - Executes the command using `subprocess.run`.
  - Handles errors if the command fails.
