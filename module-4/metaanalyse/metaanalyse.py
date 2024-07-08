import os
import csv
import argparse
from PyPDF2 import PdfReader

def extract_pdf_metadata(file_path):
    metadata = {
        'File Name': os.path.basename(file_path),
        'Title': 'undefined',
        'Author': 'undefined',
        'Creator': 'undefined',
        'Created': 'undefined',
        'Modified': 'undefined',
        'Subject': 'undefined',
        'Keywords': 'undefined',
        'Description': 'undefined',
        'Producer': 'undefined',
        'PDF Version': 'undefined'
    }
    try:
        reader = PdfReader(file_path)
        info = reader.metadata

        metadata['Title'] = info.get('/Title', 'undefined')
        metadata['Author'] = info.get('/Author', 'undefined')
        metadata['Creator'] = info.get('/Creator', 'undefined')
        metadata['Created'] = info.get('/CreationDate', 'undefined')
        metadata['Modified'] = info.get('/ModDate', 'undefined')
        metadata['Subject'] = info.get('/Subject', 'undefined')
        metadata['Keywords'] = info.get('/Keywords', 'undefined')
        metadata['Description'] = info.get('/Description', 'undefined')
        metadata['Producer'] = info.get('/Producer', 'undefined')
        
        metadata['PDF Version'] = reader.trailer.get('/Version', 'undefined')
    except Exception as e:
        print(f'Error extracting metadata from {file_path}: {e}')
    return metadata

def process_single_file(file_path, csv_path):
    metadata = extract_pdf_metadata(file_path)
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['File Name', 'Title', 'Author', 'Creator', 'Created', 'Modified', 'Subject', 'Keywords', 'Description', 'Producer', 'PDF Version']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerow(metadata)
    print(f'Metadata saved to {csv_path}')

def process_directory(directory_path, csv_path):
    metadata_list = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                file_path = os.path.join(root, file)
                metadata = extract_pdf_metadata(file_path)
                metadata_list.append(metadata)

    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['File Name', 'Title', 'Author', 'Creator', 'Created', 'Modified', 'Subject', 'Keywords', 'Description', 'Producer', 'PDF Version']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for metadata in metadata_list:
            writer.writerow(metadata)
    print(f'Metadata saved to {csv_path}')

def main():
    parser = argparse.ArgumentParser(description="Extract metadata from PDF files and save to a CSV file.")
    parser.add_argument('-f', '--file', help='Path to a single PDF file.')
    parser.add_argument('-d', '--directory', help='Path to a directory containing multiple PDF files.')
    parser.add_argument('-n', '--name', required=True, help='Name and path of the output CSV file.')

    args = parser.parse_args()

    if not args.file or not args.directory:
        raise Exception("You need to specify either -f or -d option")
    if args.file:
        process_single_file(args.file, args.name)
    elif args.directory:
        process_directory(args.directory, args.name)
    

if __name__ == "__main__":
    main()
