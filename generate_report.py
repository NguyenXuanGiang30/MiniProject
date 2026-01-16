
import pandas as pd
import base64
import os

# Paths
REPORT_PATH = "report.html"
DATA_DIR = "data/processed"

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    return ""

def generate_html():
    try:
        df_rfm = pd.read_csv(f"{DATA_DIR}/cluster_rfm_summary.csv")
        df_rules = pd.read_csv(f"{DATA_DIR}/cluster_top_rules.csv")
        df_model = pd.read_csv(f"{DATA_DIR}/model_comparison.csv")
        df_roi = pd.read_csv(f"{DATA_DIR}/roi_projections.csv")
        
        # Base64 images
        pca_base64 = get_base64_image(f"{DATA_DIR}/cluster_pca.png")
        rev_dist_base64 = get_base64_image(f"{DATA_DIR}/revenue_distribution.png")
        roi_proj_base64 = get_base64_image(f"{DATA_DIR}/roi_projection.png")
        clv_dist_base64 = get_base64_image(f"{DATA_DIR}/clv_distribution.png")
        churn_risk_base64 = get_base64_image(f"{DATA_DIR}/churn_risk.png")
        radar_base64 = get_base64_image(f"{DATA_DIR}/cluster_radar.png")
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Personas
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

    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Customer Segmentation & ROI Report</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            :root {{
                --primary: #2563eb;
                --secondary: #64748b;
                --bg: #f8fafc;
                --card: #ffffff;
                --text: #1e293b;
                --accent: #f59e0b;
            }}
            body {{
                font-family: 'Inter', sans-serif;
                background-color: var(--bg);
                color: var(--text);
                line-height: 1.6;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 1100px;
                margin: 40px auto;
                padding: 0 20px;
            }}
            header {{
                text-align: center;
                margin-bottom: 50px;
                background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
                color: white;
                padding: 60px 20px;
                border-radius: 20px;
                box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
            }}
            header h1 {{ margin: 0; font-size: 3rem; }}
            header p {{ font-size: 1.2rem; opacity: 0.9; }}
            
            .section-title {{
                display: flex;
                align-items: center;
                margin-bottom: 25px;
                padding-bottom: 10px;
                border-bottom: 2px solid #e2e8f0;
            }}
            .section-title i {{ margin-right: 15px; font-size: 1.5rem; color: var(--primary); }}
            
            .card {{
                background: var(--card);
                padding: 35px;
                border-radius: 16px;
                box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
                margin-bottom: 40px;
                transition: transform 0.2s;
            }}
            .card:hover {{ transform: translateY(-5px); }}
            
            h2 {{ color: var(--primary); margin-top: 0; }}
            
            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 25px;
            }}
            .stats-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }}
            .stat-card {{
                background: #f1f5f9;
                padding: 20px;
                border-radius: 12px;
                text-align: center;
            }}
            .stat-value {{ font-size: 1.8rem; font-weight: 700; color: var(--primary); }}
            .stat-label {{ font-size: 0.9rem; color: var(--secondary); }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
                font-size: 0.95rem;
            }}
            th, td {{
                padding: 14px;
                text-align: left;
                border-bottom: 1px solid #e2e8f0;
            }}
            th {{ background-color: #f8fafc; font-weight: 600; color: #475569; }}
            
            .persona {{
                border: 1px solid #e2e8f0;
                padding: 25px;
                border-radius: 12px;
                background: #ffffff;
                position: relative;
            }}
            .badge {{
                display: inline-block;
                padding: 6px 14px;
                border-radius: 30px;
                background: var(--primary);
                color: white;
                font-size: 0.85rem;
                font-weight: 600;
                margin-bottom: 15px;
            }}
            .strategy {{
                background: #ecfdf5;
                border: 1px solid #10b981;
                padding: 18px;
                border-radius: 10px;
                margin-top: 20px;
                font-size: 0.95rem;
            }}
            
            .chart-container {{
                text-align: center;
                margin-top: 20px;
            }}
            img {{
                max-width: 100%;
                height: auto;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            }}
            
            .roi-tag {{
                font-weight: 700;
                color: #059669;
                font-size: 1.1rem;
            }}

            .footer {{
                text-align: center;
                margin-top: 80px;
                padding: 40px;
                color: var(--secondary);
                font-size: 0.9rem;
                border-top: 1px solid #e2e8f0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>📊 Chiến Lược Phân Khúc KH & ROI</h1>
                <p>Báo cáo phân tích nâng cao: Phân cụm - Luật kết hợp - Dự báo tăng trưởng</p>
            </header>

            <section class="card">
                <div class="section-title"><h2>1. Tổng Quan Phân Cụm (Clustering Overview)</h2></div>
                <div class="grid">
                    <div class="chart-container">
                        <h3>Mặt phẳng PCA</h3>
                        <img src="data:image/png;base64,{pca_base64}" alt="PCA Plot">
                    </div>
                    <div class="chart-container">
                        <h3>Đồ thị Radar (Gốc RFM)</h3>
                        <img src="data:image/png;base64,{radar_base64}" alt="Radar Chart">
                    </div>
                </div>
            </section>

            <section class="card">
                <div class="section-title"><h2>2. Phân Tích Doanh Thu & CLV (Revenue & Lifetime Value)</h2></div>
                <div class="grid">
                    <div class="chart-container">
                        <h3>Tỷ trọng doanh thu theo cụm</h3>
                        <img src="data:image/png;base64,{rev_dist_base64}" alt="Revenue Distribution">
                    </div>
                    <div class="chart-container">
                        <h3>Ước tính CLV (Boxplot)</h3>
                        <img src="data:image/png;base64,{clv_dist_base64}" alt="CLV Distribution">
                    </div>
                </div>
            </section>

            <section class="card">
                <div class="section-title"><h2>3. Dự Báo ROI & Rủi Ro (ROI Projection & Churn Risk)</h2></div>
                <div class="grid">
                    <div class="chart-container">
                        <h3>Dự báo tỷ lệ ROI (%)</h3>
                        <img src="data:image/png;base64,{roi_proj_base64}" alt="ROI Projection">
                    </div>
                    <div class="chart-container">
                        <h3>Rủi ro rời bỏ (Recency based)</h3>
                        <img src="data:image/png;base64,{churn_risk_base64}" alt="Churn Risk">
                    </div>
                </div>
                <div style="margin-top: 30px;">
                    <h3>Bảng dữ liệu ROI dự kiến</h3>
                    {df_roi.to_html(index=False, classes='table')}
                </div>
            </section>

            <section class="card">
                <div class="section-title"><h2>4. Chân Dung Khách Hàng & Chiến Lược</h2></div>
                <div class="grid">
    """

    for cid, p in personas.items():
        html_content += f"""
                    <div class="persona">
                        <span class="badge">Cụm {cid}</span>
                        <h3>{p['name']}</h3>
                        <p>{p['desc']}</p>
                        <div class="strategy">💡 <b>Chiến lược:</b> {p['strategy']}</div>
                    </div>
        """

    html_content += """
                </div>
            </section>

            <section class="card">
                <div class="section-title"><h2>5. Quy Luật Mua Sắm Gợi Ý (Association Rules)</h2></div>
                <p>Các quy luật có chỉ số <i>Lift</i> cao nhất giúp tối ưu hóa Cross-selling trong từng nhóm.</p>
    """

    for cid in df_rules['cluster'].unique():
        cluster_rules = df_rules[df_rules['cluster'] == cid].head(5)
        html_content += f"<h3>Gợi ý cho Cụm {cid}</h3>"
        html_content += cluster_rules[['rule', 'lift']].to_html(index=False, classes='table')

    html_content += f"""
            </section>

            <section class="card">
                <div class="section-title"><h2>6. Đánh Giá Kỹ Thuật (Model Evaluation)</h2></div>
                <p>Bảng so sánh chất lượng phân cụm giữa các thuật toán và số cụm K khác nhau.</p>
                {df_model.to_html(index=False, classes='table')}
            </section>

            <div class="footer">
                &copy; 2026 Mini Project - Data Mining & BI | Hệ thống phân tích tự động
            </div>
        </div>
    </body>
    </html>
    """

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated enhanced report: {REPORT_PATH}")

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated report: {REPORT_PATH}")

if __name__ == "__main__":
    generate_html()
