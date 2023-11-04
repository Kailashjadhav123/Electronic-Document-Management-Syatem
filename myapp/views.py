from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Document

class DocumentListView(ListView):
    model = Document
    template_name = 'listview.html'  
    context_object_name = 'context'  


class DocumentDetailView(DetailView):
    model = Document
    template_name = 'detailview.html' 
    context_object_name = 'context'  


class DocumentCreateView(CreateView):
    model = Document
    fields = '__all__' 
    template_name = 'createview.html' 
    success_url = reverse_lazy('DocumentListView')  


class DocumentUpdateView(UpdateView):
    model = Document
    fields = '__all__'  
    template_name = 'updateview.html'  
    success_url = reverse_lazy('DocumentListView')  


class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'deleteview.html'  
    success_url = reverse_lazy('DocumentListView') 