# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Example scripts that illustrate the use of polymatheia-tools."""

from polymatheia_tools.analysis import PICAAnalysis
from polymatheia_tools.extraction import ValueExtraction
from polymatheia_tools.utils import DictUtils, PolymatheiaUtils
from polymatheia_tools.visualization import FieldVisualization

DEMO_FOLDER = "./metadata/data/"
OUTPUT_FOLDER = f"{DEMO_FOLDER}polymatheia-tools/"

# Extract polymatheia files into a flat hierarchy
input_folder = f"{DEMO_FOLDER}sru-picaxml"
extracted_folder = f"{DEMO_FOLDER}sru_extracted"
PolymatheiaUtils.extract(i=input_folder, o=extracted_folder, e="xml")

# Analyse files from a folder
field_analysis = f"{OUTPUT_FOLDER}field_analysis.json"
PICAAnalysis(i=input_folder, o=field_analysis).start()

# Remove unneeded keys
filtered_dict = f"{OUTPUT_FOLDER}field_analysis_filtered.json"
DictUtils.remove_keys(i=field_analysis, o=filtered_dict, k=['044A', '044K'])

# Visualize relevant keys
visualization = f"{OUTPUT_FOLDER}field_visualization.png"
FieldVisualization.start(i=filtered_dict, o=visualization)

# Extract information from original files
extracted_values = f"{OUTPUT_FOLDER}extracted_values/values"
fields = {
    "044A": ["a"],
    "044K": ["a"]
}
subfields = {
    "003@": ["0"],
    "044A": ["A", "B", "N", "S", "a", "b", "c", "d", "e", "f", "g", "h", "k", "l", "n", "p", "q", "s", "t", "v",
             "x", "y", "z"],
    "044K": ["2", "3", "6", "7", "9", "A", "C", "D", "E", "F", "G", "L", "M", "N", "P", "V", "W", "Y", "Z", "a",
             "c", "f", "g", "n", "p", "w", "x", "z"]
}
ppn_field = "003@"
ValueExtraction(i=input_folder, o=extracted_values, fields=fields, subfields=subfields, ppn_field=ppn_field).start()

# Merge value extraction results into a single dict
extracted_values_folder = f"{OUTPUT_FOLDER}extracted_values"
data_corpus = "data_corpus.json"
ValueExtraction.merge(p=extracted_values_folder, o=data_corpus)

