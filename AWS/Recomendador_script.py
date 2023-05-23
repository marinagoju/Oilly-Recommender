import numpy as np
import pandas as pd
import scipy
import sys
import re


import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

sys.path.append(r"Utilities")
import Utilities 

def recomendador(nombre):
    dataset=pd.read_csv('df_comercios.csv')
    dataset['combinacion'] = dataset[['description', 'review', 'alias','distrito']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
    dataset['Descripcion_tok'] = dataset['combinacion'].apply(lambda x: Utilities.tokenizacion(x)) 
    dataset['Descripcion_tok'] = dataset['Descripcion_tok'].apply(lambda x:Utilities.removeStopwords(x)) 
    dataset['Descripcion_tok'] = dataset['Descripcion_tok'].apply(lambda x:Utilities.removePunctuation(x)) 
    dataset['Descripcion_clean'] = dataset['Descripcion_tok'].apply(lambda x:Utilities.arrayToString(x))

    vectorizer = CountVectorizer(encoding='iso-8859-1')  
    MatrizFrecuencias = vectorizer.fit_transform(dataset['Descripcion_clean'])

    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(MatrizFrecuencias)

    tdm = tfidf.transpose()
    dtm = tfidf
    Simil = dtm.dot(tdm)

    SimilDF = pd.DataFrame(data = Simil.toarray(), index=dataset['id'].values,columns=dataset['id'].values)

    Top = 7
    nombre_restaurante= nombre
    Num_restaurante = SimilDF.index.get_loc(nombre_restaurante)
    
    RecomendacionItemItem = SimilDF.iloc[(-SimilDF.iloc[:, Num_restaurante]).argsort()[1:(Top+1)].values, Num_restaurante] 
    

    return RecomendacionItemItem




