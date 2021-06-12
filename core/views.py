import os

from django.template.response import TemplateResponse

from core.utils import get_executable_path, get_scripts_list


def main(request):
    scripts = get_scripts_list()
    script_filename = request.GET.get('scripts')
    script_path = None
    results = None
    if script_filename:
        script_path = get_executable_path(script_filename)
        results = os.popen(f'sh {script_path}').read().split('\n')
    return TemplateResponse(request, 'core/list.html', context={
        'scripts': scripts,
        'script_path': script_path,
        'results': results,
    })
