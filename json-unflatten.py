#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 12:08:56 2021

@author: azindani
"""

import json


temp ={}
data={}
parentKey =''
alternate={}
f_read = open("sample_products.txt", "r")
f_write = open("unflat.json", "w")
print("Started")
for x in f_read:
    
    x = x.strip()
    
    
    if len(x.split()) == 0:
        print("Empty Space")
    
        
    if len(x.split("="))== 2:
        key,value = x.split("=")
        if key == 'refNum':
            parentKey = "id: "+value
            
        if len(key.split("_"))== 2:
        
            temp ={}
           
            keys1,key1=key.split("_")
            if value=='':
                value= 'NULL'
            if keys1 in data:
                temp[key1]=value
                data[keys1]=[data[keys1],temp]
            else:
                temp[key1]=value
                data[keys1]=temp
        else:
            data[key]=value
            
        if value ==" ":
            value = "null"
            
            
    if x == 'REC$$':
        eject = json.dumps({parentKey:data  }, sort_keys=True, indent=4)
        f_write.write(str(eject)+'\n')
    
        body={}
        parentKey=''
        keys1 =''
        keys= ''
        
    
f_write.close()
f_read.close()
print("Completed")