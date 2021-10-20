from django.views.generic.base import TemplateView

from dietary.models import DietaryItem
from django.http import HttpResponse

from django.template import loader

FACILITIES = ['Lander', 'Riverton']
DEPARTMENTS = ['Radiology', 'Therapy', 'Workwise', 'Lab', 'ER', 'Rehab', 'Surgery', 'OPSC', 'OB', 'ICU', 'Cardiac Rehab', 'Med Surg']


def index(request):
    template = loader.get_template('dietary/index.html')
    context = {
        'facilities': FACILITIES,
        'departments': DEPARTMENTS,
        'dietary_items': DietaryItem.objects.all(),
    } 
    return HttpResponse(template.render(context, request))


class Orders(TemplateView):
    template_name = "orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dietary_items'] = DietaryItem.objects.all()

