import os
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from PyPDF2 import PdfReader
import argparse

def extract_pdf_links(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True) if link.get('href').endswith('.pdf')]
    return pdf_links

def download_pdf(url, save_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f'Downloaded: {save_path}')

def extract_pdf_metadata(file_path):
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
    
    pdf_links = extract_pdf_links(url)
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
