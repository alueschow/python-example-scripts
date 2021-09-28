# !/usr/bin/python
# -*- coding: utf-8 -*-

"""Download obsolete IDs from the CERL Thesaurus."""

import json
import os

from cerl import ample_query, ample_record, ids_from_result, by_dot, the


DB = "data.cerl.org/thesaurus"
ENCODING = "utf-8"


def get(i="./input", o="./data/obsolete_ids.json", t=25):
    """Collect obsolete IDs for a given list of CERL Thesaurus IDs only if an ID occurs more than `t` times.

    :param i: Input folder with JSON files. Files have to be in this format:
        ```
        {
            "CERL ID": Number of occurrences,
            "Another CERL ID": Number of occurrences,
            ...
        }
        ```
    :type i: ```str```
    :param o: Path to output JSON file
    :type o: ```str```
    :param t: Threshold of occurrences; default is 25
    :type t: ```int```
    """
    # create the directory o if it does not already exist
    if not os.path.exists(os.path.dirname(o)):
        os.makedirs(os.path.dirname(o))

    download_data = {}  # a python dictionary that will contain the data we collect

    # iterate over files in input folder
    for file in os.listdir(i):
        # load input file
        with open(os.path.join(i, file), "r", encoding=ENCODING) as f:
            data = json.load(f)

        # get obsolete IDS for each given CERL Thesaurus ID
        for record_id in data.keys():
            if data[record_id] >= t:

                query = f"_id:({record_id})"  # CERL Thesaurus query

                # Connect to the CERL Thesaurus and run the search query
                result = ample_query(DB, query)

                # iterate over the search results
                for idx in ids_from_result(result):
                    record = ample_record(DB, idx)  # get the record as a python dictionary
                    cid = the(by_dot(record, '_id'))  # access the record by dot notation
                    assert cid == idx  # just to make sure the correct record was downloaded

                    if cid not in download_data.keys():
                        download_data[cid] = []

                        for _id in by_dot(record, "data.previousId"):
                            download_data[cid] = _id

                        if len(download_data[cid]) == 0:
                            del download_data[cid]

    # save data
    with open(o, "w", encoding=ENCODING) as f:
        json.dump(download_data, f, indent=4)


if __name__ == "__main__":
    get()
