"""short_url URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from .views import IndexView, ShortView, ShortDashView, Criar_url

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^(?P<short>[a-zA-Z0-9]+)$', ShortView.as_view(), name='short'),
    re_path(r'^(?P<short>[a-zA-Z0-9]+)/dashboard$', ShortDashView.as_view(), name='short_dash'),
    re_path(r'^ajax/criar_url$', Criar_url.as_view(), name='criar_url'),

]
