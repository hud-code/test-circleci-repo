import http.client
import os
import json
import sys

pipeline_id = ""
job_name = ""
workflow_id = ""

# import pipeline id
pipeline_id = os.environ['PIPELINE_ID']

# import job name
job_name = os.environ['CIRCLE_JOB']

# import workflow id
workflow_id = os.environ['CIRCLE_WORKFLOW_ID']

# import job id
job_id = os.environ['CIRCLE_WORKFLOW_JOB_ID']

# import token
circ_token = os.environ['CIRCLE_TOKEN']

conn = http.client.HTTPSConnection("circleci.com")

headers = { 'Circle-Token': circ_token }

conn.request("GET", "/api/v2/pipeline/{}/workflow".format(pipeline_id), headers=headers)

res = conn.getresponse()
data = res.read()

# create python dictionary
pipeline_dict = json.loads(data)

# set number of retries
retry_limit = 2

run_num = 0

# find number of times retried
for i in pipeline_dict['items']:
    if i['name'] == job_name:
        run_num += 1

print("{} has run {} times.".format(job_name, run_num))

# if job has run more than limit, don't retry
if run_num > retry_limit:
    print("Automatic rerun workflow limit has been reached. Not retrying again.")
    sys.exit(1)
else:
    print("Tests failed, attempting to retry")
    for i in pipeline_dict['items']:
        if i['id'] == workflow_id:

            print("Found the workflow to retry. Sending retry request for workflow: {}".format(workflow_id))

            payload = "{\"enable_ssh\":false,\"from_failed\":true}"

            headers = {
                'content-type': "application/json",
                'Circle-Token': circ_token
            }
            
            conn.request("POST", "/api/v2/workflow/{}/rerun".format(workflow_id), payload, headers)
            
            res = conn.getresponse()
            data = res.read()
            
            print("The following workflow has been retried:")

            print(data.decode("utf-8"))

            print("Ending.")
            
            break

    sys.exit(0)
