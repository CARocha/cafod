from django.views.generic.simple import direct_to_template
from django.conf import settings

def search(request):
    TEMPLATE = getattr(settings, 'CSE_TEMPLATE', 'django_google_cse/default.html')
    CX_CODE = getattr(settings, 'CX_CODE', '')

    q = request.GET.get('q', '')

    return direct_to_template(
                request, 
                TEMPLATE, 
                {'q': q, 'CX_CODE': CX_CODE}
            )