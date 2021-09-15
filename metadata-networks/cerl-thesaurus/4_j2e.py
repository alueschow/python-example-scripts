# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Convert JSON to edge list."""

import os

from bibliometa.graph.conversion import JSON2EdgeList
from bibliometa.graph.similarity import Similarity

# JSON2EdgeList configuration
INPUT_FOLDER = "./metadata-networks/cerl-thesaurus/data/output/mapped/"
SIMILARITY_PATH = "./metadata-networks/cerl-thesaurus/data/output/similarity/similarity_"
GRAPH_CORPUS_PATH = "./metadata-networks/cerl-thesaurus/data/output/graph_corpus/graph_corpus_"
LOG_PATH = "./metadata-networks/cerl-thesaurus/data/logs/j2e_"
FIELDS = [("515", "a")]

CREATE_CORPUS = True
SWAP = True

SIM_FUNCTIONS = [
    {"name": "mint_1",
     "function": Similarity.Functions.mint,
     "args": {
         "f": lambda a, b: len(list(a.intersection(b))),
         "t": 1}
     },
    # {"name": "jacc",
    #  "function": Similarity.Functions.jaccard,
    #  "args": {
    #      "f": lambda a: round(a, 4),
    #      "t": 0}
    #  },
    # {"name": "ovlp",
    #  "function": Similarity.Functions.overlap,
    #  "args": {
    #      "f": lambda a: round(a, 4),
    #      "t": 0}
    #  },
]

j2e = JSON2EdgeList()

for root, dirs, files in os.walk(os.path.dirname(INPUT_FOLDER)):
    for file in files:
        filename = os.path.splitext(file)[0]
        j2e.set_config(i=root + os.sep + file,
                       o=f"{SIMILARITY_PATH}{filename}.csv",
                       create_corpus=CREATE_CORPUS,
                       corpus=f"{GRAPH_CORPUS_PATH}{filename}.json",
                       log=f"{LOG_PATH}{filename}.out",
                       fields=FIELDS,
                       sim_functions=SIM_FUNCTIONS,
                       swap=SWAP
                       )
        j2e.start()
