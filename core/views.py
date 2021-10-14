import random
from braces.views import JSONResponseMixin, AjaxResponseMixin
from django.views import View
from django.views.generic import TemplateView, RedirectView
from .queries import ShortenerQuery


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
            long = ShortenerQuery().byShort(short).long_url
        except:
            long = None

        if not long:
            long = random.choice(('lima.dev', 'github.com/pietrows'))

        if not (long.startswith('http://') or long.startswith('https://')):
            long = '//' + long
        self.url = long

        return super().get_redirect_url(*args, **kwargs)


class ShortDashView(TemplateView):
    template_name = 'dash.html'

    def get_context_data(self, **kwargs):
        short = kwargs.get('short')
        try:
            long = 's'
        except:
            long = None

        if not long:
            long = random.choice(('lima.dev', 'github.com/pietrows'))

        if not (long.startswith('http://') or long.startswith('https://')):
            long = '//' + long

        context = super().get_context_data(**kwargs)
        context['long'] = ShortenerQuery().getAcessos(short)

        return context


class Criar_url(JSONResponseMixin, AjaxResponseMixin, View):

    def get_ajax(self, request, *args, **kwargs):
        long = request.GET.get('long')
        path = request._current_scheme_host
        short = long[0:2]
        response = {
            'short': f'{path}/{short}',
            'short_dash': f'{path}/{short}/dashboard',
        }
        return self.render_json_response(response)
