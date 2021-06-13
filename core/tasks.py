import os

from core.models import AppConfiguration, ExecutableFile
from script_executor.celery import app


@app.task()
def copy_scripts():
    scripts_path = AppConfiguration.get_solo().scripts_path
    files = os.listdir(scripts_path)
    for filename in files:
        filepath = os.path.join(scripts_path, filename)
        content = os.popen(f'cat {filepath}').read()
        ExecutableFile.objects.update_or_create(
            filename=filename,
            defaults={
                'content': content,
            }
        )
