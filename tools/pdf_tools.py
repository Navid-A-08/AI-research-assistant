from crewai.tools import tool
import fitz  # PyMuPDF


@tool("PDF Reader")
def read_pdf(file_path: str) -> str:
    """Extracts raw text from a PDF file given its file path."""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text
