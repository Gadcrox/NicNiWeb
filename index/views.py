from django.shortcuts import render
from carousel import models as carousel_model

# Create your views here.
def index_view(request):
    carousel_items = carousel_model.Carousel.objects.all().order_by('-id')
    context = {'carousel_items': carousel_items}
    return render(request, 'index.html', context)
