import http.client

conn = http.client.HTTPSConnection("circleci.com")



headers = { 'authorization': "Circle-Token: $CIRCLE_TOKEN" }

conn.request("GET", "/api/v2/pipeline/4d7c2311-8332-4c6e-97c9-fb92a93463d0/workflow", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))