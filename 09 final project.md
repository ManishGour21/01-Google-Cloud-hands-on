# AUTOMATION OF A TALENT ONBOARDING WEB APPLICATIONUSING HTML/CSS/JS/BS (FRONTEND) + ‘PYTHON FLASK’ (BACKEND)WITH ‘CLOUD STORAGE’ AND ‘CLOUD FUNCTIONS’100% SERVERLESS

# Setting up a Webservice plugin on Moodle

**Login as Admin in the Moodle Web Application**

Access:Site administration > Plugins > Plugins > Category : Webservices
> Enable web services
> 
> Default: No
> 
> Save Changes
> 
> Enable protocols
> 
> REST Protocol
> 
> Click on Select a service to add a new webservice

Add

Name:webservice
Shortname:webservice
Check Enable 
Check Authorized users only
Clickon Add service


Add functions
In the section'Custom services',click on Functions
Click on Add functions
From Search,copy and past ecore_user_create_users and then select edit.
Click on Add functions

Click onSelect a specific user 
From the section Custom Services > webservice > Click on Authorized users
From Not Authorized,find and select the user Admin User,then click on Add



Click on Create a token for a user
In the section Token, select the user Admin User
In Service,select web service
Save Changes
Copy and paste in the note pad the Token generated

Token :c7143d155b895dda86c74eac3ab1173e
IP 34.125.65.162

on Gcloud run below command : 
curl -g "http://<moodle-ip-server>/webservice/rest/server.php?wstoken=<token-generated>&moodlewsrestformat=json&wsfunction=core_user_create_users&users[0][username]=929316&users[0][email]=you39@yourhost.org&users[0][lastname]=Test1&users[0][firstname]=Moodle&users[0][password]=P@40ssword123"

![image](https://user-images.githubusercontent.com/88970736/132569156-28fcf422-77a9-4738-85b1-1f0c389c8037.png)

User Created : 
![image](https://user-images.githubusercontent.com/88970736/132569311-c476d866-97ff-4349-bfb8-a0fdf74bae71.png)

# Deploying a Cloud Function
  
  **AccesstheCloud Functions services**

  ClickonCreate Function
  
  Section Basics 
  Function name: moodle User Create

  Trigger type:HTTP
  Authentication:Allow unauthenticated invocations
  CheckRequire HTTPS 
  Click on Save
  
  ![image](https://user-images.githubusercontent.com/88970736/132569977-3556b529-102e-458a-8996-f8c6e549fd40.png)

  From Runtime environment variables, add 02 Variables
  Name:MOODLE_TOKEN
  Value: insertthetoken generated
  
  Add Variable
  Name:MOODLE_SERVER
  Value: insert the Moodle Public IP Server
  Click on Next
  
  Runtime: select Python 3.8
  Entry point,type receive_request (Function name in the Main.py)


 Download code : 
  wget https://storage.googleapis.com/bootcamp-gcp-en/bootcamp-gcp-final-project.zip
  unzip bootcamp-gcp-final-project.zip
  
  ![image](https://user-images.githubusercontent.com/88970736/132571445-2563120f-f24e-48de-8db3-fc4575a5bb55.png)

  ![image](https://user-images.githubusercontent.com/88970736/132571507-0397ef26-d7a8-4230-a0ac-6c5436fe42b9.png)

  
**Copy the content of the file main.py (bootcamp-gcp-final-project\backend\main.py)
**From Cloud Functions,replace the content of the file main.py with the code copied!
**Do the same with the file requirements.txt,copy the content from the file requirements.txt
  (bootcamp-gcp-final-project\backend\requirements.txt) and replace in the Cloud Function requirements.txt file!**
  
  Click on Deploy. (This process can take 2-4 minutes)

  ![image](https://user-images.githubusercontent.com/88970736/132573158-f8dd446f-21b2-4242-b889-d59b67d345d6.png)

![image](https://user-images.githubusercontent.com/88970736/132573236-7e08b553-2b45-41bc-ae79-0143ac40d695.png)
  
  After finishingthe Cloud Function Deployment, access the function moodle User Create.
  
  From the guide Trigger, copy the Trigger URL and save it in your notepad file!
  
  From the Cloud Shell,check if the function is working:
  
  curl  -X  POST  -F  'inputName=Manish'  -F  'inputLastname=Gour'  -F
  'inputEmail=manish@gmail.com' https://asia-south1-testing-project-92255.cloudfunctions.net/moodle-User-Create
  
  ![image](https://user-images.githubusercontent.com/88970736/132573678-a9b55cd2-2e56-4c3f-9af9-8d423f4031f7.png)

  ![image](https://user-images.githubusercontent.com/88970736/132573741-cf83c06b-a24a-4acf-a340-8f1b8b491aec.png)

  
  # Setting up the Frontend
  
  Using the Cloud Editor,edit the file~/bootcamp-gcp-final-project/frontend/index.html
  In the action,replace the info to the Trigger URL.\
  
  https://asia-south1-testing-project-92255.cloudfunctions.net/moodle-User-Create
  
  ![image](https://user-images.githubusercontent.com/88970736/132575560-ecbfd20e-a472-4100-8c2e-b5efe2ab2e1b.png)

 
  **Let's create a Bucket(Cloud Storage) using the Cloud Shell**
  
  gsutil mb gs://tcb-gl-onb-manish123
  
  ![image](https://user-images.githubusercontent.com/88970736/132575783-5c8a39cf-b5c3-474d-841f-7411321fc904.png)

  
  Uploading theFront end files to the bucket created:
  
  cd ~/bootcamp-gcp-final-project/frontend/
  gsutil cp * gs://tcb-gl-onb-manish123
  
  ![image](https://user-images.githubusercontent.com/88970736/132576035-68b617ab-c9ce-4265-b3e5-1e50a05207c9.png)

  **Settiing up the Bucket**
  
  
  gsutil web set -m index.html -e 404.html gs://tcb-gl-onb-manish123
  gsutil iam ch allUsers:objectViewer gs://tcb-gl-onb-manish123
  
  ![image](https://user-images.githubusercontent.com/88970736/132576381-86c77630-dca4-4298-aa25-f6fc22b4c322.png)

  
  Testing the Application Frontend/Form/CloudFunction
  
  Accessthe Cloud Storage
  Go to the Bucket created tcb-gl-onb-manish123
  Click on the file index.html
  Click on the Public URLto access via browser
  
  ![image](https://user-images.githubusercontent.com/88970736/132577459-48dec4bf-2002-4006-add0-b9c96869df86.png)

  ![image](https://user-images.githubusercontent.com/88970736/132577539-8531beae-acdf-4d4a-9e4d-2c8189a6ab76.png)
  
  ![image](https://user-images.githubusercontent.com/88970736/132577715-a209a8d7-976b-4fc3-8aac-d5c468d8d5f9.png)


  
  
