# pattern_detection.py
from sklearn.cluster import KMeans

def detect_outbreak_clusters(df, n_clusters=2):
    features = df[['flu_cases', 'dengue_cases']]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(features)
    df['cluster'] = clusters
    return df
