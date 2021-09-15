# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Add node labels to Gephi node spreadsheet."""

import pandas as pd

# Configuration
ENCODING = "utf-8"

INPUT_FILE = "./metadata-networks/cerl-thesaurus/data/gephi_nodes.csv"
OUTPUT_FILE = "./metadata-networks/cerl-thesaurus/data/gephi_nodes_labeled.csv"
DATA = "./metadata-networks/cerl-thesaurus/source/locations.csv"
CSV_SEP = "\t"

REMOVE_COL = ["035$z", "123$d", "123$e", "123$f", "123$g"]

# read data
with open(DATA, "r", encoding=ENCODING) as f:
    data = pd.read_csv(f, sep="\t")

# remove unneeded columns
for c in REMOVE_COL:
    del data[c]

# read nodes and labels
with open(INPUT_FILE, "r", encoding=ENCODING) as f:
    df = pd.read_csv(f, sep=CSV_SEP)

# map labels from data to node file
df_new = pd.merge(df, data, left_on=['Id'], right_on=['id'], how='left')

del df_new["Label"]
del df_new["id"]

df_new[['Label', 'XYZ']] = df_new["215$a"].str.split(" ### ", 1, expand=True)

del df_new["XYZ"]
del df_new["215$a"]

# save DataFrame
with open(OUTPUT_FILE, "w", encoding=ENCODING) as f:
    df_new.to_csv(f, sep=CSV_SEP, index=False)
