# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Run graph analysis."""

import os

from bibliometa.graph.analysis import GraphAnalysis

# GraphAnalysis configuration
INPUT_FOLDER = "./metadata-networks/cerl-thesaurus/data/output/similarity/"
OUTPUT_FOLDER = "./metadata-networks/cerl-thesaurus/data/output/graph_analysis/"
IMG_FOLDER = "./metadata-networks/cerl-thesaurus/data/output/img/"
GRAPHML_FOLDER = "./metadata-networks/cerl-thesaurus/data/output/graphml/"
LOG_PATH = "./metadata-networks/cerl-thesaurus/data/logs/ga_"

CREATE_GRAPHML = True

NODES = "cities"
EDGES = "similarity"
SIMILARITY_FUNCTION = "mint_1"
SIMILARITY_FUNCTIONS_ALL = ["mint_1"]
THRESHOLD = 0
WEIGHTED = True

TYPES = ["node_count",
         "edge_count",
         "component_count",
         "max_component",
         "avg_degree",
         "degree_distribution",
         "top_dc_nodes",
         "degree_centrality_distribution",
         "graph_clique_number",
         "number_of_cliques"]

ga = GraphAnalysis()

for root, dirs, files in os.walk(os.path.dirname(INPUT_FOLDER)):
    for file in files:
        if file.endswith(".tar.gz"):
            filename = os.path.splitext(file)[0]
            ga.set_config(i=root + os.sep + file,
                          o=f"{OUTPUT_FOLDER}{filename}.txt",
                          img=IMG_FOLDER,
                          create_graphml=CREATE_GRAPHML,
                          graphml=f"{GRAPHML_FOLDER}{filename}.graphml",
                          log=f"{LOG_PATH}{filename}.out",
                          n=NODES,
                          e=EDGES,
                          sim=SIMILARITY_FUNCTION,
                          sim_functions=SIMILARITY_FUNCTIONS_ALL,
                          t=THRESHOLD,
                          weighted=WEIGHTED,
                          types=TYPES
                          )
            ga.start()
