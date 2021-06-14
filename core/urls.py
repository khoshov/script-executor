from django.urls import path

from .views import main, executables

app_name = 'core'

urlpatterns = [
    path('', main, name='list'),
    path('executables', executables, name='executables'),
]
