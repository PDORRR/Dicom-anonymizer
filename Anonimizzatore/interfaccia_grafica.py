# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:53:58 2022

@author: acer
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 15:27:41 2022

@author: acer
"""

import sys 
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QDialog , QApplication, QFileDialog
from PyQt5.uic import loadUi 

class MainWindow(QDialog): 
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.browse.clicked.connect(self.browsefiles_input)
        self.browse_2.clicked.connect(self.browsefiles_output)
        self.button_1.clicked.connect(self.Anonymize_button)
        
    def browsefiles_input(self):
        fpath_1 = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.filename.setText(fpath_1)
    
    def browsefiles_output(self):
        fpath_2 = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.filename_2.setText(fpath_2)
        
    def Anonymize_button(self):
        print ("PROVA PUSH BUTTON_1 !")
        #StampaDicom(fn, os.path.abspath(sys.argv[2]))
        
        
    
        
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1112)
widget.setFixedHeight(678)
widget.show()
sys.exit(app.exec_()) 