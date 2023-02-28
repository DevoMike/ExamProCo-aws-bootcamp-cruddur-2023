# Week 0 — Billing and Architecture
I have gone through the videos and i can create my reports.
**Create an Admin Account**
successfully created an Admin user account on AWS using the IAM management console on the AWS poprtal.
![Admin user](https://user-images.githubusercontent.com/121178341/221856293-340239f6-abdf-4282-97be-41c11a9b8437.PNG)

I was about to grant the user access to view billings and other Administrative privilages by enabling the "IAM User and Role Access to Billing Information"
![account access Activation](https://user-images.githubusercontent.com/121178341/221858388-8ab8f252-0367-4d74-8f06-8f5640e124c9.PNG)

**Used Cloud shell**
I was able to use the CLI by checking informations and running CLI commands like aws sts get-caller-identity
![using the CLI](https://user-images.githubusercontent.com/121178341/221865017-7b8c6529-af56-4c22-8db2-a8cfc04bb720.PNG)

**Generate AWS Credentials**
generating the AWS Credentials can be found in the week 0 REPOSITORY

**Installed AWS CLI**
INSTALLING THE aws cli was a bit challenging. i succeeded in using the gitpod envronment to achieve that purpose.
lunching gitpod from my Gitlab account.
![gitpod link](https://user-images.githubusercontent.com/121178341/221866353-8e61828f-93e2-434b-ba29-a0289d2ae250.PNG)
using the instruction from the video done by Andrew. i was about to activate these commands 
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

NOTE: 
During the process of installation i was unable to create the auto installation whenever Launched Gitpod. the problem here was that i need to 
do a fresh installtion whenever i tired to access AWS cli VIA Gitpod. 
so i decided to do a manual installtion anytime i wanted to use gitpod
![gitpod AWS instalation](https://user-images.githubusercontent.com/121178341/221867999-6a06c817-ea91-45b6-bde8-b13c7ba135b3.PNG)

What this means is that i do not need to run a fresh installation BUT I can only run " sudo ./aws/install" to install AWS CLI just like the picture below
![success running AWS CLI](https://user-images.githubusercontent.com/121178341/221868876-f5b5c835-9f66-45ba-96e4-872488285fb3.PNG)

**Create a Billing Alarm**
Again with the Help of the instruction by Andrew.
 i successfully created a billing alarm using the billing alarm. this was achieved via the billing console on the aws mangement page.
 
 ![billing alarm](https://user-images.githubusercontent.com/121178341/221872212-a25f948a-5b59-4552-ac50-3589a0ade31e.PNG)

 **Create a budget**
 This was done with the Aid of the instruction by Andrew and the team
![CLI billing alarm](https://user-images.githubusercontent.com/121178341/221870566-04aabf81-f511-4208-96a5-a1a01b114981.PNG)

A successful budget created appeared on the AWS ACCOUNT PAGE shown below
 ![budget creation](https://user-images.githubusercontent.com/121178341/221871341-55593de3-5453-448c-b968-f82bbd8bd101.PNG)

Thanks
 

