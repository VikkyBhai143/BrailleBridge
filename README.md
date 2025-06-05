**🦯 Day 19/30: BrailleBridge — AI-Powered Digital Braille Converter**
👨‍💻 “Accessibility is not a feature, it's a fundamental right.”

For Day 19 of my "30 Days, 30 Projects" challenge, I built BrailleBridge — a web app that converts text, PDFs, and images into Braille Unicode, making digital content more accessible to visually impaired users around the globe.

🔍 Problem
Millions of visually impaired individuals face barriers accessing digital content that's not available in Braille format.

💡 Solution
BrailleBridge uses OCR + AI to extract text from:

📄 Uploaded PDFs

🖼️ Images

✍️ Typed content

...and instantly converts it into Braille Unicode, readable through assistive tools and embossers.

🧠 How It Works
📁 Folder Structure:

pgsql
Copy
Edit
BrailleBridge/
├── app.py           # Main Flask backend
├── main.py          # Entry point for external deploy
├── ocr_handler.py   # Handles OCR & Braille conversion
├── templates/       # HTML frontend
├── static/          # CSS + JS assets
🧩 Key Components:

app.py: Manages routes like / and /convert

ocr_handler.py:

🔍 pytesseract for OCR

📄 PyPDF2 for PDF parsing

🔠 Braille conversion logic

index.html: UI with dark mode, input forms & result area

⚙️ Features
✅ Text ➡ Braille
✅ Image ➡ Braille (via OCR)
✅ PDF ➡ Braille (via parsing)
✅ Unicode Braille Output
✅ Dark theme for accessibility

🔮 Coming Next
🌐 Real-time Website ➡ Braille

🌍 Support for Multiple Braille Standards

🧠 Advanced OCR (low-quality scans)

📚 Batch Document Processing
