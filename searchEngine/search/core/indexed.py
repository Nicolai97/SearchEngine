import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
import sys
import re
import xml.etree.ElementTree as ET

def createSearchableData():   
    schema = Schema(title = TEXT(stored = True), ID = ID(stored = True), url = TEXT(stored = True), textdata = TEXT(stored = True))
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")

    ix = create_in("indexdir",schema)
    writer = ix.writer()
 

    path = '/Users/nicolaiosalchuk/Sviluppo/gestione_info/wiki_dump/dump_900.xml'
    root = ET.parse(path)
    xml_data = {}
    for item in root.iter():
        if item.tag == 'root':
            next
        elif item.tag == 'row' and len(xml_data) > 0:
            writer.add_document(title=xml_data['title'], ID=xml_data['id'], url=xml_data['url'], textdata=xml_data['text'])
            xml_data = {}
        else:
            xml_data[item.tag] = item.text

    writer.commit()
 

#createSearchableData()