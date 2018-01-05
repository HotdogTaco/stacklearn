"""  /multiplechoice/models.py
    Data models for the multiple app.
"""
from api import models as api_models
from django.conf import settings
from django.db import models
from django.urls import reverse

import uuid

class MultipleChoiceAnswer(models.Model):
    """ A `MultipleChoiceAnswer` is an answer selected by a `Student` from # choices
    """
    student = models.ForeignKey(api_models.Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject_choices = (
        ('1', 'Multiplication'),
        ('2', 'Division'),
        ('3', 'Spanish Vocab'),
        ('4', 'Mandarin Vocab'),
        ('5', 'English Grammar'),
        ('6', 'Programming'),
    )
    raw_subject = models.CharField(
        choices=subject_choices,
        max_length=50,
        default='1'
    )
    answer1 = models.IntegerField(default='0')
    answer2 = models.IntegerField(default='0')
    answer3 = models.IntegerField(default='0')
    answer4 = models.IntegerField(default='0')
    answer_choices = (
        ('1', answer1),
        ('2', answer2),
        ('3', answer3),
        ('4', answer4),
    )
    raw_answer = models.CharField(
        choices=answer_choices,
        max_length=50,
        default='1',
    )
    right_answer = '1'
    was_correct = models.BooleanField()
    question = models.CharField(max_length=50)

    def __str__(self):
        return "{} selected {}".format(self.student.username, self.raw_answer)
