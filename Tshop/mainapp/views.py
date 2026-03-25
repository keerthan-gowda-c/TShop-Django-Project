from django.shortcuts import render
from .models import CarouselImage


# Create your views here.

def homeView(request):
    template = 'mainapp/home.html'
    context = {
        'carousel_images' : CarouselImage.objects.filter(is_active = True),
        'name' : "Tea Shop"
    }
    return render(
        request = request,
        template_name = template,
        context = context
    )

def aboutView(request):
    template = 'mainapp/about.html'

    return render(
        request = request,
        template_name = template,
        context = {}
    )

def contactView(request):
    template = 'mainapp/contact.html'

    return render(
        request = request,
        template_name = template,
        context = {}
    )