from django.conf.urls import url

from .views import (DocumentCreateView, DocumentListView, DocumentDeleteView, DocumentDetailView, 
                    DocumentUpdateView)

urlpatterns = [
    url(
        regex=r'^myapp/create/', name='DocumentCreateView',
        view=DocumentCreateView.as_view()
    ),
    url(
        regex=r'^myapp/', name='DocumentListeView',
        view=DocumentListView.as_view()
    ),
    url(
        regex=r'^myapp/<int:pk>/', name='DocumentdetailView',
        view=DocumentDetailView.as_view()
    ),
    url(
        regex=r'^myapp/update/<int:pk>/', name='DocumentUpdateView',
        view=DocumentUpdateView.as_view()
    ),
    url(
        regex=r'^myapp/delete/<int:pk>/', name='DocumentDeleteView',
        view=DocumentDeleteView.as_view()
    ),
]