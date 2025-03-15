document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('conversionForm');
    const result = document.getElementById('result');
    const errorMessage = document.getElementById('errorMessage');
    const textInput = document.getElementById('textInput');
    const fileInput = document.getElementById('fileInput');
    const convertBtn = document.getElementById('convertBtn');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Show loading state
        convertBtn.disabled = true;
        convertBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Converting...';
        
        // Hide previous results and errors
        result.classList.add('d-none');
        errorMessage.classList.add('d-none');

        const formData = new FormData();

        if (fileInput.files.length > 0) {
            formData.append('file', fileInput.files[0]);
        } else if (textInput.value.trim()) {
            formData.append('text', textInput.value.trim());
        } else {
            showError('Please enter text or upload a file');
            resetButton();
            return;
        }

        try {
            const response = await fetch('/convert', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (data.success) {
                document.getElementById('detectedText').value = data.text;
                document.getElementById('brailleOutput').value = data.braille;
                result.classList.remove('d-none');
                // Announce success to screen readers
                announceToScreenReader('Conversion completed successfully');
            } else {
                showError(data.error || 'Conversion failed');
            }
        } catch (error) {
            showError('An error occurred during conversion');
        } finally {
            resetButton();
        }
    });

    // File input change handler
    fileInput.addEventListener('change', function() {
        if (this.files.length > 0) {
            textInput.value = ''; // Clear text input when file is selected
        }
    });

    // Text input change handler
    textInput.addEventListener('input', function() {
        if (this.value.trim()) {
            fileInput.value = ''; // Clear file input when text is entered
        }
    });
});

function showError(message) {
    const errorMessage = document.getElementById('errorMessage');
    errorMessage.textContent = message;
    errorMessage.classList.remove('d-none');
    announceToScreenReader('Error: ' + message);
}

function resetButton() {
    const convertBtn = document.getElementById('convertBtn');
    convertBtn.disabled = false;
    convertBtn.innerHTML = 'Convert to Braille';
}

function copyToClipboard(elementId) {
    const element = document.getElementById(elementId);
    element.select();
    document.execCommand('copy');
    announceToScreenReader('Braille text copied to clipboard');
}

function announceToScreenReader(message) {
    const announce = document.createElement('div');
    announce.setAttribute('aria-live', 'polite');
    announce.classList.add('sr-only');
    announce.textContent = message;
    document.body.appendChild(announce);
    setTimeout(() => document.body.removeChild(announce), 1000);
}
