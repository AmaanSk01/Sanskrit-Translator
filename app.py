from flask import Flask, render_template, request, jsonify, send_file
import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from docx import Document
from googletrans import Translator
from indic_transliteration.sanscript import transliterate, DEVANAGARI, IAST

app = Flask(__name__)

# Set Tesseract Path (Only for Windows)
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    POPPLER_PATH = r"C:\Users\amaan\Downloads\Release-24.08.0-0.zip"

# Function to extract text from images
def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang="san")  # Sanskrit OCR
        return text.strip()
    except Exception as e:
        return f"Error extracting text from image: {str(e)}"

# Function to extract text from PDFs
def extract_text_from_pdf(pdf_path):
    try:
        images = convert_from_path(pdf_path)
        extracted_text = ""
        for img in images:
            extracted_text += pytesseract.image_to_string(img, lang="san") + "\n"
        return extracted_text.strip()
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"

# Function to extract text from DOCX files
def extract_text_from_docx(docx_path):
    try:
        doc = Document(docx_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error extracting text from DOCX: {str(e)}"
    
    # Function to translate text
def translate_text(text, dest_language):
    translator = Translator()
    
    if dest_language == "sa":
        # Convert to Sanskrit using transliteration
        return transliterate(text, IAST, DEVANAGARI)  # Converts Latin script to Sanskrit Devanagari
    
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        return f"Translation error: {str(e)}"

# Store translated text globally
translated_text = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    global translated_text
    translated_text = ""  # Reset translation

    if 'file' in request.files and request.files['file'].filename:
        file = request.files['file']
        file_ext = file.filename.split('.')[-1].lower()
        file_path = f"uploads/{file.filename}"
        
        # Save the uploaded file
        os.makedirs("uploads", exist_ok=True)
        file.save(file_path)

        # Extract text based on file type
        if file_ext in ["jpg", "jpeg", "png", "webp"]:
            extracted_text = extract_text_from_image(file_path)
        elif file_ext == "pdf":
            extracted_text = extract_text_from_pdf(file_path)
        elif file_ext == "docx":
            extracted_text = extract_text_from_docx(file_path)
        else:
            return jsonify({"error": "Unsupported file format"}), 400

        os.remove(file_path)  # Cleanup uploaded file
    else:
        extracted_text = request.form.get("text", "").strip()

    if not extracted_text:
        return jsonify({"error": "No text found"}), 400

    target_language = request.form.get("language", "en")
    translated_text = translate_text(extracted_text, target_language)

    return jsonify({"text": translated_text})

@app.route('/download')
def download_translation():
    global translated_text
    if not translated_text:
        return "No translation available", 400  # Handle empty translation case

    file_path = "translated_text.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(translated_text)

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)