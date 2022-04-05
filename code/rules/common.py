import pandas as pd
import os

###### Config file and sample sheets #####

samples = pd.read_csv("SampleDownloadList.Labelled.tsv",sep='\t', index_col=1)

# # How to access values in samples.tsv

# print(samples)
# print( expand("Hello {sample}", sample=samples.index) )
# print( samples.at["A", "R1"] )
