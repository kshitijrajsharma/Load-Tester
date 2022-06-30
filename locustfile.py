import time, json
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(3, 5)

    @task(1)
    def raw_data_request(self):
        payload = {
            'geometry': {
        "type": "Polygon",
        "coordinates": [
          [
            [
              85.21270751953125,
              27.646431146293423
            ],
            [
              85.49629211425781,
              27.646431146293423
            ],
            [
              85.49629211425781,
              27.762545086827302
            ],
            [
              85.21270751953125,
              27.762545086827302
            ],
            [
              85.21270751953125,
              27.646431146293423
            ]
          ]
        ]
      }
        }
        
        headers = {'content-type': 'application/json'}
        
        response = self.client.post("/raw-data/current-snapshot/", data=json.dumps(payload), headers=headers)