from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Document

class DocumentListView(ListView):
    model = Document
    template_name = 'myapp/listview.html'  
    context_object_name = 'context'  


class DocumentDetailview(DetailView):
    model = Document
    template_name = 'myapp/detailview.html' 
    context_object_name = 'context'
