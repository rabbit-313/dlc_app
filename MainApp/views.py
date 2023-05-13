from django.views import generic

class IndexView(generic.TemplateView):
    template_name="index.html"
    
class IntroduceView(generic.TemplateView):
    template_name="introduce.html"
    
class ProposingView(generic.TemplateView):
    template_name="proposing.html"
class MembershipView(generic.TemplateView):
    template_name="membership.html"

