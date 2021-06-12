from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


class AppConfiguration(SingletonModel):
    scripts_path = models.CharField(
        _('Директория со скриптами'),
        max_length=255,
    )

    class Meta:
        verbose_name = _('Основные настройки')

    def __str__(self):
        return f'{self.scripts_path}'


class ExecutableFile(models.Model):
    filename = models.CharField(
        _('Имя файла'),
        max_length=255,
    )
    content = models.TextField(
        _('Содердимое файла'),
    )
    created = models.DateTimeField(
        _('Создан'),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        _('Обновлён'),
        auto_now=True,
    )

    class Meta:
        verbose_name = _('Исполняемый файл')
        verbose_name_plural = _('Исполняемые файлы')

    def __str__(self):
        return f'{self.filename} {self.updated}'
