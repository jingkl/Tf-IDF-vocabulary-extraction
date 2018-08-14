'''
Created on 26 Jul 2018

@author: goksukara
'''
#!/usr/bin/env python
from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader
import json
import bz2
from numpy import record
baseurl='http://broker10.fcla.edu/cgi/b/broker20/broker20?'
savedic='/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/Data/Corpus.csv '

if __name__ == "__main__":
   
    url = baseurl
    registry = MetadataRegistry()
    registry.registerReader('oai_dc', oai_dc_reader)
    client = Client(url, registry)
    record = client.listSets()
    for word in record:
        print(word)
    #Write to file
    #with bz2.BZ2File('out.json', 'wb') as outfile:
    with open(savedic, 'a') as outfile:
         for record in client.listRecords(metadataPrefix='oai_dc',set='physics:math-ph'):
             header, metadata, _ = record
             doc = {}
             #Extract identifier
             doc["id"] = header.identifier()
             #Extract title and other metadata
             doc["title"] = "\n".join(metadata["title"])
             doc["abstract"] = "\n".join(metadata["description"])
             doc["authors"] = metadata["creator"]
             
             #Write into outfile
             #print(doc)
             #json.dump(doc,outfile)
             #outfile.write(jsonsave)
             #outfile.write("\n")
             print("Wrote %s" % doc["id"])