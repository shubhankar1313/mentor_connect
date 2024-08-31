import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import json

# Load your data (ensure the path is correct)
data = pd.read_csv('mentors.csv')
data = data.drop(["DOJ", "CURRENT DATE", "LEAVES USED", "LEAVES REMAINING"], axis=1)
data['combined_features'] = data['UNIT'].fillna('') + ' ' + data['DESIGNATION'].fillna('') + ' ' + data['PAST EXP'].astype(str).fillna('')

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(data['combined_features'])

def search_keywords(keywords, tfidf_matrix, data, top_n=10):
    query_vec = tfidf.transform([keywords])
    cosine_similarities = (tfidf_matrix * query_vec.T).toarray().flatten()
    top_indices = cosine_similarities.argsort()[-top_n:][::-1]
    results = data.iloc[top_indices][['FIRST NAME', 'LAST NAME', 'UNIT', 'DESIGNATION', 'PAST EXP']].values.tolist()
    return results

if __name__ == "__main__":
    keyword = sys.argv[1]
    search_results = search_keywords(keyword, tfidf_matrix, data)
    print(json.dumps(search_results))
