# useful libraries to import

from turtle import color
import pandas as pd
import numpy as np
import sklearn.decomposition
import matplotlib.pyplot as plt

def plot_pca(pca , 
             bigwig_metadata=None,
             metadata_label_column=None, 
             alpha=0.5, 
             lw=0, 
             figsize=(8,8)):
    
    """ 
    Skeleton for plotting PCA and annotating the plot. 
    Can be modified/extended to answer various questions.
    """
    
    
    if metadata_label_column is not None:
        if bigwig_metadata is None: 
            raise ValueError("must provide metadata table to label by a metadata column") 
        labels = [bigwig_metadata.query(
                    "`File accession`==@ file_accession ").loc[:,metadata_label_column].values[0]
                  for file_accession in pca.feature_names_in_]
        le = sklearn.preprocessing.LabelEncoder()
        le.fit(labels)
        labels = le.transform(labels)
    else: 
        labels = None
        
    plt.figure(figsize=figsize)
    p = plt.scatter(pca.components_[0],
                pca.components_[1],
                c = labels,
                alpha = alpha,
                lw = lw)
    if labels is not None: 
        plt.legend(handles = p.legend_elements()[0], 
                   labels = le.classes_.tolist())
        plt.legend(handles = p.legend_elements()[0], 
                   labels = le.classes_.tolist())
        plt.title('PCA Plot Colored By: '+metadata_label_column)
                   
    plt.xlabel('PC1')
    plt.ylabel('PC2')

