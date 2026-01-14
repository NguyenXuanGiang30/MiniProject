
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# Ensure src is in path
project_root = os.getcwd()
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.append(src_path)

from cluster_library import RuleBasedCustomerClusterer

# Paths
CLEANED_DATA_PATH = "data/processed/cleaned_uk_data.csv"
RULES_INPUT_PATH = "data/processed/rules_apriori_filtered.csv"

# Load data
df_clean = pd.read_csv(CLEANED_DATA_PATH, parse_dates=["InvoiceDate"])
clusterer = RuleBasedCustomerClusterer(df_clean=df_clean)
clusterer.build_customer_item_matrix(threshold=1)

def evaluate_config(top_k, weighting, use_rfm):
    rules_df = clusterer.load_rules(
        rules_csv_path=RULES_INPUT_PATH,
        top_k=top_k,
        sort_by="lift",
    )
    X, meta = clusterer.build_final_features(
        weighting=weighting,
        use_rfm=use_rfm,
        rfm_scale=True,
        rule_scale=False,
    )
    # Check silhouette for K=2 to K=5
    results = []
    for k in [2, 3, 4, 5]:
        labels = clusterer.fit_kmeans(X, n_clusters=k)
        score = silhouette_score(X, labels)
        results.append(score)
    return max(results), [2,3,4,5][np.argmax(results)]

print("--- SYSTEMATIC COMPARISON ---")
configs = [
    (50, "none", False),
    (50, "lift", False),
    (50, "lift", True),
    (200, "none", False),
    (200, "lift", False),
    (200, "lift", True),
    (200, "lift_x_conf", True),
]

comparison_data = []
for top_k, weighting, use_rfm in configs:
    score, best_k = evaluate_config(top_k, weighting, use_rfm)
    comparison_data.append({
        "Top-K": top_k,
        "Weighting": weighting,
        "Use RFM": use_rfm,
        "Best Silhouette": f"{score:.4f}",
        "Chosen K": best_k
    })

comparison_df = pd.DataFrame(comparison_data)
print(comparison_df)
comparison_df.to_csv("data/processed/systematic_comparison.csv", index=False)

print("\n--- FINAL PROFILING (Top 200, Lift, RFM) ---")
# Final model: Top 200, Lift weighting, with RFM
rules_df = clusterer.load_rules(RULES_INPUT_PATH, top_k=200, sort_by="lift")
X, meta = clusterer.build_final_features(weighting="lift", use_rfm=True)
k = 2  # Based on previous run or comparison result
labels = clusterer.fit_kmeans(X, n_clusters=k)
meta['cluster'] = labels

# RFM Aggregates
rfm_summary = meta.groupby('cluster').agg({
    'CustomerID': 'count',
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean'
}).rename(columns={'CustomerID': 'Count'})
print("\nRFM Summary per Cluster:")
print(rfm_summary)
rfm_summary.to_csv("data/processed/cluster_rfm_summary.csv")

# Top rules per cluster
# We check which indices in X (the rule part) are > 0 most often for each cluster
rule_features = X[:, :200]
top_rules_per_cluster = {}

for c in range(k):
    cluster_indices = meta[meta['cluster'] == c].index
    cluster_rule_freq = (rule_features[cluster_indices] > 0).mean(axis=0)
    top_indices = np.argsort(cluster_rule_freq)[::-1][:10]
    
    top_rules = []
    for idx in top_indices:
        if cluster_rule_freq[idx] > 0:
            top_rules.append({
                "rule": rules_df.iloc[idx]['rule_str'],
                "freq": cluster_rule_freq[idx],
                "lift": rules_df.iloc[idx]['lift']
            })
    top_rules_per_cluster[c] = top_rules


# Print top 3 rules for C0 and C1 (Safe print)
for c, rules in top_rules_per_cluster.items():
    print(f"\nCluster {c} Top Rules:")
    for r in rules[:3]:
        # Replace arrow for console printing
        safe_rule = r['rule'].replace(" \u2192 ", " -> ")
        print(f" - {safe_rule} (Usage in cluster: {r['freq']:.2%})")

# Export top rules for each cluster to a CSV for the dashboard
top_rules_rows = []
for c, rules in top_rules_per_cluster.items():
    for r in rules:
        top_rules_rows.append({"cluster": c, "rule": r['rule'], "freq": r['freq'], "lift": r['lift']})
pd.DataFrame(top_rules_rows).to_csv("data/processed/cluster_top_rules.csv", index=False)

# Save final clusters with meta for Dashboard
meta.to_csv("data/processed/customer_clusters_profiled.csv", index=False)

# Visualization 2D
Z = clusterer.project_2d(X, method="pca")
plt.figure(figsize=(10, 7))
scatter = plt.scatter(Z[:, 0], Z[:, 1], c=labels, cmap='viridis', alpha=0.6)
plt.colorbar(scatter, label='Cluster')
plt.title("Customer Segmentation - PCA 2D Projection")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.savefig("data/processed/cluster_pca.png")
print("\nSaved PCA plot to data/processed/cluster_pca.png")
