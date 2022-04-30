#!/usr/bin/env python3
"""Insert document into a collection """

def insert_school(mongo_collection, **kwargs):
	"""Function that inserts into a collection
    A document into a collection """

	val = mongo_collection.insert_one(kwargs)
	return (val.inserted_id)

