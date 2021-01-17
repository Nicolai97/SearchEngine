# precision = N relevant doc / N retrived doc
# recall = N relevant doc / N total doc

# precision = N intersezione tra relevant e retrived / N retrived doc 
# recall = N intersezione tra relevant e retrived / N relevant doc


# creare un dictionary con i 10 risultati rilevanti per ogni ricerca (per ogni ricerca salviamo il titolo e il link di google)
# ricerche da considerare
# apple
# DNA
# Hollywood
# Computer Programming
# Financial meldown
# Triple Cross
# Mean Average Precision
# Much ado about nothing
# calcolare i valori di precision, average precision e recall su 10 risultati

import math

def precision_and_recall(search_results, google_results):
    total_precision = 0
    total_recall = 0
    hit = 0
    current_hit = 0
    for x in range(len(search_results)):
        if search_results[x] in google_results:
            hit += 1
            current_hit = 1
        if current_hit == 1:
            precision = round(hit / (x + 1), 2)
            total_precision += precision
        current_hit = 0
    if hit == 0:
        return {'precision': 0, 'recall': 0}

    recall = round(hit / len(google_results), 2)

    return {
        'precision': round(total_precision / hit, 3),
        'recall': recall
    }


