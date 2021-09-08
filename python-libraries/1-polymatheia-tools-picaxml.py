# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Example script for using Polymatheia-Tools, PICA-XML as record schema, and a PPN list instead of a search query."""

from polymatheia_tools.download.catalogue import CatalogueKeyDict
from polymatheia_tools.download.main import keys, main, schemas
from polymatheia_tools.download.sru_call import SRUCall

SRU_API = "http://sru.k10plus.de/gvk"

# Total number of results
total_number = SRUCall.get_total_number({"api": SRU_API, "query": "lorem ipsum"})
print(total_number)

# SRU download using a list of PPN
# Polymatheia does not support this, so we have to use the appropriate methods from Polymatheia-Tools instead
# Show available schemas
print(schemas(SRU_API))

PATH_TO_PPN_LIST = "./python-libraries/demo/ppn/list.txt"
PATH_TO_OUTPUT_FOLDER = "./python-libraries/data/sru-picaxml/"
RECORD_SCHEMA = "picaxml"

main(SRU_API, ppn=True, i=PATH_TO_PPN_LIST, o=PATH_TO_OUTPUT_FOLDER, s=RECORD_SCHEMA)

# SRU download using a custom query
# Show available SRU keys
print(keys(SRU_API))

_SW = CatalogueKeyDict(name="SW",  # name for this configuration
                       catalogue_keys=["pica.sw"],  # catalogue keys used
                       notations=["biologika"])  # values searched in the catalogue
CATALOGUE_KEYS = [_SW]
API = "https://sru.k10plus.de/opac-de-7"

main(API, query=CATALOGUE_KEYS, o=PATH_TO_OUTPUT_FOLDER, s=RECORD_SCHEMA)

