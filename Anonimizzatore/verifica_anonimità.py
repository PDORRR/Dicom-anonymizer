# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 09:42:05 2022

@author: acer
"""

import pydicom
import os
import random 

path = r"C:\Users\acer\Desktop\TESI\CODICE GUI DATASET\dataset_anonimizzato_Aryanto\0.dcm"
root, extension = os.path.splitext(path)

print(8888888888888888888888888888888888888888888888888888888888888888888888888)
print() 

if extension == ".dcm" :
    ds = pydicom.dcmread(path)
    print ("HAI INSERITO UN FILE DICOM")
    
print(ds)

