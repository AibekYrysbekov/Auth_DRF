import random

from django.core.mail import send_mail

from config import settings


def generate_otp(length=6):
    code = ''.join(random.choice('0123456789') for _ in range(length))
    return code


def send_otp_email(email, code):
    subject = 'Verification Code'
    message = f'Your verification code is: {code}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
