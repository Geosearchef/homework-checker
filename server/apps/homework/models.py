from apps.teaching.models import Lesson
from autoslug import AutoSlugField
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel, UUIDModel

from .helpers import get_exercise_rsc_path, get_submission_path, get_tests_path
from .storage import OverwriteStorage


class Exercise(UUIDModel):
    class ProgrammingLanguages(models.TextChoices):
        PYTHON = "py", "Python"
        R = "r", "R"

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name=_("Lektion")
    )

    title = models.CharField(max_length=100, verbose_name=_("Titel"))
    slug = AutoSlugField(max_length=255, populate_from="title")
    description = models.TextField(blank=True, verbose_name=_("Beschreibung"))
    max_score = models.PositiveSmallIntegerField(verbose_name=_("Maximale Punktzahl"))
    tests = models.FileField(
        storage=OverwriteStorage(), upload_to=get_tests_path, max_length=255
    )
    min_upload_size = models.PositiveIntegerField(
        "Minimale Upload Größe in Bytes",
        default=30,
    )
    max_upload_size = models.PositiveIntegerField(
        "Maximale Upload Größe in Bytes", default=5000
    )
    timeout = models.PositiveSmallIntegerField(
        "Maximale Testlaufzeit in Sekunden",
        default=10,
    )
    programming_language = models.CharField(
        max_length=2, choices=ProgrammingLanguages.choices
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Aufgabe")
        verbose_name_plural = _("Aufgaben")
        ordering = ["title"]


class Submission(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    file = models.FileField(upload_to=get_submission_path, max_length=255)
    file_hash = models.CharField(max_length=40)
    score = models.PositiveSmallIntegerField(default=0)
    output = models.TextField(blank=True)

    class Meta:
        unique_together = (
            "file_hash",
            "user",
            "exercise",
        )

    def clean(self):
        super().clean()
        lesson = self.exercise.lesson

        # Check timestamp of submission
        if lesson.start and self.created < lesson.start:
            raise ValidationError(
                _("You cannot upload a submission before the lesson started."),
            )
        if lesson.end and lesson.end < self.created:
            raise ValidationError(
                _("You cannot upload a submission after the lesson ended."),
            )


class ExerciseResource(UUIDModel, TimeStampedModel):
    exercise = models.ForeignKey(
        Exercise, on_delete=models.PROTECT, related_name="resources"
    )
    title = models.CharField(
        max_length=100,
        verbose_name=_("Titel"),
    )
    file = models.FileField(
        upload_to=get_exercise_rsc_path, storage=OverwriteStorage(), max_length=255
    )
    public = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Vorlesungsmaterial")
        verbose_name_plural = _("Vorlesungmaterialien")
        unique_together = ("exercise", "title")
