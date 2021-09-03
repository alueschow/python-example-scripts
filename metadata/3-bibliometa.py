# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Docstring."""

from bibliometa.graph.analysis import GraphAnalysis
from bibliometa.graph.conversion import JSON2EdgeList
from bibliometa.graph.similarity import Similarity

PATH = "./metadata/data/bibliometa/"

# conversion from JSON to edge list
j2e = JSON2EdgeList()

j2e.config.i = "./metadata/data/polymatheia-tools/extracted_values/data_corpus.json"
j2e.config.o = f"{PATH}similarity.csv"
j2e.config.create_corpus = True
j2e.config.corpus = f"{PATH}graph_corpus.json"
j2e.config.log = f"{PATH}json2edgelist.out"
j2e.config.sim_functions = [
    {"name": "mint_1",
     "function": Similarity.Functions.mint,
     "args": {
         "f": lambda a, b: len(list(a.intersection(b))),
         "t": 1}
     }
]
j2e.config.fields = [("044A", "a"), ("044K", "a")]

j2e.start()

# graph analysis
ga = GraphAnalysis()

ga.config.i = f"{PATH}similarity.tar.gz"
ga.config.o = f"{PATH}graph_analysis.txt"
ga.config.img = f"{PATH}img/"
ga.config.n = "documents"
ga.config.e = "keywords"
ga.config.sim = "mint_1"
ga.config.sim_functions = ["mint_1"]
ga.config.weighted = True
ga.config.t = 0  # threshold
ga.config.log = f"{PATH}graph_analysis.out"
ga.config.types = ['node_count', 'edge_count', 'component_count', 'max_component', 'avg_degree', 'degree_distribution']
ga.config.create_graphml = True
ga.config.graphml = f"{PATH}graphml/"

ga.start()
