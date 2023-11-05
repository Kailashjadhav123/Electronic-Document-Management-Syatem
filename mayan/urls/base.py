from django.urls import path, include

__all__ = ('urlpatterns',)

urlpatterns = []

urlpatterns = [
    path('myapp/', include('mayan.apps.myapp.urls')),
]
