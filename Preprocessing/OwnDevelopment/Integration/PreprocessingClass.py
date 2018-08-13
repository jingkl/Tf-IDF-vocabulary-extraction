'''
Created on 6 Aug 2018

@author: goksukara
'''

from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.porter import PorterStemmer
import pandas as pd
class PreprocessingFunctions():
    processed_data = []
    filenamecolumn=[]
    textcolumn=[]
    def __init__(self, dataframe):
        self.processed_data = dataframe
        self.filenamecolumn=self.processed_data.loc[:,'file_name']
        self.textcolumn=self.processed_data.loc[:,'text']
    def IterateoverRow(self):
        for index, row, in self.processed_data.iterrows():  
            self.cleanup(Cleanupper(),row['text'])
            #print(row['text'])
       
    def cleanup(self, cleanuper,row):
        #print(self.processed_data.loc[:,'text'])
        
        for cleanup_method in cleanuper.iterate():
            row = cleanup_method(row)
            print(row)
        #self.processed_data.loc[:,'text'] = t
    
    def tokenization(self):
        pass
    def add_document_dic(self):
        pass
    def save(self,filename):
        with open(filename, 'a',) as outfile:
            self.processed_data.to_csv(outfile,index=False,sep='\t',header=None)
           
       
    
    
    
class Cleanupper():
    p = PorterStemmer()
    def iterate(self):
        for cleanup_method in [self.convert_lowercase,
                               self.stopword_remove
                               ]:
            yield cleanup_method
    @staticmethod
    def stopword_remove(sentence):
        sentence=remove_stopwords(sentence)
        #print(sentence)
        return sentence

    def convert_lowercase(self,sentence):
        sentence=sentence.lower()
        return sentence
    def porter_stemmer(self,sentence):
        sentence=p.stem_sentence(sentence)
        return sentence    