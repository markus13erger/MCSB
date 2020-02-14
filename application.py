#!/usr/bin/env python
# coding: utf-8

# In[14]:


from rdflib import URIRef, BNode, Literal, Namespace, Graph
from rdflib.namespace import RDF, FOAF


# In[24]:


# application.py
# Import the argparse library
import argparse

import os
import sys

# Create the parser
parser = argparse.ArgumentParser(description='Query your Google and Spotify data.')

# Add the arguments
#parser.add_argument('Path',
#                       metavar='path',
#                       type=str,
#                       help='the path to list')

parser.add_argument('File',
                    metavar='file',
                    type=str,
                    help='input the path of the RDF file')

parser.add_argument('Query',
                    metavar='query',
                    type=str,
                    help='choose either "song" (all songs from artist listened to) or "time" (time listened to artist)')

parser.add_argument('Artist',
                    metavar='artist',
                    type=str,
                    help='choose artist you listened to (spaces are "+") or "all"')

# Execute the parse_args() method
args = parser.parse_args()

# Input to variables
path = args.File
whichQuery = args.Query
artist = args.Artist

if whichQuery == 'song':
    if artist == 'all':
        # Initialize RDF data
        g = Graph()
        g.parse(path, format="xml")
        
        # Songs from artist
        query = ("""
            SELECT ?title
            WHERE {
                ?a foaf:performs ?s .
                ?s foaf:title ?title .
                }
                """)
        qres = g.query(query)
        
        print("Songs you listened to from all artists:")
        for row in qres:
            print("%s" % row)
        
    else:
        # Initialize RDF data
        g = Graph()
        g.parse(path, format="xml")
        
        # Songs from artist
        query = ("""
            SELECT ?title
            WHERE {
                ?a foaf:performs ?s .
                ?s foaf:title ?title .
                ?a foaf:name "%s" .
                }
                """ % artist)
        qres = g.query(query)
        
        print("Songs you listened to from %s:" % artist)
        for row in qres:
            print("%s" % row)
        
        
elif whichQuery == 'time':
    if artist == 'all':
        # Initialize RDF data
        g = Graph()
        g.parse(path, format="xml")
        
        # User listened how long to a song
        query = ("""
            SELECT DISTINCT ?time ?name 
            WHERE {
                ?artist foaf:performs ?song .
                ?artist rdf:type ?Artist .
                ?song rdf:type ?Song .
                ?markus foaf:artist_listened ?artist.
                ?artist foaf:artist_ms ?time .
                ?song foaf:title ?title .
                ?artist foaf:name ?name .
                }
                """)
        
        qres = g.query(query)
        
        print("Listened to songs of all artists for:")
        for row in qres:
            print("%s milliseconds listened to %s" % row)
            
    else:
        # Initialize RDF data
        g = Graph()
        g.parse(path, format="xml")
        
        # User listened how long to a song
        query = ("""
            SELECT DISTINCT ?time ?name
            WHERE {
                ?artist foaf:performs ?song .
                ?artist rdf:type ?Artist .
                ?song rdf:type ?Song .
                ?markus foaf:artist_listened ?artist.
                ?artist foaf:artist_ms ?time .
                ?song foaf:title ?title .
                ?artist foaf:name "%s" .
                }
                """ % artist)
        
        qres = g.query(query)
        
        print("Listened to songs of %s for:" % artist)
        for row in qres:
            print("%s milliseconds" % row[0])
            
else:
    print('Wrong query selected, please choose either "song" or "time"')

