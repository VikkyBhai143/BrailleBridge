import os
import logging
from flask import Flask, render_template, request, flash, jsonify
from werkzeug.utils import secure_filename
from braille_converter import text_to_braille
from ocr_handler import process_image, process_pdf

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

# File upload configuration
UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                file_ext = filename.rsplit('.', 1)[1].lower()
                if file_ext == 'pdf':
                    text = process_pdf(filepath)
                elif file_ext in ['png', 'jpg', 'jpeg']:
                    text = process_image(filepath)
                else:
                    text = file.read().decode('utf-8')
                
                os.remove(filepath)  # Clean up
                braille = text_to_braille(text)
                return jsonify({'success': True, 'braille': braille, 'text': text})
        
        elif 'text' in request.form:
            text = request.form['text']
            braille = text_to_braille(text)
            return jsonify({'success': True, 'braille': braille, 'text': text})
        
        else:
            return jsonify({'success': False, 'error': 'No input provided'}), 400
            
    except Exception as e:
        logger.error(f"Error during conversion: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.errorhandler(413)
def too_large(e):
    return jsonify({'success': False, 'error': 'File is too large'}), 413

@app.errorhandler(500)
def server_error(e):
    return render_template('error.html', error=str(e)), 500
