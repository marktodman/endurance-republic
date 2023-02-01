from django.views.generic import TemplateView


# Home Page
class HomePage(TemplateView):
    """Create Home page view"""
    template_name = 'home/index.html'
