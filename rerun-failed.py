import http.client
import os

pipeline_id = os.environ['PIPELINE_ID']

conn = http.client.HTTPSConnection("circleci.com")

headers = { 'authorization': "Circle-Token: $CIRCLE_TOKEN" }

conn.request("GET", "/api/v2/pipeline/{}/workflow".format(pipeline_id), headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

print("Pipeline ID is: {}".format(pipeline_id))