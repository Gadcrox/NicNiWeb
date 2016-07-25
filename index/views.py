from django.shortcuts import render
from carousel import models as carousel_model
from configuration import models as configuration_model

# Create your views here.
def context():
    carousel_items = carousel_model.Carousel.objects.all().order_by('-id')
    configuration = configuration_model.Configuration.objects.first()
    context = {'carousel_items': carousel_items,
                'configuration': configuration}
    return context
def index_view(request):
    return render(request, 'index.html', context())

def history_view(request):
    return render(request, 'history.html', context())

def contact_view(request):
    return render(request, 'contact.html',context())
