
import os
import sys
import pandas as pd
import numpy as np

# Determine correct project root
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

# Load rules
rules_df = clusterer.load_rules(
    rules_csv_path=RULES_INPUT_PATH,
    top_k=200,
    sort_by="lift",
)

print("--- VARIATION 1: BASELINE (Binary features) ---")
X1, meta1 = clusterer.build_final_features(
    weighting="none",
    use_rfm=False,
    min_antecedent_len=1,
)
sil_df1 = clusterer.choose_k_by_silhouette(X1, k_min=2, k_max=10)
print("Top 3 K by Silhouette (Baseline):")
print(sil_df1.head(3))

print("\n--- VARIATION 2: ADVANCED (Lift weighting + RFM) ---")
X2, meta2 = clusterer.build_final_features(
    weighting="lift",
    use_rfm=True,
    rfm_scale=True,
    rule_scale=False,
    min_antecedent_len=1,
)
sil_df2 = clusterer.choose_k_by_silhouette(X2, k_min=2, k_max=10)
print("Top 3 K by Silhouette (Advanced):")
print(sil_df2.head(3))

# Choose best K for advanced and train
best_k = int(sil_df2.loc[0, 'k'])
print(f"\nFinal Choice for Advanced: K={best_k}")
labels = clusterer.fit_kmeans(X2, n_clusters=best_k)
meta2['cluster'] = labels

# Save final result
meta2.to_csv("data/processed/customer_clusters_final.csv", index=False)
print(f"Saved final clusters to data/processed/customer_clusters_final.csv")
