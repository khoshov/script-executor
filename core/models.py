from datetime import timedelta

from django.db import models
from django.db.models import Case, CharField, Value, When
from django.utils import timezone
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


class ExtendedExecutableFileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            created_string=Case(
                When(
                    created__lte=(timezone.now() - timedelta(days=1)),
                    then=Value('Создан более одного дня назад'),
                ),
                When(
                    created__gte=(timezone.now() - timedelta(days=1)),
                    then=Value('Создан менее одного дня назад'),
                ),
                output_field=CharField(),
            ),
        )


class ExecutableFile(models.Model):
    objects = models.Manager()  # The default manager.
    extended = ExtendedExecutableFileManager()  # Our custom manager.

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
    #
    # @property
    # def created_string(self):
    #     now = timezone.now()
    #     delta = now - self.created
    #     if delta.days >= 1:
    #         return 'Создан более одного дня назад'
    #     return 'Создан менее одного дня назад'

    class Meta:
        verbose_name = _('Исполняемый файл')
        verbose_name_plural = _('Исполняемые файлы')

    def __str__(self):
        return f'{self.filename} {self.created}'
