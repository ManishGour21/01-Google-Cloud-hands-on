# 01-Google-Cloud-hands-on
this is hands-on repository for google cloud learning path 
#create a test project in google cloud :

![image](https://user-images.githubusercontent.com/88970736/129485546-642682f0-4fa7-4713-a545-1bbe80172e90.png)

#ctrate a storage bucket in test account : 
![image](https://user-images.githubusercontent.com/88970736/129506325-1cda026d-3edf-4841-83c8-cb1cfc989d48.png)

#we will need a service account to communicate with cloud : 
![image](https://user-images.githubusercontent.com/88970736/129506175-9b70a569-6578-455d-a1f0-81e45d7fd645.png)

#we used below python code to communicate with google cloud : 

from google.cloud import storage
#########################################################################
import sys

# Authenticate with Google Cloud using the service account key file
key = sys.argv[1]
storage_client = storage.Client.from_service_account_json(key)

# List Cloud Storage Buckets to validate the communication
buckets = list(storage_client.list_buckets())
print(buckets)
#########################################################################

use below command from command prompt : 
python ./storage_list01.py <use service acount key>

  
