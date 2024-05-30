import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

'''
    The similarity between drugs and drugs was obtained by using Jaccard similarity
'''


df = pd.read_csv('../data/drug_fingerprints.csv', header=None, skiprows=1)

drug_names = df.iloc[:, 0].tolist()

binary_df = df.drop(columns=[0])

binary_df = binary_df.applymap(int)

cosine_sim_matrix = cosine_similarity(binary_df)

results = []

for i in range(len(drug_names)):
    for j in range(i + 1, len(drug_names)):
        drug1 = drug_names[i]
        drug2 = drug_names[j]
        cosine_sim = cosine_sim_matrix[i, j]

        results.append([drug1, drug2, cosine_sim])

results_df = pd.DataFrame(results, columns=['Array1', 'Array2', 'Cosine Similarity'])

results_df.to_csv('../data/drug_similarity_cosine.csv', index=False)
