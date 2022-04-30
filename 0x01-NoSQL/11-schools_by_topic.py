#!/usr/bin/env python3
""" Query a mongo database using pymongo """

def schools_by_topic(mongo_collection, topic):
	""" Function that takes in a mongo collection
	and a match string for query.
	Returns the list of school having match """

	return mongo_collection.find({ "topics": topic})
