from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from config import settings

def send_welcome_email(user):
    subject = 'Welcome to Our Platform!'
    html_message = render_to_string('emails/welcome.html', {
        'user': user,
        'site_name': settings.SITE_NAME
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
        fail_silently=False,
    )


def send_password_reset_email(user, token):
    subject = 'Password Reset Request'
    reset_url = f"{settings.FRONTEND_RESET_PASSWORD_URL}?token={token.key}"
    
    html_message = render_to_string(settings.PASSWORD_RESET_EMAIL_TEMPLATE, {
        'user': user,
        'token': token,
        'reset_password_url': reset_url,
        'site_name': settings.SITE_NAME
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
        fail_silently=False,
    )