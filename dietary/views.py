from django.views.generic.base import TemplateView
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import DietaryItem
from .filters import DietaryItemFilter

FACILITIES = ['Lander', 'Riverton']
DEPARTMENTS = ['Radiology', 'Therapy', 'Workwise', 'Lab', 'ER', 'Rehab', 'Surgery', 'OPSC', 'OB', 'ICU', 'Cardiac Rehab', 'Med Surg']


def index(request):
    template = loader.get_template('dietary/index.html')
    dietary_items = DietaryItem.objects.all()
    filter_set = DietaryItemFilter(request.GET, queryset=dietary_items)
    context = {
        'facilities': FACILITIES,
        'departments': DEPARTMENTS,
        'dietary_items': DietaryItem.objects.all(),
        'dietary_filter': filter_set,
    } 
    return render(request, 'dietary/index.html')


class Orders(TemplateView):
    template_name = "orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dietary_items'] = DietaryItem.objects.all()

