from django.shortcuts import render
from carousel import models as carousel_model
from configuration import models as configuration_model
from services import models as services_model
# Create your views here.
def context():
    carousel_items = carousel_model.Carousel.objects.all().order_by('-id')
    configuration = configuration_model.Configuration.objects.first()
    services_list = services_model.Services.objects.all().order_by('titulo')

    context = {'carousel_items': carousel_items,
                'configuration': configuration,
                'services_list': services_list}
    return context
def index_view(request):
    return render(request, 'index.html', context())

def history_view(request):
    return render(request, 'history.html', context())

def contact_view(request):
    return render(request, 'contact.html',context())

def service_index_view(request, slug):
    service_detail = services_model.Services.objects.get(slug = slug)
    context_page = context()
    context_page.update({'service_detail': service_detail})
    return render(request, 'service.html', context_page)
