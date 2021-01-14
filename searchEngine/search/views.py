from django.shortcuts import render, redirect
from whoosh.qparser import QueryParser, OrGroup, MultifieldParser
from whoosh.query import FuzzyTerm
from whoosh.analysis import StemmingAnalyzer
from whoosh import scoring
from whoosh.index import open_dir
from os.path import relpath

def search_bar(request):
  return render(request, 'search/search_bar.html')

def make_search(request):
  myindex = open_dir(relpath("/search/core/indexdir", start="/"))
  qp = MultifieldParser(["title", "textdata"], schema=myindex.schema, group=OrGroup, termclass=FuzzyTerm)
  qstring = request.POST.get('search_text')
  q = qp.parse(qstring)

  results_list = []

  with myindex.searcher(weighting=scoring.Frequency) as s:
    results = s.search(q, limit=30, terms=True)
    for x in results:
      result = {}
      result['title'] = x['title']
      result['url'] = x['url']
      results_list.append(result)
    corrected = s.correct_query(q, qstring)
    did_you_mean = ''
    if corrected.query != q:
      did_you_mean = corrected.query
      


  return render(request, 'search/search_results.html', {'search_text': request.POST.get('search_text'), 'results': results_list, 'did_you_mean': did_you_mean})

 