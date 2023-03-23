import telebot
from decouple import config
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from users.models import Student
from .models import Exercise

bot = telebot.TeleBot(config('BOT_TOKEN'))
ROOT_URL = config("ROOT_URL")


@csrf_exempt
def django_bot(request):
    if request.META['CONTENT_TYPE'] == 'application/json':
        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])

        return HttpResponse("")
    else:
        raise PermissionDenied


def get_exercise_student(student):
    exercise = Exercise.objects.filter(student=student)
    return exercise


def get_student(username):
    try:
        return Student.objects.get(telegram_contact=username)
    except Exception:
        return None


@bot.message_handler(commands=['start'])
def start(message):
    username = message.chat.username if message.chat.username is not None else message.chat.first_name
    student = get_student(username=username)
    exercise = get_exercise_student(student=student)

    if not student:
        messages = ()
    if not exercise:
        messages = ()

    student = Student.objects.get(telegram_contact=message.chat.username)
    student.telegram_id = message.chat.id
    student.save()
    bot.send_message(message.chat.id, messages)


def telegram_notify_user(chat_id, delay, survey_link):
   message = ' '
   if delay != 10:
      message = ()
   else:
      message = ()
   bot.send_message(chat_id, message)

def telegram_send_survey_url(chat_id, sstudent, username):
    student = get_student(username=username)
    uuid_student = student.student_uuid
    exercise = get_exercise_student(student=sstudent)
    bot.send_message(chat_id, 'Ссылка на урок')
