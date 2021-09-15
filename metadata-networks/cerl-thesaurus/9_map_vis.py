# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Visualize networks on a map."""

import os

from bibliometa_vis.visualization import Map

# input and output files
SHAPEFILE = (f"./metadata-networks/cerl-thesaurus/data/shapefiles/"
             f"ref-nuts-2021-20m.shp/NUTS_RG_20M_2021_4326_LEVL_0.shp/NUTS_RG_20M_2021_4326_LEVL_0.shp")
SHAPEFILE_COLOR = "orange"
O = "./metadata-networks/cerl-thesaurus/data/output/map_img/"
DEGREES = "./metadata-networks/cerl-thesaurus/data/output/degrees/"
COORDINATES = "./metadata-networks/cerl-thesaurus/data/lng_lat.csv"
COORDINATES_SEP = "\t"
GRAPH_CORPUS_PATH = "./metadata-networks/cerl-thesaurus/data/output/graph_corpus/graph_corpus_people_"
GRAPHML_FOLDER = "./metadata-networks/cerl-thesaurus/data/output/graphml/"
LOG_PATH = "./metadata-networks/cerl-thesaurus/data/logs/map_"

# type of nodes in graph
COMPONENTS = True
ALL_NODES = True
SINGLETONS = False

# analysis settings
KEYS_LABELS = ("id", "city")
TYPES = [
    "scatter",
    "cities",
    "degrees",
    "map"
]
# OUTPUT_FORMATS = ("png", "jpg", "pdf", "svg")
OUTPUT_FORMATS = ["png"]

# figure settings
MAP_EXTENT = [5.5, 15.5, 47.2, 55.3]  # approx. Germany
# MAP_EXTENT = [-5, 25, 40, 57]  # approx. Europe
FIGSIZE = (60, 60)
FONTSIZE = 4
MAX_FONTSIZE = 6
EDGE_WIDTH = .1

# start visualization
m = Map()
for root, dirs, files in os.walk(os.path.dirname(GRAPHML_FOLDER)):
    for file in files:
        filename = os.path.splitext(file)[0]
        m.set_config(graphml=root + os.sep + file,
                     o=O,
                     o_formats=OUTPUT_FORMATS,
                     degrees=DEGREES,
                     log=f"{LOG_PATH}{filename}.out",
                     types=TYPES,
                     shapefile=SHAPEFILE,
                     shapefile_color=SHAPEFILE_COLOR,
                     coordinates=COORDINATES,
                     coordinates_sep=COORDINATES_SEP,
                     keys_labels=KEYS_LABELS,
                     map_extent=MAP_EXTENT,
                     graph_corpus=f"{GRAPH_CORPUS_PATH}{filename.split('_')[2].split('.')[0]}.json",
                     components=COMPONENTS,
                     all_nodes=ALL_NODES,
                     singletons=SINGLETONS,
                     name=filename,
                     figsize=FIGSIZE,
                     fontsize=FONTSIZE,
                     max_fontsize=MAX_FONTSIZE,
                     edge_width=EDGE_WIDTH,
                     verbose=False
                     )
        m.start()
