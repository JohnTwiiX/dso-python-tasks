import os
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from PyPDF2 import PdfReader
import argparse

def extract_pdf_links_from_website(url: str):
    """extract pdf links from website

    Args:
        url (str): url of website

    Returns:
        pdf_links (List[str]): List of pdf links
    """
    response = response = get_response(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True) if link.get('href').endswith('.pdf')]
    return pdf_links

def download_pdf(url:str, save_path:str):
    """download pdf files

    Args:
        url (str): url of pdf file
        save_path (str): location to storage pdf
    """
    response = get_response(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f'Downloaded: {save_path}')
    
def get_response(url:str):
    # this call handles HTTP errors that arise when an unsuccessful HTTP response code is returned from the previous call, e.g. 400, 401, 500, etc.
    return requests.get(url).raise_for_status()

def extract_pdf_metadata(file_path:str):
    """extract pdf metadata

    Args:
        file_path (str): path to pdf file

    Returns:
        metadata (obj): object with metadata of the pdf
    """
    metadata = {
        'Title': '',
        'Author': '',
        'Creator': '',
        'Created': '',
        'Modified': '',
        'Subject': '',
        'Keywords': '',
        'Description': '',
        'Producer': '',
        'PDF Version': ''
    }
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            info = reader.metadata

            metadata['Title'] = info.get('/Title', '')
            metadata['Author'] = info.get('/Author', '')
            metadata['Creator'] = info.get('/Creator', '')
            metadata['Created'] = info.get('/CreationDate', '')
            metadata['Modified'] = info.get('/ModDate', '')
            metadata['Subject'] = info.get('/Subject', '')
            metadata['Keywords'] = info.get('/Keywords', '')
            metadata['Description'] = info.get('/Description', '')
            metadata['Producer'] = info.get('/Producer', '')
            
            metadata['PDF Version'] = reader.trailer.get('/Version', 'Unknown')
    except Exception as e:
        print(f'Error extracting metadata from {file_path}: {e}')
    return metadata

def main():
    parser = argparse.ArgumentParser(description="Download PDF files from a website and extract metadata.")
    parser.add_argument('-u', '--url', required=True, help='URL of the website to scan for PDF files.')
    parser.add_argument('-n', '--name', required=True, help='Name and path of the output CSV file.')
    
    args = parser.parse_args()
    url = args.url
    csv_path = args.name
    
    pdf_links = extract_pdf_links_from_website(url)
    if not pdf_links:
        print('No PDF files found.')
        return
    
    os.makedirs('pdfs', exist_ok=True)
    metadata_list = []
    
    for pdf_url in pdf_links:
        pdf_name = urlparse(pdf_url).path.split('/')[-1]
        pdf_path = os.path.join('pdfs', pdf_name)
        download_pdf(pdf_url, pdf_path)
        metadata = extract_pdf_metadata(pdf_path)
        metadata['File Name'] = pdf_name
        metadata_list.append(metadata)
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['File Name', 'Title', 'Author', 'Creator', 'Created', 'Modified', 'Subject', 'Keywords', 'Description', 'Producer', 'PDF Version']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for data in metadata_list:
            writer.writerow(data)
    
    print(f'Metadata saved to {csv_path}')

if __name__ == "__main__":
    main()
