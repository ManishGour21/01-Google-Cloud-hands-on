# Modernization steps  part 2 of lift and shift.

**in this project we will convert an existing web application and implement it using docker image to kubernetes engine.**

# Creating a GKE Cluster

**Usingg cloud command on gcloud shell**

gcloud container clusters create app-01 \
--project=$DEVSHELL_PROJECT_ID --zone=us-west1-a --machine-type n1-standard-4 \
--cluster-version=1.19.12 --release-channel=stable --image-type ubuntu \
--num-nodes 1 --enable-stackdriver-kubernetes \
--subnetwork "projects/$DEVSHELL_PROJECT_ID/regions/us-west1/subnetworks/default"

![image](https://user-images.githubusercontent.com/88970736/130497070-e2a43171-1cb2-4917-81ed-8585715cc146.png)


# Installing the Migrate for Anthos

**1 Creatingaserviceaccounttcb-m4a-install.**

gcloud iam service-accounts create tcb-m4a-install \
--project=$DEVSHELL_PROJECT_ID

![image](https://user-images.githubusercontent.com/88970736/130497230-1eba3454-170b-44df-b0ee-dc42f376c60c.png)


**2 Assigning a role storage.admin to a service account tcb-m4a-install.**

gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \
--member="serviceAccount:tcb-m4a-install@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com" \
--role="roles/storage.admin"

![image](https://user-images.githubusercontent.com/88970736/130497475-22f48475-c7e2-4174-93eb-780b613c2802.png)

![image](https://user-images.githubusercontent.com/88970736/130497805-c81eea14-6189-4eb4-907d-67aa7e821d18.png)


**3 Creating and downloading the service account tcb-m4a-install key:**

gcloud iam service-accounts keys create tcb-m4a-install.json \
--iam-account=tcb-m4a-install@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com \
--project=$DEVSHELL_PROJECT_ID

![image](https://user-images.githubusercontent.com/88970736/130498269-7fa28ff8-6c8f-475d-b9a9-c09ddcf6fa7a.png)

![image](https://user-images.githubusercontent.com/88970736/130498207-25507504-4973-429f-ad75-78e3ff60e9b7.png)

**4 Connecting to the Kubernetes cluster:**

gcloud container clusters get-credentials app-01 \
--zone us-west1-a --project $DEVSHELL_PROJECT_ID

![image](https://user-images.githubusercontent.com/88970736/130499274-84ff26ff-e13a-4cf1-971f-758a7fee5a39.png)

**5 Settingup the Migrate for Anthos components in the GKE cluster app-01**

migctl setup install --json-key=tcb-m4a-install.json

![image](https://user-images.githubusercontent.com/88970736/130499685-2168a5d1-e832-4dbf-ac8d-329e52b70d91.png)

**6 Running the command below to validate the Migrate for Anthos installation:**

migctl doctor

![image](https://user-images.githubusercontent.com/88970736/130499911-373bd577-2457-45d8-9155-0d876da6f79d.png)

# Steps for VM migration

**1 Creating a service account tcb-m4a-ce-src**

gcloud iam service-accounts create tcb-m4a-ce-src \
--project=$DEVSHELL_PROJECT_ID

![image](https://user-images.githubusercontent.com/88970736/130500483-104ec085-6ca7-4b6e-918a-3f76abd38ada.png)

**2 Assigning the role compute.viewer to a service account tcb-m4a-ce-src**

gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \
--member="serviceAccount:tcb-m4a-ce-src@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com" \
--role="roles/compute.viewer"

![image](https://user-images.githubusercontent.com/88970736/130501049-7c439078-7257-4f02-84f4-3bc21c19258f.png)


**3 Assigning the role to compute.storage Admin to a service account tcb-m4a-ce-src**

gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \
--member="serviceAccount:tcb-m4a-ce-src@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com" \
--role="roles/compute.storageAdmin"

![image](https://user-images.githubusercontent.com/88970736/130501177-e37102e8-3f50-4a8c-ba03-7e9bf868e912.png)

**4 Creating and downloading the service account tcb-m4a-ce-src key**

gcloud iam service-accounts keys create tcb-m4a-ce-src.json \
--iam-account=tcb-m4a-ce-src@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com \
--project=$DEVSHELL_PROJECT_ID

![image](https://user-images.githubusercontent.com/88970736/130501382-d5d6ecb4-3384-4609-83cb-7da2fab3106f.png)

![image](https://user-images.githubusercontent.com/88970736/130501584-192d25b9-233b-4282-a3b7-4114d4d7abdc.png)


**5 Defining the'CE'(ComputeEngine) as a source**

migctl source create ce app-01-source --project $DEVSHELL_PROJECT_ID \
--json-key=tcb-m4a-ce-src.json

![image](https://user-images.githubusercontent.com/88970736/130501825-c1f9ff77-51b5-4c35-923b-d53443b6d45b.png)


# Creating/Downloading and Checking the Migration plan

**1 Creating the migration plan**

migctl migration create my-migration --source app-01-source\ 
--vm-id webapp-01 --intent Image

![image](https://user-images.githubusercontent.com/88970736/130502348-b01417bb-3420-4838-a967-694098cd2db3.png)

![image](https://user-images.githubusercontent.com/88970736/130502476-b346a3f1-e969-4820-b9d3-3538fe48a448.png)

**3 (optional) Downloading the migration plan**

migctl migration get my-migration

**4 (Optional)If you change any thing, run the command below to update the migration plan:**

this step to be used if we want to update migration plan:

migctl migration update my-migration --file my-migration.yaml

![image](https://user-images.githubusercontent.com/88970736/130502795-2d3c656a-3df0-4ed3-8160-977c19c3de71.png)

![image](https://user-images.githubusercontent.com/88970736/130503483-e659bab4-919d-45ea-bdd1-dd32c5100ed9.png)

**5 Migrating the VM using a migration plan:**

migctl migration generate-artifacts my-migration

Status check migctl migration status my-migration

![image](https://user-images.githubusercontent.com/88970736/130503642-e079a164-146f-4821-9863-f60525bed06b.png)


# Steps to deploy the migrated workload

**1 Downloading the artifacts**

migctl migration get-artifacts my-migration

![image](https://user-images.githubusercontent.com/88970736/130504144-e157a7fc-a8a4-4b75-bb2b-6c740b2f21df.png)

![image](https://user-images.githubusercontent.com/88970736/130504277-4cd385ae-c506-43ab-8d53-6dd5f64e3619.png)


**2 From Text Editor,open the file deployment_spec.yaml.**

below code is needed in yamal files to enable port 80

apiVersion: v1
kind: Service
metadata:
  name: talent-management-portal
spec:
  selector:
    app: app-01
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer

**3 Applying the changes and deploying the workload**

kubectl apply -f deployment_spec.yaml

![image](https://user-images.githubusercontent.com/88970736/130506900-0c38f9f1-7e69-4392-8c8d-eaff22ecc77d.png)

**4 Checking the external IP :**

kubectl get service talent-management-portal

![image](https://user-images.githubusercontent.com/88970736/130507182-599b5ea6-f51d-437f-ac8f-1b6af3feb288.png)


![image](https://user-images.githubusercontent.com/88970736/130508311-0599dcea-e843-4618-993b-e51fd967b727.png)

![image](https://user-images.githubusercontent.com/88970736/130508575-b0adc31e-a5d4-4c05-8e85-1cab7e64d640.png)

Docker Registory :

![image](https://user-images.githubusercontent.com/88970736/130508878-75c19c84-0659-4c4c-896a-8289e8592b19.png)
