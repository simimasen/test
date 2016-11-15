# -*- coding: utf-8 -*-
# those are just fake data
import json
from pprint import pprint

'''
    bbc _data is a sample get from bbc database
'''
with open('bbc_data.json') as bbc_data:
    bbc_json = json.load(bbc_data)
#pprint(bbc_json['name'])
#pprint(bbc_json['ingredients'])


with open('healthy_data.json') as healthy_data:
    healthy_json = json.load(healthy_data)
#pprint(healthy_json['ingredients'])
