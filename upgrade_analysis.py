
import os
import sys
import pandas as pd
import numpy as np

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

# Configure "Advanced" features
rules_df = clusterer.load_rules(RULES_INPUT_PATH, top_k=200, sort_by="lift")
X, meta = clusterer.build_final_features(weighting="lift", use_rfm=True)

print("--- MULTI-MODEL COMPARISON (K=2 to 6) ---")
k_range = [2, 3, 4, 5, 6]
comparison_df = clusterer.evaluate_models(X, k_range=k_range)

print("\nModel Comparison Results:")
print(comparison_df)
comparison_df.to_csv("data/processed/model_comparison.csv", index=False)

# Analyze best model for each metric
best_sil = comparison_df.loc[comparison_df['silhouette'].idxmax()]
best_dbi = comparison_df.loc[comparison_df['dbi'].idxmin()]
best_ch = comparison_df.loc[comparison_df['ch_index'].idxmax()]

print(f"\nBest Model by Silhouette: {best_sil['model']} at K={best_sil['k']} (Score: {best_sil['silhouette']:.4f})")
print(f"Best Model by DBI (Lower is better): {best_dbi['model']} at K={best_dbi['k']} (Score: {best_dbi['dbi']:.4f})")
print(f"Best Model by CH (Higher is better): {best_ch['model']} at K={best_ch['k']} (Score: {best_ch['ch_index']:.4f})")

# Final decision: K-Means at K=2 seems most robust across metrics or consistent with previous findings.
# But let's check Agglomerative at K=2 for actionable comparison.
labels_agg = clusterer.fit_agglomerative(X, n_clusters=2)
meta['cluster_agg'] = labels_agg
meta.to_csv("data/processed/customer_clusters_upgraded.csv", index=False)

print("\nSaved upgraded clusters to data/processed/customer_clusters_upgraded.csv")
