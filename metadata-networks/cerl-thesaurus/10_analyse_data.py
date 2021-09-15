# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Run a few statistics on the processed data."""

import json
import os

ENCODING = "utf-8"

# count unique people records actually extracted from original data
path = "./metadata-networks/cerl-thesaurus/data/output/json/"
keys = []

for file in os.listdir(path):
    print(file)
    with open(os.path.join(path, file), "r", encoding="utf-8") as f:
        data = json.load(f)
    for e in data.keys():
        keys.append(e)

# count unique place records actually used in graph corpus
path = "./metadata-networks/cerl-thesaurus/data/output/graph_corpus/"
pl_keys = []

for file in os.listdir(path):
    print(file)
    with open(os.path.join(path, file), "r", encoding=ENCODING) as f:
        data = json.load(f)
    for e in data.keys():
        pl_keys.append(e)

print(f"Number of unique people records with activity information: {len(set(keys))}")
print(f"Number of unique place records: {len(set(pl_keys))}")
