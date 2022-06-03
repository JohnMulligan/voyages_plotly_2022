import requests
import json
from app_secrets import *

def main():

	print("+++FETCHING GEO+++")
	data={"hierarchical":"False"}
	r=requests.post(base_url+"geo/",data=data,headers=headers)
	flatgeo=json.loads(r.text)
	print("+++GEO FETCHED+++")
	
	
	type_prefixes={'place':'','region':'region__','broad_region':'region__broad_region__'}
	geo_codes={}
	default_geocode=0
	
	geo_codes[default_geocode]={
		"type": "Feature",
		"geometry": {
			"type": "Point",
			"coordinates": [0,0]
		},
		"properties": {
			"name":"Unknown",
			"id":default_geocode
		}
	}
	
	for i in flatgeo:
		for tp in type_prefixes:
			prefix=''
			geocode=i[prefix+'id']
			if geocode is None:
				geocode=default_geocode
			loc_type=i['location_type__name']
		
			longitude=i[prefix+'longitude']
			latitude=i[prefix+'latitude']
			if latitude is None:
				latitude=0
			if longitude is None:
				longitude=0
			latitude=float(latitude)
			longitude=float(longitude)
			
			d={
				"type": "Feature",
				"geometry": {
					"type": "Point",
					"coordinates": [longitude,latitude]
				},
				"properties": {
					"class":tp,
					tp:loc_type,
					"name":i['name'],
					"id":i['id']
				}
			}
			for k in [j for j in i if j.startswith(prefix+"show_on")]:
				d['properties'][k]=i[k]
			geo_codes[geocode]=d



	return geo_codes
	
if __name__=="__main__":
	geocodes=main()
	d=open("geocodes.json","w")
	d.write(json.dumps(geocodes))
	d.close()