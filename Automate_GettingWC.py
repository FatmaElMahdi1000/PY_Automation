from pathlib import Path
import PyPDF2
import docx
import pandas as pd

# Ask the user for file paths (separated by commas)
file_input = input("Enter full path(s) to file(s), separated by commas: ").strip()
file_paths = [Path(path.strip().strip('"')) for path in file_input.split(',')]

total_wc = 0  # Initialize total word count

# Loop through each file
for file_path in file_paths:
    if not file_path.exists():
        print(f"File not found: {file_path}")
        continue

    print(f"\nProcessing: {file_path.name}")

    if file_path.suffix.lower() == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            wc = len(content.split())
            print(f"Word count: {wc}")
            total_wc += wc

    elif file_path.suffix.lower() == ".pdf":
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            total_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    total_text += text + " "
            wc = len(total_text.split())
            print(f"Word count: {wc}")
            total_wc += wc

    elif file_path.suffix.lower() in [".docx", ".doc"]:
        doc = docx.Document(file_path)
        total_text = ""
        for paragraph in doc.paragraphs:
            total_text += paragraph.text + " "
        wc = len(total_text.split())
        print(f"Word count: {wc}")
        total_wc += wc

    elif file_path.suffix.lower() in [".xlsx", ".csv"]:
        try:
            if file_path.suffix.lower() == ".xlsx":
                excel_file = pd.read_excel(file_path, sheet_name=None)
            else:
                df = pd.read_csv(file_path)
                excel_file = {"Sheet1": df}

            total_text = ""
            for _, df in excel_file.items():
                for row in df.values:
                    for cell in row:
                        total_text += str(cell) + " "
            wc = len(total_text.split())
            print(f"Word count: {wc}")
            total_wc += wc

        except Exception as e:
            print(f"Error reading spreadsheet file: {e}")

    else:
        print(f"Unsupported file type: {file_path.suffix}")

print(f"\nTotal word count across all files: {total_wc}")
