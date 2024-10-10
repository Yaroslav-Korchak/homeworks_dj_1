from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().isoformat()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


# def workdir_view(request):
#     workdir = os.getcwd()
#     content = os.listdir(workdir)
#     formatted_content = "<br>".join(content)
#     return HttpResponse(f"Содержимое рабочей директории:<br>{formatted_content}")

def workdir_view(request):
    try:
        workdir = os.getcwd()
        content = os.listdir(workdir)
        # Форматируем список файлов и директорий в HTML
        formatted_content = "<ul>" + "".join(f"<li>{item}</li>" for item in content) + "</ul>"
    except FileNotFoundError:
        formatted_content = "Рабочая директория не найдена."
    except PermissionError:
        formatted_content = "Нет доступа к рабочей директории."

    return HttpResponse(f"Содержимое рабочей директории:<br>{formatted_content}")