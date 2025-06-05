(BrailleBridge)
👨‍💻 Hi everyone! Let me walk you through my Day 19 project from the "30 Days, 30 Projects" challenge — BrailleBridge, an AI-powered Digital Braille Converter designed for visually impaired users.

📁 Folder Structure
pgsql
Copy
Edit
BrailleBridge/
├── app.py               👈 Main Flask backend file (app logic & routing)
├── main.py              👈 Entry point (used by Replit or external servers)
├── ocr_handler.py       👈 Handles OCR (text from image/PDF)
├── static/              👈 CSS, JS, images (frontend assets)
├── templates/           👈 HTML files (Flask uses Jinja2)
├── pyproject.toml       👈 Project metadata and dependencies
└── uv.lock / .replit    👈 Replit deployment configs
🧠 How it Works
app.py: This is the heart of the backend.

It sets up Flask.

Handles routes like / and /convert.

Receives uploaded PDFs/images or text input.

Passes them to ocr_handler.py for processing.

ocr_handler.py:

Uses pytesseract for OCR.

Uses PyPDF2 to extract text from PDFs.

Then converts that text into Braille Unicode format using custom logic.

templates/index.html (inside templates folder):

The web interface the user interacts with — includes:

Text input box

File upload

Output preview

Dark theme for accessibility

static/:

Holds styles, custom icons, and additional scripts.

🧪 Features in This Prototype
Text to Braille

Image to Braille (via OCR)

PDF to Braille (via PyPDF2)

Dark Mode UI

Unicode Braille Output

🔧 Future Add-ons
✅ Real-time website conversion
✅ Multiple Braille standards
✅ Enhanced OCR for low-quality images
✅ Batch processing (multiple files at once)
