from evaluations.map import map
from search.make_search import make_search_service
import os
import pathlib

google_results = {
  'DNA': ['7955', '376524', '9329150', '21496', '26846483', '12388', '4250553', '21505', '4292', '25758'],
  'apple': ['856', '2593693', '1344', '501016', '16161443', '19006979', '8841749', '16179920', '7412236', '5078775']
}

for search_query in google_results:
  results = make_search_service(search_query)
  results_ids = results['results_ids']
  google_result = google_results[search_query]

  values = map(results_ids, google_result)
  print("query: '%s'\nprecision: %s\nrecall: %s\n\n" % (search_query, str(values['precision']), str(values['recall'])))



# google_resul_apple = ['856', '2593693', '1344', '501016', '16161443', '19006979', '8841749', '16179920', '7412236', '5078775']
#     precision = map(id_results, google_resul_apple)
#     print("precision= " + str(precision))