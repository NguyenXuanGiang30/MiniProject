
import pandas as pd
import base64
import os

# Paths
SLIDES_PATH = "presentation.html"
DATA_DIR = "data/processed"

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    return ""

def generate_slides():
    try:
        # Load core data for slides
        pca_base64 = get_base64_image(f"{DATA_DIR}/cluster_pca.png")
        rev_dist_base64 = get_base64_image(f"{DATA_DIR}/revenue_distribution.png")
        roi_proj_base64 = get_base64_image(f"{DATA_DIR}/roi_projection.png")
        clv_dist_base64 = get_base64_image(f"{DATA_DIR}/clv_distribution.png")
        churn_risk_base64 = get_base64_image(f"{DATA_DIR}/churn_risk.png")
        radar_base64 = get_base64_image(f"{DATA_DIR}/cluster_radar.png")
        
        df_roi = pd.read_csv(f"{DATA_DIR}/roi_projections.csv")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    html_content = f"""
    <!doctype html>
    <html lang="vi">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

        <title>Mini Project Presentation - Customer Segmentation</title>

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reset.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/theme/league.min.css">

        <style>
            .container {{ display: flex; }}
            .col {{ flex: 1; }}
            .highlight {{ color: #e7ad52; font-weight: bold; }}
            .chart-img {{ border: 5px solid #444; border-radius: 10px; max-height: 500px !important; }}
            table {{ font-size: 0.6em !important; }}
            .persona-card {{ background: #222; padding: 20px; border-radius: 10px; border-left: 5px solid #e7ad52; }}
        </style>
    </head>
    <body>
        <div class="reveal">
            <div class="slides">
                <!-- Slide 1: Welcome -->
                <section data-background-gradient="linear-gradient(to bottom, #283048, #859398)">
                    <h2 style="text-transform: uppercase;">Phân Cụm Khách Hàng Dựa Trên Luật Kết Hợp</h2>
                    <p>
                        <small>Người trình bày: <b>{os.getlogin() if hasattr(os, 'getlogin') else 'User'}</b></small>
                    </p>
                    <p><small>Công nghệ: Python | Data Mining | Reveal.js</small></p>
                </section>

                <!-- Slide 2: Mục tiêu -->
                <section>
                    <h2>Mục Tiêu Dự Án</h2>
                    <ul>
                        <li class="fragment">Phân nhóm khách hàng dựa trên hành vi (RFM).</li>
                        <li class="fragment">Kết hợp <span class="highlight">Association Rules</span> để gợi ý sản phẩm.</li>
                        <li class="fragment">Tính toán <span class="highlight">ROI & CLV</span> cho các chiến dịch Marketing.</li>
                        <li class="fragment">Xác định rủi ro rời bỏ (Churn Risk).</li>
                    </ul>
                </section>

                <!-- Slide 3: Clustering Overview -->
                <section>
                    <section>
                        <h2>1. Tổng Quan Phân Cụm</h2>
                        <p>Sử dụng K-Means & Agglomerative Clustering</p>
                    </section>
                    <section>
                        <h3>Trực quan hóa PCA</h3>
                        <img src="data:image/png;base64,{pca_base64}" class="chart-img">
                        <p><small>Các cụm được phân tách rõ rệt dựa trên đặc trưng RFM</small></p>
                    </section>
                    <section>
                        <h3>Đồ thị Radar (RFM Profile)</h3>
                        <img src="data:image/png;base64,{radar_base64}" class="chart-img">
                    </section>
                </section>

                <!-- Slide 4: Doanh thu & CLV -->
                <section>
                    <section>
                        <h2>2. Doanh Thu & Giá Trị Vòng Đời</h2>
                    </section>
                    <section>
                        <h3>Tỷ trọng Doanh Thu</h3>
                        <div class="container">
                            <div class="col">
                                <img src="data:image/png;base64,{rev_dist_base64}" class="chart-img">
                            </div>
                            <div class="col" style="text-align: left; padding-left: 20px;">
                                <p>Cụm 0: <span class="highlight">95% Doanh thu</span></p>
                                <p>Cụm 1: <span class="highlight">5% Doanh thu</span></p>
                                <p><small>Mặc dù cụm 1 ít người hơn nhưng giá trị mỗi khách hàng lại cao hơn.</small></p>
                            </div>
                        </div>
                    </section>
                    <section>
                        <h3>Phân phối CLV (Tiềm năng lâu dài)</h3>
                        <img src="data:image/png;base64,{clv_dist_base64}" class="chart-img">
                        <p><small>Cụm 1 thể hiện CLV vượt trội và ổn định.</small></p>
                    </section>
                </section>

                <!-- Slide 5: Chiến Lược ROI -->
                <section>
                    <section>
                        <h2>3. Dự Báo ROI & Churn Risk</h2>
                    </section>
                    <section>
                        <h3>Dự báo Tỷ lệ hoàn vốn (ROI)</h3>
                        <img src="data:image/png;base64,{roi_proj_base64}" class="chart-img">
                        <p><small>Chiến dịch nhắm tới Cụm 1 kỳ vọng ROI cao hơn do tỷ lệ chuyển đổi tốt.</small></p>
                    </section>
                    <section>
                        <h3>Rủi ro rời bỏ (Recency Analysis)</h3>
                        <img src="data:image/png;base64,{churn_risk_base64}" class="chart-img">
                        <p><small>Cần chiến dịch Re-engagement cho nhóm High Risk ở Cụm 0.</small></p>
                    </section>
                </section>

                <!-- Slide 6: Tổng kết chiến lược -->
                <section>
                    <h2>Chiến Lược Hành Động</h2>
                    <div class="container">
                        <div class="col persona-card" style="margin-right: 10px;">
                            <h4>Cụm 0 (Occasional)</h4>
                            <p><small>Tăng tần suất mua bằng Email Marketing & Coupon giảm giá.</small></p>
                        </div>
                        <div class="col persona-card">
                            <h4>Cụm 1 (Loyal)</h4>
                            <p><small>Chương trình VIP, ưu đãi sớm & Cross-sell theo luật kết hợp.</small></p>
                        </div>
                    </div>
                </section>

                <!-- Slide 7: Kết thúc -->
                <section data-background="#222">
                    <h2>CẢM ƠN THẦY VÀ CÁC BẠN ĐÃ LẮNG NGHE!</h2>
                    <p>Hỏi & Đáp (Q&A)</p>
                </section>
            </div>
        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.js"></script>
        <script>
            Reveal.initialize({{
                hash: true,
                slideNumber: 'c/t',
                transition: 'convex'
            }});
        </script>
    </body>
    </html>
    """

    with open(SLIDES_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated presentation slides: {SLIDES_PATH}")

if __name__ == "__main__":
    generate_slides()
