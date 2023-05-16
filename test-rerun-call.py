import http.client
import os

circ_token = ""

circ_token = os.environ['CIRCLE_TOKEN']

conn = http.client.HTTPSConnection("circleci.com")

payload = "{\"enable_ssh\":false,\"from_failed\":true}"

headers = {
    'content-type': "application/json",
    'Circle-Token': circ_token
    }

wf_id = "1a356f9c-e9b5-4c31-a2f6-99c6e1a89bee"

conn.request("POST", "/api/v2/workflow/{}/rerun".format(wf_id), payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))