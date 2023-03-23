from django.db import models
from users.models import Student, Teacher


# Create your models here.
class Exercise(models.Model):

    date = models.DateTimeField()
    
    STUDY_CHOICES = (
        ("INDIVIDUAL", 'Индивидуальные'),
        ("GROUP", 'Групповые'),
    )
        
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    study_type = models.CharField(max_length=20, choices=STUDY_CHOICES)
    exercise_link = models.URLField()
    is_paid = models.BooleanField()
    pg_currency = models.CharField(max_length=200)
    payed_at = models.DateTimeField()
    success_transaction_description = models.TextField()