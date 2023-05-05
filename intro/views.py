from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'sample':'HelloWorld'}
    return render(request, 'index.html', context)