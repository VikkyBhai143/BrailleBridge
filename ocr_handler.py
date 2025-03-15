import pytesseract
from PIL import Image
import PyPDF2
import logging

logger = logging.getLogger(__name__)

def process_image(image_path):
    """
    Extract text from image using Tesseract OCR
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        raise Exception("Failed to process image")

def process_pdf(pdf_path):
    """
    Extract text from PDF file
    """
    try:
        text = []
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text.append(page.extract_text())
        return ' '.join(text).strip()
    except Exception as e:
        logger.error(f"Error processing PDF: {str(e)}")
        raise Exception("Failed to process PDF")
