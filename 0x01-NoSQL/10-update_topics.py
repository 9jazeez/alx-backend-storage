#!/usr/bin/env python3
""" Using python function to update documents
on a mongo database """

def update_topics(mongo_collection, name, topics):
	""" Functions takes in a collection and update
	the documents with march of name """
	
	val = mongo_collection.update_many({'name': name}, 
	     {"$set":{'name': name, 'topics':topics}})

