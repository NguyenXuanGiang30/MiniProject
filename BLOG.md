# 📝 BLOG: Khám phá Chân dung Khách hàng qua Luật kết hợp & RFM

## Đặt vấn đề: Tại sao chỉ dùng RFM là chưa đủ?
Trong thương mại điện tử, chúng ta thường phân loại khách hàng dựa trên **RFM** (Recency, Frequency, Monetary). Tuy nhiên, RFM chỉ cho biết khách hàng "đáng giá" bao nhiêu, chứ không cho biết họ "thích mua gì cùng nhau". Để thực sự hiểu hành vi, chúng ta cần đi sâu vào **Luật kết hợp (Association Rules)**.

Dự án này là hành trình biến những giao dịch rời rạc thành những nhóm khách hàng có chân dung rõ nét, giúp doanh nghiệp đưa ra các chiến lược Cross-sell và Bundle hiệu quả.

---

## Hành trình 3 bước từ Dữ liệu đến Hành động

### Bước 1: Khai phá "Sức mạnh" của các món đồ đi kèm
Sử dụng thuật toán **Apriori**, chúng mình đã lọc ra hàng trăm quy luật mua sắm giá trị. 
*Ví dụ:* Khách hàng mua *Herb Marker Thyme* có xác suất hơn 90% sẽ mua kèm *Herb Marker Rosemary* (với chỉ số Lift cực cao ~86). Đây không chỉ là dữ liệu, đây là cơ hội để tạo ra các gói sản phẩm (Bundles).

### Bước 2: Biến Luật thành Đặc trưng (Feature Engineering)
Đây là phần thú vị nhất. Thay vì chỉ dùng 0/1, chúng mình đã:
- Sử dụng **Lift** làm trọng số để đề cao những quy luật có tính liên kết mạnh.
- Kết hợp với **RFM** được chuẩn hóa để đảm bảo mô hình hiểu cả "giá trị" và "hành vi".
- So sánh các biến thể để chọn ra cấu hình **Top 200 luật** tối ưu nhất.

### Bước 3: Phân cụm và So sánh mô hình (K-Means vs Agglomerative)
Chúng mình không chỉ tin vào một thuật toán. Bằng cách so sánh **K-Means** và **Agglomerative Clustering** qua các chỉ số **Silhouette, DBI, và CH Index**, kết quả cho thấy:
- **Agglomerative Clustering (K=2)** đạt độ tách biệt cụm vượt trội (Silhouette ~0.51).
- Dữ liệu khách hàng thực sự phân hóa thành 2 nhóm rõ rệt.

---

## 🏆 Chân dung Khách hàng & Chiến lược Marketing

Từ kết quả phân tích, 2 nhóm khách hàng (Personas) đã lộ diện:

### 1. Nhóm "Khách hàng Vãng lai" (Occasional Shoppers)
- **Đặc trưng:** Mới mua hoặc mua rất ít, chi tiêu thấp, hiếm khi kích hoạt các luật mua kèm.
- **Chiến lược:** *Kích hoạt lại (Re-activation)*. Gửi email tặng coupon giảm giá đơn hàng thứ 2 để biến họ thành khách hàng thường xuyên.

### 2. Nhóm "Tín đồ VIP & Trang trí" (Loyal Decorators)
- **Đặc trưng:** Chi tiêu gấp đôi mức trung bình, thường xuyên mua theo bộ (như bộ trang trí Scandi, bộ trà Regency).
- **Chiến lược:** *Khai thác giá trị (Upsell/Bundle)*. Ưu đãi mua theo combo trọn bộ trang trí, mời tham gia chương trình VIP để giữ chân lâu dài.

---

## Kết luận
Dự án đã chứng minh rằng việc kết hợp **Data Mining (Association Rules)** và **Machine Learning (Clustering)** mang lại cái nhìn sâu sắc hơn nhiều so với các phương pháp truyền thống. 

Hãy thử tưởng tượng bạn có thể Dashboard hóa toàn bộ quy trình này để bộ phận Marketing có thể "chọn cụm - nhận gợi ý bundle" chỉ trong 1 click. Đó chính là sức mạnh của dữ liệu!

---
*Thực hiện bởi: Nhóm Mini Project - Data Mining*
