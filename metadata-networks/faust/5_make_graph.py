# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Create edge list representation of the data."""

from bibliometa.graph.conversion import JSON2EdgeList
from bibliometa.graph.similarity import Similarity

PATH = "./metadata-networks/faust/data/bibliometa/"

# conversion from JSON to edge list
j2e = JSON2EdgeList()

j2e.config.i = "./metadata-networks/faust/data/corpus.json"
j2e.config.o = f"{PATH}similarity.csv"
j2e.config.create_corpus = True
j2e.config.corpus = f"{PATH}graph_corpus.json"
j2e.config.log = f"{PATH}json2edgelist.out"
j2e.config.sim_functions = [
    {"name": "iden",
     "function": Similarity.Functions.mint,
     "args": {
         "f": lambda a, b: a == b,
         "t": 1}
     },
    {"name": "mint_1",
     "function": Similarity.Functions.mint,
     "args": {
         "f": lambda a, b: len(a.intersection(b)),
         "t": 1}
     }
]
j2e.config.fields = [("022A", "9")]

j2e.start()
