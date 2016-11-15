import json
import dataset as data

#print(data.bbc_data)
bbc_data = data.bbc_json
print(bbc_data['name'])
print(bbc_data['ingredients'])

healthy_data = data.healthy_json
print(healthy_data['name'])
print(healthy_data['ingredients'])

'''
    use bbc data's ingredients to search match on healthy food dataset
'''
