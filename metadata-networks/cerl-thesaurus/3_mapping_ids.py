# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Normalize mapping IDs in input JSON data."""

import copy
import json
import os
import pandas as pd

from tqdm import tqdm

INPUT_FOLDER = f"./metadata-networks/cerl-thesaurus/data/output/json/"
OUTPUT_FOLDER = f"./metadata-networks/cerl-thesaurus/data/output/mapped/"

if not os.path.exists(os.path.dirname(OUTPUT_FOLDER)):
    os.makedirs(OUTPUT_FOLDER)

id_mapping_file = "./metadata-networks/cerl-thesaurus/data/id_mapping.csv"

# read ID mapping
with open(id_mapping_file, "r", encoding="utf-8") as f:
    mapping = pd.read_csv(f, sep="\t")

with tqdm(total=len(os.listdir(INPUT_FOLDER))) as progressbar:
    for file in os.listdir(INPUT_FOLDER):
        with open(os.path.join(INPUT_FOLDER, file), "r", encoding="utf-8") as f:
            data = json.loads(f.read())

        data_copy = copy.deepcopy(data)

        for key in data.keys():
            locations = data[key]["515"]["a"]
            for lo in locations:
                if lo in mapping["other_id"].values:
                    try:
                        place_id = mapping[mapping["other_id"] == lo]["main_id"].item()
                    except Exception as e:
                        print()
                        print(e)
                        print(file)
                        print(lo)
                    data_copy[key]["515"]["a"].append(place_id)
                    data_copy[key]["515"]["a"].remove(lo)

        with open(os.path.join(OUTPUT_FOLDER, file), "w", encoding="utf-8") as f:
            json.dump(data_copy, f, indent=4)
        progressbar.update()
