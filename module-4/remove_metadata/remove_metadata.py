import os
import subprocess
import argparse

def remove_metadata_exiftool(input_file, output_file):
    """
    Removes metadata using ExifTool.
    """
    try:
        command = f'exiftool -all= -o {output_file} {input_file}'
        subprocess.run(command, shell=True, check=True)
        print(f"Metadata successfully removed using ExifTool. Output: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error removing metadata with ExifTool: {e}")

def remove_metadata_qpdf(input_file, output_file):
    """
    Removes metadata using QPDF.
    """
    try:
        command = f'qpdf --linearize --object-streams=disable --replace-input {input_file} {output_file}'
        subprocess.run(command, shell=True, check=True)
        print(f"Metadata successfully removed using QPDF. Output: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error removing metadata with QPDF: {e}")

def main():
    parser = argparse.ArgumentParser(description="Remove metadata from a PDF document.")
    parser.add_argument('-i', '--input', required=True, help='Path to the input PDF file.')
    parser.add_argument('-o', '--output', required=True, help='Path to the output PDF file.')
    parser.add_argument('-t', '--tool', choices=['exiftool', 'qpdf'], default='exiftool',
                        help='Tool to remove metadata: "exiftool" or "qpdf" (default: "exiftool").')

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output
    tool = args.tool

    if tool == 'exiftool':
        remove_metadata_exiftool(input_file, output_file)
    elif tool == 'qpdf':
        remove_metadata_qpdf(input_file, output_file)

if __name__ == "__main__":
    main()
