from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from .models import Carousel
# Create your views here.

@login_required
def carousel_view_view(request):
    return render(request, 'carouselView.html')


class create_new_item(TemplateView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':
            try:
                titulo = request.POST.get('tittle')
                descripcion = request.POST.get('description')
                imagen = request.FILE.get('fileImage', false)
            except:
                message = {'status':'2','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                nuevo_item = Carousel()

                nuevo_item.titulo = titulo
                nuevo_item.caption = descripcion
                nuevo_item.imagen = imagen
            except:
                message = {'status':'2','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")
