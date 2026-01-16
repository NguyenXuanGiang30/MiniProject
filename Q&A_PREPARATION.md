# Danh sách Câu hỏi & Trả lời (Q&A) Thuyết trình

Tài liệu này giúp bạn chuẩn bị cho phần phản biện sau khi kết thúc thuyết trình.

---

## Nhóm 1: Câu hỏi về Kỹ thuật (Data Science)

### Q1: Tại sao bạn lại chọn thuật toán K-means/Agglomerative cho bài toán này?
**Gợi ý trả lời:** 
*   **Tiêu chuẩn ngành:** K-means là thuật toán kinh điển, hiệu quả với dữ liệu RFM quy mô lớn vì tốc độ tính toán nhanh.
*   **Tính hiệu quả:** Qua kiểm chứng bằng mặt phẳng PCA và chỉ số Silhouette, K-means cho kết quả phân nhóm rõ rệt, dễ giải thích về mặt hành vi kinh doanh.

### Q2: Việc kết hợp "Luật kết hợp" vào bộ đặc trưng (features) có tác dụng gì so với chỉ dùng RFM đơn thuần?
**Gợi ý trả lời:** 
*   RFM chỉ trả lời cho câu hỏi: "Ai mua nhiều, ai mua gần đây?".
*   Luật kết hợp trả lời cho câu hỏi: "Họ mua cái gì?".
*   **Kết quả:** Việc kết hợp giúp chúng ta phân cụm khách hàng không chỉ dựa trên mức chi tiêu mà còn dựa trên sở thích danh mục sản phẩm (ví dụ: nhóm chuyên mua đồ gia dụng vs nhóm chuyên mua đồ trang trí).

### Q3: Các outliers (điểm nhiễu) trong biểu đồ Boxplot CLV được xử lý như thế nào?
**Gợi ý trả lời:** 
*   Chúng ta giữ lại các outliers này vì trong thương mại điện tử, các "khách hàng cá mập" (whale) mua cực nhiều là đối tượng rất quan trọng, không nên bị loại bỏ.
*   Tuy nhiên, khi tính toán ROI forecast, chúng ta dùng giá trị trung vị (median) để đảm bảo dự báo không bị quá lạc quan do các điểm cực trị này.

---

## Nhóm 2: Câu hỏi về Kinh doanh & Chiến lược

### Q4: Tại sao Cụm 0 chiếm 95% doanh thu nhưng bạn lại đánh giá Cụm 1 quan trọng hơn?
**Gợi ý trả lời:** 
*   Cụm 0 đóng góp doanh thu lớn do số lượng đông, nhưng chi phí để duy trì và chuyển đổi họ rất cao (low margin).
*   **Cụm 1 là nhóm "chất lượng":** Họ có CLV cao, trung thành hơn và chi phí giữ chân thấp hơn. Một doanh nghiệp bền vững cần chăm sóc Cụm 1 để làm nền tảng lợi nhuận, đồng thời tìm cách chuyển đổi một phần Cụm 0 thành Cụm 1.

### Q5: Dự báo ROI của bạn dựa trên những cơ sở nào? Có đáng tin cậy không?
**Gợi ý trả lời:** 
*   Dự báo dựa trên các giả định thực tế: Chi phí tiếp cận mỗi khách hàng (Campaign Cost), tỷ lệ chuyển đổi lịch sử (Conversion Rate) và mức độ tăng trưởng đơn hàng (Lift factor).
*   Đây là một mô hình mô phỏng (Simulation). Nó giúp doanh nghiệp so sánh hiệu quả tương đối giữa các cụm để ưu tiên ngân sách, chứ không phải một con số tài chính tuyệt đối.

### Q6: Nếu ngân sách Marketing có hạn, bạn sẽ ưu tiên cụm nào trước?
**Gợi ý trả lời:** 
*   **Ưu tiên 1:** Nhóm "Med-High Risk" của Cụm 1 (Nhóm khách giá trị cao nhưng có dấu hiệu sắp rời bỏ). Đây là nhóm mất đi sẽ thiệt hại lớn nhất.
*   **Ưu tiên 2:** Nhóm "Potential" của Cụm 0 để tối ưu hóa nguồn thu hiện tại.

---

## Nhóm 3: Câu hỏi mở rộng

### Q7: Mô hình này có thể cải thiện thêm điều gì trong tương lai?
**Gợi ý trả lời:** 
*   Tích hợp dữ liệu thời gian thực (Real-time).
*   Sử dụng Deep Learning (như Recurrent Neural Networks) để dự báo chính xác thời điểm khách hàng sẽ mua đơn hàng tiếp theo.
*   Thử nghiệm A/B Testing trên các đề xuất hành động để đo lường ROI thực tế.
