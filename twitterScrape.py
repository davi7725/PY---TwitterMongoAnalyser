#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from pymongo import MongoClient

from pprint import pprint

client = MongoClient("URL_TO_MONGODB")
db=client.twitter
db.tweets.remove({})

with open('NAME_OF_CSV_FILE','r',encoding='utf-8', errors='ignore') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		tweet = {
			"polarity":int(row[0]),
			"_id":int(row[1]),
			"date":str(row[2]),
			"query":str(row[3]),
			"user":str(row[4]),
			"content":str(row[5])
		}
		db.tweets.insert_one(tweet)
	print ("done");

def ppall(col):
	for p in col:
		print(p)

print("\n\n\n1 - How many Twitter users are in the database?\n")
print(len(db.tweets.distinct('user')))

print("\n\n\n2 - Which Twitter users link the most to other Twitter users? (Provide the top ten.)\n")
ppall(db.tweets.aggregate([{ "$match": {"content": { "$regex": '@(?:[a-z][a-z0-9_]*)' }}},{"$group": {"_id": "$user","count": {"$sum": 1}}}, {"$sort": {"count": -1}},{"$limit": 10}]))

print("\n\n\n3 - Who are the most mentioned Twitter users? (Provide the top five.)\n")
ppall(db.tweets.aggregate([{ "$match": { "content": { "$regex": '@(?:[a-z][a-z0-9_]*)' } } },{ "$group": { "_id": {"$substrCP": [ "$content", { "$indexOfCP": [ "$content", "@" ] },{ "$indexOfCP": [ "$content", " " ] }]},"count": {"$sum": 1}}}, {"$sort": {"count": -1}},{"$limit": 6}]))

print("\n\n\n4 - Who are the most active Twitter users (top ten)?\n")
ppall(db.tweets.aggregate([{"$group" : { "_id" : "$user", "count" : {"$sum" : 1}}}, {"$sort": {"count": -1}},{"$limit": 10}]))


print("\n\n\n5 - Who are the five most grumpy (most negative tweets)?\n")
ppall(db.tweets.aggregate([ { "$match": {"polarity": 0}}, { "$group": {"_id": "$user","count": {"$sum": 1}}},{"$sort": {"count": -1}},{"$limit": 5}]))
print("\n\n\n5 - And the most happy (most positive tweets)?\n")
ppall(db.tweets.aggregate([ { "$match": {"polarity": 4}}, { "$group": {"_id": "$user","count": {"$sum": 1}}},{"$sort": {"count": -1}},{"$limit": 5}]))