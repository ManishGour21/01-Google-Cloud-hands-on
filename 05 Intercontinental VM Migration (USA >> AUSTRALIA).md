# Intercontinental VM Migration (USA >> AUSTRALIA) 


![image](https://user-images.githubusercontent.com/88970736/131009886-8266181a-2aad-49b8-ab6e-e68a5c3c5079.png)

**as first step we need to create two compute instance to host data base and applicaiton**

1. Create 02 instances with following settings
 **GCE- Application (app)**
> Name : usa-app1
> Region : Us-west-1
> Zone : b
> size : e2-micro
> OS : Debian GNU/Linux 10

gcloud compute instances create us-app01 --machine-type e2-micro --zone us-west1-b

**GCE- Application (db)**
> Name : usa-db1
> Region : Us-west-1
> Zone : b
> size : e2-micro
> OS : Debian GNU/Linux 10

gcloud compute instances create us-db01 --machine-type e2-micro --zone us-west1-b

![image](https://user-images.githubusercontent.com/88970736/131013059-fb9e8685-6d52-444a-882c-4ae0919163ce.png)


# DB:Installing, Setting up and Creating

**Run these commands for OS update, repository and package installation**

sudo apt update
sudo apt-get -y install wget
wget http://repo.mysql.com/mysql-apt-config_0.8.13-1_all.deb

![image](https://user-images.githubusercontent.com/88970736/131013903-e4a30bb4-4d11-4a70-b1e3-49423e7b60f4.png)

**Selecting mysql version**
sudo dpkg -i mysql-apt-config_0.8.13-1_all.deb

![image](https://user-images.githubusercontent.com/88970736/131014352-b9e8eeec-161b-4a3b-9edf-1a405fbe9f82.png)


**Installing MySQL Server**

sudo apt update

![image](https://user-images.githubusercontent.com/88970736/131014588-9371f272-d83b-4435-9b5d-0878ddd36b0d.png)


sudo apt install mysql-server -y

![image](https://user-images.githubusercontent.com/88970736/131015056-3c3177f0-eba7-4b24-8f30-2559de9f292a.png)

**Restarting the MySQL service**

sudo systemctl restart mysql.service

**Setting up the MySQL**

sudo mysql_secure_installation

**Downloading the file *.sql**

wget https://storage.googleapis.com/bootcamp-gcp-en/bootcamp-gcp-storage-db-en.sql

![image](https://user-images.githubusercontent.com/88970736/131016007-79175bd0-24d0-4fc1-9489-a91506ebd542.png)

**Connecting to DB**

mysql -u root -p

![image](https://user-images.githubusercontent.com/88970736/131018068-e37d6fc7-d5a7-464d-b7a3-d0087b6bacb5.png)


**Creating the 'db' and 'tables'**

source bootcamp-gcp-storage-db-en.sql

![image](https://user-images.githubusercontent.com/88970736/131018226-2b919cc2-d6f1-46de-af77-538f3e867f04.png)


**Creating an user and changing the privileges**

CREATE USER app@'%' IDENTIFIED BY 'welcome1';
GRANT ALL PRIVILEGES ON clinic.* TO app@'%';
FLUSH PRIVILEGES;
exit

![image](https://user-images.githubusercontent.com/88970736/131018526-ac61fc25-35aa-49c4-afd2-dcb820ebe194.png)


# Setting up the VM for the Application

**Updating the OS and the packages**

sudo apt-get update
sudo apt-get install -y npm

![image](https://user-images.githubusercontent.com/88970736/131021579-20bc1550-adf1-4824-8e09-8afbbc6f76e1.png)


sudo apt-get install -y zip

![image](https://user-images.githubusercontent.com/88970736/131021644-78b63bd3-5cd6-4a10-9f55-fa29f9fc369a.png)

sudo apt-get install -y wget

![image](https://user-images.githubusercontent.com/88970736/131021700-c9d3c353-a704-4666-9bce-bc180c139a0a.png)


**Creating and accessing the folder to download application files (Node.js)**

wget https://storage.googleapis.com/bootcamp-gcp-en/bootcamp-gcp-storage-clinic-mid-app.zip

![image](https://user-images.githubusercontent.com/88970736/131021846-3920e587-b72c-496f-b10f-db3d7cbef902.png)

unzip bootcamp-gcp-storage-clinic-mib-app.zip

![image](https://user-images.githubusercontent.com/88970736/131022035-99055256-caf0-4899-89e9-cf6542ab8f5e.png)


cd bootcamp-gcp-storage-clinic-mib-app

![image](https://user-images.githubusercontent.com/88970736/131022198-74eeb9ea-711b-4896-8f5f-61c74935671d.png)

**From the folder bootcamp-gcp-storage-clinic-mid-app,
run the following command to edit the file index.js
**

nano src/index.js

Once inside of the file index.js, 
in the Middlewares section,replace:

host:tothePrivate IP address of the vm usa-db01.
user:to app,
password: to welcome1
database:to clinic

**From bootcamp-gcp-storage-clinic-mid-app folder run the command below to install theNPM package:**

npm install

![image](https://user-images.githubusercontent.com/88970736/131023640-fb32cc13-8925-4fbc-b461-ead1342e071a.png)

**Start the Node.js application:**

node src/index.js

![image](https://user-images.githubusercontent.com/88970736/131023907-07bcdce4-7d56-42b5-9d6f-9bf7051aeb9d.png)


**Creating a firewall rule to allow the TCP access on 3000 port!FromFirewall services, clickonCreate Firewall Rule:**

Name: allow-app-port-3000
Targets: All instances in the network
Source IP ranges: 0.0.0.0/0
SelectTCPandtheport3000
ClickonCreate

**applicaiton is working : **

![image](https://user-images.githubusercontent.com/88970736/131026224-8274b5bc-b777-40a0-9571-5475e57edef6.png)

# Migrating the VMs using the Storage Snapshot

**01 Disk used by VMs**
us-app1
us-db1

**Creating snapshot from disks of the VMs **


gcloud compute disks snapshot us-db01 --snapshot-names us-db01-snapshot --zone us-west1-b

gcloud compute disks snapshot us-app01 --snapshot-names us-app01-snapshot --zone us-west1-b

![image](https://user-images.githubusercontent.com/88970736/131158052-a9ad5eb2-aa72-4635-ade6-1ea345dfa1eb.png)

**Creating disks in the australia-southeast1 **


gcloud compute disks create aus-db01 --source-snapshot us-db01-snapshot --zone australia-southeast1-a

![image](https://user-images.githubusercontent.com/88970736/131158327-07192ecf-916b-488f-9d53-06b9a7c3c085.png)


gcloud compute disks create aus-app01 --source-snapshot us-app01-snapshot --zone australia-southeast1-a

![image](https://user-images.githubusercontent.com/88970736/131158467-cce84573-8099-470a-abe1-428c13690379.png)

**Creating instances in the Sydney region,using as source the disks created in the previous step **


gcloud compute instances create aus-app01 --machine-type e2-micro --zone australia-southeast1-a --disk name=aus-app01,boot=yes,mode=rw

![image](https://user-images.githubusercontent.com/88970736/131159135-98437d78-ac53-4022-92c3-cdb0554302c2.png)

gcloud compute instances create aus-db01 --machine-type e2-micro --zone australia-southeast1-a --disk name=aus-db01,boot=yes,mode=rw

![image](https://user-images.githubusercontent.com/88970736/131159241-c7a5fe21-1517-4bbd-a8c1-d7a042d4c122.png)

**Accessing the instance aus-app01 via ssh**
Accessingthefolderbootcamp-gcp-storage-clinic-mib-app
CD bootcamp-gcp-storage-clinic-mid-app


**Editingthefilesrc/index.js**

vi src/index.js

In the Middlewares section, replace: 

host: to the private IP private of the VM aus-db01

**Starting the application**
node src/index.js

**Accessing the application on port 3000 in the browser:**

http://<external-ip-from-aus-app01:3000


![image](https://user-images.githubusercontent.com/88970736/131160564-efcb9508-e1f3-4a64-bbb5-faa8ee3465da.png)
