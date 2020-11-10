from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeworkConfig(AppConfig):
    name = "apps.homework"
    verbose_name = _("Übungen")