import os
import io
from pdf2image import convert_from_path
from google.cloud import vision

# Set your variables here
pdf_file_path = 'testPDF.pdf'

# Initialize Google Vision client
client = vision.ImageAnnotatorClient()

# Convert PDF to images (one image per page)
images = convert_from_path(pdf_file_path)

extracted_text = ""

for i, image in enumerate(images):

    # Convert image to bytes
    buf = io.BytesIO()
    image.save(buf, format='JPEG')
    byte_im = buf.getvalue()

    # Perform OCR
    image = vision.Image(content=byte_im)
    response = client.document_text_detection(image=image, image_context={"language_hints": ['en']})
    
    # Append extracted text for each page
    extracted_text += response.full_text_annotation.text + "\n"

# Save the full extracted text to the output file 
with open("PdfTextOutput.txt", 'w') as text_file:
    text_file.write(extracted_text)

print('OCR complete for all pages in the PDF file')
