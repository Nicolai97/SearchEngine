from django.shortcuts import render, redirect
from search.core.search.make_search import make_search_service

def search_bar(request):
  return render(request, 'search/search_bar.html')

def make_search(request):
  search_text = request.POST.get('search_text')
  if search_text:
    results = make_search_service(search_text)
    return render(request, 'search/search_results.html', {'search_text': results['search_text'], 'results': results['results'], 'did_you_mean': results['did_you_mean'], 'result_for': results['result_for']})
  else:
    return render(request, 'search/search_bar.html')
 