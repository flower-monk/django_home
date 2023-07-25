from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):

    data = {'name': 'not Found', 'age': 18}

    return render(request, 'index.html', data)

def accordion(request):

    data = {'name': 'not Found', 'age': 18}

    return render(request, 'accordion.html', data)
