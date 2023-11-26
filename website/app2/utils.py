from django.core.mail import send_mail

def send_mail_to_user(first_name, last_name, to_email):
    send_mail(
    "Welcome To the Team",
    f"Hi {first_name} {last_name}. Hearly congratulations to you for choose our organization to join. We are welcome you our great team and looking forward to work with you",
    'SNTI<email>',
    [to_email],
    fail_silently=False,
    )
    # return "Mail Successfully Send..."