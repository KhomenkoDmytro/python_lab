from django.shortcuts import render

def index(request):
    data = {
        'title': 'Main page?',
        'values': ['some', 'hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': '20',
            'hobby': 'poems'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')