from django.core.mail import send_mail
from django_movie.celery import app
from .models import Contact


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'subject',
            'ВЫ подписались на рассылку, будет много спама!!!',
            'testnord2021@gmail.com',
            [contact.email],
            fail_silently=False
        )
