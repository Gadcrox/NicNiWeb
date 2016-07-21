
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from .models import Carousel
import json, traceback
# Create your views here.

@login_required
def carousel_view_view(request):
    items = Carousel.objects.all().order_by('-id')
    context = {'items': items}
    return render(request, 'carouselView.html', context)

class create_new_item(TemplateView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':
            try:
                titulo = request.POST.get('tittle')
                descripcion = request.POST.get('description')
                imagen = request.FILES.get('fileImage', False)
            except:
                message = {'status':'2','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                nuevo_item = Carousel()

                nuevo_item.titulo = titulo
                nuevo_item.caption = descripcion
                nuevo_item.imagen = imagen
                nuevo_item.save()
                message = {'status':'3','message': 'Datos insertados correctamente'}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'2','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

class view_item(TemplateView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':

            try:
                idItem = request.POST.get('idItem')
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                if not Carousel.objects.filter(id = idItem):
                    message = {'status':'2','message': 'Lo sentimos, esta imagen no existe...'}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                item = Carousel.objects.get(id= idItem)
                response_data = {}
                response_data['status'] = '3'
                response_data['id'] = item.id
                response_data['titulo'] = item.titulo
                response_data['caption'] = item.caption
                data = json.dumps(response_data)
                return HttpResponse(data, content_type =  "application/json")

            except:
                 message = {'status':'1','message': str(traceback.format_exc())}
                 data = json.dumps(message)
                 return HttpResponse(data, content_type =  "application/json")
