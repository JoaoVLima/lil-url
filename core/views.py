from django.views.generic import TemplateView, RedirectView
from .models import Shortener


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShortView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        short = kwargs.get('short')
        try:
            long = Shortener.objects.filter(short_url=short).values_list('long_url').first()[0]
        except:
            long = None

        if not long:
            long = 'lima.dev'

        if not (long.startswith('https://') or long.startswith('https://')):
            long = '//' + long
        self.url = long

        return super().get_redirect_url(*args, **kwargs)
