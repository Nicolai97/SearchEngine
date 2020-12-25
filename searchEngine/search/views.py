from django.shortcuts import render, redirect
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir

def search_bar(request):
  return render(request, 'search/search_bar.html')

def make_search(request):
  myindex = open_dir("../indexdir")
  qp = QueryParser("textdata", schema=myindex.schema)
  q = qp.parse(request.POST.get('search_text'))

  results_list = []

  with myindex.searcher(weighting=scoring.Frequency) as s:
    results = s.search(q, limit=30)
    for x in results:
      result = {}
      result['title'] = x['title']
      result['url'] = x['url']
      results_list.append(result)

  return render(request, 'search/search_results.html', {'search_text': request.POST.get('search_text'), 'results': results_list})

