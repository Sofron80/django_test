from django.urls import path
# from django.urls.static import static

from .views import index, test_page

urlpatterns = [
    path('', index, name='index'),
    path('test/', test_page),
]
