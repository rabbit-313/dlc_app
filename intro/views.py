# from django.shortcuts import render


# Create your views here.
#def index(request):
 #   context = {'sample':'HelloWorld'}
  #  return render(request, 'index.html', context)

from django.views import generic

class IndexView(generic.TemplateView):
    template_name="index.html"
class IndexView(generic.TemplateView):
    template_name="INTRODUCING.html"
class IndexView(generic.TemplateView):
    template_name="PROPOSING GENRE.html"
class IndexView(generic.TemplateView):
    template_name="MEMBERSHIP SYSTEM.html"

