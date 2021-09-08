# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Download 'Faust' works from the GVK."""

from polymatheia_tools.download.catalogue import CatalogueKeyDict
from polymatheia_tools.download.main import main

SRU_API = "http://sru.k10plus.de/gvk"

output = "./metadata-networks/faust/data/sru-picaxml/"
schema = "picaxml"

_WORKS = CatalogueKeyDict(name="works",  # name for this configuration
                          catalogue_keys=["pica.wtp"],  # catalogue keys used
                          notations=["faust"])  # values searched for in the catalogue
CATALOGUE_KEYS = [_WORKS]

main(SRU_API, query=CATALOGUE_KEYS, o=output, s=schema)
