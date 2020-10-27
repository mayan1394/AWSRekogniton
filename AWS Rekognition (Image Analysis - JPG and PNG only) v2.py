#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import json
from pandas.io.json import json_normalize
import os
import pandas as pd


# In[2]:


os.chdir("C:\Project Work\Mayank_Data\GCP Test")


# In[3]:


def detect_labels(photo):
    client=boto3.client('rekognition')
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    labeloutput=""
    for label in response['Labels']:
        final = label['Name']+":"+str("{:.2f}".format(label['Confidence']))
        labeloutput=labeloutput+final+" "
    #print(labeloutput)
    return labeloutput


def detect_text(photo):
     client=boto3.client('rekognition')
     with open(photo,'rb') as image:
        response = client.detect_text(Image={'Bytes': image.read()})
     textDetections=response['TextDetections']
     textoutput=""
     for text in textDetections:
         final = text['DetectedText']+":"+str("{:.2f}".format(text['Confidence']))
         textoutput=textoutput+final+" "
     print(textoutput)
     return textoutput


def recognize_celebrities(photo):
     try:
         client=boto3.client('rekognition')
         with open(photo, 'rb') as image:
                 response = client.recognize_celebrities(Image={'Bytes': image.read()})
         celebrityoutput=""
         for celebrity in response['CelebrityFaces']:
             data='Name: ' + celebrity['Name']
             celebrityoutput+=data
         print (celebrityoutput)
     except:
        celebrityoutput="None"
     return celebrityoutput


def detect_faces(photo):
    client=boto3.client('rekognition')
    with open(photo, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()})
        #print (response)
    print('Detected faces for ' + photo)
    facedetails=""
    for faceDetail in response['FaceDetails']:
        data=json.dumps(faceDetail, indent=4, sort_keys=True)
        facedetails+=data
    return facedetails   
    #return len(response['FaceDetails']) 


def moderate_image(photo):
    client=boto3.client('rekognition')
    with open(photo, 'rb') as image:
        response = client.detect_moderation_labels(Image={'Bytes': image.read()})  
    moderatedimage=""
    for label in response['ModerationLabels']:
        test="Label: "+label['Name'] + ' : ' + str(label['Confidence'])+" Parent Label: "+label['ParentName']
        moderatedimage+=test
    print(moderatedimage)
    return len(response['ModerationLabels'])


def main():
    photo='Nadal.jpg'
    #celebrity=recognize_celebrities(photo)
    #print(celebrity)
    full_list=[]
    for photos in os.listdir():
        labels = detect_labels(photos)
        faces = detect_faces(photos)
        text = detect_text(photos)
        celebrity=recognize_celebrities(photos)
        moderation = moderate_image(photos)
        full_list.append([photos,labels,faces,text,celebrity,moderation])
    df=pd.DataFrame(full_list,columns=['Filename','Labels,','Faces','Text','Celebrities','Moderation'])
    df.to_csv('TestAWS.csv')
    print(df)
        
        
if __name__ == "__main__":
    main()


# In[ ]:




