# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Change keys in data corpus to have better labels in the next step."""

import json

INFILE = "./metadata-networks/faust/data/data_corpus.json"
OUTFILE = "./metadata-networks/faust/data/corpus.json"

ENCODING = "utf-8"


def _clean(a):
    a = a.lower()[:50]
    a = a.replace("ü", "ue")
    a = a.replace("ö", "oe")
    a = a.replace("ä", "ae")
    a = a.replace("ß", "ss")
    a = a.replace("@", "")
    a = a.replace("&", "u")
    a = a.replace(" und ", " u ")
    a = a.replace(" and ", " u ")
    return a


def _get(corpus, key, a, b):
    try:
        x = corpus[key][a][b]
    except:
        x = ["x"]

    return x


def main():
    with open(INFILE, 'r', encoding=ENCODING) as f:
        corpus = json.loads(f.read())

    newdict = {}
    for key in corpus.keys():
        titel = _get(corpus, key, "021A", "a")
        label = _clean(str(titel[0][:50])) + "_" + str(key)

        # fill dictionary template
        newdict[label] = corpus[key]

    with open(OUTFILE, 'w', encoding=ENCODING) as f:
        json.dump(newdict, f, indent=4)


if __name__ == "__main__":
    main()
