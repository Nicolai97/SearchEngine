from django.shortcuts import render, redirect

def search_bar(request):
  return render(request, 'search/search_bar.html')

