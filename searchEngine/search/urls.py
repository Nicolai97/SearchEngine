from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.search_bar, name='search_bar'),
  path('/make_search', views.make_search, name='make_search'),
]