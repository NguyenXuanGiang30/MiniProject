
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler

# Ensure src is in path
project_root = os.getcwd()
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.append(src_path)

# Paths
CLEANED_DATA_PATH = "data/processed/cleaned_uk_data.csv"
CLUSTERS_PATH = "data/processed/customer_clusters_upgraded.csv"
RULES_PATH = "data/processed/rules_apriori_filtered.csv"
OUTPUT_DIR = "data/processed"

def generate_roi_visuals():
    # Load data
    df_clean = pd.read_csv(CLEANED_DATA_PATH)
    df_clusters = pd.read_csv(CLUSTERS_PATH)
    df_rules = pd.read_csv(RULES_PATH)
    
    # Merge cluster labels with RFM data
    # Assuming df_clusters has CustomerID, Recency, Frequency, Monetary, cluster_agg
    cluster_col = 'cluster_agg'
    
    # 1. Revenue Distribution by Cluster
    plt.figure(figsize=(10, 6))
    rev_dist = df_clusters.groupby(cluster_col)['Monetary'].sum()
    plt.pie(rev_dist, labels=[f"Cluster {i}" for i in rev_dist.index], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("viridis"))
    plt.title("Phân bổ doanh thu theo cụm (Revenue Distribution)")
    plt.savefig(f"{OUTPUT_DIR}/revenue_distribution.png")
    plt.close()

    # 2. ROI Projections
    # Assumptions:
    # Cluster 0: Occasional Shoppers, Cost=$1, Conv=5%, Lift=1.2
    # Cluster 1: Loyal Decorators, Cost=$2, Conv=15%, Lift=1.5
    roi_data = []
    for cid in df_clusters[cluster_col].unique():
        count = len(df_clusters[df_clusters[cluster_col] == cid])
        avg_monetary = df_clusters[df_clusters[cluster_col] == cid]['Monetary'].mean()
        
        if cid == 0:
            cost_per_cust = 1.0
            conv_rate = 0.05
            lift = 1.2
        else:
            cost_per_cust = 2.0
            conv_rate = 0.15
            lift = 1.5
            
        total_cost = count * cost_per_cust
        projected_rev = count * conv_rate * (avg_monetary * lift)
        roi = ((projected_rev - total_cost) / total_cost) * 100
        
        roi_data.append({
            'Cluster': cid,
            'Total Cost': total_cost,
            'Projected Revenue': projected_rev,
            'ROI (%)': roi
        })
    
    df_roi = pd.DataFrame(roi_data)
    df_roi.to_csv(f"{OUTPUT_DIR}/roi_projections.csv", index=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_roi, x='Cluster', y='ROI (%)', palette="viridis")
    plt.title("Dự kiến tỷ lệ hoàn vốn (Projected ROI %)")
    plt.ylabel("ROI (%)")
    plt.savefig(f"{OUTPUT_DIR}/roi_projection.png")
    plt.close()

    # 3. Customer Lifetime Value (CLV) Estimation
    # Simple CLV = Avg Order Value * Frequency * Lifespan (assume 2 years) * Margin (assume 30%)
    df_clusters['CLV'] = (df_clusters['Monetary'] / df_clusters['Frequency']) * df_clusters['Frequency'] * 2 * 0.3
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_clusters, x=cluster_col, y='CLV', palette="viridis")
    plt.title("Ước tính giá trị vòng đời khách hàng (CLV Estimation)")
    plt.yscale('log')
    plt.savefig(f"{OUTPUT_DIR}/clv_distribution.png")
    plt.close()

    # 4. Churn Risk (based on Recency)
    # Risk Categories: Low (Recency < 30), Medium (30-90), High (>90)
    def churn_risk(r):
        if r < 30: return 'Low'
        elif r < 90: return 'Medium'
        else: return 'High'
    
    df_clusters['ChurnRisk'] = df_clusters['Recency'].apply(churn_risk)
    churn_matrix = pd.crosstab(df_clusters[cluster_col], df_clusters['ChurnRisk'], normalize='index') * 100
    
    plt.figure(figsize=(10, 6))
    churn_matrix.plot(kind='bar', stacked=True, color=['#4caf50', '#ffeb3b', '#f44336'])
    plt.title("Tỷ lệ rủi ro rời bỏ khách hàng (Churn Risk by Cluster)")
    plt.ylabel("Phần trăm (%)")
    plt.legend(title='Risk Level')
    plt.savefig(f"{OUTPUT_DIR}/churn_risk.png")
    plt.close()

    # 5. Radar Chart for Cluster Profiles
    # Normalize RFM for radar chart
    rfm_cols = ['Recency', 'Frequency', 'Monetary']
    scaler = MinMaxScaler()
    df_norm = pd.DataFrame(scaler.fit_transform(df_clusters[rfm_cols]), columns=rfm_cols)
    df_norm[cluster_col] = df_clusters[cluster_col]
    cluster_profiles = df_norm.groupby(cluster_col).mean().reset_index()

    categories = rfm_cols
    fig = go.Figure()

    for i, row in cluster_profiles.iterrows():
        fig.add_trace(go.Scatterpolar(
            r=row[categories].values,
            theta=categories,
            fill='toself',
            name=f'Cluster {int(row[cluster_col])}'
        ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True,
        title="Chân dung các cụm khách hàng (Cluster Profiles)"
    )
    # Plotly to static image (requires kaleido, but we can save as html or just rely on plt for static)
    # We will use mathplotlib for the report to be safe if kaleido is missing
    
    plt.figure(figsize=(8, 8))
    for i, row in cluster_profiles.iterrows():
        values = row[categories].values.tolist()
        values += values[:1]
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        angles += angles[:1]
        
        ax = plt.subplot(1, 1, 1, polar=True)
        ax.plot(angles, values, label=f'Cluster {int(row[cluster_col])}')
        ax.fill(angles, values, alpha=0.25)
        
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    plt.title("Chân dung các cụm (Radar Chart)")
    plt.legend()
    plt.savefig(f"{OUTPUT_DIR}/cluster_radar.png")
    plt.close()

    print("Success: Generated ROI and strategic visualizations in data/processed/")

if __name__ == "__main__":
    generate_roi_visuals()
