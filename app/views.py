from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .models import *

class ChampionsView(ListView):
    model = Champions
    template_name = 'home.html'
    context_object_name = 'one'

    def get_queryset(self):
        sort = Champions.objects.all().order_by('champions_year')
        return sort
    
class ChampionsDetail(DetailView):
    model = Champions
    template_name = 'about.html'
    context_object_name = 'onex'

def page_objects(request):
        if request.method == 'POST':
            page = request.POST['Page']
            to_number = int(page)
            data = Champions.objects.filter(id__range=(1, to_number))
            context = {'data': data}
            return render(request, 'list.html', context)
        return render(request, 'list.html')