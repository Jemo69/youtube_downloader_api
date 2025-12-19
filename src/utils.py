import email
from dotenv import load_dotenv
import os
import smtplib
import jwt

load_dotenv()


def send_email(to, subject, text):
    bot_email = os.getenv('BOT_EMAIL')
    password = os.getenv('BOT_EMAIL_PASSWORD')
    msg = email.message.EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = to
    msg.set_content(text)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(bot_email,password)
        server.send_message(msg)

def verify_token(token):
    try:
        payload = jwt.decode(token, os.getenv('JWT_SECRET_KEY'))
        return payload
    except jwt.ExpiredSignatureError:
        return {"message": "Token expired"}
    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}
    except Exception as e:
        return {"message": str(e)}
