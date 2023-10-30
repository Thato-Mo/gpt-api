import pdfplumber
import sys

def pdf_to_text(pdf_path):

    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    
    print(text, f"type{text}")
    return text

def main(arg):
    pdf_to_text(arg)


if __name__ == "__main__":
    main(sys.argv[1])