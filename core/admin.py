from datetime import timedelta

from django.contrib import admin
from django.utils import timezone
from solo.admin import SingletonModelAdmin

from core.models import AppConfiguration, ExecutableFile

admin.site.register(AppConfiguration, SingletonModelAdmin)


class CreatedStringFilter(admin.SimpleListFilter):
    title = 'Создан'
    parameter_name = 'Создан'

    def lookups(self, request, model_admin):
        return (
            ('more_than_day', 'Больше одного дня назад'),
            ('less_than_day', 'Меньше одного дня назад'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'more_than_day':
            return queryset.filter(created__lte=(timezone.now() - timedelta(days=1)))
        elif value == 'less_than_day':
            return queryset.filter(created__gte=(timezone.now() - timedelta(days=1)))
        return queryset


@admin.register(ExecutableFile)
class ExecutableFileAdmin(admin.ModelAdmin):
    list_display = (
        'filename',
        'created_string_col',
    )

    list_filter = (
        CreatedStringFilter,
    )

    search_fields = (
        'created_string',
    )

    def get_queryset(self, request):
        return self.model.extended.all()

    def created_string_col(self, obj):
        return obj.created_string

    created_string_col.short_description = 'Создан'
    created_string_col.admin_order_field = 'created_string'
