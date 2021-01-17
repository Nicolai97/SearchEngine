from django.shortcuts import render, redirect
from whoosh.qparser import QueryParser, OrGroup, MultifieldParser
from whoosh.query import FuzzyTerm
from whoosh.analysis import CharsetFilter, StemmingAnalyzer
from whoosh.support.charset import default_charset, charset_table_to_dict
from whoosh import scoring
from whoosh.index import open_dir
from whoosh import highlight
from os.path import relpath
from search.core.evaluations.map import map
from functools import reduce

def search_bar(request):
  return render(request, 'search/search_bar.html')

def make_search(request):
  charmap = charset_table_to_dict(default_charset)
  custom_analyzers = StemmingAnalyzer() | CharsetFilter(charmap)


  myindex = open_dir(relpath("/search/core/indexdir", start="/"))
  qp = MultifieldParser(["title", "textdata"], schema=myindex.schema, termclass=FuzzyTerm, fieldboosts={'title': 3.0, 'textdata': 1.0})
  qstring = request.POST.get('search_text')
  q = qp.parse(qstring)

  results_list = []

  myWeighting= scoring.MultiWeighting(scoring.Frequency(), textdata=scoring.Frequency(), title=scoring.BM25F(title_B=2.0))

  with myindex.searcher(weighting=myWeighting) as s:
    results = s.search(q, limit=30, terms=True)

    #query expansion
    keywords = [keyword for keyword, score in results.key_terms("textdata", docs=3, numterms=3)]
    query_keyword = qp.parse(reduce(lambda a, b: a + ' ' + b, keywords))
    results_keyword = s.search(query_keyword, limit=30, terms=True)
    results.upgrade_and_extend(results_keyword)

    #sorting
    key_sort = lambda result: result.score
    results = sorted(results, key=key_sort, reverse=True)


    #results.fragmenter.format = highlight.Highlighter()
    
    for ris in results:
      result = {}
      result['title'] = ris['title']
      result['url'] = ris['url']
      result['id'] = ris['ID']
      result['highlight'] = ris.highlights("textdata")
      results_list.append(result)

  


    #correzione parola
    corrected = s.correct_query(q, qstring)
    did_you_mean = ''
    if corrected.query != q:
      did_you_mean = corrected.query

    #valutazione
    id_results = [ris['id'] for ris in results_list[:10]] 

    google_resul_apple = ['856', '2593693', '1344', '501016', '16161443', '19006979', '8841749', '16179920', '7412236', '5078775']
    precision = map(id_results, google_resul_apple)
    print("precision= " + str(precision))

    
      


  return render(request, 'search/search_results.html', {'search_text': request.POST.get('search_text'), 'results': results_list, 'did_you_mean': did_you_mean})

 