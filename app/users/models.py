from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import UserManager
from .utils import uuid_generator

from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    CITY_CHOICES = (
        ("BISHKEK", 'Бишкек'),
        ("OSH", 'Ош'),
        ("KARA-BALTA", "Кара-Балта"),
        ("NARYN", "Нарын")
    )

    email = models.EmailField('email address', unique=True)
    phone_number = PhoneNumberField(
        verbose_name='Phone number',
        unique=True
    )

    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=100)

    birth = models.DateField('birth date')

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_created = models.DateTimeField(default=timezone.now)

    city = models.CharField('city', max_length=30, choices=CITY_CHOICES)

    picture = models.ImageField(upload_to="user_avatar",
                                verbose_name="Avatar",
                                null=True,
                                blank=True)

    activation_code = models.CharField(
        max_length=4,
        verbose_name="Код активации",
        null=True,
        blank=True
    )


    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        unique_together = ['email', 'phone_number']

    def save(self, *args, **kwargs):
        if self.is_active == True and self.activation_code is not None:
            self.activation_code = None


class Student(User):

    school = models.CharField('school', max_length=30)


class Teacher(User):

    about = models.TextField('about')
    study_time = models.CharField(max_length=200)