import http.client

conn = http.client.HTTPSConnection("circleci.com")



headers = { 'authorization': "Circle-Token: $CIRCLE_TOKEN" }

conn.request("GET", "/api/v2/pipeline/{<< pipeline.id >>}/workflow", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))