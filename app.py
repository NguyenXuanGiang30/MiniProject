
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set page config
st.set_page_config(page_title="Shopping Cluster Dashboard", layout="wide")

st.title("🛍️ Customer Segmentation Dashboard")
st.markdown("Dashboard phân tích khách hàng dựa trên **Luật kết hợp** và **RFM**.")

# Load data
@st.cache_data
def load_data():
    df_profile = pd.read_csv("data/processed/customer_clusters_profiled.csv")
    df_rfm = pd.read_csv("data/processed/cluster_rfm_summary.csv")
    df_rules = pd.read_csv("data/processed/cluster_top_rules.csv")
    df_compare = pd.read_csv("data/processed/systematic_comparison.csv")
    return df_profile, df_rfm, df_rules, df_compare

try:
    df_profile, df_rfm, df_rules, df_compare = load_data()
except Exception as e:
    st.error(f"Lỗi tải dữ liệu: {e}. Vui lòng chạy pipeline trước.")
    st.stop()

# Sidebar
st.sidebar.header("Filter & Navigation")
page = st.sidebar.selectbox("Chọn trang", ["Overview", "Cluster Profiling", "Association Rules", "Comparison", "Model Upgrade (Bonus)"])

if page == "Overview":
    st.header("1. Overview & Visualization")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Bản đồ phân cụm (PCA 2D)")
        if os.path.exists("data/processed/cluster_pca.png"):
            st.image("data/processed/cluster_pca.png", use_container_width=True)
        else:
            st.info("Không tìm thấy hình ảnh PCA.")
            
    with col2:
        st.subheader("Thống kê tổng quan")
        st.dataframe(df_rfm.style.background_gradient(cmap='Greens'))
        
        st.info("""
        **Nhận xét:**
        - Các cụm được phân tách khá rõ rệt trên không gian PCA.
        - Cụm 1 có số lượng khách hàng ít hơn nhưng giá trị mang lại cao hơn hẳn (tần suất mua cao, chi tiêu lớn).
        """)

elif page == "Cluster Profiling":
    st.header("2. Cluster Profiling & Personas")
    
    cluster_id = st.sidebar.selectbox("Chọn Cụm", df_rfm['cluster'].unique())
    
    # Custom definitions
    personas = {
        0: {
            "name": "Occasional Shoppers - Khách hàng vãng lai",
            "desc": "Khách hàng mua sắm không thường xuyên, giá trị đơn hàng trung bình thấp.",
            "strategy": "Gửi email re-engagement, tặng mã giảm giá cho đơn hàng tiếp theo để tăng tần suất quay lại."
        },
        1: {
            "name": "Loyal Decorators - Tín đồ trang trí thân thiết",
            "desc": "Khách hàng mua sắm thường xuyên, chi tiêu cao, đặc biệt quan tâm đến các bộ sản phẩm trang trí.",
            "strategy": "Chương trình khách hàng thân thiết (VIP), ưu đãi mua theo combo (Bundle Scandi decoration), giới thiệu sớm các bộ sưu tập mới."
        }
    }
    
    p = personas.get(cluster_id, {"name": "Unknown", "desc": "", "strategy": ""})
    
    st.subheader(f"Cụm {cluster_id}: {p['name']}")
    st.write(f"**Mô tả:** {p['desc']}")
    
    # Show stats
    row = df_rfm[df_rfm['cluster'] == cluster_id].iloc[0]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Số lượng", f"{int(row['Count'])}")
    c2.metric("Recency (Ngày)", f"{row['Recency']:.1f}")
    c3.metric("Frequency (Lần)", f"{row['Frequency']:.1f}")
    c4.metric("Monetary (GBP)", f"{row['Monetary']:.0f}")
    
    st.success(f"**Chiến lược Marketing:** {p['strategy']}")
    
    # Customer preview
    st.write("### Danh sách khách hàng tiêu biểu")
    st.dataframe(df_profile[df_profile['cluster'] == cluster_id].head(50))

elif page == "Association Rules":
    st.header("3. Top Association Rules & Bundles")
    
    cluster_id = st.sidebar.selectbox("Chọn Cụm", df_rules['cluster'].unique())
    
    st.subheader(f"Gợi ý mua sắm cho Cụm {cluster_id}")
    
    filtered_rules = df_rules[df_rules['cluster'] == cluster_id].sort_values('freq', ascending=False)
    
    st.write("Top quy luật mua hàng được kích hoạt nhiều nhất trong cụm này:")
    st.dataframe(filtered_rules[['rule', 'freq', 'lift']])
    
    st.write("### 💡 Gợi ý Bundle/Cross-sell")
    for idx, rule in filtered_rules.head(5).iterrows():
        st.info(f"Khuyến nghị Bundle: **{rule['rule']}** (Độ mạnh liên kết: {rule['lift']:.2f})")

elif page == "Comparison":
    st.header("4. Systematic Comparison of Feature Engineering")
    st.write("So sánh hiệu quả của các cấu hình đặc trưng khác nhau dựa trên Silhouette Score.")
    
    st.dataframe(df_compare)
    
    st.markdown("""
    **Kết luận:**
    - Việc thêm **RFM** và dùng **Lift** làm trọng số cải thiện đáng kể khả năng phân tách cụm.
    - Cấu hình **Top 200 luật + RFM** mang lại sự cân bằng tốt giữa tính chi tiết và tính ổn định.
    """)

elif page == "Model Upgrade (Bonus)":
    st.header("5. Model Upgrade: KMeans vs Agglomerative")
    st.write("Để nâng cao chất lượng phân tích, nhóm đã thực hiện so sánh hai thuật toán phân cụm khác nhau.")
    
    # Load model comparison data
    if os.path.exists("data/processed/model_comparison.csv"):
        df_model_comp = pd.read_csv("data/processed/model_comparison.csv")
        
        st.subheader("Bảng so sánh đa chỉ số (Multi-metric Comparison)")
        st.dataframe(df_model_comp.style.highlight_max(axis=0, subset=['silhouette', 'ch_index']).highlight_min(axis=0, subset=['dbi']))
        
        st.markdown("""
        **Các chỉ số đánh giá:**
        - **Silhouette Score**: (Cao là tốt) Đánh giá độ gắn kết của cụm.
        - **DBI (Davies-Bouldin Index)**: (Thấp là tốt) Tỷ lệ khoảng cách nội cụm và ngoại cụm.
        - **CH Index (Calinski-Harabasz)**: (Cao là tốt) Tỷ lệ biến thiên giữa các cụm và trong cụm.
        """)
        
        st.info("""
        **Phân tích chuyên sâu:**
        1. **Agglomerative Clustering (K=2)** cho thấy điểm **Silhouette (0.507)** và **DBI (1.159)** vượt trội so với KMeans. Điều này gợi ý rằng cấu trúc phân cấp (Hierarchical) phù hợp hơn để tách biệt nhóm khách hàng chủ chốt.
        2. Tuy nhiên, **KMeans** lại có điểm **CH Index** cao hơn, cho thấy sự phân tán giữa các cụm rất mạnh mẽ.
        3. Trong thực tế, mặc dù Agglomerative tốt hơn về mặt toán học, **KMeans** thường mang lại các tâm cụm (centroids) dễ giải thích hơn cho các chiến dịch marketing đại trà.
        """)
    else:
        st.warning("Vui lòng chạy `upgrade_analysis.py` để tạo dữ liệu so sánh.")
