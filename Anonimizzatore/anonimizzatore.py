"""
Created on Tue Apr 26 15:27:41 2022

@author: Giuseppe Squillace
"""
import pydicom 
import glob 
import sys
import os
import time 

from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QDialog , QApplication, QFileDialog
from PyQt5.uic import loadUi 

class MainWindow(QDialog):
    
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.browse.clicked.connect(self.browsefiles_input)
        self.browse_2.clicked.connect(self.browsefiles_output)
        self.button_1.clicked.connect(self.onRunClick)
    
    def browsefiles_input(self):
        self.fpath_1 = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.filename.setText(self.fpath_1)

    
    def browsefiles_output(self):
        self.fpath_2 = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.filename_2.setText(self.fpath_2)
    
    def onRunClick(self):  
        Data_folder = glob.glob(self.fpath_1 + "\*")
    
        data_elements = ["StudyDate", "SeriesDate" , "AcquisitionDate" , "ContentDate", "PatientsTelephoneNumbers",
                         "OverlayDate", "CurveDate", "AcquisitionDatetime", "StudyTime","PatientsMothersBirthName",
                         "SeriesTime", "AcquisitionTime", "ContentTime", "OverlayTime","PhysicianOfRecordIDSequence",
                         "CurveTime", "AccessionNumber", "InstitutionName", "InstitutionAddress","OtherPatientNames",
                         "ReferringPhysiciansName", "ReferringPhysiciansAddress","ReferringPhysiciansTelephoneNumber",
                         "ReferringPhysicianIDSequence","InstitutionalDepartmentName","StudyID","CurrentPatientLocation",
                         "PerformingPhysiciansName", "PerformingPhysicianIDSequence", "NameOfPhysicianReadingStudy",
                         "PhysicianReadingStudyID", "Sequence", "OperatorsName", "PatientName", "PatientID","Time",
                         "IssuerOfPatientID", "PatientsBirthDate", "PatientsBirthTime", "PatientsSex","PersonName", 
                         "OtherPatientIDs", "PatientsBirthName", "PatientsAge" ,"PatientsAddress","DateTime", "Date", 
                          "CountryOfResidence", "RegionOfResidence","PatientsInstitutionResidence","PhysicianOfRecord",
                         "StudyInstanceUID", "SeriesInstanceUID", "FrameOfReferenceUID", "SeriesDescription", 
                         "StudyDescription", "MediaStorageSOPInstanceUID"]
        
    
        for i, current_file in enumerate(Data_folder):
            
            try:
                my_dataset = pydicom.dcmread(current_file) 
            except Exception:
                print("ERROR!")
                continue
            self.Anonymizer_tags_single_file(my_dataset, data_elements)        
            enumerate_slices = (str(i) +'.dcm')
            my_dataset.save_as(os.path.join(self.fpath_2, enumerate_slices))
            del(my_dataset)
            #print(my_dataset) 

   
        
    def Anonymizer_tags_single_file(self, dataset, data_element):
        t0 = time.time()
        for element in data_element:
            if hasattr(dataset, element):
                dataset[element].value = "anonymus"          
                tempo_anonimizzazione_slice = (str(t0 - time.time()) + (" secondi"))
        print (("tempo di anomizizzazione della slice: ") + str(tempo_anonimizzazione_slice))
 
    
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1112)
widget.setFixedHeight(678)
widget.show()
sys.exit(app.exec_()) 