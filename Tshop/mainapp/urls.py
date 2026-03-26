from django.urls import path
from .views import homeView, aboutView, contactView

from .views import (CarouselImageList)

urlpatterns = [
    path('', homeView, name = 'home_page'),
    path('about/', aboutView, name = 'about_page'),
    path('contact/', contactView, name = 'contact_page'),

    path('carousels/', CarouselImageList.as_view(), name = 'carousel_page')
]