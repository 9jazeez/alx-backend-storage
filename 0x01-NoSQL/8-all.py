#!/usr/bin/env python3
""" List all documents in a collection of a mongo database """

def list_all(mongo_collection):
	"""Function that list doc"""
	docs = []
	for doc in mongo_collection.find():
		docs.append(doc)
	return (docs)

