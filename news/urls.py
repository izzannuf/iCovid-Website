from django.urls import path
from .views import index, read, postArticle
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('add/', postArticle)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)