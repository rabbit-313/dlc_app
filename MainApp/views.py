from django.shortcuts import render


# Create your views here.
def index(request):
   context = {'sample':'HelloWorld'}
   return render(request, 'index.html', context)

from django.views import generic

class IndexView(generic.TemplateView):
    template_name="introduce.html"
    
class IndexView(generic.TemplateView):
    template_name="introduce.html"
    
class IndexView(generic.TemplateView):
    template_name="propose.html"
class IndexView(generic.TemplateView):
    template_name="menbership.html"

