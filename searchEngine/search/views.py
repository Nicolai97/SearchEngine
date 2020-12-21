from django.shortcuts import render, redirect

def search_bar(request):
  return render(request, 'search/search_bar.html')

def make_search(request):
  return render(request, 'search/search_results.html', {'search_text': request.POST.get('search_text')})

