from django.core.mail import send_mail

def send_mail_to_user(first_name, last_name, to_email):
    send_mail(
    """Welcome To the Team""",
    f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Contact Page</h1>
    Hello {first_name}
</body>
</html>""",
    'SNTI<email>',
    [to_email],
    fail_silently=False,
    )
    # return "Mail Successfully Send..."