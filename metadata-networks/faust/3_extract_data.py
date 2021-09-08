# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Extract values from original data."""

from polymatheia_tools.extraction import ValueExtraction

input_folder = "./metadata-networks/faust/data/sru-picaxml"
output_folder = "./metadata-networks/faust/data/polymatheia-tools/"
extracted_values = f"{output_folder}extracted_values/values"
fields = {
    "021A": ["a"],
    "022A": ["9"]
}
subfields = {
    "003@": ["0"],
    "021A": ["a"],
    "022A": ["9"]
}
ppn_field = "003@"
ValueExtraction(i=input_folder, o=extracted_values, fields=fields, subfields=subfields, ppn_field=ppn_field).start()

# Merge value extraction results into a single dict
extracted_values_folder = f"{output_folder}extracted_values"
data_corpus = "../../data_corpus.json"
ValueExtraction.merge(p=extracted_values_folder, o=data_corpus)
