from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    """
    Контроллер для отображения домашней страницы
    """
    context = {
        'page_title': 'Главная страница',
        'welcome_message': 'Добро пожаловать в интернет-магазин!'
    }
    return render(request, 'home.html', context)


def contacts(request: HttpRequest) -> HttpResponse:
    """
    Контроллер для отображения страницы с контактной информацией
    """
    # Пример обработки POST-запроса
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Здесь можно добавить логику отправки email или сохранения в БД
        print(f"Получено сообщение от {name} ({email}): {message}")

    context = {
        'page_title': 'Контакты',
        'phone': '+7 (999) 123-45-67',
        'email': 'info@catalog.ru',
        'address': 'г. Москва, ул. Примерная, д. 123'
    }
    return render(request, 'contacts.html', context)