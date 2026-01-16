# 🛒 PHÂN CỤM KHÁCH HÀNG DỰA TRÊN LUẬT KẾT HỢP
## (Customer Segmentation via Association Rules & Strategic Analysis)

Dự án này thực hiện phân khúc khách hàng chuyên sâu bằng cách kết hợp kỹ thuật **Khai phá luật kết hợp (Association Rules)** và các chỉ số **RFM truyền thống**. Điểm nổi bật của dự án là việc tích hợp phân tích tài chính chiến lược bao gồm **Dự báo ROI**, **Ước tính CLV** và **Phân tích Rủi ro rời bỏ (Churn Risk)**.

---

## 🚀 Tính năng nổi bật

1.  **Phân cụm thông minh**: Kết hợp hành vi mua sắm chéo (Cross-buy) từ luật kết hợp và sức mua (RFM) để tạo ra các phân cụm khách hàng có chiều sâu.
2.  **So sánh đa mô hình**: Đánh giá hiệu quả giữa **K-Means** và **Agglomerative Clustering** qua các chỉ số Silhouette, DBI, và CH Index.
3.  **Phân tích ROI & CLV**: Mô phỏng hiệu quả kinh tế của các chiến dịch Marketing nhắm mục tiêu, giúp tối ưu hóa ngân sách.
4.  **Dự báo Churn**: Xác định các nhóm khách hàng có nguy cơ rời bỏ cao dựa trên độ tươi mới của giao dịch (Recency).
5.  **Dashboard tương tác**: Trực quan hóa kết quả qua ứng dụng Streamlit hiện đại.

---

## 📦 Cấu trúc dự án

```text
├── data/
│   ├── raw/                # Dữ liệu gốc (Online Retail dataset)
│   └── processed/          # Kết quả phân tích, biểu đồ và CSV trung gian
├── notebooks/              # Quy trình thực hiện từng bước (Jupyter Notebooks)
├── src/
│   └── cluster_library.py  # Lõi xử lý (Cleaning, Mining, Clustering, Visualization)
├── app.py                  # Streamlit Dashboard chính
├── roi_analysis.py         # Script phân tích ROI, CLV và Churn Risk
├── run_papermill.py        # Tự động hóa Pipeline chạy Notebooks
├── requirements.txt        # Danh sách thư viện cần thiết
└── README.md
```

---

## 🛠️ Hướng dẫn sử dụng

### 1. Cài đặt môi trường
Yêu cầu Python 3.9+. Nên sử dụng môi trường ảo (venv).
```bash
pip install -r requirements.txt
```

### 2. Chạy quy trình phân tích (Pipeline)
Bạn có thể chạy toàn bộ quy trình từ tiền xử lý đến phân cụm tự động:
```bash
python run_papermill.py
```

### 3. Phân tích tài chính & ROI
Để cập nhật các biểu đồ và số liệu về ROI, CLV và rủi ro:
```bash
python roi_analysis.py
```

### 4. Khởi chạy Dashboard
Trực quan hóa kết quả và xem đề xuất chiến lược:
```bash
streamlit run app.py
```

---

## 📈 Tóm tắt Phân khúc (Personas)

| Cụm | Nhãn khách hàng | Đặc điểm chính | Chiến lược đề xuất |
| :--- | :--- | :--- | :--- |
| **0** | **Occasional Shoppers** | Chiếm 95% doanh thu tổng, mua sắm rời rạc, rủi ro rời bỏ cao. | Email Marketing, mã giảm giá kích cầu, nhắc nhở thương hiệu. |
| **1** | **Loyal Decorators** | Chi tiêu lớn, tần suất cao, CLV vượt trội, ROI đầu tư cao. | Chương trình VIP, ưu đãi đặc quyền, Cross-sell theo luật kết hợp. |

---

## 🧪 Công nghệ sử dụng
- **Ngôn ngữ**: Python 3.10+
- **Thư viện chính**: `pandas`, `scikit-learn`, `mlxtend` (Apriori/FP-Growth), `seaborn`, `plotly`.
- **Giao diện**: Streamlit.

---
*Dự án được thực hiện phục vụ cho Mini Project - Data Mining.*
