# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Convert coordinates from degrees-minutes-seconds format to decimal format."""

import csv
import pandas as pd


def dms_dd(degrees, minutes, seconds):
    return degrees + minutes/60.0 + seconds/3600.0


def get_coordinates(row, col):
    _data = str(row[col])    
    if _data != "nan":
        _d = _data.split(split_char)[0]
        decimal = dms_dd(
            int(_d[1:4]),
            int(_d[4:6]),
            int(_d[6:8])
            )
        decimal = round(decimal, 4)
        if _d[0] == "w" or _d[0] == "s":
            decimal = decimal * -1
        return decimal
    return None


# Configuration
ENCODING = "utf-8"
CSV_SEP = "\t"

infile = "./metadata-networks/cerl-thesaurus/source/locations.csv"
outfile = "./metadata-networks/cerl-thesaurus/data/lng_lat.csv"

split_char = " ### "

city = "215$a"
obs_id = "035$z"  # obsolete record identifiers
lng = "123$d"  # westernmost longitude
# lng = "123$e"  # easternmost longitude (not needed, identical to subfield $d)
lat = "123$f"  # northernmost latitude
# lat = "123$g"  # southernmost latitude  (not needed, identical to subfield $f)

OUTPUT_HEADER = ['id', 'city', 'lng', 'lat']
outdata = []  # collect data here

# read input file
with open(infile, "r", encoding=ENCODING) as f:
    df = pd.read_csv(f, sep=CSV_SEP)

# get longitutde/latitude data and convert it
for i, row in df.iterrows():
    name = str(row[city]).split(split_char)[0]
    i_lng = get_coordinates(row, lng)
    i_lat = get_coordinates(row, lat)
    if i_lng and i_lat:
        outdata.append((row["id"], name, i_lng, i_lat))

# save to file
with open(outfile, "w", encoding=ENCODING, newline="") as f:
    csv_out = csv.writer(f, delimiter=CSV_SEP)
    csv_out.writerow(OUTPUT_HEADER)
    for row in outdata:
        csv_out.writerow(row)
