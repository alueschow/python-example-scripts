# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Analyze fields in the downloaded data."""

from polymatheia_tools.analysis import PICAAnalysis
from polymatheia_tools.utils import DictUtils, PolymatheiaUtils
from polymatheia_tools.visualization import FieldVisualization

INPUT = "./metadata-networks/faust/data/"
OUTPUT_FOLDER = f"{INPUT}polymatheia-tools/"

# Extract polymatheia files into a flat hierarchy
input_folder = f"{INPUT}sru-picaxml"
extracted_folder = f"{INPUT}sru_extracted"
PolymatheiaUtils.extract(i=input_folder, o=extracted_folder, e="xml")

# Analyse files from a folder
field_analysis = f"{OUTPUT_FOLDER}field_analysis.json"
PICAAnalysis(i=extracted_folder, o=field_analysis).start()

# Remove unneeded keys
filtered_dict = f"{OUTPUT_FOLDER}field_analysis_filtered.json"
DictUtils.remove_keys(i=field_analysis, o=filtered_dict, k=['021A', '022A'])

# Visualize relevant keys
visualization = f"{OUTPUT_FOLDER}field_visualization.png"
FieldVisualization.start(i=filtered_dict, o=visualization)
