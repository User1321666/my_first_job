from django.core.mail import send_mail


def celery_send_confirmation_email(code, email):
    full_link = f'http://localhost:8000/account/active/{code}/'
    send_mail(
        'From firstproject',
        full_link,
        'kubabk7@gmail.com',
        [email]
    )


def restore_p_mail(code, email, username):
    body = f'Здравствуйте {username.title()} \n Ваш код для восстановления пароля \n{code}'
    send_mail(
        'From firstproject',
        body,
        'kutyabk7@gmail.com',
        [email]
    )
