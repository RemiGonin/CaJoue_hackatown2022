import requests
import json
import sql_app.schemas as schemas

def populate_db(file):
    with open(file, 'r') as f:
        data = json.load(f)
    for arr in data:
        patinoires = arr.get("patinoires")
        for patinoire in patinoires:
            if not (patinoire.get("lat") == None or patinoire.get("lng") == None):
                request = json.dumps(dict(schemas.PatinoireCreate(**patinoire)))
                response = requests.post('http://127.0.0.1:8000/patinoires', data=request)

populate_db('patinoires.json')