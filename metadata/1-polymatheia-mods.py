# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Example script for using Polymatheia and the MODS record schema."""

from polymatheia.data.reader import SRUExplainRecordReader, SRURecordReader
from polymatheia.data.writer import XMLWriter

SRU_API = "http://sru.k10plus.de/gvk"
MAXIMUM_RECORDS = 10
QUERY = "lorem ipsum"
RECORD_SCHEMA = "mods"

# Get SRU Explain record using Polymatheia
reader = SRUExplainRecordReader(SRU_API)
print(reader.schemas)
print(reader.echo)
print(reader.echo.version)

# SRU Request using Polymatheia
reader = SRURecordReader(SRU_API,
                         query=QUERY,
                         max_records=MAXIMUM_RECORDS,
                         record_schema=RECORD_SCHEMA
                         )

print(SRURecordReader.result_count(SRU_API, QUERY))

for record in reader:
    try:
        print(record.zs_recordData["{http://www.loc.gov/mods/v3}mods"].titleInfo.title._text)
    except:
        pass

# write files to disk using Polymatheia
OUTPUT_PATH = "./metadata/data/sru-mods/"
w = XMLWriter(OUTPUT_PATH,
               ["zs_recordData", "{http://www.loc.gov/mods/v3}mods", "recordInfo", "recordIdentifier", "_text"])
w.write(reader)
