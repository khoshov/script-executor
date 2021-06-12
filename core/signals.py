import os

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ExecutableFile
from .utils import get_executable_path


def write_to_file(instance):
    executable_path = get_executable_path(instance.filename)
    os.system(f"echo '{instance.content}' > {executable_path}")
    os.system(f'chmod +x {executable_path}')


@receiver(post_save, sender=ExecutableFile)
def create_executable_file(sender, instance, **kwargs):
    # TODO: Проверить если при сохранении содержимое файла
    #  не изменилось тогда ничего не делам
    write_to_file(instance)
