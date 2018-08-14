'''
Created on 6 Aug 2018

@author: goksukara
'''
import pandas as pd
from PreprocessingClass import PreprocessingFunctions,Cleanupper 
corpuspath='/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/Data/'

filename='corpus'
for chunck_df in pd.read_csv(corpuspath+filename+'.csv',dtype={'file_name': str,"text": str}, chunksize=3,header=0,index_col=False,sep='\t',encoding='utf-8'):
    
    dataprocesing=PreprocessingFunctions(chunck_df)
    dataprocesing.IterateoverRow()
    
    
    dataprocesing.save(filename+'_preprocessed.csv')