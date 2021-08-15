
import googleapiclient.discovery
from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
credentials=GoogleCredentials.get_application_default()

service = discovery.build('compute','v1',credentials=credentials)

PROJECT_ID=input("ENTER PROJECT id : ")
# PROJECT_ID="testing-project-92255"

compute = googleapiclient.discovery.build('compute', 'v1')
zones = compute.zones().list(project=PROJECT_ID).execute()
configs=[]
for zone in zones['items']: 
    instances = compute.instances().list(project=PROJECT_ID, zone=zone['name']).execute()
    if 'items' in instances:
        for instance in instances['items']:
            configs.append(instance['name'])
print(configs)

