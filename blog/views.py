from django.http import HttpResponse
from django.shortcuts import render
from blog.models import News


def index(request):
    data = {
        'message': 'Проверка связи',
        'news': News.objects.all()
    }

    return render(request, 'index.html', context=data)


def test_page(request):
    return HttpResponse('<h1>Тестовая страница</h1>')
    # return render(request, 'test.html', context={'message': 'Test Проверка связи'})
