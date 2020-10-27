# AWSRekogniton
API code which runs AWS Rekognition on your local system

Before using the AWS Rekognition API you will have to set up a free account on AWS using your Credit Card and configure AWS CLI on your system. To configure AWS CLI,Google AWS CLI version 2, which will take you to an official AWS Page - from which you have to install the .exe file on your system. You will have to download a MSI installer from the link which will open. Now open command prompt and type the following command
aws --version  #if this tells you the version of AWS CLI, it means that AWS CLI is installed on your system

You will need to create an Access Key. To do that, login with your IAM User account and navigate to Access Management -> Users -> Security Credentials Tab -> Create Access Key. This will generate Access Key ID and Secret Access Key for you. Please do not share your Access Keys with anyone.

Now open Command Prompt (on Windows Laptop) and enter the following commands-
aws configure  #Please enter and paste your Access Key and Secret Access Key when prompted
               #Enter a default region name which is close to the place you are staying in
               #Press enter when asked about default output format

Now AWS CLI is configured on your system. To test, if your system is connected to AWS, enter the following command
aws iam list-users #This will list all the current active users on your AWS account. Make sure you have the relevant access permissions for your IAM User Account

You have now configured AWS on your system and the Python SDK will be able to access AWS programatically. 

