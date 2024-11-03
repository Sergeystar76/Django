from django.shortcuts import render

# Create your views here.
title = 'мой сайт'
def platform(request):
    # title = 'мой сайт'
    home = 'Главная страница '
    context = {'title': title, 'home': home}
    return render(request, 'platform.html', context)

def games(request):
    context = {'title': title}
    return render(request, 'games.html', context)

def cart(request):
    return render(request, 'cart.html')