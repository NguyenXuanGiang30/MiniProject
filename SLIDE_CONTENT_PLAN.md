# Kế hoạch Nội dung Slide Thuyết trình

Bản kế hoạch này giúp bạn nắm bắt logic dẫn dắt câu chuyện (storytelling) cho bài thuyết trình về dự án **"Phân cụm khách hàng dựa trên Luật kết hợp"**.

---

## Slide 1: Tiêu đề & Giới thiệu
*   **Nội dung chính:** Tên dự án, tên người thực hiện, công nghệ sử dụng.
*   **Thông điệp:** Đây là một dự án kết hợp kỹ thuật khai phá dữ liệu (Data Mining) với bài toán kinh doanh thực tế.

## Slide 2: Đặt vấn đề & Mục tiêu
*   **Nội dung chính:** 
    *   Tại sao cần phân cụm? (Dữ liệu lớn, khách hàng không giống nhau).
    *   Tại sao dùng Luật kết hợp? (Hiểu sâu hơn hành vi mua sản phẩm đi kèm).
    *   Mục tiêu: Tối ưu ROI (Tỷ lệ hoàn vốn) và CLV (Giá trị vòng đời).
*   **Thông điệp:** Biến dữ liệu thô thành chiến lược ra tiền.

## Slide 3: Tổng quan Phân cụm (Kỹ thuật)
*   **Vị trí biểu đồ:** 
    *   Ảnh 1: `cluster_pca.png` (Mặt phẳng PCA) - Chứng minh phân cụm rõ rệt.
    *   Ảnh 2: `cluster_radar.png` (Đồ thị Radar) - Giải thích đặc trưng RFM từng cụm.
*   **Phân tích:** 
    *   Cụm 0: Nhóm phổ thông (Low-mid RFM).
    *   Cụm 1: Nhóm khách hàng giá trị cao (High RFM).
*   **Thông điệp:** Hai phân khúc khách hàng có chân dung hoàn toàn khác biệt.

## Slide 4: Phân tích Doanh thu & CLV (Kinh doanh)
*   **Vị trí biểu đồ:** 
    *   Ảnh 3: `revenue_distribution.png` (Biểu đồ tròn) - Cụm 0 chiếm tỷ trọng doanh thu chính.
    *   Ảnh 4: `clv_distribution.png` (Boxplot CLV) - Cụm 1 có giá trị tiềm năng vượt trội.
*   **Phân tích:** 
    *   Cụm 0: Số lượng đông, đóng góp 95% doanh thu tổng (Cần duy trì).
    *   Cụm 1: Số lượng ít nhưng giá trị/cá nhân rất cao (Cần chăm sóc VIP).
*   **Thông điệp:** Đừng chỉ nhìn vào số đông, hãy nhìn vào giá trị lâu dài.

## Slide 5: Dự báo ROI & Rủi ro rời bỏ (Chiến lược)
*   **Vị trí biểu đồ:** 
    *   Ảnh 5: `roi_projection.png` (Biểu đồ ROI) - Hiệu quả đầu tư vào từng cụm.
    *   Ảnh 6: `churn_risk.png` (Stacked bar Churn) - Cảnh báo tỷ lệ rời bỏ ở Cụm 0.
*   **Phân tích:** 
    *   ROI cao nhất khi đầu tư vào Cụm 1.
    *   Rủi ro rời bỏ tập trung ở Cụm 0 (Cần chiến dịch kích cầu gấp).
*   **Thông điệp:** Đầu tư thông minh vào đúng người, đúng thời điểm.

## Slide 6: Gợi ý hành động (Actionable Insights)
*   **Nội dung chính:** Đề xuất cụ thể cho từng cụm.
    *   Cụm 0: Tăng tần suất bằng khuyến mãi, nhắc nhở thương hiệu.
    *   Cụm 1: Ưu đãi đặc quyền, Cross-sell (bán chéo) dựa trên **Luật kết hợp**.
*   **Thông điệp:** Kỹ thuật phục vụ chiến lược.

## Slide 7: Tổng kết & Kết thúc
*   **Nội dung chính:** Khẳng định lại hiệu quả của mô hình và cảm ơn.
*   **Thông điệp:** Hệ thống sẵn sàng triển khai thực thế.
