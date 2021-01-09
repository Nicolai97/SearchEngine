import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.analysis import StemmingAnalyzer
from whoosh.index import open_dir
import sys
import re
import xml.etree.ElementTree as ET
from os.path import relpath

def createSearchableData():   
    stem_ana = StemmingAnalyzer()
    schema = Schema(title = TEXT(stored = True, analyzer=stem_ana), ID = ID(stored = True), url = TEXT(stored = True), textdata = TEXT(stored = True, analyzer= stem_ana))
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")

    ix = create_in("indexdir",schema)
    writer = ix.writer()
 

    path = os.path.relpath("/searchEngine/search/core/dump/dump_900.xml",start="/")
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
 

createSearchableData()