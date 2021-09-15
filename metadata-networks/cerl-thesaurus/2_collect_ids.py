# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Map multiple IDs for a place to the single (main/correct) ID."""

import csv
import pandas as pd

INFILE = "./metadata-networks/cerl-thesaurus/source/locations.csv"
ID_MAPPING_FILE = "./metadata-networks/cerl-thesaurus/data/id_mapping.csv"
MAIN_ID_HEADER = 'main_id'
OTHER_ID_HEADER = 'other_id'
MAPPING_FILE_HEADER = [MAIN_ID_HEADER, OTHER_ID_HEADER]

SPLIT_CHAR = " ### "
OBS_ID = "035$z"  # obsolete record identifiers
ID_COL = "id"  # column name of input IDs
CSV_SEP = "\t"
ENCODING = "utf-8"

outdata = []  # collect ID mappings here

# read input file
with open(INFILE, "r", encoding=ENCODING) as f:
    df = pd.read_csv(f, sep=CSV_SEP)
    
# collect different IDs for each place, if available
for i, row in df.iterrows():
    _ids = str(row[OBS_ID])
    if _ids != "nan":
        for alt_i in _ids.split(SPLIT_CHAR):
            if len(alt_i.strip()) > 0:
                outdata.append((row[ID_COL], alt_i.strip()))

# make sure that no duplicates are in the data
assert len(outdata) == len(set(outdata))

# save mapping to file
with open(ID_MAPPING_FILE, "w", encoding=ENCODING, newline="") as f:
    csv_out = csv.writer(f, delimiter=CSV_SEP)
    csv_out.writerow(MAPPING_FILE_HEADER)
    for row in outdata:
        csv_out.writerow(row)

# make sure that no wrong ID information is in the data
# i.e., that each ID can have only one main "correct" id
with open(ID_MAPPING_FILE, "r", encoding=ENCODING) as f:
    df_orig = pd.read_csv(f, sep=CSV_SEP)

df = df_orig[OTHER_ID_HEADER]
df = df[df.duplicated(keep=False)]
duplicates = set(df.values)

if len(duplicates) > 0:
    # list all values in OTHER_ID_HEADER column that appear more than once
    print(f"Duplicate IDs: {duplicates}")
    for dup in duplicates:
        print(f"Probably duplicate records: {df_orig[df_orig[OTHER_ID_HEADER] == dup][MAIN_ID_HEADER].values}")
else:
    print("No duplicates found!")
