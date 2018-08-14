""" 
Script with Document class that will create documents such as operational schedules,
stop schedules.
"""
from PyPDF2 import PdfFileWriter, PdfFileReader

class Document():
    
    def __init__(self, doc_type):
        self.doc_type = doc_type
        
            
            
        
