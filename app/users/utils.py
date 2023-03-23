from django.conf import settings
from datetime import datetime
import random, string, requests


def uuid_generator():
    """ GENEREATE ACTIVATION CODE TO LOGIN/REGISTER"""
    from .models import User
    
    while True:
        uuid = ''.join(random.choice(string.digits) for x in range(6))
        if not User.objects.filter(activation_code=uuid).exists():
            return uuid



def send_sms(phone, message, message_id=None):
    """
    SMS NIKITA FUNC
    """
    try:
        if settings.DEBUG == False:
            if not message_id:
                message_id = str(round(datetime.now().timestamp(), 2)).replace('.', '')
            data = '<?xml version="1.0" encoding="UTF-8"?>'
            data += '<message>'
            data += f'  <login>{settings.SMS_NIKITA_LOGIN}</login>'
            data += f'  <pwd>{settings.SMS_NIKITA_PASSWORD}</pwd>'
            data += '  <id>{0}</id>'.format(message_id)
            data += f'  <sender>{settings.SMS_NIKITA_SENDER_NAME}</sender>'
            data += '  <text>{0}</text>'.format(message)
            data += '  <phones>'
            data += '    <phone>{0}</phone>'.format(phone)
            data += '  </phones>'
            data += '</message>'
            headers = {'Content-Type': 'application/xml'}
            requests.post('http://smspro.nikita.kg/api/message',
                          data=data.encode('utf-8'), headers=headers)
    except Exception as e:
        print(e)
