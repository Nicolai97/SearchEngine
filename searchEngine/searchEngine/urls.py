from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('search.urls')),
    re_path(r'^$', RedirectView.as_view(url='search/', permanent=False), name='index'),
]
