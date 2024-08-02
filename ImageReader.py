import os
from google.cloud import vision


def perform_ocr(image_path, output_text_file):
    # Set up Google Cloud Vision client
    client = vision.ImageAnnotatorClient()

    # Read the image file
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    
    # Perform text detection on the image file
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    # Extract the raw text
    raw_text = texts[0].description if texts else ""

    # Write the raw text to the output file
    with open(output_text_file, 'w') as output_file:
        output_file.write(raw_text)
    
    print(f"Text extracted and written to {output_text_file}")

# Example usage
perform_ocr('TestImage.png', 'ImageTextOutput.txt')