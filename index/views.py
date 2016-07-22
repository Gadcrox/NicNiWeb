from django.shortcuts import render
from carousel import models as carousel_model
from configuration import models as configuration_model

# Create your views here.
def index_view(request):
    carousel_items = carousel_model.Carousel.objects.all().order_by('-id')
    configuration = configuration_model.Configuration.objects.first()
    context = {'carousel_items': carousel_items,
                'configuration': configuration}
    return render(request, 'index.html', context)
