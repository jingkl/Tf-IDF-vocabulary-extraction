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
baseurl='http://cogprints.ecs.soton.ac.uk/perl/oai2?'
extantionurl=''

if __name__ == "__main__":
   
    url = baseurl+extantionurl
    registry = MetadataRegistry()
    registry.registerReader('oai_dc', oai_dc_reader)
    client = Client(url, registry)
    record = client.listSets()
    for word in record:
        print(word)
    #Write to file
    #with bz2.BZ2File('out.json', 'wb') as outfile:
    with open('data.txt', 'w') as outfile:
         for record in client.listRecords(metadataPrefix='oai_dc',set='econ'):
             header, metadata, _ = record
             doc = {}
             #Extract identifier
             doc["id"] = header.identifier()
             #Extract title and other metadata
             doc["title"] = "\n".join(metadata["title"])
             doc["abstract"] = "\n".join(metadata["description"])
             doc["authors"] = metadata["creator"]
             #Write into outfile
             print(doc)
             #json.dump(doc,outfile)
             #outfile.write(jsonsave)
             #outfile.write("\n")
             print("Wrote %s" % doc["id"])
