# PDF Metadata Extractor

This Python script downloads PDF files from a specified website and extracts metadata such as title, author, creation date, etc., saving them into a CSV file.

- **Web Scraping**: Extracts all PDF links from a given website using `BeautifulSoup` and `requests` modules.
- **PDF Download**: Downloads each PDF file found to a local directory (`pdfs/`).
- **Metadata Extraction**: Uses the `PyPDF2` library to extract metadata (title, author, creation date, etc.) from each downloaded PDF file.
- **CSV Export**: Saves extracted metadata into a CSV file with semicolon (`;`) as a delimiter for better readability.

## Function Descriptions

Ensure the website allows scraping of PDF links and complies with legal and ethical guidelines.
The script may encounter issues with PDF files that have restricted access or malformed metadata.
Customize the script further based on specific PDF metadata extraction needs or website structures.

### `extract_pdf_links(url)`

This function takes a URL as an input and extracts all PDF links from the webpage. It uses the `requests` module to fetch the page content and `BeautifulSoup` to parse the HTML.

- **Parameters**:
  - `url` (str): The URL of the webpage to scan for PDF files.
- **Returns**:
  - `pdf_links` (list): A list of URLs to PDF files found on the webpage.

### `download_pdf(url, save_path)`

This function downloads a PDF file from the provided URL and saves it to the specified path.

- **Parameters**:
  - `url` (str): The URL of the PDF file to download.
  - `save_path` (str): The local file path to save the downloaded PDF.
- **Outputs**:
  - The function prints a confirmation message indicating the download is complete.

### `extract_pdf_metadata(file_path)`

This function extracts metadata from a PDF file. It reads the PDF file using `PyPDF2` and retrieves various metadata attributes.

- **Parameters**:
  - `file_path` (str): The local file path of the PDF file to extract metadata from.
- **Returns**:
  - `metadata` (dict): A dictionary containing metadata fields such as title, author, creation date, etc.

### `main()`

This is the main function that orchestrates the entire process. It parses command-line arguments, extracts PDF links from the given URL, downloads each PDF, extracts metadata, and saves the results into a CSV file.

- **Command-Line Arguments**:
  - `-u` / `--url` (str): The URL of the website to scan for PDF files.
  - `-n` / `--name` (str): The name and path of the output CSV file.
- **Outputs**:
  - The function prints messages to indicate progress, such as downloaded files and saved metadata.

## Usage

1. **Setup Environment**:
    - Ensure Python 3.12.3 and necessary libraries (`requests 2.31`, `beautifulsoup4 4.12`, `PyPDF2 2.12`) are installed.
    - see [requirements.txt](./requirements.txt)

    ```python
    pip install -r requirements.txt
    ```

2. **Run the Script**:

    ```bash
    python3 metascan.py -u <website_url> -n <output_csv_filename>
    ```

    - Replace `<website_url>` with the URL of the website containing PDF files.
    - Replace `<output_csv_filename>` with the desired name and path for the output CSV file.

3. **Output**:
    - The script will create a directory `pdfs/` to store downloaded PDF files.
    - It will generate a CSV file containing metadata for each PDF file found, with each metadata attribute displayed on a new line for readability.

## Example

Suppose you want to extract PDF metadata from `https://example.com` and save it to `example_metadata.csv`:

```bash
python3 metascan.py -u https://example.com -n example_metadata.csv
```

## Dependencies

- `requests`: For making HTTP requests to fetch web pages.
- `beautifulsoup4`: For parsing HTML and extracting data from web pages.
- `PyPDF2`: For extracting metadata from PDF files.
