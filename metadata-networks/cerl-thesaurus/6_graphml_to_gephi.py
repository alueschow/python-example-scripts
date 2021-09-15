# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Create nodes and edges spreadsheets for Gephi."""

import os

from bibliometa.configuration import Config
from bibliometa.graph.utils import load_graph

# Configuration
ENCODING = "utf-8"

CSV_NODES = "./metadata-networks/cerl-thesaurus/data/gephi_nodes.csv"
CSV_EDGES = "./metadata-networks/cerl-thesaurus/data/gephi_edges.csv"

GRAPHML_FOLDER = "./metadata-networks/cerl-thesaurus/data/output/graphml/"

string_nodes = "Id\tLabel\n"
string_edges = "Source\tTarget\tType\tLabel\tTimeset\tWeight\n"

nodes_list = []
edges = []
count = 0

for root, dirs, files in os.walk(os.path.dirname(GRAPHML_FOLDER)):
    for file in files:
        year = int(file.split("_")[2].split(".")[0])
        begin = f"{year}-01-01"
        end = f"{year+9}-12-31"
        print(year)

        g = load_graph(Config({"graphml": os.path.join(root, file)}), False)

        for e in g.edges(data=True):
            if e[0] not in nodes_list:
                nodes_list.append(e[0])
            if e[1] not in nodes_list:
                nodes_list.append(e[1])
            edge_row = f"{e[0]}\t{e[1]}\tundirected\t{count}\t{begin}\t{int(e[2]['weight'])}\n"
            string_edges += edge_row
            count += 1

for n in nodes_list:
    string_nodes += f"{n}\t{n}\n"

with open(CSV_NODES, "w", encoding=ENCODING) as f:
    f.write(string_nodes)

with open(CSV_EDGES, "w", encoding=ENCODING) as f:
    f.write(string_edges)
