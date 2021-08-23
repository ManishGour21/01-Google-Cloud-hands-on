# Follow below steps 

**Enable following APIs on project : **
- Cloud Resource manager
- Compute engine
- Kuberneties Engine

# Lift and shift APIs 

**1 **Open cloud shell and setting projevt as default project :

gcloud config set project prod-project-322417

![image](https://user-images.githubusercontent.com/88970736/130488604-0a0f5421-b060-4444-8541-88d3df10f0ba.png)


**2 Settingupthecomputezoneus-west1-aasdefault.**

gcloud config set compute/zone us-west1-a

![image](https://user-images.githubusercontent.com/88970736/130488679-43172b8c-c85f-4f40-ae0b-32fa9f32e5bb.png)


**3 Adding firewall rules to allow traffic on htt pand ssh ports.**

for post 22
gcloud compute firewall-rules create allow-ssh --network default \--allow tcp:22 --source-ranges 0.0.0.0/0

![image](https://user-images.githubusercontent.com/88970736/130488747-7f0b5c59-ea3e-4242-a012-3c36390d215b.png)


For port 80
gcloud compute firewall-rules create allow-http --network default \--allow tcp:80 --source-ranges 0.0.0.0/0

![image](https://user-images.githubusercontent.com/88970736/130488797-b16cfd05-fc20-4cfc-a02e-812f4133b715.png)


**4 Run the command below to create the VM to perform the Lift & Shift steps**

gcloud compute instances create webapp-01 --project=$DEVSHELL_PROJECT_ID \
--zone=us-west1-a --machine-type=n1-standard-1 --subnet=default \
--scopes="cloud-platform" --tags=http-server,https-server \
--image=ubuntu-minimal-1604-xenial-v20210119a --image-project=ubuntu-os-cloud \
--boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=app-01

![image](https://user-images.githubusercontent.com/88970736/130488888-9ec97ec9-b3ea-4371-824f-b8c4a8544d40.png)

**5 Generating key pair and setting up the permissions.**

ssh-keygen -t rsa -f ~/.ssh/app-key -C [USERNAME]

chmod 400 ~/.ssh/app-key

![image](https://user-images.githubusercontent.com/88970736/130489209-38f6b545-f66f-40af-968b-977eae3c579d.png)

**6 Importing the key pair generated to Google Cloud:**

gcloud compute config-ssh --ssh-key-file=~/.ssh/app-key

![image](https://user-images.githubusercontent.com/88970736/130489580-27f483a5-592f-4a19-b67d-a6e4d30989b9.png)


# Implimentation 

**7 Connecting to the new VM created via SSH and running the following commands**

sudo apt-get update && sudo apt-get install apache2 unzip -y

![image](https://user-images.githubusercontent.com/88970736/130490125-427d92ca-2b8b-424c-8bc0-653418c18819.png)

cd /var/www/html

![image](https://user-images.githubusercontent.com/88970736/130490296-a70550a4-47c7-4a94-91c0-72ec94310a92.png)

sudo mv index.html index.html.bkp

sudo curl -O https://storage.googleapis.com/bootcamp-gcp-en/hands-on-compute-website-files-en.zip

![image](https://user-images.githubusercontent.com/88970736/130490551-e5a8279e-b11e-437b-85c5-cf5df91f3819.png)


sudo unzip hands-on-compute-website-files-en.zip

![image](https://user-images.githubusercontent.com/88970736/130490705-decf9e68-4db2-4366-aa7d-e570d16b78f5.png)

to sets read and write purmission to usersgroups and VM 
sudo chmod 644 *

**8 CopytheExternalIPoftheComputeEnginecreatedandaccessitviabrowsertovalidateiftheLift & Shiftprocesswascompletedsuccessfully**

![image](https://user-images.githubusercontent.com/88970736/130491390-1313a154-af5d-415b-ad01-15b1a7489a95.png)

