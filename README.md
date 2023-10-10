# Dicom-anonymizer
_______________________________________________________________________________________________________________
ITA-VERSION & ENG-VERSION
_______________________________________________________________________________________________________________
ITA-VERSION 

Le immagini biomediche tipicamente hanno un formato standardizzato, il formato DICOM.
Le immagini biomediche vanno considerate nella loro interezza, ricordando che sono strutturate
anche da una parte prettamente informativa, costituita da intestazioni contenti dati su struttura,
personale, paziente e macchinari, chiamati metadati. Anonimizzare i file dicom è necessario negli 
studi clinici e nella ricerca medica per far sì che i file possano essere forniti all’esterno senza 
violare il regolamento dell'Unione europea in materia di trattamento dei dati personali e di privacy,
nello specifico consideriamo l’articolo 9 paragrafo 1 il quale afferma che è una violazione esportare 
i dati di una persona sulla salute, sia fisica che mentale, passata presente e futura. 
Lo standard DICOM (Digital Imaging and Communication in Medicine) è stato utilizzato per archiviare,
visualizzare e trasmettere informazioni nell'imaging medico. È stato sviluppato per avere un formato 
standard in output da tutti i macchinari di imaging biomedico. Questo non contiene solo un'immagine 
anatomica, metabolica o funzionale , ma contiene anche delle intestazioni con un'ampia varietà di attributi. 
Ogni attributo è rappresentato da un tag univoco, il cui valore è contenuto nel value field VF. 
Ogni valore è tipizzato dal value representation o VR. 

Nel codice sono stati importati i moduli pydicom, glob, os e sys.
Pydicom ci da la possibilità di visualizzare e manipolare i file dicom.
Glob, OS e SYS sono stati utilizzati far interagire il programma con il sistema operativo. 
Ci si è affidati a Qt Designer per creare l’interfaccia grafica. Qt tramite il modulo «load ui» 
importa direttamente l’interfaccia grafica statica, priva di funzionalità nel codice sorgente. 
Ogni struttura vista e studiata è stata utilizzata a nostro vantaggio, poiché conoscendo il modo 
con cui le informazioni sono contenute è più facile capire in che modo si possono modificare. 
Nel secondo step sono state fatte diverse ricerche per capire quali fossero i tags da anonimizzare 
all’interno di un file DICOM, in modo che venisse garantita la privacy. Al termine queste ricerche 
sono tutti i tag da anonimizzare e sono stati inseriti in una lista utilizzata successivamente per
far presente al programma quali valori modificare.  

Utilizzando un modulo python chiamato time, si è riuscito ad avere contezza del tempo impiegato
nell’anonimizzazione della singola slice, che è in media di 1 millisecondo e 
con una deviazione standard di 0.721 ms. 
__________________________________________________________________________________________________________________________________________
ENG-VERSION 

Biomedical images typically have a standardized format, the DICOM format. Biomedical images should be considered in their entirety,
bearing in mind that they are structured, including an informational part consisting of headers containing data about the structure,
personnel, patients, and equipment, known as metadata. Anonymizing DICOM files is necessary in clinical studies and medical research
to ensure that files can be shared externally without violating the European Union regulations on personal data processing and privacy.
Specifically, we consider Article 9, paragraph 1, which states that exporting a person's health data, both physical and mental, 
past, present, and future, is a violation.The DICOM standard (Digital Imaging and Communication in Medicine) has been used to store,
display, and transmit information in medical imaging. It was developed to provide a standardized output format for all biomedical
imaging equipment. This format not only contains an anatomical, metabolic, or functional image but also includes headers with a wide 
variety of attributes. Each attribute is represented by a unique tag, whose value is contained in the Value Field (VF). Each value is 
typed by the Value Representation (VR).

In the code, the pydicom, glob, os, and sys modules have been imported. Pydicom allows us to view and manipulate DICOM files.
Glob, OS, and SYS were used to interact with the operating system. We relied on Qt Designer to create the graphical interface.
Qt, through the "load ui" module, directly imports the static graphical interface, devoid of functionality in the source code.
Each structure seen and studied has been used to our advantage since understanding how information is contained makes it easier 
to understand how it can be modified. In the second step, several searches were conducted to understand which tags needed to be
anonymized within a DICOM file to ensure privacy. At the end of these searches, all the tags to be anonymized were identified 
and placed in a list used later to inform the program which values to modify.

Using a Python module called time, we were able to measure the time taken for anonymizing a single slice,
which averages around 1 millisecond with a standard deviation of 0.721 milliseconds.
___________________________________________________________________________________________________________________________________________
