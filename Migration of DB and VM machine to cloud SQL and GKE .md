# MIGRATION OF A STAND-ALONE APPLICATIONAND DATABASE FROM GCE (VM)TO A ‘MODERN ARCHITECTURE’ USING GKE (APP)+ CLOUD SQL (DB) WITH HA

![image](https://user-images.githubusercontent.com/88970736/132048348-c2263ab1-6bfe-4f0e-8e4b-60ef201df1a5.png)

# Modernization process to Cloud SQL + Kubernetes

**CreatingCloudSQLinstance(Australiaregion)**

1 Instance ID:tcb-gcp-aus-db01;
2 Password:welcome1
3 Version:MySQL 5.7;
4 Region:(australia-southest1);
5 EnableHA:Multiple Zones;
  a Primary zone:australia-southest1-a
  b Primary zone:australia-southest1-b
6 Customizeyourinstance;
  a Machine type->SelectLightweight;
  b Storage ->Storage capacity->Select10GB;

![image](https://user-images.githubusercontent.com/88970736/132052812-bc805be8-75d4-40c8-93d6-3ef6e4d13753.png)


**After created the Cloud SQL instance. **

Click on Databases.
Then,click on Create Database.

Database name:clinic;
ClickonCreate.

![image](https://user-images.githubusercontent.com/88970736/132053024-00236b86-2347-43c0-aaec-134afbc5571f.png)


**CreatinganuserintheCloud SQL instance**

ClickonUsers.
Add user account:
Username: app
Password:welcome1
Host name | Allow any host (%)

![image](https://user-images.githubusercontent.com/88970736/132053234-c5c514cf-fca8-4b29-9e85-eea1d9095a8e.png)


# Containerizing (docker) the application

**Downloding the application files**

wget https://storage.googleapis.com/bootcamp-gcp-en/bootcamp-gcp-module-db.zip

![image](https://user-images.githubusercontent.com/88970736/132051327-5a870751-1552-4000-ad99-abb7d718f025.png)


unzip bootcamp-gcp-module-db.zip

![image](https://user-images.githubusercontent.com/88970736/132051409-5b079a21-2748-4e7e-a905-9a64ae9a6c1f.png)

# Creating a new image

cd ~/bootcamp-gcp-module-db/app

![image](https://user-images.githubusercontent.com/88970736/132051796-d289d3ac-13a1-4201-a9a9-36583892346c.png)

docker build -t tcb-clinic-app .

![image](https://user-images.githubusercontent.com/88970736/132051698-bc100a87-aa16-4e96-ad7c-0c5487f560b9.png)

# Adding tag and uploading it to the Container Registry

docker tag tcb-clinic-app asia.gcr.io/$DEVSHELL_PROJECT_ID/tcb-clinic-app:latest

docker push asia.gcr.io/$DEVSHELL_PROJECT_ID/tcb-clinic-app:latest

![image](https://user-images.githubusercontent.com/88970736/132052075-cdb6a8a1-46fe-4981-8e51-27d9ececb01d.png)

![image](https://user-images.githubusercontent.com/88970736/132052150-cfd0956e-ae61-4d1d-8a3c-b17432c0eb3b.png)


# From Kubernetes Engine services

FromtheKubernetesEngineservices,clickon[+] Create |Autopilor cluster|Configure
Name: autopilot-cluster-1
Region: australia-southeast1
ClickonCreate.

![image](https://user-images.githubusercontent.com/88970736/132053339-0be357da-562a-4a1b-9df1-cf948bff2e14.png)


**IntheCloud Shell,downloadingthefiletcb-clinic.yaml**

wget https://storage.googleapis.com/bootcamp-gcp-en/tcb-clinic.yaml

![image](https://user-images.githubusercontent.com/88970736/132053478-71c7a383-e440-43a3-b7df-f97b9742e097.png)


**Edit the file tcb-clinic.yaml using the Cloud Editor,changethePrivateIP(DBHOST)oftheCloudSQL:**
  Imagepath(image:asia.gcr.io/<project-name>/tcb-clinic-app:latest)

  **Connecting to the Cluster(Console->GKE->the Cluster created->Connect)**
  
  IntheCommand-line access,clickonRun in Cloud Shell [ Enter ]
  
  ![image](https://user-images.githubusercontent.com/88970736/132054544-2fa5b578-4707-4004-bb02-7cdffe69df21.png)

# Deploying the application from the yaml file:
  
  kubectl apply -f tcb-clinic.yaml
  
  ![image](https://user-images.githubusercontent.com/88970736/132054717-85694423-1940-4965-b298-53da064e55ad.png)


  
  

  
