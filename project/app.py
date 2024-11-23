from flask import Flask, render_template, request, session, redirect, url_for
from flask_mail import Mail, Message
import secrets
app = Flask(__name__)



app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
# app.secret_key = 'your_secret_key_here'
mail = Mail(app)






def generate_otp():
    return str(secrets.randbelow(10000)).zfill(4)

@app.route('/send_otp', methods=['GET', 'POST'])
def send_otp():
    if request.method == 'POST':
        email = request.form['email']
        otp = generate_otp()
        session['otp'] = otp
        session['email'] = email
        msg = Message('Your OTP for Email Verification', sender='your_email@example.com', recipients=[email])
        msg.body = f'Your OTP is: {otp}'
        mail.send(msg)

        return redirect(url_for('verify_otp'))

    return render_template('send_otp.html')

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        user_otp = request.form['otp']
        stored_otp = session.get('otp', None)

        if user_otp == stored_otp:
            return "OTP verified successfully!"
        else:
            return "Invalid OTP. Please try again."

    return render_template('verify_otp.html')

if __name__=='__main_':
    app.run(debug=True)
