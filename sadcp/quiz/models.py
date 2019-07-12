from django.db import models

from sadcp.utils import prefixed_uuid


class Quiz(models.Model):
    id = models.CharField(
        primary_key=True,
        default=prefixed_uuid(prefix="quiz"),  # don't change this prefix
        editable=False,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO:
    # user = models.ForeignKey(...)

    # OneToMany QuestionAnswer


class QuestionAnswer(models.Model):
    id = models.CharField(
        primary_key=True,
        default=prefixed_uuid(prefix="qa"),  # don't change this prefix
        editable=False,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)


class Question(models.Model):
    id = models.CharField(
        primary_key=True,
        default=prefixed_uuid(prefix="q"),  # don't change this prefix
        editable=False,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
