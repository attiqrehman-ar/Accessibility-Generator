
from flask import Flask, render_template, jsonify, request
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change in production

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate-statement', methods=['GET', 'POST'])
def generate_statement():
    if request.method == 'POST':
        store_name = request.form.get('store_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        # Generate statement using the template
        statement = {
            'html': f'''<p><strong>{store_name}</strong> is committed to providing an inclusive and accessible experience to everyone, including those with disabilities.</p>
            <p>Our commitment is guided by our accessibility policy to ensure that people with disabilities have full and equal opportunity to access and benefit from its products and information provided on the website using the Web Content Accessibility Guidelines (WCAG) version 2.2 AA.</p>
            <h2>Support / Feedback</h2>
            <p>How can we provide support and improve accessibility?</p>
            <p>We welcome your questions and feedback on the accessibility of our website. Please let us know how we can assist you if you encounter any barriers to access:</p>
            <ul>
                <li>Email: <a href="mailto:{email}">{email}</a> with subject line: <strong>Accessibility Support</strong></li>
                <li>Accessibility Support Phone: <a href="tel:{phone}">{phone}</a></li>
            </ul>''',
            'generated': True
        }
        
        return render_template('generate_statement.html', statement=statement)
    
    return render_template('generate_statement.html', statement={'generated': False})

@app.route('/book-call')
def book_call():
    return render_template('book-call.html', active_section='book-call')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')