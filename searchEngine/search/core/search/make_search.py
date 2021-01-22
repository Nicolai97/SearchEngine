from django.shortcuts import render, redirect
from whoosh.qparser import QueryParser, MultifieldParser, AndGroup
from whoosh.query import FuzzyTerm
from whoosh.analysis import CharsetFilter, StemmingAnalyzer
from whoosh.support.charset import default_charset, charset_table_to_dict
from whoosh import scoring
from whoosh.index import open_dir
from whoosh import highlight
from os.path import relpath, curdir, join
from functools import reduce
import pathlib

def make_search_service(search_text):
  charmap = charset_table_to_dict(default_charset)
  custom_analyzers = StemmingAnalyzer()

  index_path = join(pathlib.Path(__file__).parent.parent.absolute(), 'indexdir')
  myindex = open_dir(index_path)
  qp = MultifieldParser(["title", "textdata"], schema=myindex.schema, group=AndGroup, fieldboosts={'title': 3.0, 'textdata': 0.8})
  qstring = search_text
  q = qp.parse(qstring)

  results_list = []

  myWeighting= scoring.MultiWeighting(scoring.BM25F(textdata_B=0.5), textdata=scoring.Frequency(), title=scoring.BM25F(title_B=2.0))
  with myindex.searcher(weighting=myWeighting) as s:
    results = s.search(q, limit=30, terms=True)

    #forse cercavi e risultati relativi a
    corrected = s.correct_query(q, qstring)
    did_you_mean = str
    result_for = str
    if corrected.query != q:
      if len(results) < 1:
        results = s.search(qp.parse(corrected.string), limit=30, terms=True)
        result_for = corrected.string
      else:
        did_you_mean = corrected.string


    #query expansion
    keywords = [keyword for keyword, score in results.key_terms("textdata", docs=3, numterms=5)]
    if not keywords and keywords == " ":
      query_keyword = qp.parse(reduce(lambda a, b: a + ' ' + b, keywords))
      results_keyword = s.search(query_keyword, limit=30, terms=True)
      results.upgrade_and_extend(results_keyword)

    #sorting
    key_sort = lambda result: result.score
    results = sorted(results, key=key_sort, reverse=True)

    
    for ris in results:
      result = {}
      result['title'] = ris['title']
      result['url'] = ris['url']
      result['id'] = ris['ID']
      result['highlight'] = ris.highlights("textdata")
      results_list.append(result)


    #per calcolo precisione e recall
    id_results = [ris['id'] for ris in results_list[:10]]

    return {
      'search_text': search_text,
      'results': results_list, 
      'did_you_mean': did_you_mean,
      'result_for': result_for,
      'results_ids': id_results
    }