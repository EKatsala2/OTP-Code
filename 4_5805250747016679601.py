from flask import Flask, render_template, request
import random
from twilio.rest import Client
import pyotp


secret_key = pyotp.random_base32()
totp = pyotp.TOTP(secret_key)
otp= totp.now()


# Example usage
phone_number = '+265997583979'  # Replace with the recipient's phone number

# Generate OTP
def generate_otp():
    otp = random.randint(1000, 9999)
    return otp

# Send OTP via SMS
def send_otp_via_sms(phone_number, otp):
    account_sid = 'AC3ded4f9f79f4c38a4ae4216daa85c2dc'
    auth_token = '604b2410f22a74af0413bd9823cfb138'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Your OTP is: {otp}',
        from_='(815) 982-3153',
        to=phone_number
    )

app = Flask(__name__)

#routes
@app.route('/')
def index():
    return render_template('user-home.html')

@app.route('/home')
def home():
    return render_template('user-home.html')

@app.route('/admin')
def admin():
    return render_template('admin-dashboard.html')


@app.route('/scan-card')
def card():
    return render_template('scan-card.html')


@app.route('/scan-fingerprint')
def fingerprint():
    return render_template('scan-fingerprint.html')


@app.route('/otp')
def otp_generation():
    send_otp_via_sms(phone_number, otp)
    print(f"OTP sent successfully to {phone_number}!")
    return render_template('otpp.html',otp=otp)


@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form.get('otp_input')
    # Now you can process the input as needed
    print(f"You entered: {user_input}")
    return render_template('admin-dashboard.html')
