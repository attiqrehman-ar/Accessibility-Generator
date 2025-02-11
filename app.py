from flask import Flask, render_template, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change in production

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate-statement', methods=['POST'])
def generate_statement():
    # Placeholder for statement generation logic
    return jsonify({
        'status': 'success',
        'statement': 'Your accessibility statement will appear here.'
    })

@app.route('/book-call')
def book_call():
    return render_template('home.html', active_section='book-call')
