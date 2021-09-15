# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Convert CSV data from the CERL Thesaurus to a JSON format."""

from bibliometa.conversion import CSV2JSON

# CSV2JSON configuration
INPUT_FILE = "./metadata-networks/cerl-thesaurus/source/people.csv"
OUTPUT_FILE = f"./metadata-networks/cerl-thesaurus/data/output/json/people.json"
LOG = f"./metadata-networks/cerl-thesaurus/data/logs/csv2json.out"

YEARS = (1500, 1900)
STEP = 50
INTERVALS = (25, 25)

FIELDS = [
    {"content": ("515", "a"),
     "type": ("515", "0"),
     "categories": ["actv"]}  # i.e., only activity places are considered
]
DATE_INDICATOR = ["0", "1"]  # i.e., both biographical and activity dates are considered
DATEFIELD = ("340", "x")

# CSV2JSON conversion
c2j = CSV2JSON()
c2j.set_config(i=INPUT_FILE,
               o=OUTPUT_FILE,
               from_=YEARS[0],
               to=YEARS[1],
               step=STEP,
               fields=FIELDS,
               date_indicator=DATE_INDICATOR,
               datefield=DATEFIELD,
               interval_lower=INTERVALS[0],
               interval_upper=INTERVALS[1],
               log=LOG
               )
c2j.start()
