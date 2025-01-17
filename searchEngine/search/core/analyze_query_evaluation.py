from evaluations.precision_and_recall import precision_and_recall
from search.make_search import make_search_service
import os
import pathlib

google_results = {
  'DNA': ['7955', '376524', '9329150', '21496', '26846483', '12388', '4250553', '21505', '4292', '25758'],
  'Hollywood': ['53849', '84485', '990782', '1423694', '914512', '27421416', '871371', '105776', '2539634', '56717294'],
  'Maya': ['18449273', '77041', '355254', '113014', '4967305', '5958027', '147476', '9617641', '1494968', '1524237'],
  'Microsoft': ['19001', '1545193', '4240094', '18784745', '18890', '709683', '20288', '6947642', '4395735', '16358617'],
  'Apple': ['856', '2593693', '1344', '501016', '16161443', '19006979', '8841749', '16179920', '7412236', '5078775'],
  'Precision': ['14343887', '41572', '1164930', '18421531', '24467258', '866638', '10614570', '11946231', '17449489', '3962145'],
  'Epigenetics': ['49033', '37122597', '35812169', '31182307', '46697210', '14938064', '42647878', '56840878', '42684750', '30932051'],
  'Tuscany': ['21967242', '14448498', '679153', '9083550', '319100', '4535978', '59217770', '548647', '46169', '11525'],
  '99 balloons': ['884209', '6687843', '345742', '209669', '11124013', '1572117', '2964276', '32922685', '15290506','25349705'],
  'Least squares': ['82359', '27118759', '1651906', '971437', '15652764', '4504135', '2593771', '2407860', '1046736', '2713327'],
  'Computer programming': ['5311', '5783', '23015', '144146', '6301802', '4119246', '6021', '27661', '3882218', '189897'],
  'Financial meltdown': ['2878852', '32005855', '21553168', '19337279', '22652683', '10062100', '735925', '26152387', '1693352', '933495'],
  'Justin Timberlake': ['69323', '10429878', '35974124', '37620375', '2300849', '7325720', '40245278', '56196328', '38453748', '466563'],
  'Steve Jobs': ['7412236', '44519131', '33428137', '45145038', '47603179', '35304421', '37656556', '46240685', '864271', '27848'],
  'Solar energy': ['27743', '13690575', '3507365', '32793086', '6328047', '413092', '54269557', '652531', '17805223', '35295938'],
  'Roman empire': ['25507', '504379', '219117', '17958273', '25791', '3072770', '22290735', '923406', '521555', '314732'],
  'Mars robots': ['421366', '252908', '36645032', '1632896', '426143', '10297736', '37837437', '421051', '421049', '21134515'],
  'Page six': ['2562498', '102227', '56208270', '483472', '207444', '23257580', '20931146', '21599513', '4690051', '2016668'],
  'The maya': ['18449273', '355254', '46998769', '4967305', '6721754', '30974186', '5958027', '10443117', '1494968', '21110575'],
  'Triple cross': ['9283532', '10139650', '9283529', '978650', '48613699', '1687809', '40462433', '7987443', '10906715', '46436562'],
  'Statistical Significance': ['160995', '554994', '30284', '1311951', '5657877', '935655', '1361141', '226680', '9444220', '23658675'],
  'US constitution': ['31644', '31646', '497752', '9119240', '31647', '932529', '31650', '31653', '31666', '31662'],
  'Read the manual': ['136530', '316050', '5655064', '40079206', '1256791', '44484413', '749736', '35495222', '85332', '1472613'],
  'Physics Nobel Prizes': ['52497', '1175987', '21201', '1528075', '9053562', '19653466', '1175987', '1811842', '43229605', '24636986'],
  'Spanish Civil War': ['18842471', '9468339', '31596058', '31594699', '1555138', '24125782', '31842251', '32580812', '15369', '58859770'],
  'Mean Average Precision': ['50716473', '14343887', '11184711', '15271', '3440396', '8379669', '41932', '43218024', '33274', '25050663'], 
  'Much ado about nothing': ['8781048', '1615355', '33528868', '41517346', '27817491', '57465117', '33568270', '2612489', '3113126', '31323944'],
  'Eye of horus': ['967176', '1350710', '49448', '24836888', '23409619', '506916', '97350', '69035', '49471', '59236']
}

n_query = 0
final_accuracy = 0
for search_query in google_results:
  results = make_search_service(search_query)
  results_ids = results['results_ids']
  google_result = google_results[search_query]

  values = precision_and_recall(results_ids, google_result)
  n_query += 1
  final_accuracy += values['precision']
  
  print("query: '%s'\nprecision: %s\nrecall: %s\n\n" % (search_query, str(values['precision']), str(values['recall'])))

final_accuracy /= n_query
print("final accuracy: %s" % final_accuracy)