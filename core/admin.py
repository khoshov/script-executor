from django.contrib import admin
from solo.admin import SingletonModelAdmin

from core.models import AppConfiguration, ExecutableFile

admin.site.register(AppConfiguration, SingletonModelAdmin)
admin.site.register(ExecutableFile, admin.ModelAdmin)
