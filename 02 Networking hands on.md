# Below are steps to complet the project : 

# prerequisites: 
create AWS account
Create GCP accout

# Key setup :


**#1 Creat Project in GCP**

project name - tcb-gcp-aws
poject ID tcb-gcp-aws-323117

![image](https://user-images.githubusercontent.com/88970736/129603074-57864c06-c028-4f31-8b5b-769166dc0f85.png)

**#2 Checking if the Billing is enabled**

**#3 Enabling the Compute Engine API**

use below link to enable API : 
https://console.cloud.google.com/flows/enableapi?apiid=compute_component,deploymentmanager&_ga=2.90885017.2003023334.1613150551-112422406.1602704538

![image](https://user-images.githubusercontent.com/88970736/129604756-4e62293b-bd59-4a46-a600-e680a9b5f07c.png)

**# 4 Starting the Cloud Shell**

![image](https://user-images.githubusercontent.com/88970736/129606216-3ef5ad01-fe15-4957-bc59-e8319f0dcd92.png)

**# 5 Download project files :**

use curl command on cloud shell 

curl -O C:\Users\manis\OneDrive\Desktop\project 01\Networking\hands-on-tcb-bmc-gcp.zip

![image](https://user-images.githubusercontent.com/88970736/129607092-693ceea1-fa79-477b-9ce5-c9e2a9176272.png)

**# 6 Unzip the project file :**

unzip hands-on-tcb-bmc-gcp.zip

![image](https://user-images.githubusercontent.com/88970736/129607319-0b026056-b96a-44b1-8eaf-20ca921c7550.png)

**# 7 Acessing the folder "hands-on-tcb-bmc-gcp"**

cd hands-on-tcb-bmc-gcp

![image](https://user-images.githubusercontent.com/88970736/129607833-ae6e0b76-c8ad-4495-9d64-2b0620d7995d.png)

**# 8 Allowing 'execute' permission for all files .sh**

chmod +x *.sh

![image](https://user-images.githubusercontent.com/88970736/129607966-e0bd2dc4-c178-4b3b-ad96-6df34e4b76df.png)

# Creating credentials in the GCP

**# 1 Creating and downloading the Service Account Key (JSON format)**

Serviceaccount[Name:Compute Engine default service account]

![image](https://user-images.githubusercontent.com/88970736/129608835-2ffbdc2f-3be4-4b29-84d1-badd09388aff.png)


![image](https://user-images.githubusercontent.com/88970736/129608687-acf710e3-cb0f-463e-a8e0-49262c7700c5.png)

**# 2 Uploading the file (key) .json to the Cloud Shell.**

![image](https://user-images.githubusercontent.com/88970736/129609363-4ffa6a32-2f0b-48b4-ba5f-269c332249fd.png)

**# 3 Running the command:**

./gcp_set_credentials.sh ~/file.json

![image](https://user-images.githubusercontent.com/88970736/129610968-853cfd40-7c99-4335-9050-8fcf0ba285c6.png)

# Creating credentials in the AWS (Oregon - us-west-2)

**# 1 AWS console create user **

AWS console>>IAM >> Users >> Add user >> Programmatic access

Attachexistingpoliciesdirectly:
AdministratorAccess Next >> Next >> Create User

![image](https://user-images.githubusercontent.com/88970736/129612016-229315df-1cd4-4c51-97c8-3452a41a8278.png)


**# 2 Renaming the .csv file to accessKeys.csv**

**# 3 Uploading the file (key) .csv to the Cloud Shell.**

![image](https://user-images.githubusercontent.com/88970736/129612420-bd60429a-efd4-43a8-a7c3-14f53a799ac3.png)


**# 4 Running the command:**

./aws_set_credentials.sh ~/accessKeys.csv

![image](https://user-images.githubusercontent.com/88970736/129612679-5f965edb-cd41-4e1b-90fd-0fb5f3d42080.png)


# Getting the Terraform ready

Makesureyou'reinthefolder'hands-on-tcb-bmc-gcp'Andrunthecommand:
./get_terraform.sh

![image](https://user-images.githubusercontent.com/88970736/129612984-a2bf4f8c-c9c6-44c8-b36d-581f7aaec855.png)


# Setting up the GCP Project

**# 1 From Cloud Shell, run the command:**

gcloud config set project [YOUR-PROJECT-ID]

![image](https://user-images.githubusercontent.com/88970736/129613665-436814b1-75fc-4e0c-bbf2-b3151f611850.png)


**# 2 Run the command: **

./gcp_set_project.sh

![image](https://user-images.githubusercontent.com/88970736/129613868-5b3646d7-5ca8-4804-81e5-f0d18a331fc1.png)


**# 3 Check if the project-id was inserted into the file terraform.tfvars**

cat /home/[YOUR-USERNAME]/hands-on-tcb-bmc-gcp/terraform/terraform.tfvars

![image](https://user-images.githubusercontent.com/88970736/129614245-640311e8-aaa8-477e-b0a4-580f99413a43.png)


# Generating a Key Pairs

**# 1 Run the command 'whoami' to get your username**

![image](https://user-images.githubusercontent.com/88970736/129614412-a6926fcf-28b8-4fc3-964b-aebcde0fb675.png)

**# 2 Run the command below, replacing 'YOUR-USERNAME'**

ssh-keygen -t rsa -f ~/.ssh/vm-ssh-key -C [YOUR-USERNAME]

![image](https://user-images.githubusercontent.com/88970736/129614616-36d94839-06df-47ce-a79f-a9abe84b96e3.png)

**# 3 Run the command below to set up a permission to the private key:**

Run the command below to set up a permission to the private key:

chmod 400 ~/.ssh/vm-ssh-key

![image](https://user-images.githubusercontent.com/88970736/129614856-17cdb9d5-0266-4c1e-9896-b8e4546a3847.png)


# Importing the public key to GCP
FromCloud Shell,runthefollowingcommand

gcloud compute config-ssh --ssh-key-file=~/.ssh/vm-ssh-key

![image](https://user-images.githubusercontent.com/88970736/129615149-3262628c-b06a-4e7e-b320-5468f03d516c.png)

Compute engin >> Metadeta : 

![image](https://user-images.githubusercontent.com/88970736/129615613-4a6718ae-a199-4e14-9954-96cee347d7c0.png)


# Importing the public key to AWS
Proceed with the download of the 'Public Key' generated in the Cloud Shell

how to get public key path : 

![image](https://user-images.githubusercontent.com/88970736/129616524-7de3c35f-ba09-45e7-87e3-30897303f1c9.png)

download key from : 
/home/manishgourgcp21/.ssh/vm-ssh-key.pub

![image](https://user-images.githubusercontent.com/88970736/129616820-8dcebc6b-28ef-4597-b095-c8a90f217da4.png)

# AWS console >> EC2 >> Network & Security >> Key Pairs >> Action

![image](https://user-images.githubusercontent.com/88970736/129617038-a60c74c2-52aa-4bff-b88e-6f4fa7d6785b.png)

# Terraform time

1 From Cloud Shell, make sure you're in the folder 'hands-on-tcb-bmc-gcp'
2 Go to the Terraform's folder:cd terraform
3 Run the command below to initialize the Terraform:
  terraform init
  
  ![image](https://user-images.githubusercontent.com/88970736/129822975-970a468a-8565-4376-a8cf-7b0fcd9f4514.png)

4 Run this command to validate the Terraform configuration:
  terraform validate
  
  ![image](https://user-images.githubusercontent.com/88970736/129823149-15ffddec-e8f7-4827-8b03-5ca759d30ce9.png)

5 Run the command below to check the Terraform planning deployment:
  terraform plan
  
  ![image](https://user-images.githubusercontent.com/88970736/129823329-f2424255-fd68-4d8e-a58b-3babaf639472.png)

6  Terraform deployment:
  terraform apply
![image](https://user-images.githubusercontent.com/88970736/129824271-89a38856-5153-424a-863c-d245a078e4d4.png)
![image](https://user-images.githubusercontent.com/88970736/129824443-30f87417-1e59-491d-bfc5-f3037970693b.png)


# Command to view the variables shown at the end of deployment.

terraform output

# Connectivity validation :

>> go to VM Instance
>> Click on SSH to open Lunix console
![image](https://user-images.githubusercontent.com/88970736/129825908-4d19b2eb-89f9-4ed7-b021-b1ef2abe43a8.png)
>> go to AWS and copy private IP :

![image](https://user-images.githubusercontent.com/88970736/129826106-0a87fb79-a7f9-4267-9db1-02d21a59ed6b.png)

>> ping the IP in SSH console : 
![image](https://user-images.githubusercontent.com/88970736/129826447-1e959296-2f6c-4bf0-bcfb-372759b949ef.png)


# Connectivity test from GCP 

>> go to Network Inteligence 
>> creat a new test
>> provide source and destination IP and network detaisls
>> submmit test 

![image](https://user-images.githubusercontent.com/88970736/129827185-ecb43d06-94a1-45ab-b1ba-964bbb870a5d.png)





