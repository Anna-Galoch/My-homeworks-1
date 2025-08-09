from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    
    pages = {
        'Домашняя страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def current_time_view(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = f'Текущее время: {current_time}'
    return HttpResponse(result)


def workdir_view(request):
    files = os.listdir()
    # Создаем HTML-список файлов
    file_list = "<ul>" + "".join([f"<li>{file}</li>" for file in files]) + "</ul>"
    return HttpResponse(f"Содержимое рабочей директории:{file_list}")

