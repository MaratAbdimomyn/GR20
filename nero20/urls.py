from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ChampionsView.as_view(), name='home'),
    path('about/<int:pk>/', ChampionsDetail.as_view(), name='about'),
    path('list', page_objects, name='list')
]
