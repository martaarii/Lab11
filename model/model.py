from collections import defaultdict

from database.DAO import products_DAO, vendite_DAO
import networkx as nx

class Model:
    def __init__(self):

        self.grafo = nx.DiGraph()


    def get_all_color(self):
        return products_DAO.get_colori(products_DAO)

    def get_grafo(self, anno, colore):
        prodotti = products_DAO.get_prodotti_colori(products_DAO, colore)
        for prodotto in prodotti:
            self.grafo.add_node(prodotto.product_number)
        print(f"numero di prodotti trovati : {len(prodotti)}")
        vendite = vendite_DAO.get_vendite(vendite_DAO, colore, anno)

        vendite_giorno = defaultdict(list)

        for vendita in vendite:
            vendite_giorno[vendita.Date].append(vendita.Product_number)
        for data in vendite_giorno.keys():
            prodotti_list = vendite_giorno[data]
            for i in range(len(prodotti_list)):
                for j in range(i + 1, len(prodotti_list)):
                    p1 = prodotti_list[i]
                    p2 = prodotti_list[j]
                    if self.grafo.has_edge(p1, p2):
                        self.grafo[p1][p2]['weight'] += 1
                    else:
                        self.grafo.add_edge(p1, p2, weight=1)
    def num_vertici(self):
        print(self.grafo.nodes)
        return self.grafo.number_of_nodes()
    def num_archi(self):
        return self.grafo.number_of_edges()
