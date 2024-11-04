import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self.graph = nx.DiGraph()

        self._listChromosome = []
        self._listConnectedGenes = []
        self._listGenes = []
        self._idMap = {}

        self._listLocalizations = []
        self._listConnectedLocalizations = []

    def build_graph(self):
        self.graph.clear()
        self._nodes = DAO.getAllChromosomes()
        self.graph.add_nodes_from(self._nodes)

        self._edges = DAO.getAllConnectedGenes()
        for edge in self._edges:
            peso = edge[4]
            if edge[0] in self._nodes and edge[1] in self._nodes and edge[0] != edge[1]:
                if self.graph.has_edge(edge[0], edge[1]):
                    self.graph[edge[0]][edge[1]]['weight'] += peso
                else:
                    self.graph.add_edge(edge[0], edge[1], weight=peso)

    def count_edges(self, t):
        count_bigger = 0
        count_smaller = 0
        for x in self.get_edges():
            if x[2]['weight'] > t:
                count_bigger += 1
            elif x[2]['weight'] < t:
                count_smaller += 1
        return count_bigger, count_smaller

    def get_nodes(self):
        return self.graph.nodes()

    def get_edges(self):
        return list(self.graph.edges(data=True))

    def get_num_of_nodes(self):
        return self.graph.number_of_nodes()

    def get_num_of_edges(self):
        return self.graph.number_of_edges()

    def get_min_weight(self):
        return min([x[2]['weight'] for x in self.get_edges()])

    def get_max_weight(self):
        return max([x[2]['weight'] for x in self.get_edges()])
