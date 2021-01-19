from evaluations.precision_and_recall import precision_and_recall
from search.make_search import make_search_service
import os
import pathlib

google_results = {
  'DNA': ['7955', '376524', '9329150', '21496', '26846483', '12388', '4250553', '21505', '4292', '25758'],
  'apple': ['856', '2593693', '1344', '501016', '16161443', '19006979', '8841749', '16179920', '7412236', '5078775'],
  'precision': ['14343887', '41572', '1164930', '18421531', '24467258', '866638', '10614570', '11946231', '17449489', '3962145'],
  'computer programming': ['5311', '5783', '23015', '144146', '6301802', '4119246', '6021', '27661', '3882218', '189897']
  'epigenetics': ['49033', '37122597', '35812169', '31182307', '46697210', '14938064', '42647878', '56840878', '42684750', '30932051'],
  'tuscany': ['21967242', '14448498', '679153', '9083550', '319100', '4535978', '59217770', '548647', '46169', '11525'],
  'steve jobs': ['7412236', '44519131', '33428137', '45145038', '47603179', '35304421', '37656556', '46240685', '864271', '27848'],
  'solar energy': ['27743', '13690575', '3507365', '32793086', '6328047', '413092', '54269557', '652531', '17805223', '35295938'],
  'read the manual': ['136530', '316050', '5655064', '40079206', '1256791', '44484413', '749736', '35495222', '85332', '']
}

for search_query in google_results:
  results = make_search_service(search_query)
  results_ids = results['results_ids']
  google_result = google_results[search_query]

  values = precision_and_recall(results_ids, google_result)
  print("query: '%s'\nprecision: %s\nrecall: %s\n\n" % (search_query, str(values['precision']), str(values['recall'])))



# google_resul_apple = ['856', '2593693', '1344', '501016', '16161443', '19006979', '8841749', '16179920', '7412236', '5078775']
#     precision = map(id_results, google_resul_apple)
#     print("precision= " + str(precision))