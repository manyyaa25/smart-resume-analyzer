from PyPDF2 import PdfReader

def extract_text(uploaded_file):

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text

    return text