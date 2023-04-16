# -*- coding: utf-8 -*-
#!pip install -q streamlit

#!npx localtunnel --port 8501

#!npm install localtunnel

#!pip install db-sqlite3

#!pip install matplotlib
import git
import pandas as pd
import json
import os
import numpy as np
#import matplotlib.pyplot as plt
import requests
#import plotly.express as px
import streamlit as st

#This is to direct the path to get the data as states

path="C:/Users/s/PycharmProjects/mystreamlit/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
#Agg_state_list
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm1={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr_list=os.listdir(p_i)    
    for j in Agg_yr_list:
        p_j=p_i+j+"/"
        Agg_qtr_list=os.listdir(p_j)        
        for k in Agg_qtr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
               clm1['State'].append(i)
               clm1['Year'].append(j)
               name=z['name']
               count=z['paymentInstruments'][0]['count']
               amount=z['paymentInstruments'][0]['amount']
               clm1['Transaction_type'].append(name)
               clm1['Transaction_count'].append(count)
               clm1['Transaction_amount'].append(amount)
               #clm['State'].append(i)
               #clm['Year'].append(j)
               clm1['Quarter'].append(int(k.strip('.json')))


#now creating and importing i, j, k, into the dataframe
df1 = pd.DataFrame(clm1)

df1.head()

df1.isnull().sum()

path= "C:/Users/s/PycharmProjects/mystreamlit/pulse/data/aggregated/user/country/india/state/"
Agg_state_list=os.listdir(path)
clm2={'State':[], 'Year':[],'Quarter':[],'Brand':[], 'Count':[], 'Percentage':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr_list = os.listdir(p_i)    
    for j in Agg_yr_list:
        p_j=p_i+j+"/"
        Agg_qtr_list=os.listdir(p_j)        
        for k in Agg_qtr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
                for z in D['data']['usersByDevice']:
                   clm2['Brand'].append(z['brand'])
                   clm2['Count'].append(z['count'])
                   clm2['Percentage']=(z['percentage'])
                   clm2['State'].append(i)
                   clm2['Year'].append(j)
                   clm2['Quarter'].append(int(k.strip(".json")))
            except:
              pass


#now creating and importing i, j, k, into the dataframe
df2= pd.DataFrame(clm2)

df2.head()

df2.isnull().sum()

path="C:/Users/s/PycharmProjects/mystreamlit/pulse/data/map/transaction/hover/country/india/state/"
Map_state_list=os.listdir(path)
clm3={'State':[], 'Year':[],'Quarter':[],'District':[], 'Count':[], 'Amount':[]}
for i in Map_state_list:
  p_i = path+i+'/'
  Map_yr_list=os.listdir(p_i)
  for j in Map_yr_list:
    p_j=p_i+j+'/'
    Map_qtr_list=os.listdir(p_j)
    for k in Map_qtr_list:
      p_k=p_j+k
      data=open(p_k,'r')
      D=json.load(data)
      for z in D['data']['hoverDataList']:
        name=z['name']
        count=z['metric'][0]['count']  # giving variable name to value inside the z
        amount=z['metric'][0]['amount']
        clm3['District'].append(name)   # adding the value from variable to list inside clm2
        clm3['Count'].append(count)
        clm3['Amount'].append(amount)
        clm3['State'].append(i)
        clm3['Year'].append(j)
        clm3['Quarter'].append(int(k.strip('.json')))

df3=pd.DataFrame(clm3)
df3.head()

df3.isnull().sum()

path = "C:/Users/s/PycharmProjects/mystreamlit/pulse/data/map/user/hover/country/india/state/"
Map_state_list= os.listdir(path)

clm4={'State':[], 'Year':[],'Quarter':[],'District':[], 'Users':[]}
for i in Map_state_list:
  p_i=path+i+'/'
  Map_yr_list=os.listdir(p_i)
  for j in Map_yr_list:
    p_j=p_i+j+'/'
    Map_qtr_list=os.listdir(p_j)
    for k in Map_qtr_list:
      p_k=p_j+k
      data =open(p_k,'r')
      d=json.load(data)
      for z, values in d['data']['hoverData'].items():
        users=values['registeredUsers']
        dist=z
        clm4['State'].append(i)
        clm4['Year'].append(j)
        clm4['Quarter'].append(int(k.strip('.json')))
        clm4['District'].append(dist)
        clm4['Users'].append(users)

#succesfully created a dataframe
df4=pd.DataFrame(clm4)
df4.head()

df4.isnull().sum()

path="C:/Users/s/PycharmProjects/mystreamlit/pulse/data/top/transaction/country/india/state/"
Top_state_list=os.listdir(path)

clm5={'State':[], 'Year':[],'Quarter':[],'District':[], 'Count':[], 'Amount':[]}
for i in Top_state_list:
  p_i=path+i+'/'
  Top_yr_list=os.listdir(p_i)
  for j in Top_yr_list:
    p_j=p_i+j+'/'
    Top_qtr_list=os.listdir(p_j)
    for k in Top_qtr_list:
      p_k=p_j+k
      data =open(p_k,'r')
      d=json.load(data)
      for z in d['data']['districts']:
        cnt=z['metric']['count']
        amount=z['metric']['amount']
        name=z['entityName']
        clm5['State'].append(i)
        clm5['Year'].append(j)
        clm5['Quarter'].append(int(k.strip('.json')))
        clm5['District'].append(name)
        clm5['Count'].append(cnt)
        clm5['Amount'].append(amount)

#succesfully created a dataframe
df5=pd.DataFrame(clm5)
df5.head()

df5.isnull().sum()

path="C:/Users/s/PycharmProjects/mystreamlit/pulse/data/top/user/country/india/state/"
Top_state_list=os.listdir(path)


clm6={'State':[], 'Year':[],'Quarter':[],'District':[], 'Users':[]}
for i in Top_state_list:
      p_i=path+i+'/'
      Top_yr_list=os.listdir(p_i)
      for j in Top_yr_list:
        p_j=p_i+j+'/'
        Top_qtr_list=os.listdir(p_j)
        for k in Top_qtr_list:
           p_k=p_j+k
           data =open(p_k,'r')
           d=json.load(data)
           for z in d['data']['districts']:
             name=z['name']
             users=z['registeredUsers']
             clm6['State'].append(i)
             clm6['Year'].append(j)
             clm6['Quarter'].append(int(k.strip('.json')))
             clm6['District'].append(name)
             clm6['Users'].append(users)

# succesfuly created the dataframe
df6=pd.DataFrame(clm6)
df6.head()

df6.isnull().sum()

df3['State'].value_counts()
# this is just to try value counts inside the dataframes

# converting all dataframe into csv file
df1.to_csv('agg_transaction.csv',index=False)
df2.to_csv('agg_users.csv',index=False)
df3.to_csv('map_transcation.csv',index=False)
df4.to_csv('map_users.csv',index=False)
df5.to_csv('top_transcation.csv',index=False)
df6.to_csv('top_users.csv',index=False)
print("created all csv files")

