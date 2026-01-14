# 🛒 Shop Customer Segmentation via Association Rules

Dự án này thực hiện phân khúc khách hàng dựa trên hành vi mua sắm kết hợp (Co-purchase behavior) bằng cách sử dụng các thuật toán khai thác luật kết hợp (Association Rules) như Apriori và FP-Growth, kết hợp với các chỉ số RFM truyền thống.

## 🚀 Quy trình thực hiện (Pipeline)

Quy trình được thiết kế theo các bước logic từ tiền xử lý dữ liệu đến ứng dụng thực tế:

1.  **Preprocessing & EDA**: Làm sạch dữ liệu, xử lý nhiễu và phân tích khám phá (EDA).
2.  **Basket Preparation**: Chuyển đổi dữ liệu giao dịch thành ma trận giỏ hàng (Basket matrix).
3.  **Association Rule Mining**: 
    - Khai thác luật bằng thuật toán **Apriori** và **FP-Growth**.
    - Lọc luật dựa trên các chỉ số: Support, Confidence, Lift.
4.  **Feature Engineering**:
    - Chuyển đổi các luật kết hợp thành đặc trưng hành vi của khách hàng.
    - So sánh giữa đặc trưng nhị phân- [x] Define targeted marketing strategies per cluster
- [x] Build Streamlit dashboard
- [x] **BLOG**: Create comprehensive project blog post
- [x] **UPGRADE**: Implement multi-model comparison (K-Means vs Agglomerative)
**: 
    - So sánh **K-Means** và **Agglomerative Clustering**.
    - Sử dụng các metric nâng cao: Silhouette, Davies-Bouldin Index (DBI), Calinski-Harabasz Index (CH).
6.  **Customer Clustering**: 
    - Lựa chọn số cụm K tốt nhất dựa trên phân tích đa chỉ số.
7.  **Profiling & Marketing Strategy**:
    - Phân tích chân dung khách hàng (Personas).
    - Đề xuất chiến lược Marketing cụ thể cho từng nhóm.
8.  **Interactive Dashboard**: Trực quan hóa kết quả qua giao diện Streamlit.

## 📦 Cấu trúc thư mục

- `data/`: Chứa dữ liệu thô và dữ liệu đã qua xử lý (CSV, Parquet).
- `notebooks/`: Chứa các Jupyter Notebook thực hiện từng bước của dự án.
- `src/`: Chứa thư viện `cluster_library.py` - lõi xử lý của dự án.
- `app.py`: Ứng dụng Streamlit Dashboard.
- `report.html`: Báo cáo kết quả dự án dưới dạng HTML tĩnh (không cần chạy server).
- `BLOG.md`: Bài viết Blog tóm tắt quá trình và kết quả dự án.
- `run_papermill.py`: Script tự động chạy toàn bộ pipeline notebook.
- `final_analysis.py`: Script thực hiện so sánh hệ thống và profiling cuối cùng.

## 🛠️ Cài đặt & Sử dụng

### 1. Cài đặt môi trường
Khuyên dùng Python 3.10+.
```bash
pip install -r requirements.txt
```

### 2. Chạy toàn bộ Pipeline
Bạn có thể chạy toàn bộ các bước phân tích tự động qua Papermill:
```bash
python run_papermill.py
```

### 3. Chạy Dashboard
Để xem kết quả phân cụm và gợi ý Marketing tương tác:
```bash
python -m streamlit run app.py
```

## 📊 Kết quả Phân cụm (Personas)

| Cụm | Tên (Tiếng Việt) | Mô tả ngắn | Chiến lược Marketing |
| :--- | :--- | :--- | :--- |
| **0** | **Khách hàng vãng lai** | Mua ít, chi tiêu thấp, ít mua theo bộ. | Email Re-engagement, mã giảm giá kích cầu. |
| **1** | **Khách hàng VIP** | Mua thường xuyên, chi tiêu lớn, thích mua theo combo. | Loyalty Program, ưu đãi Bundle (trang trí), VIP care. |

## 📈 Trực quan hóa
Sử dụng PCA để trực quan hóa mức độ tách cụm trong không gian 2D, giúp đánh giá chất lượng của mô hình phân cụm.

---
*Dự án được thực hiện như một phần của Mini Project - Data Mining.*
