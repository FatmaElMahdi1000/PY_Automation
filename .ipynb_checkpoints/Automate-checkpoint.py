from sys import exit, argv
from pathlib import Path
import PyPDF2 #for PDF files 
import docx #for word-document 
import pandas as pd #for excel sheets 


FileName = input("Where are your file:  ").strip()  #path must be provided like this: Where are your file:  C:\Users\USER\Auto_files for testing\File1.txt, strip()for removing any leading or trailing spaces

file_path = Path(FileName) #converting the string i provided , as a file path using Path method

if not file_path.exists():
    print("No File/Files are found!")
    exit(1)

if file_path.suffix == ".pdf": #I am checking if the file we're reading is not PdF #PDFs
    with open (file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            print(page.extract_text())
    
elif file_path.suffix == ".txt":   #txt files 
    with open (file_path, "r", encoding="utf-8") as file:
        Content = file.read()
        print(Content)
        
elif (file_path.suffix == ".docx") or (file_path.suffix == ".doc"):  #word documents
    doc = docx.Document(file_path)
    for paragraph in doc.paragraphs:
        print(paragraph.text)

elif file_path.suffix == ".xlsx":                        #xlsx files / excels
    try:
        excel_file = pd.read_excel(file_path, sheet_name=None)  # Read all sheets
        for sheet_name, df in excel_file.items():  #keys: sheets, values: df (data frames like tables with data in a single sheet)
            print(f"\n --- sheetName: {sheet_name}---")
            print(df.to_string(index=False))  #needs more explanations 
            
    except Exception as e:
        print(f"Error reading spreadsheet file: {e}")
        
elif file_path.suffix == ".csv":
    try:
        df = pd.read_csv(file_path)  # Read the CSV into a DataFrame
        print(df.to_string(index=False))  # Print table without row indices
    except Exception as e:
        print(f"Error reading CSV file: {e}")
else:
    print("Unsupported file type.")









    
    

