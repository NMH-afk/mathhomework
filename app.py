from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from flask_mail import Mail, Message
import os

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/login')
#def login():
#    return render_template('login.html')

@app.route('/portfolio2')
def portfolio2():
    return render_template('portfolio2.html')

@app.route('/portfolio3')
def portfolio3():
    return render_template('portfolio3.html')

@app.route('/portfolio1')
def portfolio1():
    return render_template('portfolio1.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message_body = request.form['message']
        
        msg = Message(f"New Contact Form Submission from {name}",
                      recipients=['helphomework748@gmail.com'])
        msg.body = f"""
        Name = {name}
        Email = {email}
        Phone = {phone}
        Message = {message_body}
        """
        
        mail.send(msg)
        return jsonify({'success': True, 'message': 'Email sent successfully'}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({'success': False, 'message': 'Email failed to send'}), 500

if __name__ == '__main__':
    app.run(debug=True)
 
#@app.route('/index.html')
#def index():
#    return render_template('index.html')