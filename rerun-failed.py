import http.client

conn = http.client.HTTPSConnection("circleci.com")



headers = { 'authorization': "Circle-Token: $CIRCLE_TOKEN" }

conn.request("GET", "/api/v2/pipeline/{$PIPELINE_ID}/workflow", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

print("{$PIPELINE_ID}")