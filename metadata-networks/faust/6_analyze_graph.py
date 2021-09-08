# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Conduct graph analysis."""

from bibliometa.graph.analysis import GraphAnalysis

PATH = "./metadata-networks/faust/data/bibliometa/"

# graph analysis
ga = GraphAnalysis()

ga.config.i = f"{PATH}similarity.tar.gz"
ga.config.o = f"{PATH}graph_analysis.txt"
ga.config.img = f"{PATH}img/"
ga.config.n = "documents"
ga.config.e = "works"
ga.config.sim = "mint_1"
ga.config.sim_functions = ["iden", "mint_1"]
ga.config.weighted = True
ga.config.t = 0  # threshold
ga.config.log = f"{PATH}graph_analysis.out"
ga.config.create_graphml = True
ga.config.graphml = f"{PATH}graphml/"  # this file may be used with tools such as Gephi etc. for visualizing the graph

print(f"Graph analysis will create the following: {ga.config.types}")

ga.start()
