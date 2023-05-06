# from django.shortcuts import render


# Create your views here.
#def index(request):
 #   context = {'sample':'HelloWorld'}
  #  return render(request, 'index.html', context)

from django.views import generic

class IndexView(generic.TemplateView):
    template_name="index.html"
class INTRODUCINGView(generic.TemplateView):
    template_name="introducing.html"
class PROPOSINGGENREView(generic.TemplateView):
    template_name="proposing.html"
class MEMBERSHIPSYSTEMView(generic.TemplateView):
    template_name="membership.html"

