from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):

    data = {'name': 'cong', 'age': 18}

    return render(request, 'test.html', data)
