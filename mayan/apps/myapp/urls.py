from django.urls import path

from .views import DocumentListView, DocumentDetailview

urlpatterns = [
    path('', name='home',view=DocumentListView.as_view()),
    path('detail/<int:pk>/', view=DocumentDetailview.as_view(), name='detail'),
]
