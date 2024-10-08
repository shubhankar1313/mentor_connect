import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('mentors.csv')
# data

# print(data.columns)
# data

data = data.drop(["DOJ", "CURRENT DATE", "LEAVES USED", "LEAVES REMAINING"], axis=1)

# print(data.columns)
# data

from sklearn.feature_extraction.text import TfidfVectorizer
data['combined_features'] = data['UNIT'].fillna('') + ' ' + data['DESIGNATION'].fillna('') + ' ' + data['PAST EXP'].astype(str).fillna('')

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(data['combined_features'])

def search_keywords(keywords, tfidf_matrix, data, top_n=10):
    # Transform the input keywords into the tf-idf space
    query_vec = tfidf.transform([keywords])

    # Compute the cosine similarity between the query and all the documents
    cosine_similarities = (tfidf_matrix * query_vec.T).toarray().flatten()

    # Get the indices of the top_n most similar entries
    top_indices = cosine_similarities.argsort()[-top_n:][::-1]

    # Extract relevant columns and convert to a list of lists
    results = data.iloc[top_indices][['FIRST NAME', 'LAST NAME', 'UNIT', 'DESIGNATION', 'PAST EXP']].values.tolist()

    return results

# Example usage
search_results = search_keywords('IT', tfidf_matrix, data)
print(search_results)